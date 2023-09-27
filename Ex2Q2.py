import networkx as nx
from itertools import combinations
import Ex2Q1


# A function that gets a path to directed graph, it extracts the data and returns the corresponding directed graph
def loadGraphFromText(pathToDirectedGraph):
    directedGraph = nx.DiGraph()
    graph = open(pathToDirectedGraph)
    lines = graph.readlines()[0:]
    for line in lines:
        u, v = map(int, line.split())
        directedGraph.add_edges_from([(u, v)])
    return directedGraph


# A function that gets a size n (positive int), and a path to directed graph.
# It outputs  to text file all the connected directed sub-graphs of size n and the number of their appearances in the given graph
def countAppearancesOfMotifsInGraph(n, pathToDirectedGraph):
    # Extract the directed graph from the given text file
    directedGraph = loadGraphFromText(pathToDirectedGraph)

    # Find all the connected sub-graphs of size n
    allGraphs = Ex2Q1.generateAllConnectedSubGraphs(n)

    # Count the number of appearances of each sub-graph in the given graph
    countAppearances = []
    for subGraph in allGraphs:
        countAppearances.append(countSubgraphOccurrences(directedGraph, subGraph))

    # Output to text file all the connected directed sub-graphs of size n and the number of their appearances in the given graph
    writeSubgraphsWithCountingToFile(allGraphs, countAppearances, n)


# A function that gets a directed graph and a directed sub-graph
# It returns how many instances of the given sub-graph appear in the given graph
def countSubgraphOccurrences(directedGraph, subGraph):
    count = 0

    # Generate all possible combinations of the nodes from the given sub-graph
    subgraphNodes = list(subGraph.nodes)
    nodesCombinations = combinations(directedGraph.nodes, len(subgraphNodes))

    # Iterate over all the possible nodes combinations
    for nodes in nodesCombinations:
        # Generate the induced sub-graph from the directed graph using the current nodes combination
        inducedSubgraph = directedGraph.subgraph(nodes)

        # Check if the induced sub-graph is isomorphic to the given sub-graph
        if nx.is_isomorphic(inducedSubgraph, subGraph):
            count += 1

    return count


# A function that get a list of sub-graphs, a list of number of appearances for each sub-graph and the number of nodes
# It outputs to text file the value of n, the number of sub-graphs, the edges of each sub-graph and his number of appearances
def writeSubgraphsWithCountingToFile(subGraphs, countAppearances, n):
    filename = f"SubgraphsWithCounting_n_{n}.txt"
    count = len(subGraphs)

    with open(filename, "w") as file:
        file.write(f"n={n}\n")
        file.write(f"count={count}\n")

        for i, subGraph in enumerate(subGraphs, start=1):
            file.write(f"#{i}\n")
            file.write(f"count appearances={countAppearances[i-1]}\n")
            for edge in subGraph.edges:
                file.write(f"{edge[0]} {edge[1]}\n")

    print(f"The sub-graphs with the counting were written to {filename} successfully!")
    return 0


if __name__ == '__main__':
    # Test the program
    n = 4  # The required number of nodes
    countAppearancesOfMotifsInGraph(n, "graph.txt")