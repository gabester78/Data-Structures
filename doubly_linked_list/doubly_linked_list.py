
"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            # set new node link to previous head
            new_node.next = self.head
            # set old head link to new node
            self.head.prev = new_node
            # set new node as head
            self.head = new_node

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1

        # set node to tail and head if list is empty
        if not self.head and not self.tail:
            self.tail = new_node
            self.head = new_node

        # if list isn't empty set new node as tail
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        if node is self.head:
            return None
        if node is self.head:
            self.remove_from_tail()
        else:
            self.delete(node)
            # self.length -= 1
            self.add_to_head(node.value)

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        if node is self.tail:
            return None
        if node is self.tail:
            self.remove_from_head()
        else:
            self.delete(node)
            # self.length -= 1
            self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        # if list is empty, nothing to delete so return none
        if not self.head and not self.tail:
            return None

        # decrease length of list
        self.length -= 1

        # if list has one element remove it by setting
        # head and tail to None
        if self.head == self.tail:
            self.head = None
            self.tail = None

        # if node to delete is head or tail, set node to next
        # as head or previous as tail and cuts connections to
        # related nodes
        elif self.head == node:
            self.head = node.next
            self.head.prev = None
        elif self.tail == node:
            self.tail = node.prev
            self.tail.next = None
        else:
            # sets prev node to point to next node in line
            node.prev = node.next
            # sets next node to point to the previous node in line
            node.next = node.prev

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        # checks if list is empty if so returns none
        if not self.head:
            return None
        # sets inital value as head value
        max_val = self.head.value
        # checks next node in line
        current = self.head
        # loop through the list
        while current:
            # compare if current value is great than max value
            if current.value > max_val:
                # if current value is great, current value is now max value
                max_val = current.value
            # checks next for another comparison
            current = current.next
        # gives max value of list
        return max_val
