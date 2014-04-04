from LinkedList import LinkedList


def main():
	# comparator that is passed into the LinkedList
	def comparator(value_one, value_two):
		if value_one == value_two:
			return 0
		elif value_one > value_two:
			return 1
		else:
			return -1

	test_one = LinkedList(comparator)
	test_two = LinkedList(comparator)
	test_three = LinkedList(comparator)

	test_one.insert(2)
	test_one.insert(3)
	test_one.insert(1)

	test_two.insert(5)

	test_three.insert(10)
	test_three.insert(20)
	test_three.insert(30)
	test_three.insert(40)
	test_three.insert(50)

	print("Test one: ")
	test_one.print()

	print("\nTest two: ")
	test_two.print()

	print("\nTest three: ")
	test_three.print()

	test_one.remove(2)
	test_one.remove(6)

	test_two.remove(5)

	test_three.remove(10)
	test_three.remove(50)

	print("\nTest one after removals: ")
	test_one.print()

	print("\nTest two after removals: ")
	test_two.print()

	print("\nTest three after removals: ")
	test_three.print()

main()