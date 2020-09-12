# Analyze Complexity Graph Bipartite Matching
This project aims to analyze the complexity of the bipartite graph matching algorithms.

## Technologies
Below is the list of technologies used in this project.
* Python 3.7
* scipy
* pandas
* matplotlib
* numpy
* networkx

## Analyzed Algorithms
### Hopcroft Karp

## Method
The graphs were generated randomly with the Python Network X library. The size of the graph was based on the Fibonacci sequence, where the number of nodes in the graph grows according to Fibonnacci.

The analysis was made based on the growth in the size of the number of connections between the nodes and the execution time.

## Create Graphs
The graphs are created in the graphs folder, after executing the command below.
```
python graph_random.py
```
## Generate Runtime Results
The analysis is made based on the graphs contained in the graphs folder, based on a number following the fibonacci sequence by executing the command below.
```
python complexity_analysis.py
```

## Generate Fit Curve
The graph with Fit Curve is generated based on the command below.
```
python create_fit_curve.py
```
