# author :  https://www.alphacodingskills.com/python/ds/python-delete-the-first-node-of-the-linked-list.php

# node structure
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

#class LinkedList
class LinkedList:
    def __init__(self):
        self.head = None

    
    def push_back(self, newElement):
        """ 
        Add new element at the end of the list
        """
        newNode = Node(newElement)
        if(self.head == None):
            self.head = newNode
            return
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = newNode


    def pop_front(self):
        """ 
        Delete first node of the list
        """
        if(self.head != None):
            temp = self.head
            self.head = self.head.next
            temp = None 

    
    def print_list(self):
        """ 
        Display the content of the list
        """
        temp = self.head
        if(temp != None):
            print("The list contains:", end=" ")
            while (temp != None):
                print(temp.data, end=" ")
                temp = temp.next
            print()
        else:
            print("The list is empty.")

    
    def print_first(self):
        """ 
        Display the first node of the list
        """
        temp = self.head
        if(temp != None):
            print("The first element of the linkedlist contains:", end=" ")
            print(temp.data, end=" ")
            return temp.data
        else:
            print("The list is empty.")

''' # test the code                 
MyList = LinkedList()

#Add four elements in the list.
MyList.push_back(10)
MyList.push_back(20)
MyList.push_back(30)
MyList.push_back(40)
MyList.PrintList()

#Delete the first node
MyList.pop_front()
MyList.PrintList()   '''