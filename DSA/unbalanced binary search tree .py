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
        if not self.root:
            self.root=Node(data)
        else:
            q_temp=queue.Queue(maxsize=0)
            q_temp.put(self.root)

            while True:
                res=q_temp.get()

                if not res.leftc:
                    res.leftc=Node(data)
                    break
                else:
                    q_temp.put(res.leftc)
                
                if not res.rightc:
                    res.rightc=Node(data)
                    break
                else:
                    q_temp.put(res.rightc)

    def levelOrder(self):
        stack=[]

        if not self.root:
            return stack 

        q_temp=queue.Queue(maxsize=0)
        q_temp.put(self.root)

        while not q_temp.empty():
            res=q_temp.get()
            stack.append(res.data)

            if res.leftc:
                q_temp.put(res.leftc)
            if res.rightc:
                q_temp.put(res.rightc)
        return stack

    def search(self,key):
        return self._search(self.root,key)

    def _search(self,root,key):
        if not root:
            return -1
        # a search in an AVL tree or balanced
        # binary search tree will be faster

        # searching will only take
        # a number of comparisons as to an
        # unbalanced binary search tree

        # might take O(n) due to the
        # linear manner of the representation
        # of the nodes in the tree
        
        elif key==root.data:
            return root
        elif key>=root.data:
            return self._search(root.rightc,key)
        else:
            return self._search(root.leftc,key)

    def maxHeight(self):
        return self._maxHeight(self.root)

    def _maxHeight(self,root):
        if not root:
            return -1

        # accumulate the values of each subtree
        # recursively then compare
        # left and right values of each subtree
        # even the last nodes which has height of 0
        return max(1+self._maxHeight(root.leftc),1+self._maxHeight(root.rightc))

    def balanceTree(self):
        pass

    # formula for balance is b(n)=left height - right height
    # where n is the current root
    # formula for threshold is |left height - right height|<=1


if __name__ == "__main__":
    tree=Tree()
    for data in [7,6,9,6,4]:
        tree.insert(data)

    print(tree.levelOrder())
    print(tree.search(1))
    print(tree.maxHeight())



                