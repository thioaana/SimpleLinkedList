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

    def setData(self, new_data):
        self.__data = new_data

    def setNext(self, new_next):
        self.__next = new_next


class LinkedList:
    def __init__(self):
        self.__head = None

    def isEmpty(self):
        return self.__head is None

    def size(self):
        count = 0
        cur_node = self.__head

        while cur_node is not None:
            count += 1
            cur_node = cur_node.getNext()

        return count

    def push(self, new_data):
        """
        Insert a new node in the beggining of the list
        """
        new_node = Node(new_data)
        new_node.setNext(self.__head)
        self.__head = new_node

    def pop(self):
        """
        Return the header node and move the Head to the next node
        """
        if self.isEmpty():
            return None

        initial_node = self.__head
        self.__head = initial_node.getNext()
        return initial_node

    def append(self, new_data):
        """
        Insert a new node in the end of the list
        """
        current = self.__head
        if current is None:
            self.push(new_data)
        else:
            while current.getNext() is not None:
                current = current.getNext()

            new_node = Node(new_data)
            current.setNext(new_node)
            new_node.setNext(None)

    def extractList(self):
        s = ""
        current = self.__head
        while current is not None:
            s += f"{current.getData()}\n"
            current = current.getNext()
        s = s[:-1]
        return s


if __name__ == "__main__":
    myList = LinkedList()
    # myList.push('A')
    print(f"---\n{myList.extractList()}\n---")
