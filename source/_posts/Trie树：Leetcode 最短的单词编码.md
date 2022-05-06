---
title: Trie树：Leetcode 最短的单词编码
date: 2022/5/6 23:17:00
author: solar-
categories: 
  - 刷题
tags:
- 字典树
- leetcode
---

# Trie树：Leetcode 最短的单词编码

Link: [https://leetcode-cn.com/problems/iSwD2y/]()

题目要求计算所有不为其他单词后缀的单词长度之和（加上#）。考虑使用Trie树，将字符串反向插入。

复杂度：时间O($\sum{w_i}$) 空间O($\sum{26w_i}$)

$w_i$指第i个单词的长度，26是字符集大小

Code:

```c++
class Solution {
public:
    struct TrieNode{
        TrieNode* children[26];
        int sonNum;
        TrieNode(){
            sonNum = 0;
            for(int i=0;i<26;++i){
                children[i]=NULL;
            }
        }

        TrieNode* getSon(char c){
            if(children[c-'a']==NULL){
                children[c-'a']=new TrieNode();
                sonNum++;
            }
            return children[c-'a'];
        }

    };
    int minimumLengthEncoding(vector<string>& words) {
        TrieNode* root = new TrieNode();
        unordered_map<TrieNode*,int> nodeMap;
        int res = 0;

        for(int i=0;i<words.size();++i){
            TrieNode* cur = root;
            string str = words[i];
            for(int j=str.size()-1;j>=0;--j){
                cur = cur->getSon(str[j]);
            }
            nodeMap[cur]=str.size()+1;
        }

        for(auto [node,i]: nodeMap){
            if(node->sonNum==0){
                res+=i;
            }
        }

            return res;
    }
};
```

