import networkx as nx 
import matplotlib.pyplot as plt 

# Primer Grafo 
G = nx.Graph()

# Nodo Central 
nodo_central = "Yo"
G.add_node(nodo_central, comunidad="Centro")

# Comunidades y sus Integrantes 
familia = ["Mamá", "Papá", "Abuelo"]
amigos_barrio = ["Juan Camilo", "Tomas", "Esteban"]
compas_uni = ["Alejandro", "Marco", "Jorge"]

# Agregamos Nodos
for persona in familia:
    G.add_node(persona, comunidad="Familia")
for persona in amigos_barrio:
    G.add_node(persona, comunidad="Amigos del barrio")
for persona in compas_uni:
    G.add_node(persona, comunidad="Universidad")

# Conectamos los Nodos 
for persona in familia + amigos_barrio + compas_uni:
    G.add_edge(nodo_central, persona)

# Agregamos conexiones internas
G.add_edge("Mamá", "Papá")
G.add_edge("Mamá", "Abuelo")
G.add_edge("Papá", "Abuelo")

# Conexiones amigos del barrio 
G.add_edge("Juan Camilo", "Tomas")
G.add_edge("Tomas", "Esteban")
G.add_edge("Juan Camilo", "Esteban")

# Conexiones amigos de la Universidad 
G.add_edge("Alejandro", "Marco")
G.add_edge("Marco", "Jorge")
G.add_edge("Alejandro", "Jorge")

# Dibujo 
nx.draw(G, with_labels=True)
plt.show()