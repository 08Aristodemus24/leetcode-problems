class Node:
    def __init__(self,data):
        self.data=data
        self.leftc=None
        self.rightc=None
        self.height=0

class Tree:
    def __init__(self):
        self.root=None
        self.getHeight=lambda root: -1 if not root else root.height
        self.getBalance=lambda root: abs(self.getHeight(root.leftc)-self.getHeight(root.rightc))

    def convert(self,root):
        # method:
        # we recurse down the tree first
        # on our way up we check if each subtree is balanced
        # 