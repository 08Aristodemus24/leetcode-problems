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
            q_temp=queue.Queue(100)
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

                # after dequeuing element
                # if even one of these children is 
                # NULL dont enqueue anymore
                if res.leftc: 
                    q_temp.put(res.leftc)
                if res.rightc:
                    q_temp.put(res.rightc)
            return stack

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

    @property
    def getRoot(self):
        return self.root


if __name__ == "__main__":
    tree = Tree()
    dataset = input('enter input as a queue ex. 1 null 2 null 3 4 5 6 null: ').split(' ')
    tree.createInLevelOrder(dataset)

    print('inorder: ')
    tree.inOrder()

    print('preorder: ')
    tree.preOrder()

    print('postorder: ')
    tree.postOrder()

    print('root: ')
    print(tree.getRoot.data)
