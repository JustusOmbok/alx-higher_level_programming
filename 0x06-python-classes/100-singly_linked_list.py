#!/usr/bin/python3

""")
Write a class Node that defines a node of a singly linked list"""
class Node:
    """Class Node that defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """initialize a node instance"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter method to retrieve the data"""
        return self.__data

    @data.setter
    def data(self, value):
        """setter method to set the data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """getter method to retrieve the next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter method to set next_node"""
        if value is not None and not isinstance(value, node):
            raise TypeError("next_noden must be a node object")
        self.__next_node = value


"""write a class SinglyLinkedList that defines a singly linked list"""
class SinglyLinkedList:
    """class that defines a singly linked list"""

    def __init__(self):
        """initialize a singly linked list instance"""
        self.head = None

    def sorted_insert(self, value):
        """inserts a new node into the correct sorted position in the list"""
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and value > current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
    def __str__(self):
        """returns a string representation of the list"""
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.rstrip()
