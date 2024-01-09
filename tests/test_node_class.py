from src.main import Node


class TestNodeClass:
    def test_get_data(self):
        node = Node("A")
        assert node.getData() == "A"

    def test_set_data(self):
        node = Node("A")
        node.setData("B")
        assert node.getData() == "B"

    def test_get_set_next(self):
        node1 = Node("A")
        assert node1.getNext() is None

        node2 = Node("B")
        node1.setNext(node2)
        assert node1.getNext() == node2
