def main():

    arr=[1,2]*10
    arr.remove(arr[0])
    
    print(arr)
    print(arr[19]) # this will be out of range since array has been resized because of the self.remove() function
    print(len(arr))

main()
