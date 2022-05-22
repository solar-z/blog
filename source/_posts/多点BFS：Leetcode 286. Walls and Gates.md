---
title: 多点BFS：Leetcode 286. Walls and Gates
date: 2022/5/21 23:33:00
author: solar-
categories: 
  - 刷题
tags:
- 
- leetcode

---

# 多点BFS：Leetcode 286. Walls and Gates

Link：[286. Walls and Gates](https://leetcode.cn/problems/walls-and-gates/)

题目要求寻找每一个空房间最近的门，显然使用bfs，由于有多个门，可以使用多点bfs，同时开始搜索。

由于本题中可以通过当前房间的数字来判断是否已经访问过，所以不需要额外的visit数组，可以节省相当多的空间和时间。

时间复杂度和空间复杂度均为O(mn)。

```c++
class Solution
{
public:
    const int inf = 2147483647;
    bool isGate(int i, int j, vector<vector<int> > &rooms)
    {
        if (i >= 0 && i < n && j >= 0 && j < m && rooms[i][j] > 0)
        {
            return true;
        }
        return false;
    }
    int n;
    int m;
    vector<vector<int> > dir = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
    void wallsAndGates(vector<vector<int> > &rooms)
    {
        n = rooms.size();
        m = rooms[0].size();
        queue<pair<int, int> > qRoom;
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < m; ++j)
            {
                if (rooms[i][j] == 0)
                {
                    qRoom.emplace(i, j);
                }
            }
        }
        while (!qRoom.empty())
        {
            int x = qRoom.front().first;
            int y = qRoom.front().second;
            qRoom.pop();
            for (int k = 0; k < 4; ++k)
            {
                int newX = x + dir[k][0];
                int newY = y + dir[k][1];
                if (isGate(newX, newY, rooms) && (rooms[newX][newY] > rooms[x][y] + 1))
                {
                    rooms[newX][newY] = rooms[x][y] + 1;
                    qRoom.emplace(newX, newY);
                }
            }
        }
    }
};
```



