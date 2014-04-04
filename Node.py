class Node(object):
	def __init__(self, value, prev_node=None, next_node=None):
		self.value = value
		self.prev_node = prev_node
		self.next_node = next_node

	def get_prev_node(self):
		return self._prev_node

	def set_prev_node(self, prev_node):
		self._prev_node = prev_node

	def del_prev_node(self):
		del self.prev_node

	prev_node = property(get_prev_node, set_prev_node, del_prev_node)

	def get_next_node(self):
		return self._next_node

	def set_next_node(self, next_node):
		self._next_node = next_node

	def del_next_node(self):
		del self._next_node

	next_node = property(get_next_node, set_next_node, del_next_node)

	def get_value(self):
		return self._value

	def set_value(self, value):
		self._value = value

	def del_value(self, value):
		del self._value

	value = property(get_value, set_value, del_value)