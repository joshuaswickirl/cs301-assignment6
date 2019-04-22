import env

from directed_graph import DirectedGraph, Vertex

#
#   Tests for Vertex class
#

# .__init__
def test_Vertex_init_1():
    vertex = Vertex(1)
    assert vertex.data == 1

def test_Vertex_init_2():
    vertex = Vertex(2)
    assert vertex.directed_edges == set()


# .get_data
def test_Vertex_get_data_1():
    vertex = Vertex(1)
    assert vertex.get_data() == 1

def test_Vertex_get_data_2():
    vertex = Vertex(3)
    assert vertex.get_data() == 3


# .set_data
def test_Vertex_set_data_1():
    vertex = Vertex(1)
    vertex.set_data(2)
    assert vertex.get_data() == 2

def test_Vertex_set_data_2():
    vertex = Vertex(1)
    vertex.set_data(0)
    assert vertex.get_data() == 0


# .get_directed_edges
def test_Vertex_get_directed_edges_1():
    vertex = Vertex(1)
    assert vertex.get_directed_edges() == set()

def test_Vertex_get_directed_edges_2():
    vertex = Vertex(1)
    edge_1 = Vertex(2)
    edge_2 = Vertex(3)
    vertex.directed_edges = {edge_1,edge_2}
    assert vertex.get_directed_edges() == {edge_1,edge_2}


# .add_directed_edge
def test_Vertex_add_directed_edge_1():
    vertex = Vertex(1)
    edge_1 = Vertex(2)
    vertex.add_directed_edge(edge_1)
    assert vertex.directed_edges == {edge_1}

def test_Vertex_add_directed_edge_2():
    vertex = Vertex(1)
    edge_1 = Vertex(3)
    edge_2 = Vertex(4)
    vertex.add_directed_edge(edge_1)
    vertex.add_directed_edge(edge_2)
    assert vertex.directed_edges == {edge_1,edge_2}


#
#   Tests for DirectedGraph class
#

# .__init__
def test_DirectedGraph_init_1():
    graph = DirectedGraph()
    assert graph.verticies == set()


# .create_vertex
def test_DirectedGraph_create_vertex_1():
    graph = DirectedGraph()
    graph.create_vertex(1)
    assert next(iter(graph.verticies)).get_data() == 1


# .create_edge
def test_DirectedGraph_create_edge_1():
    graph = DirectedGraph()
    vertex_1 = graph.create_vertex(1)
    vertex_2 = graph.create_vertex(2)
    graph.create_edge(vertex_1,vertex_2)
    assert vertex_1.get_directed_edges() == {vertex_2}


# .search_for
def test_DirectedGraph_search_for_1():
    graph = DirectedGraph()
    graph.create_vertex(1)
    assert graph.search_for(1) == True

def test_DirectedGraph_search_for_2():
    graph = DirectedGraph()
    vertex_1 = graph.create_vertex(1)
    vertex_2 = graph.create_vertex(2)
    graph.create_edge(vertex_1,vertex_2)
    assert graph.search_for(2) == True


# .is_empty
def test_DirectedGraph_is_empty_1():
    graph = DirectedGraph()
    assert graph.is_empty() == True

def test_DirectedGraph_is_empty_2():
    graph = DirectedGraph()
    graph.create_vertex(1)
    assert graph.is_empty() == False