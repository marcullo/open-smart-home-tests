import paho.mqtt.client as mqtt
from tinylog import tinylog


class Publisher:
	def __init__(self, config):
		self._name = 'Publisher'
		self._config = config
		self._log = tinylog(self._name)
		self._client = mqtt.Client(self._name)
		self._client.username_pw_set(config['user'], config['password'])

	def loop_start(self):
		self._client.connect(self._config['broker'])
		self._client.loop_start()

	def publish(self, subtopic, msg):
		topic = '{}/{}'.format(self._config['topic'], subtopic)
		self._log.inf('Publishing on {}'.format(topic))
		self._client.publish(topic, msg)
