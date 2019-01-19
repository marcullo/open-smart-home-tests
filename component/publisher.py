import paho.mqtt.client as mqtt
from tinylog import tinylog
import json

class Publisher:
	def __init__(self, config):
		self._name = 'Publisher'
		self._config = config
		self._log = tinylog(self._name)
		self._client = mqtt.Client(self._name)
		self._client.username_pw_set(config['user'], config['password'])
                self.sensors = {}

	def loop_start(self):
		self._client.connect(self._config['broker'])
		self._client.loop_start()

	def publish(self, subtopic, name, value):
		topic = '{}/{}'.format('domoticz', subtopic)
                print('Name {} value {}'.format(name, value))
#		self._log.inf('Publishing on {}'.format(topic))

                self.sensors[name] = value

                print(self.sensors)

                if 'temperature' not in self.sensors:
                    return
                if 'humidity' not in self.sensors:
                    return
                if 'pressure' not in self.sensors:
                    return

                to_pub = {
                    'idx': 1,
                    'nvalue': 0,
                    'svalue': '{};{};0;{};0'.format(
                        self.sensors['temperature'], self.sensors['humidity'], self.sensors['pressure']
                    )
                }

                msg = json.dumps(to_pub)

                print('Publishing {}'.format(msg))

		self._log.inf(msg)
		self._client.publish(topic, msg)
                self.sensors = {}
