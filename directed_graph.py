class Vertex():
    def __init__(self, input_data=None):
        """
        Creates new vertex with input data and an empty list
        of directed edges

        Runs in constant time, O(1).
        """
        self.data = input_data
        self.directed_edges = []
    

    def get_data(self):
        """
        Returns the vertex's data.

        Runs in constant time, O(1).
        """
        return self.data


    def set_data(self, new_data):
        """
        Sets the vertex's data, overwritting existing data.

        Runs in constant time, O(1).
        """
        self.data = new_data


    def get_directed_edges(self):
        """
        Returns list of vertex's directed edges. 

        Runs in constant time, O(1).
        """
        return self.directed_edges
    

    def add_directed_edge(self, edge_vertex):
        """
        Creates a new node and lists it as a child node.

        Runs in constant time, O(1).
        """
        new_vertex = Node(input_data)
        self.directed_edges.append(new_vertex)


    def remove_directed_edge(self, edge_vertex):
        pass


class DirectedGraph():
    def __init__(self, input_data=None):
        pass


    def search_for(self, item):
        pass

    
    def is_empty(self):
        pass