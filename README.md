# BFS vs DFS Performance Profiling

## SLE-2: Empirical Performance Analysis of Search Algorithms

**Name:** Namrata Negarale  
**PRN:** 25UAM115  
**Course:** 02AML204 – Introduction to Artificial Intelligence  
**Program:** SY B.Tech CSE (AI & ML)  
**SLE-2:** BFS vs DFS Performance Profiling  

---

## Overview

This project is part of the Self Learning Exercise (SLE-2) for the **Introduction to Artificial Intelligence** course.

The purpose of this experiment is to compare the practical performance of two uninformed search algorithms:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)

Both algorithms were tested on the **same graph**, with the same start node and goal node, to make the comparison fair.

The experiment measures:

- Execution time
- Number of nodes expanded
- Runtime behavior using `py-spy`

---

## Objective

The main objectives of this SLE-2 experiment are:

1. Implement BFS and DFS in Python.
2. Run both algorithms on the same graph.
3. Use the same start and goal nodes for comparison.
4. Measure their execution time.
5. Count the number of nodes expanded.
6. Run the benchmark multiple times and calculate the average time.
7. Use `py-spy` for additional runtime profiling.
8. Compare the experimental results with the expected behavior of the algorithms.
9. Understand the difference between theoretical complexity and practical execution performance.

---

## Problem Used

A small graph containing **15 nodes** was used for the experiment.

**Start Node:** A  
**Goal Node:** O

The same graph was used for both BFS and DFS.

### Graph Used

```text
             A
           /   \
          B     C
         / \   / \
        D   E F   G
       /\  /\ /\  /\
      H I J K L M N O