# NetworkX: Overview

### What is a network?

A network is a collection of nodes (or vertices) connected by edges. These nodes could represent users, roads, or genes (among many other entities), and these nodes can have attributes like age, speed limit, or subsequence. Edges typically represent some type of interaction between the entities represented in the network and can also have characteristics attributed to them, such as direction, weight (strength of interaction), or age.

![Zachary's karate club](https://user-images.githubusercontent.com/6633242/38507505-e91797e0-3bd9-11e8-8cc9-0b14ec758c0d.png)
_Here is an example of a network, called [Zachary's karate club](https://en.wikipedia.org/wiki/Zachary%27s_karate_club). Shown in the two colors are the two factions within the Karate Club. You can load up this graph in `networkx` by calling: `G = networkx.karate_club_graph()` in Python._

The Python software [`networkx`](https://networkx.github.io) provides a lot of functionality for creating networks and calculating the properties of them, which I will discuss in this essay.

### Centrality and Assortativity

There are [many attributes of a network](https://en.wikipedia.org/wiki/Network_science#Network_properties) that are worthy of study. Here, I will just highlight a few simple, and useful network properties.

#### [Centrality](https://en.wikipedia.org/wiki/Centrality)

Centrality is a node-level attribute measuring how important (or, well, how central) a node is in a given network. There are many ways of calculating centrality. Each of which defines a node's importance differently.

*Degree centrality* ranks nodes by their degree - the number of edges out of, or into that node. 

*Closeness centrality* ranks nodes by how close they are on, on average, to every other node in the network.

*Betweenness centrality* ranks nodes by how many of the network's shortest paths pass through that node.

The above algorithms are implemented in `networkx` [here](https://networkx.github.io/documentation/stable/reference/algorithms/centrality.html).

#### [Assortativity](https://en.wikipedia.org/wiki/Assortativity)

Assortativity can be a node-level attribute or a network-level attribute. On a network-level, it defines how likely a node is to connect to nodes of similar type. In particular, [degree assortativity](https://en.wikipedia.org/wiki/Assortativity#Assortativity_coefficient) measures how similar the connections of nodes are to each other.

It is implemented in `networkx` [here](https://networkx.github.io/documentation/stable/reference/algorithms/assortativity.html).

### Getting started with networks and NetworkX



### References

Author: Allie Morgan (allison.morgan@colorado.edu)