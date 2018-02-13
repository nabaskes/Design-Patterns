
class CompositePattern:
    def __init__(self, data=None, children=[]):
        self.data = data
        self.children = children

    def apply(self, function):
        self.data = function(self.data)
        ch = []
        for child in self.children:
            ch.append(function(child))
        self.children = ch

    def add_data(self, data):
        self.children.append(self.__class__(data=data))

    def add_children(self, children):
        for child in children:
            self.children.append(child)
