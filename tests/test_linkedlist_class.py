import pytest
from src.main import *


class TestLinkedList:
    def testIsEmpty(self):
        # Test when List is empty
        myList = LinkedList()
        assert myList.isEmpty() == True

        # Test when List is not empty
        myList.push("A")
        assert myList.isEmpty() == False

    def testExtractList(self):
        myList = LinkedList()
        myList.push("A")
        myList.push("B")
        assert myList.extractList() == "B\nA"

    def testPushOperation(self):
        scenarios = [
            (("push", "A"), "A"),
            (("push", "A"), ("push", "B"), "B\nA"),
        ]

        for scenario in scenarios:
            myList = LinkedList()
            for method_name, *args in scenario[:-1]:
                method = getattr(myList, method_name)
                method(*args)

            expected_result = scenario[-1]
            assert myList.extractList() == expected_result

    def testPopOperation(self):
        scenarios = [
            (("pop",), ""),
            (("push", "A"), ("push", "B"), ("pop",), "A"),
            (("push", "A"), ("pop",), ("push", "B"), "B"),
        ]

        for scenario in scenarios:
            myList = LinkedList()
            for method_name, *args in scenario[:-1]:
                method = getattr(myList, method_name)
                method(*args)

            expected_result = scenario[-1]
            assert myList.extractList() == expected_result

    def testSizeCalculation(self):
        scenarios = [
            (("push", "A"), ("pop",), 0),
            (("push", "A"), ("push", "B"), 2),
            (("push", "A"), ("push", "B"), ("pop",), 1),
            (("push", "A"), ("pop",), ("push", "B"), 1),
        ]

        for scenario in scenarios:
            myList = LinkedList()
            assert myList.size() == 0

            for method_name, *args in scenario[:-1]:
                method = getattr(myList, method_name)
                method(*args)

            expected_result = scenario[-1]
            assert myList.size() == expected_result