import queue

class Node:
    def __init__(self,data):
        self.data=data
        self.leftc=None
        self.rightc=None

class Tree:
    def __init__(self):
        self.root=None
        self.COUNT=[10]

    def createInLevelOrder(self,data_set:list):

        length,i=len(data_set),0

        while True:
            if not self.root:
                self.root=Node(data_set[i])
                
                # create a temporary queue
                # and enqueue created root initially
                q_temp=queue.Queue(100)
                q_temp.put(self.root)
                i+=1
                if i==length:
                    break
            else:
                # deQueue node from queue and use children
                # to check if either one is NULL
                res=q_temp.get()
                if not res.leftc:

                    # if left child NULL append a node and its
                    # data from the array
                    res.leftc=Node(data_set[i])
                    q_temp.put(res.leftc)
                    i+=1
                    if i==length:
                        break
                if not res.rightc:
                    
                    # if right child NULL append a node and its
                    # data from the array
                    res.rightc=Node(data_set[i])
                    q_temp.put(res.rightc)
                    i+=1

                    # since loop runs forever break
                    # when either of the two ifs have reached
                    # out of range index 
                    if i==length:
                        break
        
    def display(self,root,space): 
        # Base case  
        if not root: 
            return
  
        # Increase distance between levels  
        space+=self.COUNT[0] 
  
        # Process right child first  
        self.display(root.rightc,space)  
  
        # Print current node after space  
        # count
        print()  
        for _ in range(self.COUNT[0],space): 
            print(end=" ")  
        print(root.data)  
  
        # Process left child  
        self.display(root.leftc,space)

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


def checkIfBST(root):
    pass


if __name__ == "__main__":
    tree=Tree()
    tree.createInLevelOrder([1,2,3])
    tree.display(tree.root,0)

