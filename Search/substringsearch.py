class CheckSubString:
    def __init__(self, tree, sub_string):
        self.tree = tree
        self.sub_string = sub_string
        self.main_string = tree._string
        self.last_index = 0

    def traverse(self, node, sub_string, latest_end):
        if sub_string:
            # Since each child starts with a unique character we will pursue the process for the child that sub-string
            # Starts with the frist character of this edge
            item = next(((char, child) for char, child in node.children.items() if sub_string.startswith(char)), None)

            if item:
                char, child = item
                start, end = child.start, child.end
                # If the edge is equal with sub-string returns the index
                if self.tree._string[start: end + 1] == sub_string:
                    return end - len(self.sub_string) + 1, 1
                # sub-string starts with the frist character of our edge but es not equal with it
                # So call the travese for the rest of sub-string (from the lenght of previous edge)
                print([sub_string, start, end])
                return self.traverse(child, sub_string[end - start + 1:], start + len(sub_string))
            else:
                # At this level there were no edge that sub-string starts with its leading character.
                return -1

        return latest_end - len(self.sub_string)

    def check(self):
        if self.tree.root is None:
            return -1
        if not isinstance(self.sub_string, str):
            return -1
        if not self.sub_string:
            # Every string starts with an empty string
            return 0

        return self.traverse(self.tree.root, self.sub_string, 0)
