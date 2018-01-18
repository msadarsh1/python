#LinkedList - insertion, deletion, swap nodes, reverse, middle node, length
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

	def delete(self,data):
		if self.head is None:
			return

		current = self.head
		prev = None

		while current is not None and current.data != data:
			prev = current
			current = current.next

		if prev is None:
			self.head = current.next
		else:
			prev.next = current.next

#1-->2-->3-->4-->5-->6-->7
	def swap(self, x, y):

		if self.head is None:
			return

		if x == y:
			return

		currX = self.head
		prevX = None

		currY = self.head
		prevY = None

		while currX.data != x:
			prevX = currX
			currX = currX.next

		while currY.data != y:
			prevY = currY
			currY = currY.next

		if (currX is None) or (currY is None):
			return

		if prevX is not None:
			prevX.next = currY
		else:
			self.head = currY


		if prevY is not None:
			prevY.next = currX
		else:
			self.head = currX

		temp = currX.next
		currX.next = currY.next
		curry.next = temp

	def reverse(self):
		if self.head is None:
			return

		current = self.head
		prev = None

		while current is not None:
			next = current.next
			current.next = prev
			prev = current
			current = next

		self.head = prev

	def length(self):
		count = 0
		current = self.head

		while current is not None:
			count += 1
			current = current.next

		return count


	def middle(self):
		if self.head is None:
			return

		fast = slow = self.head
		

#1-->2-->3-->4-->5-->6-->7		
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next

		if fast is not None:
			slow = slow.next	

		print("middle node is : {}".format(slow.data))