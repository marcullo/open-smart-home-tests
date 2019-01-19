import tinylog
import json

class Sensor():
	def __init__(self, owner, name, unit, publisher):
		self._log = tinylog.tinylog('Sensor')
		self._owner = owner
		self._name = name
		self._unit = unit
		self._publisher = publisher

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
		self._publisher.publish('in', self._name, self._value)
