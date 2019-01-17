#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tinylog import tinylog
from collector import Collector
from publisher import Publisher
import json


def load_secrets():		
	with open('.secrets') as f:
		secrets = json.load(f)
		mac = secrets['MAC']
		mqtt_params = secrets['MQTT']
		return mac, mqtt_params


def load_config():
	with open('config.json') as f:
		return json.load(f)['sensors']


def run():
	mac, mqtt_params = load_secrets()
	sensors = load_config()

	publisher = Publisher(mqtt_params)
	collector = Collector(mac, sensors, publisher)
	if not collector.connected:
		return

	publisher.loop_start()
	
	while True:
		collector.collect()


if (__name__ == '__main__'):
	exlog = tinylog('Exception')

	try: 
		run()
	except ValueError, ParseError:
		exlog.err('Invalid secrets or config!')
	except KeyboardInterrupt, SystemExit:
		pass
