# class LinkedList: 
#     def __init__(self): #Create a new node
#     def append(self, value): # Create a new node and append it to the end of the list 
#     def prepend(self, value): # create a new node and prepend it to the beginning of the list

class Node: 
    def __init__(self, value): # Create a new node with a value
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node =Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_linked_list(self):
        temp =self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        new_node =Node(value)
        if self.length ==0:# if the list is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
        return True

my_linked_list = LinkedList(10)

my_linked_list.append(5)

my_linked_list.print_linked_list()

# print(my_linked_list.head.value)



    