

class Recurse: # to access this class it must be assigned to an object
    def rbsearch(self,arr,hi,lo,key):
    
        mid=int((hi+lo)/2)
        if key==arr[mid]:
            return mid

        elif key>arr[mid]:
            return self.rbsearch(arr,hi,mid+1,key)

        else:
            return self.rbsearch(arr,mid-1,lo,key)
    
    def bubblesort(self,arr):
        
        for i in range(len(arr)-1,0,-1):
            for j in range(i):
                if arr[j]>arr[j+1]:
                    temp=arr[j]
                    arr[j]=arr[j+1]
                    arr[j+1]=temp

class Strings(Recurse):
    def func(self):
        pass

class Ints(Recurse):
    def func(self):
        pass # this simply means pass self and then execution is done    
        

def main():
    arr=[10,4,3,2,5,6,9,8,7,1]

    search=Strings() # search is a variable that needs access to a function
    #key=int(input("enter number to be searched: "))
    search.bubblesort(arr)
    print(arr)
    key=int(input("enter a number to be searached: "))
    print(search.rbsearch(arr,len(arr)-1,0,key))

main() # main is now called execution of other functions started

