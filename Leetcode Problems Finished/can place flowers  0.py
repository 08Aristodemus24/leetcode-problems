def canPlaceFlowers(flowerbed,flowers):
    length=len(flowerbed)
    if length==1:
        return True

    i=0
    while(flowers!=0 and i<length): # when all flowers have been planted stop, when i reaches length stop
        if i==0:
            if flowerbed[i]==0 and flowerbed[i+1]!=1: # if detected an empty pot at first position
                flowerbed[i]=1
                flowers-=1
        elif i==length-1:
            if flowerbed[i]==0 and flowerbed[i-1]!=1: # if detected an empty pot at middle
                flowerbed[i]=1
                flowers-=1
        else:
            if flowerbed[i]==0 and flowerbed[i+1]!=1 and flowerbed[i-1]!=1: # if detected an empty pot at the last position
                flowerbed[i]=1
                flowers-=1
        i+=1
    return flowers==0 # return false if flowers is still not zero
    
    

def Main():
    flowerbed=[0,0,1,0,1,1,0,0,0,0,0,0,0]
    ans=canPlaceFlowers(flowerbed,3)
    print(ans)
    print(flowerbed)
    # [0,0,1,0,1,0,0,1,0,0,0,1]
    #  ^
    # [1,0,1,0,1,0,0,1,0,0,0,1]
    #    ^
    # [1,0,1,0,1,0,0,1,0,0,0,1]
    #                    ^
    # [1,0,1,0,1,0,0,1,0,1,0,1]

Main()
