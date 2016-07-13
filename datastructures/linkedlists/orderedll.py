from node import Node

class OrderedList:
    def __init__(self):
        self.head = None

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

    def add(self, item):
      current = self.head
      previous = None
      stop = False
      while current != None and not stop:
          if current.getData() > item:
              stop = True
          else:
              previous = current
              current = current.getNext()

      temp = Node(item)
      if previous == None:
          temp.setNext(self.head)
          self.head = temp
      else:
          temp.setNext(current)
          previous.setNext(temp)

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

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

    def index(self, item):
        # get position of item in LL
        # assume item is in list?
        found = False
        stop = False
        current = self.head
        count = 0
        while not found and current != None and not stop:
            if current.getData() == item:
                found = True 
            elif current.getData() > item:
                stop = True
            else:
                  current = current.getNext()
                  count += 1
        if found is False:
            return None
        return count

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

    def pop(self, pos=None):
        if pos is None:
            # if the position is not specified
            # assume that pop must happen at end of LL
            pos = self.size()-1
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
