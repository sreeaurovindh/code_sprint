# DFS

Title : Depth First Search (DFS)
Date : Sep 25, 2020 10:55:22 PM
Tags: #Trees #DFS
External Link: https://medium.com/leetcode-patterns/leetcode-pattern-1-bfs-dfs-25-of-the-problems-part-1-519450a84353

DFS is all about diving as deep as possible before coming back to take a dive again. Below is the iterative DFS pattern using a stack that will allow us to solve a ton of problems.

DFS magic spell: 
1. push to stack, 
2. pop top , 
3. retrieve unvisited neighbours of top, push them to stack
4. repeat 1,2,3 while stack not empty. Now form a rap !


Its always vertical flow!! So we have to use #Stack. On the other hand if we are concenred with horizontal flow we use a #Queue

1. 
