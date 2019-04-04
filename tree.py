class List():
    
    def __init__(self):
        """
        Constructor method for class List
        """
        self.head = None
    
    def add(self,item):
        """
        Adds new item to the start of the list. Requires item and returns nothing. 
        
        Runs in constant time.
        """
        new_node = Node(item)
        new_node.set_next_node(self.head)
        self.head = new_node
        
    def remove(self,item):
        """
        Removes an item from list. Requires item and modifies the list and if 
        item is not found, error is raised.
        
        Runs in linear time.
        """
        current_node = self.head
        last_node = None
        item_found = False
        while not item_found:
            if current_node.data == item:
                next_node = current_node.get_next_node()
                del current_node
                if last_node == None:
                    self.head = next_node
                else:
                    last_node.set_next_node(next_node)
                item_found = True
            else:
                # prep for next iteration
                last_node = current_node
                current_node = current_node.get_next_node()

    def search(self,item):
        """
        Searches list for item. Requires item and returns boolean value.
        
        Runs in linear time.
        """
        node = self.head
        item_found = False
        while not item_found:
            if node.data == item:
                item_found = True
            else:
                node = node.get_next_node()
                if node == None:
                    break
        return item_found

    def isEmpty(self):
        """
        Checks if list is empty, Requires nothing and returns boolean value.
        
        Runs in constant time.
        """
        if self.head == None:
            return True
        else:
            return False

    def size(self):
        """
        returns the size of the list. Requires no parameters and returns an int. 
        
        Runs in linear time.
        """
        num_nodes = 0
        node = self.head
        while node is not None:
            num_nodes += 1
            node = node.get_next_node()
        return num_nodes
    
    def append(self,item):
        """
        This adds a new item to the end of the list. Requires item and returns nothing. 
        
        Runs in linear time.
        """
        new_node = Node(item)
        current_node = self.head
        if current_node == None:
            self.head = new_node
        else:
            last_node = False
            while not last_node:
                next_node = current_node.get_next_node()
                if next_node == None:
                    current_node.set_next_node(new_node)
                    last_node = True
                else:
                    current_node = current_node.get_next_node()

    def index(self,item):
        """
        Returns the position of item in list. Requires item and returns index. 
       
        Runs in linear time.
        """
        item_index = 0
        item_found = False
        current_node = self.head
        while not item_found:
            if current_node == None:
                raise IndexError
            if current_node.get_data() == item:
                item_found = True
            else:
                current_node = current_node.get_next_node()
                item_index += 1
        return item_index

    def insert(self,pos,item):
        """
        Adds new item to the list at position pos. Requires item and returns nothing.
        If list is too short, raises an error. 
        
        Runs in linear time.
        """
        current_node = self.head
        current_index = 0
        index_found = False
        new_node = Node(item)
        while not index_found:
            if current_node == None and pos == 0:
                self.add(item)
                index_found = True
            elif current_node == None:
                raise IndexError
            elif pos == current_index + 1:
                next_node = current_node.get_next_node()
                if next_node == None:
                    current_node.set_next_node(new_node)
                else:
                    new_node.set_next_node(next_node)
                    current_node.set_next_node(new_node)
                index_found = True
            else:
                current_node = current_node.get_next_node()
                current_index += 1

    def pop(self):
        """
        Pops the last item in the list.Requires nothing and returns an item. 
        If list is entered, an error is raised. 
        
        Runs in linear time.
        """
        current_node = self.head
        while True:
            # No node exists
            if current_node == None:
                raise IndexError
            # This is the last node, only happens when there is one node
            elif current_node.get_next_node() == None:
                item = current_node.get_data()
                del current_node
                self.head = None
                return item
            # The next node is the last node
            elif current_node.get_next_node().get_next_node() == None:
                next_node = current_node.get_next_node()
                item = next_node.get_data()
                del next_node
                current_node.set_next_node(None)
                return item
            else:
                current_node = current_node.get_next_node()

    def pop(self,pos):
        """
        Removes an item at the position pos. Requires positiona and returns item. 
        
        Runs in linear time.
        """
        current_node = self.head
        current_index = 0
        last_node = None
        while True:
            # No node exists
            if current_node == None:
                raise IndexError
            # Pop index 0, shift head if next_node exists
            elif pos == 0:
                item = current_node.get_data()
                next_node = current_node.get_next_node()
                if next_node != None:
                    self.head = next_node
                else:
                    self.head = None
                del current_node
                return item
            # Node before requested index
            elif current_index == (pos - 1):
                target_node = current_node.get_next_node()
                if target_node == None:
                    raise IndexError
                current_node.set_next_node(target_node.get_next_node())
                item = target_node.get_data()
                del target_node
                return item
            # Prep next iteration
            else:
                current_node = current_node.get_next_node()
                current_index += 1


    def print(self):
        """
        Prints list.
        """        
        node = self.head
        while node is not None:
            print(f"Current node data: {node.get_data()}, next node: {node.get_next_node()}")
            node = node.get_next_node()

class Node():
    def __init__(self, input_data):
        """
        Constructor method for class node.
        """
        self.data = input_data
        self.next_node = None
    
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

    def get_next_node(self):
        """
        Gets refrence to next node, Requires nothing and returns node. 
        """
        return self.next_node

    def set_next_node(self, new_next_node):
        """
        Sets refrence to the next node, requires new_next_node and returns nothing.
        """
        self.next_node = new_next_node
