class Node():
    def __init__(self, input_data=None):
        """
        Creates new node with input data and an empty list
        of children nodes.

        Runs in constant time, O(n).
        """
        self.data = input_data
        self.children = []
    

    def get_data(self):
        """
        Returns the node's data.

        Runs in constant time, O(n).
        """
        return self.data


    def set_data(self, new_data):
        """
        Sets the node's data, overwritting existing data.

        Runs in constant time, O(n).
        """
        self.data = new_data


    def get_children(self):
        """
        Returns list of children nodes. 

        Runs in constant time, O(n).
        """
        return self.children
    

    def add_child(self, input_data):
        """
        Creates a new node and lists it as a child node.

        Runs in constant time, O(n).
        """
        newNode = Node(input_data)
        self.children.append(newNode)


class Tree():
    def __init__(self, input_data=None):
        """
        Adds tree head and inital Node.

        Runs in constant time, O(1).
        """
        self.head = Node(input_data)


    def search_for(self, item, node=None):
        """
        Recursively searches for the given item starting at 
        the tree head unless a specific node is given.

        Runs in linear time, O(n).
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
        Checks if tree is empty.
        
        Runs in constant time, O(1).
        """
        if self.head.get_data() == None and self.head.children == []:
            return True
        else:
            return False


    def print_tree(self, node=None):
        """
        Prints tree structure.

        Runs in linear time, O(n).
        """
        if node == None:
            node = self.head
        print(node.data, end='')
        print("[", end='')
        for child in node.children:
            self.print_tree(child)
        print("]", end='')
