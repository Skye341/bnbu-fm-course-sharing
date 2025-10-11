/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


#include <cstdlib>
#include "Sorting.h"
#include "stdio.h"
#include "array"
#include <iostream>
#include <ctime>
#include <cmath>
using namespace std;

/*Create an array of random numbers with length k*/
void Sorting::CreateArray(int k){
    NumList = new int[k];
    for (int i=0; i<k; i++){
        NumList[i] = rand()%(k+10);
    }
    num = k;
}

/*Copy the created array*/
int* Sorting::CopyArray(){
    int* list = new int[num];
    for(int i=0; i<num; i++){
        list[i] = *(NumList+i);
    }
    return list;
}

void Sorting::Print(int* NumList){
    for(int i=0; i<num; i++){
        cout << NumList[i] << ",";
    }
    cout << endl;
}

/**==========================For Bubble Sort===================================*/
void Sorting::BubbleSort(int* NumList){
    //Write your code here.

}

/**==========================For Insertion Sort===================================*/
void Sorting::InsertSort(int* NumList){
    //Write your code here.

}

/**==========================For Merge Sort===================================*/

/*Merge two sorted array. Used in MergeSort*/
void Merge(int* NumList, int start, int mid, int end){      
    //Write your code here.

}

void Sorting::MergeSort(int* NumList, int start, int end){
    //Write your code here.

}

/**==========================For Quick Sort===================================*/
/*Swap the i'th and j'th element in the array*/
void Swap(int* NumList, int i, int j){
    //Write your code here.

}

int MedianOfThree(int* NumList, int begin, int tail){
    //Write your code here.

}

int Partition(int* NumList, int begin, int tail){  
    //Write your code here.

}

void Sorting::QuickSort(int* NumList, int begin, int tail){
    //Write your code here.
   
}


/**==========================For Heap Sort===================================*/

/**Maintain max-heap order*/
void percolateUp(int* heap, int currentSize) {
    //Write your code here.


}

/**Append an element to the end of heap, and adjust heap to maintain the max-heap order.*/
void InsertHeap(int* heap, int& currentSize, const int ele){
    //Write your code here.

    
}

/*Construct a max heap (Parent larger than its children)*/
int* BuildMaxHeap(int* NumList, int num){
    //Write your code here.


}

/**Adjust heap to maintain the heap order*/
void percolateDown(int* MaxHeap, int currentSize){   
    //Write your code here.

    
}


void DeleteMin(int* MaxHeap, int& currentSize){
    //Write your code here.


}


void Sorting::HeapSort(int* NumList){
    //Write your code here.


}



/*
 * 
 */
int main(int argc, char** argv) {
    Sorting s;
    int t = 10; //You may try different numbers here, e.g. from 3 to 17.
    int num = pow(2, t); 
    s.CreateArray(num);  //Created an Array "A" with "num" elements.
    clock_t start;
    double duration; //Time duration of running each sorting algorithm.

    
    int* BubbleSortList = s.CopyArray();  //Copy array "A" for BubbleSort.
    cout << "Original Array: " << endl;
    s.Print(BubbleSortList);
    start = std::clock();    //Start timer.
    s.BubbleSort(BubbleSortList);       //Run sorting algorithm;
    cout << "Bubble Sort Array: " << endl;
    s.Print(BubbleSortList);
    duration = ( std::clock() - start ) / (double) CLOCKS_PER_SEC;  //Record running time.
    cout << "Bubble Sort needs time: " << duration << endl;

    
    int* InsertSortList = s.CopyArray();
    start = std::clock();
    s.InsertSort(InsertSortList);
    cout << "Insertion Sort Array: " << endl;
    s.Print(InsertSortList);
    duration = ( std::clock() - start ) / (double) CLOCKS_PER_SEC;  
    cout << "Insertion Sort needs time: " << duration << endl;

    int* MergeSortList = s.CopyArray();
    start = std::clock();
    s.MergeSort(MergeSortList, 0, num-1);
    cout << "Merge Sort Array: " << endl;
    s.Print(MergeSortList);
    duration = ( std::clock() - start ) / (double) CLOCKS_PER_SEC;  
    cout << "Merge Sort needs time: " << duration << endl;

    
    int* QuickSortList = s.CopyArray();
    start = std::clock();
    s.QuickSort(QuickSortList, 0, num-1);
    cout << "Quick Sort Array: " << endl;
    s.Print(QuickSortList);
    duration = ( std::clock() - start ) / (double) CLOCKS_PER_SEC;
    cout << "Quick Sort needs time: " << duration << endl;


    int* HeapSortList = s.CopyArray();
    start = std::clock();
    s.HeapSort(HeapSortList);
    cout << "Heap Sort Array: " << endl;
    s.Print(HeapSortList);
    duration = ( std::clock() - start ) / (double) CLOCKS_PER_SEC;
    cout << "Heap Sort needs time: " << duration << endl;

    return 0;
}

