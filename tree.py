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
    def __init__(self, input_data=None):
        """
        Adds tree head and inital Node.
        """
        self.head = Node(input_data)

    def search_for(self, item, node=None):
        """
        Recursively searches for the given item starting at 
        the tree head unless a specific node is given.
        """
        item_found = False
        if node == None:
            node = self.head
        if node.get_data() == item:
            item_found = True
        else:
            for child_node in node.get_children():
                if item_found == True:
                    break
                else:
                    item_found = self.search_for(item,child_node)
        return item_found

    def is_empty(self):
        """
        Checks if list is empty, Requires nothing and returns boolean value.
        
        Runs in constant time.
        """
        if self.head.data == None and self.head.children == []:
            return True
        else:
            return False

    def print_tree(self,node=None):
        """
        Prints tree structure
        """
        if node == None:
            node = self.head
        print(node.data, end='')
        print("[", end='')
        for child in node.children:
            self.print_tree(child)
        print("]", end='')
