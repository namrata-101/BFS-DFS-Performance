# AI Contribution Log

## SLE-2: BFS vs DFS Performance Profiling

**Name:** Namrata Negarale  
**PRN:** 25UAM115  
**Course:** 02AML204 – Introduction to Artificial Intelligence  
**Project:** BFS vs DFS Performance Profiling

---

## 1. AI Tools Used

The following AI tools were used during the development of this SLE-2 project:

- ChatGPT
- GitHub Copilot

---

## 2. Contribution Log

| Sr. No. | AI Tool | Purpose / Assistance | Student's Work |
|---|---|---|---|
| 1 | ChatGPT | Helped understand the SLE-2 profiling requirements and report structure. | Read and understood the requirements and prepared the experiment accordingly. |
| 2 | ChatGPT | Explained BFS and DFS concepts and their implementation. | Implemented and tested the algorithms on the selected graph. |
| 3 | GitHub Copilot | Provided code suggestions for BFS/DFS and performance-testing code. | Reviewed, modified, and tested the suggested code. |
| 4 | ChatGPT | Helped understand Python `timeit` and execution-time measurement. | Ran the benchmark program and collected actual timing results. |
| 5 | ChatGPT | Helped understand manual node counting. | Added and checked the node counter and verified the number of nodes expanded. |
| 6 | ChatGPT | Helped understand repeated benchmark runs and average execution time. | Performed five experimental runs and calculated the final average values. |
| 7 | ChatGPT | Helped understand and troubleshoot `py-spy`. | Installed `py-spy`, executed the profiling commands, and generated BFS and DFS profiling files. |
| 8 | ChatGPT | Helped troubleshoot Git/GitHub commands and repository organization. | Managed the Git repository, commits, and GitHub push operations. |
| 9 | ChatGPT | Helped organize the README and project documentation. | Reviewed the documentation and added the actual project information and results. |

---

## 3. AI-Assisted Code

AI assistance was used for understanding and generating code suggestions related to:

- BFS implementation
- DFS implementation
- Execution-time benchmarking
- Node counting
- Repeated benchmark testing
- `py-spy` profiling setup
- Git/GitHub commands
- Project documentation

The AI-generated suggestions were reviewed and modified according to the requirements of the experiment.

---

## 4. Work Performed by Student

The following work was performed and verified by the student:

- Created and used the 15-node graph.
- Implemented and tested BFS and DFS.
- Selected `A` as the start node and `O` as the goal node.
- Ran the programs locally.
- Performed the timing experiments.
- Performed five experimental benchmark runs.
- Collected the actual execution-time results.
- Calculated the average execution time.
- Verified the number of nodes expanded.
- Installed and executed `py-spy`.
- Generated BFS and DFS profiling output.
- Verified that both profiling runs completed with `Errors: 0`.
- Organized the project files.
- Created and maintained the GitHub repository.
- Prepared the final experimental analysis.

---

## 5. Actual Experimental Results

The reported values were obtained from actual program execution.

### Node Expansion Results

| Algorithm | Start | Goal | Nodes Expanded |
|---|---|---|---:|
| BFS | A | O | 15 |
| DFS | A | O | 15 |

### Five Benchmark Runs

| Run | BFS Time (µs/search) | DFS Time (µs/search) |
|---|---:|---:|
| Run 1 | 5.09 | 5.36 |
| Run 2 | 6.36 | 5.29 |
| Run 3 | 5.07 | 4.52 |
| Run 4 | 3.76 | 4.30 |
| Run 5 | 3.73 | 6.53 |
| **Average** | **4.80** | **5.20** |

### Final Experimental Values

| Metric | BFS | DFS |
|---|---:|---:|
| Nodes Expanded | 15 | 15 |
| Average Time (µs/search) | 4.80 | 5.20 |

---

## 6. py-spy Profiling

The student installed and used `py-spy` for runtime profiling.

### BFS Profiling

```bash
py-spy record -o bfs_profile.svg -- python profile_search.py bfs

DFS Profiling
py-spy record -o dfs_profile.svg -- python profile_search.py dfs

Both profiling processes completed successfully with:

Errors: 0

The generated profiling files were:

bfs_profile.svg
dfs_profile.svg
7. Ownership Statement

AI tools were used as assistance for learning, code suggestions, troubleshooting, profiling setup, and documentation.

The student reviewed and understood the suggestions, executed the programs locally, collected the experimental data, verified the results, and performed the final analysis.

The performance values in the project were obtained from the student's actual experimental runs.


