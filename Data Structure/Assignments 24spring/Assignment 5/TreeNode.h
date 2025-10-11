/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   Node.h
 * Author: ericzhao
 *
 */

#ifndef NODE_H
#define NODE_H
#include <queue>

class TreeNode{
       
public:
    int data;
    TreeNode* left;
    TreeNode* right;
    
    TreeNode(int x): data(x), left(NULL), right(NULL){}
};



#endif /* NODE_H */

