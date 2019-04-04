import env

from tree import Tree, Node

#
#   Tests for Tree class
#

# .__init__
def test_init_1():
    _tree = Tree()
    assert _tree.head == None


# .is_empty()
def test_is_empty_1():
    _tree = Tree()
    assert _tree.is_empty() == True

def test_is_empty_2():
    _tree = Tree()
    _tree.data = 1
    assert _tree.is_empty() == False


# .search_for(item)
def test_search_for_1():
    pass

def test_searh_for_2():
    pass


# .print_tree()
def test_print_tree():
    pass


#
#   Tests for Node class
#

# .__init__
def test_node_init_1():
    _node = Node(1)
    assert _node.data == 1

def test_node_init_2():
    _node = Node(1)
    assert _node.children = []


# .get_data
def test_node_get_data():
    _node = Node(1)
    assert _node.get_data == 1


# .set_data
def test_node_set_data():
    _node = Node(1)
    _node.set_data(2)
    assert _node.data == 2


# .get_children
def test_node_get_children_1():
    _node = Node(1)
    assert _node.get_children == []

def test_node_get_children_2():
    _node = Node(1)
    _node.children = [1,2,3]
    assert _node.get_children == [1,2,3]


# .add_child
def test_node_add_child_1():
    _node = Node(1)
    _node.add_child(2)
    assert _node.data == 2

def test_node_add_child_2():
    _node = Node(1)
    child_node_1 = Node(2)
    child_node_2 = Node(3)
    _node.add_child(_child_node_1)
    _node.add_child(_child_node_2)
    assert _node.children == [_child_node_1,child_node_2]

