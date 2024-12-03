
class Node:
    def __init__(self,data,right=None,left=None):
        self.left=left
        self.data=data
        self.right=right

    def append(self):
        pass

def main():
    event=Node(2)
    print(event.data)
    print("exection successful!")




main()