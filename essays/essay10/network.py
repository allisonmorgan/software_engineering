import networkx as nx

G = nx.karate_club_graph()

dc = nx.degree_centrality(G)
cc = nx.closeness_centrality(G)
bc = nx.betweenness_centrality(G)

print "Top 5 by degree: %s" % sorted(dc.items(), key = lambda x: x[1], reverse = True)[:5]
print "Top 5 by closeness: %s" % sorted(cc.items(), key = lambda x: x[1], reverse = True)[:5]
print "Top 5 by betweenness: %s" % sorted(bc.items(), key = lambda x: x[1], reverse = True)[:5]

print "Assortativity coefficient: %s" % nx.degree_assortativity_coefficient(G)