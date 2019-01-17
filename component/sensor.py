import tinylog

class Sensor():
	def __init__(self, owner, name, unit):
		self._log = tinylog.tinylog('Sensor')
		self._owner = owner
		self._name = name
		self._unit = unit
	
	def __repr__(self):
		return '{} [{}]'.format(self.name, self.unit)
	
	@property
	def name(self):
		return self._name
	
	@property
	def value(self):
		return self._value
	
	@property
	def unit(self):
		return self._unit

	def update(self, value):
		self._value = value
		self._log.inf('Updated {} with {} {}'.format(
				self._name, self._value, self._unit))
