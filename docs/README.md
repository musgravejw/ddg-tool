# Data Dependency Graphs
A modern CPU re-orders instructions during execution based on various factors.  This is done on the condition that the processor maintains semantic consistency between the equivalent programs.  This is done by maintaining the structure of dependencies of various kinds.  Name and control flow dependencies also affect semantic equivalence.  This tool is focused on data dependency.  Once the program is segmented into basic block segments based on control transition instructions and a control flow graph is derived, each node in the control flow graph is subject to data dependency structure.  We do not consider the product of all the graphs in the program currently.

A single basic block is likely to contain several instructions for data movement, and some arithmetic operations.  These are the most frequent, and others are defined by the instruction set architecture.

Data dependency is important because the most frequently used instructions are data movement instructions, and this typically has a larger impact than all other instructions combined, (Musgrave, et al., 2020-2024).

So, to represent the behavior of the program, its semantics, the pattern of data movement is required to be captured.  We can do this by measuring the graph features of the data dependency graphs.  We can also compare these graphs for equivalence in terms of their pattern of isomorphism.

This tool returns a collection of graphs in a **set** representing the isomorphism of data dependency for each node in the program's control flow graph.  This set represents the isomorphism of the program as a collection of its component graphs.  The isomorphism of the graphs compose the complete isomorphism of the program.

This is useful because set operations are simple to perform.  Hashing for isomorphism can be performed efficiently.  So behavioral overlap between programs can be measured in terms of set operations, or Jaccard coefficient (Musgrave, et al., 2022, 2024).

The method of isomorphic hashing used is the Weisfeiler-Lehman hashing algorithm.  This is implemented in the NetworkX library.  [Weisfeiler-Lehman] (https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.graph_hashing.weisfeiler_lehman_graph_hash.html#networkx.algorithms.graph_hashing.weisfeiler_lehman_graph_hash)

The instructions have two operands in the case of data movement, destination and source.  We consider register indirect operands to be a separate node in the data dependency graph as an approximation, although isomorphic equivalence would have to take into consideration the composition of indirect operands.

This method may be expanded to other instructions, arithmetic instructions for example, which also have a data dependency structure between their operands.  We have focused on the instruction with the highest frequency, but intend to expand this method.  Accurate data dependency graphs for a segment would take into consideration dependencies between all instructions and all operands used.


References:
- Musgrave et al., "kNN Classification of Malware Data Dependency Graph Features", 2024.  https://arxiv.org/abs/2406.02654
- Musgrave et al., "Search and Retrieval in Semantic-Structural Representations of Novel Malware", 2023-2024.  http://dx.doi.org/10.54364/aaiml.2024.41117
- Musgrave et al., "A Novel Feature Representation for Malware Classification", 2022.  https://arxiv.org/abs/2210.09580
- Musgrave et al., "Empirical Network Structure of Malicious Programs", 2022-2024.  https://doi.org/10.54364/aaiml.2024.41112
- Musgrave, "Addressing Architectural Semantic Gaps With Explainable Program Feature Representations", 2024.
