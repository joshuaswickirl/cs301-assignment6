import env

from tree import Tree, Node

#
#   Tests for Node class
#

# .__init__
def test_Node_init_1():
    _node = Node(1)
    assert _node.data == 1

def test_Node_init_2():
    _node = Node(1)
    assert _node.children == []


# .get_data
def test_Node_get_data():
    _node = Node(1)
    assert _node.get_data() == 1


# .set_data
def test_Node_set_data():
    _node = Node(1)
    _node.set_data(2)
    assert _node.data == 2


# .get_children
def test_Node_get_children_1():
    _node = Node(1)
    assert _node.get_children() == []

def test_Node_get_children_2():
    _node = Node(1)
    _node.children = [1,2,3]
    assert _node.get_children() == [1,2,3]


# .add_child
def test_Node_add_child_1():
    _node = Node(1)
    _node.add_child(2)
    assert _node.children[0].data == 2

def test_Node_add_child_2():
    _node = Node(1)
    _node.add_child(2)
    _node.add_child(3)
    assert _node.children[1].data == 3


#
#   Tests for Tree class
#

# .__init__
def test_Tree_init_1():
    _tree = Tree()
    assert _tree.head.data == None


# .is_empty()
def test_Tree_is_empty_1():
    _tree = Tree()
    assert _tree.is_empty() == True

def test_Tree_is_empty_2():
    _tree = Tree()
    _tree.head.data = 1
    assert _tree.is_empty() == False


# .search_for(item)
def test_Tree_search_for_1():
    _tree = Tree(1)
    _tree.head.add_child(2)
    _tree.head.add_child(3)
    _tree.head.get_children()[0].add_child(4)
    _tree.head.get_children()[0].add_child(5)
    _tree.print_tree()
    assert _tree.search_for(5) == True

def test_Tree_search_for_2():
    _tree = Tree(1)
    _tree.head.add_child(2)
    _tree.head.add_child(3)
    _tree.head.get_children()[0].add_child(4)
    _tree.head.get_children()[0].add_child(5)
    _tree.print_tree()
    assert _tree.search_for(6) == False

def test_Tree_search_for_3():
    _tree = Tree(1)
    _tree.head.add_child(2)
    _tree.head.add_child(3)
    _tree.head.get_children()[0].add_child(4)
    _tree.head.get_children()[0].add_child(5)
    _tree.head.get_children()[1].add_child(6)
    _tree.head.get_children()[1].add_child(7)
    _tree.print_tree()
    assert _tree.search_for(6) == True