class BNode(Object):
    """ Binary tree node. """

    def __init__(self, data, left=None, right=None):
        assert left is None or isinstance(left, BNode)
        assert right is None or isinstance(right, BNode)

        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        """ Debugging-friendly representation. """

        return "<BNode %s>" % self.data

    def find(self, sought):
        """ Return node with this data.

            Start here. Return None if not found.
        """

        node = self

        while node:
            print "checking", node.data

            # concept is that if the node.data
            # where we are currently on has the
            # value of sought, we found the node.
            # if the node.data is greater than sought
            # we know that we should look to the left
            # where data is lesser. Else, go right.
            if node.data == sought:
                return node
            elif sought < node.data:
                node = node.left
            elif sought > node.data:
                node = node.right

