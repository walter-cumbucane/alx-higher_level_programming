#!/usr/bin/python3
"""This code defines Node and SinglyLinkedList classes"""


class Node:
    """Represents a node of a singly linked list
    Attributes:
        __data (int): value inside the node
        next_node  : the next node in the singly linked list
    Methods:
        getters and setters: to manipulate the attributes
    """
    def __init__(self, data, next_node=None):
        """initializes the node
        Args:
            data (int): the data to store inside the node
            next_node(Node): the next node in the singly linked list
        Returns:
            None
        """
        if isinstance(data, int):
            self.__data = data
            self.__next_node = next_node
        else:
            raise TypeError("data must be an integer")

    """ data getter """
    @property
    def data(self):
        return self.__data

    """ data setter"""
    @data.setter
    def data(self, value):
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    """ next_node getter """
    @property
    def next_node(self):
        return self.__next_node

    """next_node setter"""
    @next_node.setter
    def next_node(self, value):
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """Represents a singly linked list
    Attributes:
        __head: the head of the singly linked list
    Methods:
        sorted_insetrt: inserts a new node in the SLL
    """
    def __init__(self):
        """initializes the singly linked list
        Args:
            None
        Returns:
            None
        """
        self.__head = None

    def __str__(self):
        """turns an instance of the class printable
        Args:
            None
        Returns:
            None
        """
        node = self.__head
        sll_print = ""
        while node:
            if node.next_node:
                sll_print += str(node.data) + '\n'
            else:
                sll_print += str(node.data)
            node = node.next_node
        return sll_print

    def sorted_insert(self, value):
        """inserts a node in the sll in a sorted way
        Args:
            None
        Returns:
            The square's area
        """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        else:
            current = self.__head
            previous = None
            flag = None
            while current:
                if new_node.data < current.data and previous is None:
                    new_node.next_node = current
                    self.__head = new_node
                    flag = 1
                    break
                elif new_node.data < current.data:
                    new_node.next_node = current
                    previous.next_node = new_node
                    flag = 1
                    break
                previous = current
                current = current.next_node
                if current is None and flag is None:
                    previous.next_node = new_node
