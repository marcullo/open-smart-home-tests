class tinylog:
	def __init__(self, name):
		name_len = len(name)
		if name_len < 10:
			improved_name = '=' * (10 - name_len)
			improved_name += name
		else:
			improved_name = name[:10]
		self._name = improved_name
	
	def inf(self, msg):
		print('[{}][{}] {}'.format('INF', self._name, msg))

	def wrn(self, msg):
		print('[{}][{}] {}'.format('WRN', self._name, msg))

	def err(self, msg):
		print('[{}][{}] {}'.format('ERR', self._name, msg))
