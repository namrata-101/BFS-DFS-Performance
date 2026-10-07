# SLE-3 Architecture – Full C4 Model

## BFS and DFS Graph Search System

**Student:** Namrata Negarale  
**PRN:** 25UAM115  
**Course:** 02AML204 – Introduction to Artificial Intelligence  
**Program:** SY B.Tech CSE (AI & ML)  
**Division:** B  
**Architecture Model:** Full C4 Model

---

## 1. System Overview

The **BFS and DFS Graph Search System** is a Python-based Artificial Intelligence search system that explores a graph from a given start node to a goal node.

The system implements:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)

The project uses a **15-node graph** represented using an adjacency-list structure. It also includes benchmarking and profiling support for comparing the performance of BFS and DFS.

This SLE-3 architecture continues the implementation and performance analysis completed in the earlier SLE activities.

---

## 2. C4 Model

The architecture is represented using four levels:

1. **Level 1 – System Context**
2. **Level 2 – Container Diagram**
3. **Level 3 – Component Diagram**
4. **Level 4 – Code Level Overview**

---

## 3. Level 1 – System Context

### Main Elements

- **User**
- **Graph Search System**
- **Search Result**

### Flow

**User → Graph Search System:** Search Input

**Graph Search System → Search Result:** Search Result

The user provides the required search input to the Graph Search System. The system performs BFS or DFS on the graph and produces the search result.

The system is self-contained and does not depend on an external API or network service.

---

## 4. Level 2 – Container Diagram

The system is divided into the following main containers:

### Input Module

Receives the search input such as the start node, goal node, and selected search method.

### Graph Management

Stores and manages the 15-node graph using an adjacency-list representation.

### Search Engine – BFS / DFS

Contains the main search logic. It executes either Breadth-First Search or Depth-First Search.

### Visited / Memory

Keeps track of nodes that have already been visited during the search and helps avoid repeated processing.

### Output Module

Presents the final search result and related search information.

The containers represent the major functional blocks of the system without showing internal implementation details.

---

## 5. Level 3 – Component Diagram

At Level 3, only the **Search Engine** container is expanded.

### BFS

Implements Breadth-First Search and explores nodes level by level.

### DFS

Implements Depth-First Search and explores a branch deeply before backtracking.

### Queue

Supports the BFS search process by maintaining the frontier in queue order.

### Stack

Supports the DFS search process by maintaining the frontier in stack order.

### Goal Test

Checks whether the currently explored node is the required goal node.

The component diagram focuses on the internal organization of the main AI search logic.

---

## 6. Level 4 – Code Level Overview

The code level shows the main implementation elements rather than complete source code.

| File / Function | Responsibility |
|---|---|
| `bfs_dfs.py – graph` | Stores the 15-node graph using adjacency-list representation |
| `bfs_dfs.py – bfs()` | Performs Breadth-First Search using a queue |
| `bfs_dfs.py – dfs()` | Performs Depth-First Search using a stack |
| `bfs_dfs.py – visited` | Stores already visited nodes during the search |
| `bfs_dfs.py – nodes_expanded` | Counts the nodes explored during the search |
| `benchmark.py – measure_bfs()` | Measures average BFS execution time using `timeit` |
| `benchmark.py – measure_dfs()` | Measures average DFS execution time using `timeit` |
| `profile_search.py` | Runs repeated BFS/DFS searches for `py-spy` profiling |

---

## 7. Design Decisions

- The same graph and start/goal nodes are used for a fair BFS versus DFS comparison.
- The **Search Engine** is expanded at component level because it contains the core AI search logic.
- BFS uses queue-based exploration, while DFS uses stack-based exploration.
- Benchmarking and profiling are treated as supporting parts of the system.

---

## 8. Connection with SLE-2

SLE-3 extends the BFS and DFS performance analysis from SLE-2 into a complete software architecture.

The BFS and DFS algorithms remain the core search components. The benchmark module supports execution-time comparison using `timeit`, while the profiling module supports runtime analysis using `py-spy`.

Therefore, the C4 architecture connects the implementation, search logic, and performance-analysis work into one system design.

---

## 9. Conclusion

The Full C4 Model provides four levels of architectural detail for the BFS and DFS Graph Search System.

The architecture connects the user interaction, system containers, core search components, and actual implementation files. It also connects the SLE-3 design with the BFS/DFS performance analysis completed in the previous SLE activity.

This architecture gives a clear and structured view of how the AI graph search system is organized and implemented.