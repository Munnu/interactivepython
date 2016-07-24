class Node(object):
    """ Node in a tree. """

    def __init__(self, data, children=None):
        # children holds a list of Node types
        children = children or []  # empty list if children is None
        assert isinstance(children, list), \
            "children must be a list!"
        self.data = data
        self.children = children

    def __repr__(self):
        """ reader-friendly representation. """

        return "<Node %s>" % self.data

    def find_dft(self, data):
        """ Return node object with this data.
            Start here. Return None if not found.
            DFT (Depth-first Traversal) implementation
            also uses the concept of a stack
        """

        to_visit = [self]

        while to_visit:
            node = to_visit.pop()  # small differences
            if node.data == data:
                return node

            to_visit.extend(node.children)

    def find_bft(self,data):
        """ Return node object with this data.
            BFT (Breadth-first Traversal) implementation
            also uses the concept of a queue
        """

        to_visit = [self]

        while to_visit:
            node = to_visit.pop(0)  # small differences
            if node.data == data:
                return node

            to_visit.extend(node.children)


# example of implementation
sharon = Node("Sharon")
sharon.children.append(Node("Angie"))
sharon.children.append(Node("Stefan"))
sharon.children

# another way to do this would be something like this
# sharon = Node("sharon", [ Node("Angie"), Node("Stefan")])
