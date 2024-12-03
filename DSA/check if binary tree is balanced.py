import queue

class Node:
    def __init__(self,data):
        self.data=data
        self.leftc=None
        self.rightc=None


class Tree:
    def __init__(self):
        self.root=None

    def insert(self,data):
        