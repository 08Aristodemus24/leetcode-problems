#include <vector>
#include <iostream>
#include <math.h>
#include <cstring>

void swap(std::vector<int>&arr, int i, int j){
    // swap elements in array
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}

int partition(std::vector<int>& arr, int lo, int hi){
    // get mid point of arr and use as pivot
    int pivot = floor((lo + hi) / 2) + 1;

    // swap last element with pivot element
    swap(arr, pivot, hi);
    // for(int i = 0; i <= arr.size(); i++){
    //     std::cout << arr[i] << " ";
    // }
    // std::cout << "\n";

    // set j pointer to second to the last element right next to
    // the element we just made our pivot
    int i = lo, j = hi - 1;

    while(i <= j){
        if(arr[i] >= arr[hi] && arr[j] < arr[hi]){
            swap(arr, i, j);
            i++;
            j--;

        }else if(arr[i] >= arr[hi] && arr[j] >= arr[hi]){
            j--;

        // i pointers value is already in the left partition where
        // it's supposed to be but j pointer needs to be swapped but
        // we can't swap it with i so we need to move i pointer to the
        // right side once to provide incentive for j pointer to swap 
        // with i pointer value
        }else if(arr[i] < arr[hi] && arr[j] < arr[hi]){
            i++;

        }else{
            i++;
            j--;
        }
    }

    // swap pivot element located in [hi] and swap with i
    swap(arr, i, hi);

    // return new position of fixed pivot element
    return i; 
}

void quicksort(std::vector<int>& arr, int lo, int hi){
    // if lo is greater than or equal hi, means array length reached 1
    if(lo < hi){
        int fixed = partition(arr, lo, hi);
        // std::cout << fixed << "\n";

        // process sorted left side of pivot 
        quicksort(arr, lo, fixed - 1);

        // process sorted right side of pivot 
        quicksort(arr, fixed + 1, hi);
    }
}

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

    if(lo >= hi){
        return arr;
    }

    // slice arrays
    std::vector<int> s_left_arr, s_right_arr, e_left_arr, e_right_arr;
    s_left_arr = slice(arr, 0, mid - 1);
    s_right_arr = slice(arr, mid, hi);

    // pass the slices to a recursive call of mergesort
    e_left_arr = mergesort(s_left_arr, lo, mid - 1);
    e_right_arr = mergesort(s_right_arr, 0, hi - mid);

    int i = 0, j = 0, k = 0;
    std::vector<int> final_arr;
    while(i <= (mid - 1) && j <= (hi - mid)){
        // arr is only modified for the specific temp array passed  

        // let's say {2, 2, 5, 9, 10} is the left side that has already 
        // been sorted and processed and {-1, 0, 1, 3, 4} is the right side
        // that has gone through the same. i pointer is for the left side
        // and j is for the right side.
        if(e_left_arr[i] > e_right_arr[j]){
            // if left[i] greater than right[j] then we append right[j]
            // to the new array and move pointer j to the next element
            // and check again 
            final_arr.push_back(e_right_arr[j]);
            j++;

        }else{
            // if left[i] less than or equal right[j] then we append left[i]
            // to the new array and move pointer i to the next element
            // and check again
            final_arr.push_back(e_left_arr[i]);
            i++;
        }
    }
    
    int val;
    if(j <= (hi - mid)){
        for(int r = j; r <= hi - mid; r++){
            val = e_right_arr[r];
            final_arr.push_back(val);
        }
        
    }else{
        for(int l = i; l <= mid - 1; l++){
            val = e_left_arr[l];
            final_arr.push_back(val);
        }

    }

    return final_arr;
}

// compile using: g++ mergesort.cpp -o mergesort
int main(int argc, char** argv){
    // declare needed variables 
    std::vector<int> arr = {2, 2, 10};
    int lo = 0, hi = arr.size() - 1;

    // sorter
    std::vector<int> (*sorter)(std::vector<int>&, int, int);

    // if chosen sorter is mergesort assign sorter to mergesort callback
    
    if(!strcmp(argv[1], "mergesort")){
        // sorter = &mergesort;
        
        // initial prompt
        std::cout << "running " << argv[1] << "\n";

        // sort array
        std::vector<int> new_arr = mergesort(arr, lo, hi);
        for(int i = 0; i < new_arr.size(); i++){
            std::cout << new_arr[i] << " ";
        }

    }else if(!strcmp(argv[1], "quicksort")){
        // sorter = &quicksort;

        // initial prompt
        std::cout << "running " << argv[1] << "\n";

        // sort array inplace
        quicksort(arr, lo, hi);
        for(int i = 0; i < arr.size(); i++){
            std::cout << arr[i] << " ";
        }
    }
    
    return 0;
}