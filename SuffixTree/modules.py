class Base:
    def __init__(self, tree):
        self.tree = tree
        self.main_string = tree._string
        self.root = tree.root


class CheckSubString(Base):
    def __init__(self, tree, sub_string, find_all=False):
        super(CheckSubString, self).__init__(tree)
        self.sub_string = sub_string
        self.latest_index = 0
        self.find_all = find_all
        self.continue_flag = False

    def traverse(self, node, sub_string):
        if sub_string:
            # Since each child starts with a unique character we will pursue the process for the child that sub-string
            # Starts with the frist character of this edge
            item = next(((char, child) for char, child in node.children.items() if sub_string.startswith(char)), None)

            if item:
                char, child = item
                start, end = child.start, child.end
                # If the edge is equal with sub-string returns the index
                if self.main_string[start: end + 1].startswith(sub_string):
                    self.latest_index = start - len(self.sub_string) + len(sub_string)
                    if self.find_all:
                        return self.find_all_match(child, sub_string)
                    return self.latest_index
                # sub-string starts with the frist character of our edge but is not equal with it
                # So call the travese for the rest of sub-string (from the lenght of previous edge)
                return self.traverse(child, sub_string[end - start + 1:])
            else:
                # At this level there were no edge that sub-string starts with its leading character.
                return -1
        self.latest_index = start - len(self.sub_string) + len(sub_string)
        if self.find_all:
            return self.find_all_match(node, sub_string)
        return self.latest_index

    def check(self):
        if self.root is None:
            return -1
        if not isinstance(self.sub_string, str):
            return -1
        if not self.sub_string:
            # Every string starts with an empty string
            return 0

        item = next(((char, child) for char, child in self.root.children.items() if self.sub_string.startswith(char)), None)
        if item:
            _, child = item
            start, end = child.start, child.end
            self.frist_start = start
            return self.traverse(child, self.sub_string[end - start + 1:])
        else:
            return -1

    def find_all_match(self, node, sub_string):

        def inner(bode, sub_string):
            for char, child in node.children.items():
                if node.leaf:
                    yield child.start - len(self.sub_string) + len(sub_string)
                else:
                    start, end = node.start, node.end
                    yield from inner(child, sub_string[end - start + 1:])

        first = node.start - len(self.sub_string) + len(sub_string)
        return first, *inner(node, sub_string)
