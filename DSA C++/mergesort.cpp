#include <vector>
#include <iostream>
#include <math.h>




std::vector<int> slice(std::vector<int>& arr, int X, int Y){
    // Function to slice a given vector
    // from range X to Y    

    // Starting and Ending iterators
    auto start = arr.begin() + X;
    auto end = arr.begin() + Y + 1;

    // To store the sliced vector
    std::vector<int> result(Y - X + 1);

    // Copy vector using copy function()
    copy(start, end, result.begin());

    // Return the final sliced vector
    return result;
}

std::vector<int> mergesort(std::vector<int>& arr, int lo, int hi){

    // get mid point of arr
    int mid = floor((lo + hi) / 2) + 1;

    if(lo <= hi){
        return arr;
    }

    // slice arrays
    std::vector<int> left_arr, right_arr;
    left_arr = slice(arr, 0, mid - 1);
    right_arr = slice(arr, mid, hi);

    // for(int i = 0, j = 0; i < left_arr.size(), j < right_arr.size(); i++, j++){
    //     std::cout << left_arr[i] << " " << right_arr[j] << "\n";
    // }

    


    return arr;
}

int main(int argc, char** argv){
    std::vector<int> arr = {2, 2, 10, 9, 5, -1, 0, 3, 2, 4};
    int lo = 0, hi = arr.size() - 1;

    std::cout << "running mergesort" << "\n";
    // for(int i = 0; i < arr.size(); i++){
    //     std::cout << arr[i] << "\n";
    // }

    

    std::vector<int> new_arr = mergesort(arr, lo, hi);
    
    return 0;
}