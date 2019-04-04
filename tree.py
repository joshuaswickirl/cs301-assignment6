class Tree(Node):
    """
    Extends Node
    """

    def search(self,item):
        """
        Searches tree for item. Requires item and returns boolean value.
        
        Runs in linear time.
        """
        pass
        

    def is_empty(self):
        """
        Checks if list is empty, Requires nothing and returns boolean value.
        
        Runs in constant time.
        """
        if self.head == None:
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
            child.printNode()
        print("]", end='')


class Node():
    def __init__(self, input_data):
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
    
    def add_child(self):
        """
        adds a child node
        """
        newNode = Node(input_data)
        self.children.append(newNode)
