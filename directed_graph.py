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
        print(f"Vertex: {self}, Data: {self.data}, Directed Edges: {self.directed_edges}")


class DirectedGraph():
    def __init__(self):
        """
        Creates an empty Directed Graph.

        Runs in constant time, O(1).
        """
        self.verticies = set()


    def create_vertex(self, vertex_data):
        """
        Creates a new Vertex and adds it to the set
        of verticies associated with the graph.

        Runs in constant time, O(1).
        """
        new_vertex = Vertex(vertex_data)
        self.verticies.add(new_vertex)
        return new_vertex


    def create_edge(self, vertex_1, vertex_2):
        """
        Adds second vertex as a directed edge of the first.

        Runs in constant time, O(1).
        """
        vertex_1.add_directed_edge(vertex_2)


    def search_for(self, item):
        """
        Searchs through known verticies for for the data.

        Runs in linear time, O(n).
        """
        item_found = False
        for vertex in self.verticies:
            vertex_data = vertex.get_data()
            if vertex_data == item:
                item_found = True
                break
        return item_found

    
    def is_empty(self):
        """
        Returns True if the list is empty, False otherwise.

        Runs in constant time, O(1).
        """
        if len(self.verticies) > 0:
            return False
        else:
            return True
        
    
    def print(self):
        """
        Prints the location, data, and directed edges for each
        Vertex in the graph.

        Runs in linear time, O(n).
        """
        for vertex in self.verticies:
            vertex.print()