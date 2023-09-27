# Biological_Computation_Project
This repository contains a biological computation project in the study of motifs.
Network motifs are statistically over-represented sub-structures (sub-graphs) in a network. Study of biological network motifs may reveal answers to many important biological questions.

The code of the first part of the project is in the file "Ex2Q1.py". This program gets as input a positive integer n and generates all the connected sub-graphs of size n. It outputs a text file that contains the value of n, the number of sub-graphs, and the edges of each sub-graph.

The code of the second part of the project is in the file "Ex2Q2.py". This program gets as input a positive integer n and a path to text file that represents a directed graph (it contains all the edges of the graph). The program generates all the connected sub-graphs of size n and it counts the number of appearances of each sub-graph. It outputs a text file that contains the value of n, the number of sub-graphs, the edges of each sub-graph, and the number of appearances of each sub-graph.

# How to run the codes
In order to run the codes of the project, follow these steps:

Clone the repository to your local machine:

git clone https://github.com/BarDaabul/Biological_Computation_Project.git

Open the code files - Ex2Q1.py and Ex2Q2.py in a work environment that can run Python files

## For the first part, run the code in the following way:

Open the code file Ex2Q1.py in a work environment that can run Python files

In the main function, write the required value of n and call the function outputAllConnectedSubGraphs with n as input (in the current main, the value of n is 4)

Run the program (After the running, a text file with the required output will be created in the same directory of the code)

## For the second part, run the code in the following way:

Make sure that the file Ex2Q1.py is in the same directory as the file Ex2Q2.py

Open the code file Ex2Q2.py in a work environment that can run Python files

In the main function, write the required value of n and call the function countAppearancesOfMotifsInGraph with input of n and with the path to text file that represents the required graph (in the current main, the value of n is 4 and the path is to "graph.txt")

Run the program (After the running, a text file with the required output will be created in the same directory of the code)

# Acknowledgements
Bar, Nadav
