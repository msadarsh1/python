#LinkedList - loop detection
class Node(object):
	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList(object):
	def __init__(self):
		self.head = None


	def push(self, data):
		newNode = Node(data)

		if self.head is None:
			self.head = newNode
		else:
			newNode.next = self.head
			self.head = newNode

	def detectLoop(self):
		if self.head is None:
			return False

		slow = self.head
		fast = self.head

		while slow and fast and fast.next:
			slow = slow.next
			fast = fast.next.next
			if slow == fast:
				return True

		