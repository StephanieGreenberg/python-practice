class Element(object):
    def __init__(self, value):
        self.value = value;
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def size(self):
        current = self.head
        counter = 0

        while current:
            counter += 1
            current = current.next
        return counter

    def empty(self):
        return head is None

    def value_at(self, index):
        counter = 0
        current = self.head

        while current:
            if index == counter:
                return current.value
            counter += 1
            current = current.next
        return None

    def push_front(self, value):
        new_item = Element(value)
        new_item.next = self.head
        self.head = new_item

    def pop_front(self):
        if self.head:
            front = self.head
            self.head = self.head.next
            front.next = None
            return front.value
        return None

    def push_back(self, value):
        new_item = Element(value)
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_item
        else:
            self.head = new_item

    # removes end item and returns its value
    def pop_back(self):
        current = self.head
        if self.head:
            if self.head.next is None:
                deleted_val = self.head.value
                self.head = None
                return deleted_val
            while current.next.next:
                current = current.next
            deleted_val = current.next.value
            current.next = current.next.next
            return deleted_val
        return None

    def front(self):
        return self.head.value if self.head else None

    def back(self):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            return current.value
        else:
            return None

    # insert value at index, so current item at that index is pointed to by new item at index
    def insert(self, index, value):
        current = self.head
        counter = 1
        new_item = Element(value)

        if index == 0:
            new_item.next = self.head
            self.head = new_item
        else:
            while current:
                if counter == index:
                    new_item.next = current.next
                    current.next = new_item
                    break
                current = current.next
                counter += 1

    # removes node at given index
    def erase(self, index):
        counter = 1
        current = self.head
        while current.next:
            if index == 0:
                self.head = self.head.next
                break
            elif counter == index:
                current.next = current.next.next
                break
            counter += 1
            current = current.next

    # returns the value of the node at nth position from the end of the list
    def value_n_from_end(self, n):
        counter = self.size() - 1
        current = self.head

        while current:
            if n == counter:
                return current.value
            counter -= 1
            current = current.next
        return None

    # reverses the list
    def reverse(self):
        prev = nextNode = None
        current = self.head

        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        self.head = prev

    # removes the first item in the list with this value
    def remove_value(self, value):
        current = self.head
        prev = Element(0)
        prev.next = self.head

        while current:
            if current.value == value:
                if current == self.head:
                    self.head = self.head.next
                    break
                else:
                    prev.next = current.next
                    break
            current = current.next
            prev = prev.next

    def print_list(self):
        current = self.head
        while current:
            print(str(current.value) + "->", end='')
            current = current.next
        print("None", end='')

#tests
"""
e1 = Element(1)

ll = LinkedList(e1)

# should be 1
print(ll.front())
# should be 1
print(ll.back())
# should be 1
print(ll.size())

ll.push_back(2)
ll.push_back(3)
ll.push_back(40)

print(ll.front())
print(ll.back())
print(ll.size())

print(ll.pop_front())

print(ll.value_at(0))

ll.insert(0, 60)
print(ll.front())
ll.insert(2, 50)
print(ll.size())

ll.print_list()
print()
ll.remove_value(40)
ll.print_list()
print()
ll2 = LinkedList(e1)
ll2.push_back(2)
ll2.push_back(3)
ll2.push_back(4)

ll2.erase(2)
ll2.print_list()

ll2.push_back(75)
ll2.push_back(87)
print("\n")
ll2.print_list()
ll2.reverse()
print("\n")
ll2.print_list()
print("\n")
print(ll2.value_n_from_end(2))
print(ll2.value_n_from_end(0))
print(ll2.value_n_from_end(8))"""
