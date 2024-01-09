# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def getData(self):
        return self.__data

    def getNext(self):
        return self.__next

    def setData(new_data):
        self.__data = new_data
    
    def setNext(new-next):
        self.__next = new_next


class LinkedList:
    def __init__(self):
        self.__head = None

    def isEmpty():
        return self.__head is None

    def size():
        count = 0
        cur_node = self.__head

        while cur_node is not None:
            count += 1
            cur_node = cur_node.getNext()
        
        return count

    def push(new_data):
        """
        Insert a new node in the beggining of the list
        """
        new_node = Node(new_data)
        new_node.setNext = self.__head
        self.__head = new_node

    def pop():
        """
        Return the header node and move the Head to the next node
        """
        if self.isEmpty() :
            return None

        initial_node = self.__head
        self.__head = initial_node.getNext()
        return initial
        

        


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
