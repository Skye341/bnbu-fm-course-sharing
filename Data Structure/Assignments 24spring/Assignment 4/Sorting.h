/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   Sort.h
 * Author: ericzhao
 *
 * Created on March 18, 2017, 5:34 PM
 */

#ifndef SORT_H
#define SORT_H

class Sorting{
private:
    int* NumList;
    int num;
    
public:
    void CreateArray(int k);
    int* CopyArray();
    int Size() {return num;}
    void Print(int* NumList);
    void BubbleSort(int* NumList);
    void InsertSort(int* NumList);
    void MergeSort(int* NumList, int start, int end);
    void QuickSort(int* NumList, int start, int end);
    void HeapSort(int* NumList);
};

#endif /* SORT_H */

