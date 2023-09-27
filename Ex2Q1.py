import networkx as nx
from itertools import permutations
import timeit


# A function that gets a size n (positive int)
# It outputs to text file a list of all the connected directed sub-graphs of size n
def outputAllConnectedSubGraphs(n):
    allGraphs = generateAllConnectedSubGraphs(n)
    writeSubgraphsToFile(allGraphs, n)


# A function that gets a size n (positive int), and returns a list of all the connected directed sub-graphs of size n
def generateAllConnectedSubGraphs(n):
    allGraphs = []

    # if n=1, so there is only one graph with a one edge to itself
    if(n==1):
        edges=[]
        edges.append((0,0))
        graph = nx.DiGraph(edges)
        allGraphs.append(graph)
        return allGraphs

    # Generate all the possible edges
    allEdges = list(permutations(range(n), 2))

    # Generate all the possible combinations of edges
    totalCombinations = 2 ** len(allEdges)
    for i in range(totalCombinations):
        combination = []
        for j in range(len(allEdges)):
            # If the j-th bit of the binary representation of i is set to 1, append the j-th edge to the current combination
            if (i >> j) & 1:
                combination.append(allEdges[j])

        # Create a directed graph using the current combination of edges
        graph = nx.DiGraph(combination)

        # Check if need to take the current graph: Check if the graph has the expected number of nodes
        # Check also if it isn't isomorphic to previous graphs and if the corresponding undirected graph is connected
        if len(graph.nodes) == n and isConnected(graph) and not isIsomorphic(graph, allGraphs):
            allGraphs.append(graph)

    return allGraphs


# A boolean function that gets a directed graph, and check if the corresponding undirected graph is connected
def isConnected(graph):
    undirectedGraph = graph.to_undirected()
    if nx.is_connected(undirectedGraph):
        return True
    return False


# A boolean function that gets a directed graph, and all the taken graphs
# It checks if the given graph is isomorphic to the other given graphs
def isIsomorphic(graph, graphs):
    # Check if the generated graph is isomorphic to any previously generated graph
    for g in graphs:
        if nx.is_isomorphic(graph, g):
            return True
    return False


# A function that get a list of sub-graphs and the number of nodes (n).
# It outputs to text file the value of n, the number of sub-graphs (count) and the edges of each sub-graph
def writeSubgraphsToFile(subGraphs, n):
    filename = f"subgraphs_n_{n}.txt"
    count = len(subGraphs)

    with open(filename, "w") as file:
        file.write(f"n={n}\n")
        file.write(f"count={count}\n")

        for i, subGraph in enumerate(subGraphs, start=1):
            file.write(f"#{i}\n")
            for edge in subGraph.edges:
                file.write(f"{edge[0]} {edge[1]}\n")

    print(f"The sub-graphs were written to {filename} successfully!")
    return 0


if __name__ == '__main__':
    # Test the program
    n = 4  # The required number of nodes

    startTime = timeit.default_timer()
    outputAllConnectedSubGraphs(n)
    endTime = timeit.default_timer()

    executionTime = endTime - startTime
    print("The execution time for n = ", n, "is ", executionTime, "seconds")