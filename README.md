### Background and Motivation
Indirect memory accesses arise in many emerging and important domains, including sparse deep learning, graph analytics, database processing and scientific computing.
They became a bottleneck in the performance of modern computer systems because (1)the indirect patterns are hard to predict and (2) memory hierarchy is optimized for sequential accesses,often at the expense of random accesses. Those indirect memory accesses will cause a large number of cache misses and memory stalls, which will significantly degrade the performance of the system.
We have categorized related papers into three categories: Prefetch-based Solutions, Domain-specific Solutions, and General-purposed Solutions.

### Prefetch-based Solutions
- [Ainsworth, Sam, and Timothy M. Jones. "Software prefetching for indirect memory accesses." 2017 IEEE/ACM International Symposium on Code Generation and Optimization (CGO). IEEE, 2017.](https://ieeexplore.ieee.org/abstract/document/7863749) (Citations: 72) - Data Structure
- [Ainsworth, Sam, and Timothy M. Jones. "Graph prefetching using data structure knowledge." Proceedings of the 2016 International Conference on Supercomputing. 2016.](https://dl.acm.org/doi/abs/10.1145/2925426.2926254) (Citations: 85) - Prefetch BFS using information about application's data structure
- [Ainsworth, Sam, and Timothy M. Jones. "An event-triggered programmable prefetcher for irregular workloads." ACM Sigplan Notices 53.2 (2018): 578-592.](https://dl.acm.org/doi/pdf/10.1145/3296957.3173189) (Citations: 32) - Event-based Programmable Prefetcher
- [Cavus, Mustafa, Resit Sendag, and Joshua J. Yi. "Informed prefetching for indirect memory accesses." ACM Transactions on Architecture and Code Optimization (TACO) 17.1 (2020): 1-29.](https://dl.acm.org/doi/abs/10.1145/3374216) (Citations: 13)
- [Talati, Nishil, et al. "Prodigy: Improving the memory latency of data-indirect irregular workloads using hardware-software co-design." 2021 IEEE International Symposium on High-Performance Computer Architecture (HPCA). IEEE, 2021.](https://ieeexplore.ieee.org/abstract/document/9407222) (Citations: 60) - Prefetch Indirect
- [Basak, Abanti, et al. "Analysis and optimization of the memory hierarchy for graph processing workloads." 2019 IEEE International Symposium on High Performance Computer Architecture (HPCA). IEEE, 2019.](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8675225) (Citations: 88) - Prefetch and analysis of memory level parallelism
- [Yu, Xiangyao, et al. "IMP: Indirect memory prefetcher." Proceedings of the 48th International Symposium on Microarchitecture. 2015.](https://scholar.google.com/scholar_url?url=https://dl.acm.org/doi/pdf/10.1145/2830772.2830807&hl=en&sa=T&oi=gsr-r-gga&ct=res&cd=0&d=4440176624741026881&ei=3-tuZvP2FoaM6rQPpe-zqAs&scisig=AFWwaeZ-3V-E2ZHJ6eT77HM2SxS3) (Citations: 181)

### Fetcher-based Solutions
- [Mukkara, Anurag, et al. "Exploiting locality in graph analytics through hardware-accelerated traversal scheduling." 2018 51st Annual IEEE/ACM International Symposium on Microarchitecture (MICRO). IEEE, 2018.](https://ieeexplore.ieee.org/abstract/document/8574527) (Citations: 148) - Decoupled access-execute by bounded DFS scheduling
- [Kocberber, Onur, et al. "Meet the walkers: Accelerating index traversals for in-memory databases." Proceedings of the 46th Annual IEEE/ACM International Symposium on Microarchitecture. 2013.](https://dl.acm.org/doi/abs/10.1145/2540708.2540748) (Citations: 264) - Fetcher for database hash lookups
- [Kumar, Snehasish, et al. "SQRL: Hardware accelerator for collecting software data structures." Proceedings of the 23rd international conference on Parallel architectures and compilation. 2014.](https://dl.acm.org/doi/abs/10.1145/2628071.2628118) (Citations: 28)
- [Yang, Yifan, Joel S. Emer, and Daniel Sanchez. "SpZip: Architectural support for effective data compression in irregular applications." 2021 ACM/IEEE 48th Annual International Symposium on Computer Architecture (ISCA). IEEE, 2021.](https://ieeexplore.ieee.org/abstract/document/9499902) (Citations: 24) - General indirect memory access accelerator using fine-grained pipelining

### Others Solutions
- [Kiriansky, Vladimir, Yunming Zhang, and Saman Amarasinghe. "Optimizing indirect memory references with milk." Proceedings of the 2016 International Conference on Parallel Architectures and Compilation. 2016.](https://dl.acm.org/doi/abs/10.1145/2967938.2967948) (Citations: 45) - Software-level reordering indirect memory accesses  using programmer's annotation

### Comments on Prefetch-based Solutions:
* Pros1: No need to rewrite the code for triggering the prefetcher
* Pros2: Efficiently hide the latency of memory accesses
* Cons1: Redundant memory accesses and similar computations to the cores
* Cons2: If cannot prefetch correctly, will pollute the cache

### Comments on Fetcher-based Solutions:
* Pros1: No redundant memory accesses and similar computations to the cores
* Pros2: Efficiently hide the latency of memory accesses
* Pros3: Since cores are specifying the memory access, there would be no cache pollution
* Cons1: Need to rewrite the code for triggering the fetcher

### Aspects for comparing the solutions within a category:
* Generality: How general the solution is for different applications
* Programmability: How easy to use the solution, does that need to rewrite the whole program or just add some annotations or not
* Performance: How much performance improvement can be achieved, this can be further divided into three parts:
    * Speedup: How much speedup can be achieved, including the throughput of whole system, the latency of the memory accesses and bandwidth of the memory accesses
    * Energy: How much energy can be saved
    * Area: How much area can be saved 