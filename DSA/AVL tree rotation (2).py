import queue


class Node:
    def __init__(self, data):
        self.data = data
        self.leftc = None
        self.rightc = None

        # after every insert 
        self.height = 0

class Tree:
    def __init__(self):
        self.root = None
        self.COUNT = [10]

        # return height of the node passed
        # using this Tree attribute
        self.getHeight = lambda root: -1 if not root else root.height

        # this will get the balance
        # of the children of the current root
        self.getBalance = lambda root: self.getHeight(root.leftc) - self.getHeight(root.rightc)

        self.getMinValueNode = lambda root: root if root is None or root.leftc is None else self.getMinValueNode(root.leftc)

    def insert(self, data):
        # everytime a rotation is done
        # self.root is updated to point to that
        # new root that has been rotated
        self.root = self._insert(self.root,data)

    def _insert(self, root, data):
        if not root:
            return Node(data)
        elif data >= root.data:
            root.rightc = self._insert(root.rightc, data)
        else:
            root.leftc = self._insert(root.leftc, data)

        # when a node is inserted each node's height
        # is updated recursively
        root.height = 1 + max(self.getHeight(root.leftc), self.getHeight(root.rightc))

        # here we calculate the balance for each subtree
        # check if it exceeds the max threshhold of 1
        # we pass in the current root of the recursive call
        # or the top most function call with the root
        balance = self.getBalance(root)
        # is if subtree is left heavy
        
        # if subtree if right heavy
        if balance < -1 and data >= root.rightc.data:
            root = self.leftRotate(root)
        
        # if recently inserted node does not comply
        # with order of the x,y nodes optimize its rotation first
        elif balance < -1 and data < root.rightc.data:
            root.rightc = self.rightRotate(root.rightc)
            root = self.leftRotate(root)

        # subtree is left heavy
        elif balance > 1 and data >= root.leftc.data:
            root.leftc = self.leftRotate(root.leftc)
            root = self.rightRotate(root)

        elif balance > 1 and data < root.leftc.data:
            root = self.rightRotate(root)
        
        # if balance is does not exceed 
        # absolute threshold of 1 return root 
        return root

    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, root, key): 
        # Step 1 - Perform standard BST delete 
        if not root: 
            return root 
        elif key < root.data: 
            root.leftc = self._delete(root.leftc, key) 
        elif key > root.data: 
            root.rightc = self._delete(root.rightc, key) 
        else: 
            if root.leftc is None: 
                temp = root.rightc 
                root = None
                return temp 
            elif root.rightc is None: 
                temp = root.leftc 
                root = None
                return temp 

            temp = self.getMinValueNode(root.rightc) 
            root.data = temp.data 
            root.rightc = self._delete(root.rightc, temp.data) 
  
        # If the tree has only one node, 
        # simply return it 
        if root is None: 
            return root 

        # Step 2 - Update the height of the  
        # ancestor node 
        root.height = 1 + max(self.getHeight(root.leftc), self.getHeight(root.rightc)) 
  
        # Step 3 - Get the balance factor 
        balance = self.getBalance(root) 
  
        # Step 4 - If the node is unbalanced,  
        # then try out the 4 cases 
        # Case 1 - Left Left 
        if balance > 1 and self.getBalance(root.leftc) >= 0: 
            return self.rightRotate(root) 
  
        # Case 2 - Right Right 
        if balance < -1 and self.getBalance(root.rightc) <= 0: 
            return self.leftRotate(root) 
  
        # Case 3 - Left Right 
        if balance > 1 and self.getBalance(root.leftc) < 0: 
            root.leftc = self.leftRotate(root.leftc) 
            return self.rightRotate(root) 
  
        # Case 4 - Right Left 
        if balance < -1 and self.getBalance(root.rightc) > 0: 
            root.rightc = self.rightRotate(root.rightc) 
            return self.leftRotate(root) 
  
        return root 
        
    def levelOrder(self):
        if self.root:
            q_temp = queue.Queue(10)
            root = self.root
        
            # enqueue the first element in
            # the tree which is the root node
            q_temp.put(root)

            # while q_temp is full that means that 
            # there are still elements to traverse
            while not q_temp.empty():

                # dequeue element at the front and get its value 
                res = q_temp.get()  
                print(res.data, end=' ')
                
                # after dequeuing element
                # if even one of these children 
                # is NULL dont enqueue anymore
                if res.leftc: 
                    q_temp.put(res.leftc)
                if res.rightc:
                    q_temp.put(res.rightc)

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
  
        # Process leftc child  
        self.display(root.leftc, space)

    def leftRotate(self, root_X):
        # * this is root X
        #   * this is root Y
        # *   * get the left side of root Y
        root_Y = root_X.rightc
        LEFT_Y = root_Y.leftc

        # connect Y.left to root X
        root_Y.leftc = root_X
        
        # connect X.right to root saved value
        root_X.rightc = LEFT_Y

        # after rotation heights will be different 
        # so update x and y nodes heights
        # pass the children of each x and y node
        root_X.height = 1 + max(self.getHeight(root_X.leftc), self.getHeight(root_X.rightc))
        root_Y.height = 1 + max(self.getHeight(root_Y.leftc), self.getHeight(root_Y.rightc))

        # return new root Y
        return root_Y

    def rightRotate(self, root_X):
        #     * this is root X
        #   * this is root Y
        # *   * get the right side of root Y
        root_Y = root_X.leftc
        RIGHT_Y = root_Y.rightc

        # connect root Y.right to root X
        root_Y.rightc = root_X

        # connect root X.left to the saved value
        root_X.leftc = RIGHT_Y

        # after rotation heights will be different 
        # so update x and y nodes heights
        # pass the children of each x and y node
        root_X.height = 1 + max(self.getHeight(root_X.leftc), self.getHeight(root_X.rightc))
        root_Y.height = 1 + max(self.getHeight(root_Y.leftc), self.getHeight(root_Y.rightc))

        # return root Y
        return root_Y



if __name__ == "__main__":
    tree = Tree()
    if input('numbers or letters?') == "n":
        while True:
            raw = input('input: ').split(' ')
            print(raw)
            raw = [int(x, base=10) for x in raw]
            for i in raw:
                tree.insert(i)
            tree.display(tree.root, 0)

            trash = input('delete: ').split(' ')
            trash = [int(x) for x in trash]
            for i in trash:
                tree.delete(i)
            tree.display(tree.root, 0)

    else:
        while True:
            raw = input('input: ').split(' ')
            for i in raw:
                tree.insert(i)
            tree.display(tree.root, 0)

            trash = input('delete: ').split(' ')
            for i in trash:
                tree.delete(i)
            tree.display(tree.root, 0)
