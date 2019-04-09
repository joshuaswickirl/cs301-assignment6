class Node():
    def __init__(self, input_data=None):
        """
        Constructor method for class node.
        """
        self.data = input_data
        self.children = []
    
    def get_data(self):
        """
        Gets the data from list, Requires nothing and returns item. 
        """
        return self.data

    def set_data(self, new_data):
        """
        Sets data, requires new_data and returns nothing.
        """
        self.data = new_data

    def get_children(self):
        """
        Gets refrence to children nodes. 
        """
        return self.children
    
    def add_child(self, input_data):
        """
        adds a child node
        """
        newNode = Node(input_data)
        self.children.append(newNode)


class Tree(Node):
    """
    Extends Node
    """
    def __init__(self, input_data=None):
        self.data = input_data
        self.head = self.data
        self.children = []


    def search(self, item):
        if self.data == item:
            return True
        elif self.children == []:
            return False
        else:
            for node in self.children:
                node.search(item)
        

    def is_empty(self):
        """
        Checks if list is empty, Requires nothing and returns boolean value.
        
        Runs in constant time.
        """
        if self.head == None and self.children == []:
            return True
        else:
            return False


    def print_tree(self):
        """
        Prints tree structure
        """
        print(self.data)
        print("[", end='')
        for child in self.children:
            child.print_tree()
        print("]", end='')
