class Vertex():
    def __init__(self, input_data=None):
        """
        Creates new vertex with input data and an empty list
        of directed edges

        Runs in constant time, O(1).
        """
        self.data = input_data
        self.directed_edges = set()
    

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
        self.directed_edges.add(edge_vertex)

    def print(self):
        print(f"Vertex: {self}, Data: {self.get_data}, Directed Edges: {self.get_directed_edges})


class DirectedGraph():
    def __init__(self):
        self.verticies = set()


    def create_vertex(self, vertex_data):
        new_vertex = Vertex(vertex_data)
        self.verticies.add(new_vertex)
        return new_vertex


    def create_edge(self, vertex_1, vertex_2):
        vertex_1.add_directed_edge(vertex_2)


    def search_for(self, item):
        pass

    
    def is_empty(self):
        empty = True
        if len(self.verticies) > 0:
            empty = False
        return 
        
    
    def print(self):
        pass