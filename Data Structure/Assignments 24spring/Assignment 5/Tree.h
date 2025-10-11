/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   BST.h
 * Author: ericzhao
 *
 */

#ifndef TREE_H
#define TREE_H

#include "TreeNode.h"

class Tree{
private:
    TreeNode* root;
    
public:
    Tree(int *array, int arrayLength);
    TreeNode* GetRoot() {return root;}
    void PreTraversal(TreeNode* root);
    void InTraversal(TreeNode* root);
    void PostTraversal(TreeNode* root);
    int TreeHeight(TreeNode* root);
    bool Search(TreeNode* root, int val);
    bool IsBalanced(TreeNode* root);
};

#endif /* TREE_H */

