import array
import sys

def show_sizeof(x, level=0):

    print("\t" * level, x.__class__, sys.getsizeof(x), x)

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_sizeof(xx, level + 1)
        else:
            for xx in x:
                show_sizeof(xx, level + 1)


def main():
    arr=array.array('i',[1,2,3,4,5]) 
    for nums in arr:
        print(id(nums))


    show_sizeof(8)
main()