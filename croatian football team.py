
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from([('1', {'label': 'Livakovic', 'position': 'goalkeeper'}),
                  ('2', {'label': 'Vida', 'position': 'defender'}),
                  ('3', {'label': 'Čaleta Car', 'position': 'defender'}),
                  ('4', {'label': 'Vrsaljko', 'position': 'defender'}),
                  ('5', {'label': 'Gvardiol', 'position': 'defender'}),
                  ('6', {'label': 'Modrić', 'position': 'midfielder'}),
                  ('7', {'label': 'Brozović', 'position': 'midfielder'}),
                  ('8', {'label': 'Kovačić', 'position': 'midfielder'}),
                  ('9', {'label': 'Perišić', 'position': 'midfielder'}),
                  ('10', {'label': 'Rebić', 'position': 'midfielder'}),
                  ('11', {'label': 'Petković', 'position': 'striker'}),
                  ])

G.add_edges_from([('1', '2'),('1', '3'),('2', '3'),('2', '5'),('4', '10'),('5', '9'),('6', '7'),
                  ('3', '4'),('2', '7'),('3', '6'),('6', '8'),('6', '10'),('7', '8'),
                  ('7', '9'),('8', '9'),('8', '10'),('8', '11'),('9', '11'),('10','11')],
                  type='starter')

G.add_nodes_from([('12', {'label': 'Kalinic', 'position': 'goalkeeper'}),
                  ('13', {'label': 'Lovren', 'position': 'defender'}),
                  ('14', {'label': 'Škorić', 'position': 'defender'}),
                  ('15', {'label': 'juranović', 'position': 'defender'}),
                  ('16', {'label': 'Barišić', 'position': 'defender'}),
                  ('17', {'label': 'Badelj', 'position': 'midfielder'}),
                  ('18', {'label': 'Vlašić', 'position': 'midfielder'}),
                  ('19', {'label': 'Pašalić', 'position': 'midfielder'}),
                  ('20', {'label': 'Brekalo', 'position': 'midfielder'}),
                  ('21', {'label': 'Oršić', 'position': 'midfielder'}),
                  ('22', {'label': 'Kramarić', 'position': 'striker'}),
                  ])

G.add_edges_from([('1','12')],
                  type='goalkeeper')

G.add_edges_from([('12', '13'),('12', '14'),('13', '14'),('13', '15'),('14', '16'),('13', '17'),
                  ('14', '17'),('15', '17'),('15', '20'),('16', '17'),('16', '21'),('17', '18'), 
                  ('17', '19'),('18', '19'),('18', '20'),('19', '21'),('20', '22'),('21', '22')],
                  type='bench')

pos = nx.spring_layout(G)

nx.draw(G, pos)
node_labels = nx.get_node_attributes(G, 'label')
nx.draw_networkx_labels(G, pos, labels=node_labels)

plt.show()