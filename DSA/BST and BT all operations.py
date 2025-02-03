import queue
from argparse import ArgumentParser
import ast

from sys import maxsize as MAX

class Node:
    def __init__(self,data=None):
        self.data=data
        self.leftc=None
        self.rightc=None

class Tree:
    def __init__(self):
        self.root=None
        self.COUNT=[10]
        self.MAX = MAX
        self.MIN = -MAX - 1

    def insert(self,data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(self.root, data) 
            # this is the helper method for insert since recursion 
            # cannot be done directly especially if attribute passed will be changed

    def _insert(self, root, data):
        """
        data cannot be null here as this insertion involves creating a binary search
        """
        if data >= root.data:
            if not root.rightc:
                root.rightc=Node(data)
            else:
                self._insert(root.rightc,data)
        else:
            if not root.leftc:
                root.leftc=Node(data)
            else:
                self._insert(root.leftc,data)

    def createInLevelOrder(self, dataset: list):
        # sample dataset: [1], [1,2]
        length, i = len(dataset), 0
        q_temp = queue.Queue()

        # O(n) time complexity
        while True:
            if not self.root:
                self.root = Node(dataset[i])        
                q_temp.put(self.root)

                # when node has already been inserted in the queue and the tree that means
                # the index has moved in the next position in the dataset provided
                i += 1
                if i == length:
                    break
            else:
                res = q_temp.get()
                if res.leftc is None:
                    if dataset[i] is None:
                        res.leftc = None
                    else:
                        res.leftc = Node(dataset[i])
                        q_temp.put(res.leftc)
                    
                    i += 1
                    # if the node has been inserted that means the index has moved so it's index 
                    # number is increased when the index == length that means there is nothing to insert
                    if i == length:
                        break

                if res.rightc is None:
                    if dataset[i] is None:
                        res.rightc = None
                    else: 
                        res.rightc = Node(dataset[i])
                        q_temp.put(res.rightc)

                    i += 1
                    if i == length:
                        break

    def display(self,root,space): 
        # Base case  
        if not root:
            return
  
        # Increase distance between levels  
        space += self.COUNT[0] 
  
        # Process right child first  
        self.display(root.rightc, space)  
  
        # Print current node after space count
        print()
        for _ in range(self.COUNT[0], space): 
            print(end=" ")  
        print(root.data)  
  
        # Process left child  
        self.display(root.leftc, space)

    def levelOrder(self):
        if self.root:
            q_temp=queue.Queue()
            stack=[]

            # enqueue the first element in the 
            # tree which is the root node
            q_temp.put(self.root) 

            # while q_temp is full that means that 
            # there are still elements to traverse
            while not q_temp.empty(): 

                # dequeue element at the front and get its value
                res=q_temp.get()  
                stack.append(res.data)
                print(res.data, end=' ')

                # after dequeuing element
                # if even one of these children is 
                # NULL dont enqueue anymore
                if res.leftc: 
                    q_temp.put(res.leftc)
                if res.rightc:
                    q_temp.put(res.rightc)

            return stack
        
    def reverseLevelOrder(self):
        if self.root:
            q_temp = queue.Queue()
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

            rev_stack = []
            while stack:
                res = stack.pop()
                rev_stack.append(res.data)
                print(res.data, end=' ')

            return rev_stack

    def preOrder(self): 
        # root, left, right
        self._preOrder(self.root)

    def _preOrder(self,root): 
        # if real or current root is NULL then
        #  function just returns
        if root: 
            print(root.data, end=' ')
            # always process root first then left then right
            self._preOrder(root.leftc) 
            self._preOrder(root.rightc)

    def postOrder(self): 
        # left, right, root
        self._postOrder(self.root)
        
    def _postOrder(self, root):
        # real root will only be excuted only when 
        # left and right subtrees are done
        if root:
            self._postOrder(root.leftc)
            self._postOrder(root.rightc)
            print(root.data, end=' ')

    def inOrder(self): 
        # left, root, right
        self._inOrder(self.root)

    def _inOrder(self, root):
        # last left that is NULL indicates that root can 
        # now be processed since last left is now done
        if root: 
            self._inOrder(root.leftc)
            print(root.data, end=' ')
            self._inOrder(root.rightc)

    def print2DUtil(self,root,space): 
        # Base case  
        if not root: 
            return
  
        # Increase distance between levels  
        space += self.COUNT[0] 
  
        # Process right child first  
        self.print2DUtil(root.rightc, space)  
  
        # Print current node after space  
        print('')  
        for _ in range(self.COUNT[0], space): 
            print(end=" ")  
        print(root.data)  
  
        # Process left child  
        self.print2DUtil(root.leftc, space)

    def maxHeight(self):
        return self._maxHeight(self.root)

    def _maxHeight(self,root):
        # when base case is reached all 1's will be accumulated and build the height of the tree
        if not root: 
            return 0
        
        # left will be compared to rights height and return the height of larger value
        left_max = 1 + self._maxHeight(root.leftc) 
        right_max = 1 + self._maxHeight(root.rightc)

        # there is no telling what the depth of both subtrees will be, either left or right is the largest
        return max(left_max, right_max) 

    def maxWidth(self):
        return self._maxWidth(self.root)

    def _maxWidth(self,root):
        if root:
            # when tree is empty it just returns zero since loop never gets executed
            cur_max = 0 
            q_temp = queue.Queue()
            # enqueue root node to initialize
            q_temp.put(root)

            # when queue is empty it has traversed all nodes so stop
            while not q_temp.empty():
                # get the current length of level
                length = q_temp.qsize()
                # get length of current queue and compare with cur_max
                cur_max = max(length, cur_max) 

                # dequeing should be based in length of current queue 
                while length: 
                    res = q_temp.get()
                    if res.leftc:
                        q_temp.put(res.leftc)

                    # enqueue the children of the parents that were dequeued
                    if res.rightc: 
                        q_temp.put(res.rightc)
                    length -= 1
            return cur_max
        
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
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
        
        elif key == root.data:
            return root
        elif key >= root.data:
            return self._search(root.rightc,key)
        else:
            return self._search(root.leftc,key)
        
    # def insert(self, data):
    #     if not self.root:
    #         self.root=Node(data)
    #     else:
    #         q_temp = queue.Queue(maxsize=0)
    #         q_temp.put(self.root)

    #         while True:
    #             res = q_temp.get()

    #             if not res.leftc:
    #                 res.leftc = Node(data)
    #                 break
    #             else:
    #                 q_temp.put(res.leftc)
                
    #             if not res.rightc:
    #                 res.rightc=Node(data)
    #                 break
    #             else:
    #                 q_temp.put(res.rightc)

    @property
    def maxNum(self):
        # this is if root is NULL
        if not self.root:
            return -1
        return self._maxNum(self.root)

    def _maxNum(self,root):
        if not root:
            return 0
        
        left_val = self._maxNum(root.leftc)
        right_val = self._maxNum(root.rightc)
        return self.maxOfThree(left_val, right_val, root.data)

    @property
    def minNum(self):
        if not self.root:
            return -1
        return self._minNum(self.root)

    def _minNum(self,root):
        # if we return 0 just like in the
        # max of a tree then 0 will just be the min
        # so initially when NULL is reached we have to return its current root.data
        if not root:
            return MAX
        
        # when values are returned compare
        # both values and return the max of the two
        left = self._minNum(root.leftc)
        right = self._minNum(root.rightc)
        return self.minOfThree(root.data, left, right)

    def maxOfThree(self, num1, num2, num3):
        if num1 >= num2 and num1 >= num3:
            return num1
        elif num2 >= num1 and num2 >= num3:
            return num2
        return num3

    def minOfThree(self, num1, num2, num3):
        if num1 <= num2 and num1 <= num3:
            return num1
        elif num2 <= num1 and num2 <= num3:
            return num2
        return num3
        
    @property
    def getRoot(self):
        return self.root
    

    
if __name__ == "__main__":
    # problem:

    # method:

    # idea:
    # when first depth is found set it as the current max
    # when 2nd depth is found compare it always to the current max
    # if that 2nd depth is > than cur max then change cur max to/= depth
    # 

    # figure out:

    # cases:
    # 1. if tree is empty return 0
    # 2. root only then return 1 max is incremented by one

    # samples:
    #               *
    #         *          *
    #      *     *    *     *
    #    *   * *   *
    #           *  
    # as left side goes down max is incremented 
    # when left reaches NULL return
    # right side is now proceessed but we see it is still NULL
    # so we return from the function
    # if right is not NULL then we 
    parser = ArgumentParser()
    parser.add_argument("--create_method", type=str, default="level-order", help="specifies whether the tree should be created recursively or by level order (breadth)")
    parser.add_argument("--data", nargs="+", default=["1"], help="ex. 1 None 2 None 3 4 5 6 None if 'level-order' is chosen as --create_method, and 1 5 3 1 5 4 10 8 if 'recursive' is chosen as --create_method")
    args = parser.parse_args()
    
    tree = Tree()

    if args.create_method == "level-order":
        # sample command: python "BST and BT all operations.py" --create_method "level-order" --data 1 None 2 None 3 4 5 6 None

        data = [ast.literal_eval(datum) for datum in args.data]
        tree.createInLevelOrder(data)

        print('inorder: ')
        tree.inOrder()

        print('preorder: ')
        tree.preOrder()

        print('postorder: ')
        tree.postOrder()

        tree.print2DUtil(tree.root, 0)
    
    elif args.create_method == "recursive":
        # sample command: python "BST and BT all operations.py" --create_method "recursive" --data 1 5 3 1 5 4 10 8
        
        # insert data in the binary search tree
        for datum in args.data:
            datum = ast.literal_eval(datum)
            tree.insert(datum)

        tree.print2DUtil(tree.root, 0)

        print(f"the tree's max height is {tree.maxHeight()}")
        print(f"the tree's max width is {tree.maxWidth()}")


    