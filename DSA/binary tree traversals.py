import queue 

class Node:
    def __init__(self, data):
        self.data = data
        self.leftc = None
        self.rightc = None

class Tree:
    def __init__(self):
        self.root = None
        self.COUNT = [10]

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, root, data):
        if data >= root.data:
            if not root.rightc:
                root.rightc = Node(data)
            else:
                self._insert(root.rightc, data) # keep traversing until it reaches leaf node or last node before NULL
        else:
            if not root.leftc:
                root.leftc = Node(data)
            else:
                self._insert(root.leftc, data)

    def display(self, root, space): 
        # Base case  
        if not root: 
            return
  
        # Increase distance between levels  
        space += self.COUNT[0] 
  
        # Process right child first  
        self.display(root.rightc, space)  
  
        # Print current node after space  
        # count
        print()  
        for _ in range(self.COUNT[0], space): 
            print(end=" ")  
        print(root.data)  
  
        # Process left child  
        self.display(root.leftc, space)

    def levelOrder(self):
        if self.root:
            q_temp = queue.Queue(10)
            root = self.root
        
            q_temp.put(root) # enqueue the first element in the tree which is the root node
            while not q_temp.empty(): # while q_temp is full that means that there are still elements to traverse
                res = q_temp.get() # dequeue element at the front and get its value 
                print(res.data, end=' ')

                # after dequeuing element
                if res.leftc: # if even one of these children is NULL dont enqueue anymore
                    q_temp.put(res.leftc)
                if res.rightc:
                    q_temp.put(res.rightc)

    def reverseLevelOrder(self):
        if self.root:
            q_temp = queue.Queue(10)
            stack = []
            root = self.root


            q_temp.put(root) # enqueue the first element in the tree which is the root node
            while not q_temp.empty(): # while q_temp is full that means that there are still elements to traverse
                res = q_temp.get() # dequeue element at the front and get its value 
                stack.append(res)

                # after dequeuing element
                if res.leftc: # if even one of these children is NULL dont enqueue anymore
                    q_temp.put(res.leftc)
                if res.rightc:
                    q_temp.put(res.rightc)

            while stack:
                res = stack.pop()
                print(res.data, end=' ')

    def preOrder(self): # root, left, right
        self._preOrder(self.root)

    def _preOrder(self,root): 
        if root: # if real or current root is NULL then function just returns
            print(root.data, end=' ')
            self._preOrder(root.leftc) # always process root first then left then right
            self._preOrder(root.rightc)

    def postOrder(self): # left, right, root
        self._postOrder(self.root)
        
    def _postOrder(self, root):
        if root: # real root will only be excuted only when left and right subtrees are done
            self._postOrder(root.leftc)
            self._postOrder(root.rightc)
            print(root.data, end=' ')

    def inOrder(self): # left, root, right
        self._inOrder(self.root)

    def _inOrder(self, root):
        if root: # last left that is NULL indicates that root can now be processed since last left is now done
            self._inOrder(root.leftc)
            print(root.data, end=' ')
            self._inOrder(root.rightc)



if __name__ == "__main__":
    # the goal here is to read each keyword in the input file aka the program 
    # and to create a parse tree out of it
    # int = a + b;
    # <program> => {<stmts>} note that braces here symbolizes as the braces to enircle a block
    # {stmts} => <data type> 
    # what if all keywords are read and put in an array first, and then each keyword in the
    # array will be enqueued and inserted in a tree
    # at first level it will be a program
    # then we go to stmts
    # then stmts
    # then data type 
    # so on...
    pass

    
    



