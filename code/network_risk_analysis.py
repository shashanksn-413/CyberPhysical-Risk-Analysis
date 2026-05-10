import numpy as np
import numpy.linalg as npla
import networkx as nx

print("\nCYBER-PHYSICAL NETWORK RISK ANALYSIS\n")

# -------------------------------------------------------------------
# NODE DEFINITIONS
# -------------------------------------------------------------------
# Replace these node labels with any infrastructure, organization,
# system, region, or dependency network being analyzed.
#
# Example use cases:
# - Water infrastructure networks
# - Power grid systems
# - Supply chain dependency analysis
# - Transportation systems
# - Cybersecurity attack propagation models
# - SCADA / ICS environments
# -------------------------------------------------------------------

# Example node order:
# 1: Node_A
# 2: Node_B
# 3: Node_C
# 4: Node_D
# 5: Node_E
# 6: Node_F
# 7: Node_G
# 8: Node_H
# 9: Node_I
# 10: Node_J

# -------------------------------------------------------------------
# ADJACENCY MATRIX
# -------------------------------------------------------------------
# C[i][j] = 1 indicates a connection between nodes
# C[i][j] = 0 indicates no connection
#
# This matrix can represent:
# - Cyber connectivity
# - Physical flow paths
# - Communication dependencies
# - Operational dependencies
# - Supply chain relationships
# -------------------------------------------------------------------

C = np.array([
    [0,1,0,0,1,0,0,0,0,0],
    [1,0,1,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,1,1,0],
    [0,0,0,0,0,0,1,0,0,1],
    [1,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0,0,0],
    [0,0,0,1,0,1,0,0,0,1],
    [0,0,1,0,0,0,0,0,0,0],
    [0,0,1,0,0,0,1,0,0,1],
    [0,0,0,1,0,0,0,0,1,0]
])

print("CASCADE / UNDIRECTED NETWORK ANALYSIS\n")

print("Adjacency Matrix:")
print(C)
print()

# -------------------------------------------------------------------
# NODE DEGREE ANALYSIS
# -------------------------------------------------------------------
# Degree represents the number of direct connections each node has.
# Higher degree nodes are often more influential or critical.
# -------------------------------------------------------------------

degrees = np.sum(C, axis=1)

for i, deg in enumerate(degrees, start=1):
    print(f"Degree of Node {i} = {deg}")

network_degree = np.max(degrees)

print("\nMaximum Network Degree =", network_degree)

# -------------------------------------------------------------------
# EIGENVALUE & SPECTRAL ANALYSIS
# -------------------------------------------------------------------
# Spectral radius is often used in:
# - Epidemic propagation modeling
# - Cascading failure analysis
# - Network resilience analysis
# - Stability estimation
# -------------------------------------------------------------------

eigenvalues, eigenvectors = npla.eig(C)

print("\nEigenvalues:\n", eigenvalues)

spectral_radius = np.max(eigenvalues)

print("\nSpectral Radius =", spectral_radius)

print("\nEigenvectors:\n", eigenvectors)

# -------------------------------------------------------------------
# BUILD UNDIRECTED GRAPH
# -------------------------------------------------------------------
# Used for cyber-style propagation where failures can spread in
# multiple directions across the network.
# -------------------------------------------------------------------

G = nx.from_numpy_array(C)

# -------------------------------------------------------------------
# DEGREE CENTRALITY
# -------------------------------------------------------------------
# Identifies highly connected nodes in the network.
# -------------------------------------------------------------------

DC = nx.degree_centrality(G)

print("\nDegree Centrality (Undirected):")
print(DC)

# -------------------------------------------------------------------
# BETWEENNESS CENTRALITY
# -------------------------------------------------------------------
# Measures how frequently a node appears on shortest paths.
# High betweenness nodes often act as bridges or bottlenecks.
# -------------------------------------------------------------------

BC = nx.betweenness_centrality(G, normalized=True)

print("\nBetweenness Centrality (Undirected):")
print(BC)

# -------------------------------------------------------------------
# EIGENVECTOR CENTRALITY
# -------------------------------------------------------------------
# Measures node influence based on the importance of neighboring nodes.
# -------------------------------------------------------------------

EC = nx.eigenvector_centrality_numpy(G)

print("\nEigenvector Centrality (Undirected):")
print(EC)

# ===================================================================
# DIRECTED FLOW NETWORK ANALYSIS
# ===================================================================
# Used for systems where movement follows direction:
# - Water flow
# - Power transmission
# - Supply chains
# - Transportation routes
# - Data routing
# ===================================================================

print("\n\nDIRECTED FLOW NETWORK ANALYSIS\n")

# -------------------------------------------------------------------
# CONVERT TO DIRECTED GRAPH
# -------------------------------------------------------------------

CF = C.copy()

GF = nx.from_numpy_array(CF, create_using=nx.DiGraph)

# -------------------------------------------------------------------
# IN-DEGREE / OUT-DEGREE ANALYSIS
# -------------------------------------------------------------------
# In-Degree  = incoming dependencies or flows
# Out-Degree = outgoing influence or distribution
# -------------------------------------------------------------------

print("\nDirected Node Degrees:")

for i in range(10):
    print(
        f"Node {i+1}: "
        f"In-Degree = {GF.in_degree(i)}, "
        f"Out-Degree = {GF.out_degree(i)}"
    )

# -------------------------------------------------------------------
# DIRECTED DEGREE CENTRALITY
# -------------------------------------------------------------------

DC_in = nx.in_degree_centrality(GF)
DC_out = nx.out_degree_centrality(GF)

print("\nIn-Degree Centrality (Directed):")
print(DC_in)

print("\nOut-Degree Centrality (Directed):")
print(DC_out)

# -------------------------------------------------------------------
# DIRECTED BETWEENNESS CENTRALITY
# -------------------------------------------------------------------
# Important for identifying nodes that control directional flow paths.
# -------------------------------------------------------------------

BC_directed = nx.betweenness_centrality(GF, normalized=True)

print("\nBetweenness Centrality (Directed):")
print(BC_directed)

# -------------------------------------------------------------------
# DIRECTED EIGENVECTOR CENTRALITY
# -------------------------------------------------------------------

EC_directed = nx.eigenvector_centrality_numpy(GF)

print("\nEigenvector Centrality (Directed):")
print(EC_directed)

# -------------------------------------------------------------------
# EDGE BETWEENNESS CENTRALITY
# -------------------------------------------------------------------
# Identifies critical links or pathways whose failure may significantly
# impact network connectivity or flow propagation.
# -------------------------------------------------------------------

edge_bet = nx.edge_betweenness_centrality(GF, normalized=True)

print("\nLink (Edge) Betweenness Centrality (Directed):")

for edge, val in edge_bet.items():
    print(f"Edge {edge} = {val}")