---
title: 归并+分治：Leetcode 327 区间和的个数
date: 2022/5/8 01:14:00
author: solar-
categories: 
  - 刷题
tags:
- bfs
- 预处理
- leetcode
---

# bfs：Leetcode 433 最小基因变化

Link: [433. 最小基因变化 - 力扣（LeetCode） (leetcode-cn.com)](https://leetcode-cn.com/problems/minimum-genetic-mutation/)

预处理生成图，降低树的宽度

Bfs加visited数组防止重复访问

题目中说start可能不在bank中，但是也可能在，如果把start加入bank中一起预处理的话，需要考虑start已经存在于其中的情况。

Code:

```c++
class Solution {
public:
    int bfs(string start, string end,vector<vector<int>>& g,int m,int endIndex){
        queue<int> q;
        queue<int> nums;
        q.push(m-1);
        nums.push(0);
        vector<bool> visited(m,false);
        visited[m-1]=true;
        while(!q.empty()){
            int i = q.front();
            int num = nums.front();
            q.pop();
            nums.pop();
            for(int j=0;j<g[i].size();++j){
                if(visited[g[i][j]]==true){
                    continue;
                }
                if(g[i][j]==endIndex){
                    return num+1;
                }
                q.emplace(g[i][j]);
                nums.emplace(num+1);
            }
        }
        return -1;
    }
    int minMutation(string start, string end, vector<string>& bank) {
        int m = bank.size();
        for(auto i=bank.begin();i!=bank.end();i++){
            if(*i==start){
                bank.erase(i);
                m--;
                break;
            }
        }

        m++;
        bank.emplace_back(start);
        vector<vector<int>> g(m,vector<int>());
        int endIndex=-1;
        for(int i=0;i<m;++i){
            if(bank[i]==end){
                endIndex=i;
            }
            for(int j=i+1;j<m;++j){
                int count = 0;
                int k=0;
                for(;k<8;++k){
                    if(bank[i][k]!=bank[j][k]){
                        count++;
                    }
                    if(count>1){
                        break;
                    }
                }
                if(count==1){
                    g[i].emplace_back(j);
                    g[j].emplace_back(i);
                }
            }
        }
        if(endIndex == -1){
            return -1;
        }
        return bfs(start,end,g,m,endIndex);
    }
};
```

