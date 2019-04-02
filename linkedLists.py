'''
Given an Linked List define a function to return the reverse Linked List.
Define another function to find if a node exists inside a Linked List.
Remember Python don't provide a linked list implementation.

Example:
Input
30->40->50->60->NONE
linkedList.find(50)

Output
60->50->40->30->NONE
50

Solved by: Sadri Shehu
Date: 4/2/2019
'''
# Node class
class Node:
    # Function to initialize the node object
    def __init__(self, nodeValue):
        self.val = nodeValue  # Assign value
        self.next = None  # Initialize next as null
  
# LinkedList class
class ListNode:
    # Function to initialize the LinkedList
    def __init__(self): 
        self.head = None

    def push(self, nodeValue):
    # Pushes all nodes and to insert a new 
    # node in the beginning of the list
        newNode = Node(nodeValue)
        newNode.next = self.head
        self.head = newNode

    def append(self, nodeValue):
    # Appends the LinkedList by inserting
    # at the end of the list a new node
        if not self.head:
        # If the list is empty we must
        # initialize the head first
            newNode = Node(nodeValue)
            self.head = newNode
            return
        # Otherwise if we have nodes
        # in the list than we append
        curr = self.head
        while curr.next:
            curr = curr.next
        newNode = Node(nodeValue)
        curr.next = newNode

    def find(self, key):
        # Search for the value and the key
        # If it's found will return the value
        curr = self.head
        while curr and curr.val != key:
            curr = curr.next
        return curr  # Will be None if not found

    def printList(self): 
        curr = self.head 
        while(curr): 
            print(curr.val,'->', end = ' ')
            curr = curr.next
        print('NONE')

    def reverse(self):
        curr = self.head
        prevNode = None
        nextNode = None
        while curr:
        # Here we revers all nodes starting from the head by
            nextNode = curr.next # saving the current next to the nextNode
            curr.next = prevNode # current next becomes preview node
            prevNode = curr # preview node becomes the current one
            curr = nextNode # current node becomes the next one saved to nextNode
        self.head = prevNode # Finally when we reach NONE the head of the list  
        # becomes the preview node

linkedList = ListNode()
linkedList.push(40)
linkedList.append(50)
linkedList.push(30)
linkedList.append(60)
linkedList.printList()
linkedList.reverse()
linkedList.printList()
