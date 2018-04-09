# NetworkX: Overview

### What is a network?

A network is a collection of nodes (or vertices) connected by edges. For example, these nodes could represent users, roads, genes, or combinations of these types. Nodes can have attributes like age, speed limit, subsequence, etc. Edges typically represent some type of interaction between the entities represented in the network and can also have characteristics attributed to them, such as direction, weight (strength of interaction), or age, for example. 

![Zachary's karate club](https://user-images.githubusercontent.com/6633242/38507505-e91797e0-3bd9-11e8-8cc9-0b14ec758c0d.png)

_Here is an example of a network, called [Zachary's karate club](https://en.wikipedia.org/wiki/Zachary%27s_karate_club). Shown in the two colors are the two factions within the Karate Club. You can load up this graph in `networkx` by calling: `G = networkx.karate_club_graph()` in Python._

The Python software [`networkx`](https://networkx.github.io) provides a lot of functionality for creating networks and calculating the properties of them, which I will discuss in this essay.

### Centrality and Assortativity

There are [many attributes of a network](https://en.wikipedia.org/wiki/Network_science#Network_properties) that are worthy of study. Here, I will just highlight a few simple, and useful network properties.

#### [Centrality](https://en.wikipedia.org/wiki/Centrality)

Centrality is a node-level attribute measuring how important (or, well, how central) a node is in a given network. There are many ways of calculating centrality. Each of which defines a node's importance differently, so when it comes to using one, it will depend on your use case and what your working definition of importance is. Some examples include:

- **Degree centrality** ranks nodes by their degree - the number of edges out of, or into that node. 
- **Closeness centrality** ranks nodes by how close they are on, on average, to every other node in the network.
- **Betweenness centrality** ranks nodes by how many of the network's shortest paths pass through that node.

The above algorithm, and many more, are implemented in `networkx` [here](https://networkx.github.io/documentation/stable/reference/algorithms/centrality.html). Using these different centrality measures on the network above, we can rank the top five influential nodes:

```python
import networkx as nx

G = nx.karate_club_graph()

dc = nx.degree_centrality(G)
cc = nx.closeness_centrality(G)
bc = nx.betweenness_centrality(G)

print "Top 5 by degree: %s" % sorted(dc.items(), key = lambda x: x[1], reverse = True)[:5]
print "Top 5 by closeness: %s" % sorted(cc.items(), key = lambda x: x[1], reverse = True)[:5]
print "Top 5 by betweenness: %s" % sorted(bc.items(), key = lambda x: x[1], reverse = True)[:5]
```

Yields different rankings of these nodes:
```
Top 5 by degree: [(33, 0.5151515151515151), (0, 0.48484848484848486), (32, 0.36363636363636365), (2, 0.30303030303030304), (1, 0.2727272727272727)]
Top 5 by closeness: [(0, 0.5689655172413793), (2, 0.559322033898305), (33, 0.55), (31, 0.5409836065573771), (8, 0.515625)]
Top 5 by betweenness: [(0, 0.4376352813852815), (33, 0.304074975949976), (32, 0.145247113997114), (2, 0.14365680615680618), (31, 0.13827561327561325)]
```

#### [Assortativity](https://en.wikipedia.org/wiki/Assortativity)

Assortativity can be a node-level attribute or a network-level attribute. On a network-level, it defines how likely a node is to connect to nodes of similar type. In particular, [degree assortativity](https://en.wikipedia.org/wiki/Assortativity#Assortativity_coefficient) measures how similar the connections of nodes are to each other. Assortativity ranges from +1 (nodes exclusively attach to other nodes of the same type, ["homophily"](https://en.wikipedia.org/wiki/Homophily)) to -1 (nodes only attach to nodes of different type, "disassociative"). It is implemented in `networkx` [here](https://networkx.github.io/documentation/stable/reference/algorithms/assortativity.html).

```python
print "Assortativity coefficient: %s" % nx.degree_assortativity_coefficient(G)
```

returns -0.475613097685 for this network, suggesting that the Zachary karate club is somewhat disassociative. 

### Getting started with networks and networkx

To start using networkx, if you are a Python user, you can just run:

```
pip install networkx
```

The code I used for this essay can be found [here](https://github.com/allisonmorgan/software_engineering/blob/master/essays/essay10/network.py). 

To get started with network data, you might check out the [Index of Complex Networks (ICON)](https://icon.colorado.edu/#!/) hosted here at CU Boulder.

### References

Author: Allie Morgan (allison.morgan@colorado.edu)
