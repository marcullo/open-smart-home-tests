#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tinylog import tinylog
from collector import Collector
import json


def load_secrets():		
	with open('.secrets') as f:
		secrets = json.load(f)
		mac = secrets['MAC']
		return mac


def load_config():
	with open('config.json') as f:
		return json.load(f)['sensors']


def run():
	mac = load_secrets()
	sensors = load_config()

	collector = Collector(mac, sensors)
	if not collector.connected:
		return
	
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
