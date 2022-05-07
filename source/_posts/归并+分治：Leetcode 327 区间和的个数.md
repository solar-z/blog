---
title: 归并+分治：Leetcode 327 区间和的个数
date: 2022/5/8 00:50:00
author: solar-
categories: 
  - 刷题
tags:
- 归并
- 分治
- leetcode

---

# 归并+分治：Leetcode 327 区间和的个数

Link: [327. 区间和的个数 - 力扣（LeetCode） (leetcode-cn.com)](https://leetcode-cn.com/problems/count-of-range-sum/)

题目要求返回范围内的区间和个数，数组为无序，直接求没有思路。

可转换为另一个问题：区间和一共有$n^2$个，但区间和实际上为两个前缀和之差，前缀和一共只有n+1个，原问题转换为，求前缀和之差在范围内的个数。

此时联想到另一个问题：两个升序数组a、b，其中元素称为$n_a$、$n_b$，求$n_b$-$n_a$在指定范围内的组合数。这个问题很好解决，因为数组为升序，可以在b上使用滑动窗口，窗口只会向右移动，复杂度为O(n)。

问题已经基本解决，可求出前缀和数组，对其使用归并排序，将数组排为升序。使用分治求出两个子数组中前缀和之差在指定范围的组合数。然后利用上面所说的滑动窗口算法，求出两个前缀和分别在两个子数组中的组合数（只需要$n_b$-$n_a$，不需要$n_a$-$n_b$，因为前缀和永远是后面的减前面的），加在一起即为这一层归并的返回值。

Code:

```c++
class Solution {
    int recurSort(vector<long>& prefixes, int lower, int upper, int left,int right){
        if(left==right){
            return 0;
        }
        int mid = (left+right)/2;
        int leftRes = recurSort(prefixes,lower,upper,left,mid);
        int rightRes = recurSort(prefixes,lower,upper,mid+1,right);
        int res = leftRes+rightRes;

        int l = mid+1;
        int r = mid+1;
        int i = left;
        for(;i<=mid;++i){
            while(l<=right&&prefixes[l]<prefixes[i]+lower){
                l++;
            }
            while(r<=right&&prefixes[r]<=prefixes[i]+upper){
                r++;
            }
            res+=r-l;
        }
        vector<long> tmp(right-left+1);
        int a=left;
        int b=mid+1;
        int t=0;
        while(a<=mid&&b<=right){
            if(prefixes[a]<prefixes[b]){
                tmp[t]=prefixes[a];
                a++;
                t++;
            }
            else{
                tmp[t]=prefixes[b];
                b++;
                t++;
            }
        }
        if(a<=mid){
            while(a<=mid){
                tmp[t]=prefixes[a];
                a++;
                t++;
            }
        }
        if(b<=right){
            while(b<=right){
                tmp[t]=prefixes[b];
                b++;
                t++;
            }
        }
        for(int x=0;x<tmp.size();x++){
            prefixes[left+x]=tmp[x];
        }
        return res;
    }
public:
    int countRangeSum(vector<int>& nums, int lower, int upper) {
        long cur=0;
        vector<long> prefixes{0};
        for(auto n:nums){
            cur+=n;
            prefixes.emplace_back(cur);
        }
        return recurSort(prefixes,lower,upper,0,prefixes.size()-1);
    }
};
```

