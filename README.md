# BFS vs DFS Performance Profiling

## SLE-2: Empirical Performance Analysis of Search Algorithms

**Name:** Namrata Negarale  
**PRN:** 25UAM115  
**Course:** 02AML204 – Introduction to Artificial Intelligence  
**Program:** SY B.Tech CSE (AI & ML)

---

## Overview

This project compares the performance of two uninformed search algorithms:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)

Both algorithms are tested on the same graph using the same start and goal nodes.

The experiment measures:

- Number of nodes expanded
- Execution time
- Runtime profiling using `py-spy`

---

## Graph Used

A graph containing **15 nodes** is used.

**Start Node:** A  
**Goal Node:** O

```text
             A
           /   \
          B     C
         / \   / \
        D   E F   G
       /\  /\ /\  /\
      H I J K L M N O

Algorithms
Breadth-First Search (BFS)

BFS explores the graph level by level and uses a queue.

Time Complexity: O(V + E)
Space Complexity: O(V)

Depth-First Search (DFS)

DFS explores a branch deeply before backtracking and uses a stack.

Time Complexity: O(V + E)
Space Complexity: O(V)

Tools Used
Python
timeit
py-spy
Git
GitHub
Visual Studio Code
Methodology

Both BFS and DFS were tested using:

The same 15-node graph
Start node A
Goal node O
Same Python environment

Each benchmark run performed 100,000 searches for each algorithm.

The benchmark was executed 5 times, and the average execution time was calculated.

Experimental Results
Nodes Expanded
Algorithm	Start	Goal	Nodes Expanded
BFS	A	O	15
DFS	A	O	15
Execution Time
Run	BFS (µs/search)	DFS (µs/search)
1	5.09	5.36
2	6.36	5.29
3	5.07	4.52
4	3.76	4.30
5	3.73	6.53
Average	4.80	5.20

For this particular graph and experimental setup:

BFS Average: 4.80 µs/search
DFS Average: 5.20 µs/search

These values are specific to the selected graph, implementation, Python environment, and system conditions.

py-spy Profiling

py-spy was used to profile the runtime behavior of both algorithms.

BFS
py-spy record -o bfs_profile.svg -- python profile_search.py bfs
DFS
py-spy record -o dfs_profile.svg -- python profile_search.py dfs

Both profiling runs completed successfully with:

Errors: 0

Generated files:

bfs_profile.svg
dfs_profile.svg
Project Files
File	Description
bfs_dfs.py	Graph, BFS and DFS implementation
benchmark.py	Measures execution time using timeit
profile_search.py	Runs repeated searches for py-spy
bfs_profile.svg	BFS profiling flamegraph
dfs_profile.svg	DFS profiling flamegraph
README.md	Project documentation

Note: contribution_log.md is maintained separately and is not included as part of this README.

How to Run
Clone Repository
git clone https://github.com/namrata-101/BFS-DFS-Performance.git
cd BFS-DFS-Performance
Run BFS and DFS
python bfs_dfs.py

Expected output:

BFS Nodes Expanded: 15
DFS Nodes Expanded: 15
Run Benchmark
python benchmark.py
Run BFS Profiling
py-spy record -o bfs_profile.svg -- python profile_search.py bfs
Run DFS Profiling
py-spy record -o dfs_profile.svg -- python profile_search.py dfs
Conclusion

This experiment demonstrates the practical performance analysis of BFS and DFS using execution-time measurements and runtime profiling.

Both algorithms expanded 15 nodes on the selected graph.

Across five benchmark runs, the average measured execution times were:

BFS: 4.80 µs/search
DFS: 5.20 µs/search

The experiment shows that actual execution time can vary depending on the graph, implementation, Python environment, and system conditions.

Repository

GitHub:
https://github.com/namrata-101/BFS-DFS-Performance
