from bluepy import btle, thingy52
from tinylog import tinylog
from sensor import Sensor
import binascii


class NotificationDelegate(btle.DefaultDelegate):
	def __init__(self, sensors):
		self.sensors = {}
		for s in sensors:
			self.sensors[s.name] = s

	def handleNotification(self, hnd, value):
		if hnd == thingy52.e_humidity_handle:
			self._update_humidity(value)
		elif hnd == thingy52.e_temperature_handle:
			self._update_temperature(value)
		elif hnd == thingy52.e_pressure_handle:
			self._update_pressure(value)

	def _update_humidity(self, value):
		humidity = int(binascii.b2a_hex(value), 16)
		self.sensors['humidity'].update(humidity)

	def _update_temperature(self, value):
		buf = binascii.b2a_hex(value)
		temperature = self._calculate_temperature(buf)
		self.sensors['temperature'].update(temperature)

	def _update_pressure(self, value):
		buf = binascii.b2a_hex(value)
		pressure = self._calculate_pressure(buf)
		self.sensors['pressure'].update(pressure)

	def _calculate_temperature(self, buf):
		temp_int = int(buf[:-2], 16)
		if temp_int >= 2**7:
			temp_int -= 2**8
		temp_dec = int(buf[:-2], 16)
		div = 100 if ((int(buf[-2:], 16) / 10) > 1.0) else 10
		return temp_int + (temp_dec / div)

	def _calculate_pressure(self, buf):
		pressure_int = 0
		for i in range(4):
			pressure_int += int(buf[i<<1:(i<<1)+2], 16) << 8*i
		pressure_dec = int(buf[-2:], 16)
		div = 100 if ((pressure_dec / 10) > 1.0) else 10
		return pressure_int + (pressure_dec / div)


class Collector:
	def __init__(self, mac, sensors):
		try:
			self._log = tinylog('Collector')
			self._connected = False
			self.sensors = []

			self._log.inf('Connecting to {}'.format(mac))
			self._thingy = thingy52.Thingy52(mac)
			self._connected = True

			self._log.inf('Setting up environment')
			self._thingy.environment.enable()

			if 'humidity' in sensors:
				interval = sensors['humidity']['interval']
				self._thingy.environment.set_humidity_notification(True)
				self._thingy.environment.configure(humid_int=interval)

			if 'temperature' in sensors:
				interval = sensors['temperature']['interval']
				self._thingy.environment.set_temperature_notification(True)
				self._thingy.environment.configure(temp_int=interval)

			if 'pressure' in sensors:
				interval = sensors['pressure']['interval']
				self._thingy.environment.set_pressure_notification(True)
				self._thingy.environment.configure(press_int=interval)

			for name in sensors:
				unit = sensors[name]['unit']
				s = Sensor(self._thingy, name, unit)
				self.sensors.append(s)
				self._log.inf('Configured sensor: {}'.format(s))

			self._thingy.setDelegate(NotificationDelegate(self.sensors))
		except btle.BTLEDisconnectError as ex:
			self._log.err(ex)
		except (KeyboardInterrupt, SystemExit) as ex:
			if self._thingy is not None:
				self._log.inf('Disconnecting')
				self._thingy.disconnect()
			raise ex

	@property
	def sensors(self):
		return self._sensors

	@property
	def connected(self):
		return self._connected
	
	def collect(self):
		try:
			self._thingy.waitForNotifications(timeout=5)
		except (KeyboardInterrupt, SystemExit) as ex:
			if self._thingy is not None:
				self._log.inf('Disconnecting')
				self._thingy.disconnect()
			raise ex
