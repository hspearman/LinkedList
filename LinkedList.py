from Node import Node


class LinkedList(object):
	# comparator is a function used by LinkedList to compare nodes
	# it's expected to take two parameters:
	# it returns 0 if both parameters are equal, 1 if the left parameter is greater, and -1 if the lft parameter is lesser
	def __init__(self, comparator):
		self.head = None
		self.comparator = comparator

	# Adds a value to the LinkedList while maintaining a sorted state
	def insert(self, value):
		node = Node(value)

		# If the linked list is empty, make this the head node
		if self.head is None:
			self.head = node
		# Otherwise, insert the node into the sorted linked list
		else:
			curr_node = self.head
			b_node_not_added = True
			while b_node_not_added:
				result = self.comparator(node.value, curr_node.value)

				# Store the next and previous node for readability
				prev = curr_node.prev_node
				next = curr_node.next_node

				# If the current node is greater, then insert this node into its spot
				if result < 0:
					# If the curr_node was the head, replace it with this node
					if self.head == curr_node:
						self.head = node
					# Otherwise, it has a previous node so hook it up to this node
					else:
						node.prev_node = prev
						prev.next_node = node

					# Hook the current node up to this node
					node.next_node = curr_node
					curr_node.prev_node = node

					b_node_not_added = False
				# Otherwise, continue traversing
				else:
					# If we haven't reached the end of the list, keep traversing
					if next is not None:
						curr_node = next
					# Otherwise, append this node
					else:
						curr_node.next_node = node
						node.prev_node = curr_node

						b_node_not_added = False

	def remove(self, value):
		curr_node = self.head

		while curr_node is not None:
			# Store the current node's neighbors for readability
			prev = curr_node.prev_node
			next = curr_node.next_node

			# Check if this is the node we're looking for
			result = self.comparator(value, curr_node.value)

			# If it's equal, then remove the current node
			b_node_is_equal = result == 0
			if b_node_is_equal:
				# If the removed node is the head node, re-assign the head node
				if self.head == curr_node:
					self.head = next
				# Otherwise, remove the node normally
				else:
					if prev is not None:
						prev.next_node = next
					if next is not None:
						next.prev_node = prev

					curr_node = None
			# Otherwise, continue traversing the list
			else:
				curr_node = next

	# Print out the contents of the linked list
	def print(self):
		curr_node = self.head
		while curr_node is not None:
			print(curr_node.value)
			curr_node = curr_node.next_node

