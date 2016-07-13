class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self, item):
        # appends to the tail of the LL
        # want to traverse through LL until current is none
        # and once found, set current.next as the new item 
        # in linked list, and set the new item's current.next()
        # as none
        current = self.head
        while current.getNext() != None:
            current = current.getNext()
        new_node = Node(item)
        current.setNext(new_node)

    def index(self, item):
        # get position of item in LL
        # assume item is in list?
        found = False
        current = self.head
        count = 0
        while not found and current != None:
            if current.getData() == item:
                found = True 
                break
            else:
                current = current.getNext()
            count += 1
        if found is False:
            return None
        return count

    def insert(self, pos, item):
        # insert item at position
        count = 0
        current = self.head
        previous = None
        while count < pos:
            previous = current
            current = current.getNext()
            count = count + 1
        new_node = Node(item)
        new_node.setNext(current)
        if previous is not None:
            previous.setNext(new_node)
        else:
            self.head = new_node
 
#    def pop(self):
#        # pops lastmost item
#        current = self.head
#        previous = None
#        if current is not None:
#            while current.getNext() is not None:
#                previous = current
#                current = current.getNext()
#            if previous is not None:
#                previous.setNext(None)
#            else:
#               self.head = None 
#            return current.getData()
    
    def pop(self, pos=0):
        current = self.head
        previous = None
        count = 0
        while count != pos:
            previous = current
            current = current.getNext()
            count = count + 1
        if current is not None:
            if pos == 0:
                self.head = current.getNext() 
            elif pos == self.size():
                previous.setNext(None)
            else:
                previous.setNext(current.getNext()) 
            return current.getData()
        return None
