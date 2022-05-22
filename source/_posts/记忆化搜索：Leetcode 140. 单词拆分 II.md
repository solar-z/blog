---
title: 记忆化搜索：Leetcode 140. 单词拆分 II
date: 2022/5/16 20:33:00
author: solar-
categories: 
  - 刷题
tags:
- 记忆化搜索
- leetcode

---

# 记忆化搜索：Leetcode 140. 单词拆分 II

Link: [140. 单词拆分 II](https://leetcode.cn/problems/word-break-ii/)https://leetcode-cn.com/problems/iSwD2y/)

本题如果不要求给出拆分结果，只要求给出能否拆分，那么实际上是一道非常容易的dp。

本题原则上来讲依然可以用dp解决，但是由于可能会出现完全不可能匹配到的情况，比如下面这个：

```c++
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
```

这种情况下，由于字典中不含有字母b，所以实际上不可能匹配，但如果使用dp算法，那么即使已经匹配到b之后了，算法仍然会继续遍历执行。而如果使用记忆化搜索，由于dfs会在第一次递归就深入到分支的最深处，从而可以标记b附近开始的子串为不可匹配，之后再匹配到b附近的时候就可以直接返回而不必继续往底层搜索，使得记忆化搜索可以提前判断出失败。

换句话说，就是dp会多次碰撞不可匹配子串内部的搜索，但是记忆化搜索一旦发现不可匹配的子串就不会再去碰撞。

当然dp也有记忆化搜索没有的优点，比如循环写法比递归更快，可以用滚动数组来降低空间复杂度。

时间/空间复杂度：*O*(*n*⋅2^n)

Code:

```c++
class Solution {
    unordered_set<string> words;
    unordered_map<int,vector<string>> res;
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        words=unordered_set(wordDict.begin(),wordDict.end());
        backtrack(s,0);
        return res[0];
    }
    void backtrack(string & s, int index){
        if(res.count(index)==0){
            if(index == s.size()){
                res[index]={""};
                return;
            }
            res[index]={};
            for(int end=index;end<s.size();++end){
                string w=s.substr(index,end-index+1);
                if(words.count(w)==0){
                    continue;
                }
                backtrack(s,end+1);
                for(string & str:res[end+1]){
                    res[index].push_back(str.empty()?w:w+" "+str);
                }
            }
        }
    }
};
```

