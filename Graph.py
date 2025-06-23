import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

G = nx.DiGraph()

nodes = ["Rumah Bachtiar", "Rumah Indri", "Rumah Khaila", "Rumah Fiki", "Rumah Riki",
         "ITERA", 'Sukadamai', 'Karang Anyar', 'Sukarame', 'Way Halim',
         'Gunung Sugih', 'Terbanggi Besar', 'Natar', 'Kedaton', 'Tegineneng',
         'Hajimena', 'Belambangan', 'Kalibalok', 'Metro Kibang',
         'Boemiratoe', 'Bangunrejo', 'Ulusemung', 'Bukit Kemuning', 'Labuhan Ratu',
         'Trimurjo', 'Umbulan Pepanggar', 'Sidomulyo', 'Tarahan', 'Universitas Malahayati',
         'Tanjung Bintang', 'Sabah Balau', 'Merbau mataram', 'Branti', 'Pasar Untung',
         'Pringsewu', 'Kalirejo', 'Tugu Coklat'
         ]

G.add_nodes_from(nodes)
G.nodes()

edges = [('Sukarame','ITERA',1.1),
         ('Rumah Bachtiar','Metro Kibang',9.8),
         ('Rumah Bachtiar','Trimurjo',4.8),
         ('Rumah Indri','ITERA',6),
         ('Rumah Indri','Sukarame',7),
         ('Kedaton','Way Halim', 2.5),
         ('Rumah Riki','Umbulan Pepanggar',14),
         ('Rumah Fiki','Belambangan',38),
         ('Rumah Fiki','Bukit Kemuning',28),
         ('Rumah Khaila','Pringsewu',64),
         ('Metro Kibang','Sukadamai',5.2),
         ('Sukadamai','Karang Anyar',13),
         ('Karang Anyar','Pasar Untung',6.5),
         ('Karang Anyar','Sukarame',10),
         ('Labuhan Ratu','Kedaton',2.5),
         ('Way Halim','Sukarame',2.5),
         ('Trimurjo','Tegineneng',11),
         ('Tegineneng','Branti',7.3),
         ('Natar','Hajimena',11),
         ('Hajimena','Pasar Untung',4.7),
         ('Umbulan Pepanggar','Sidomulyo',14),
         ('Sidomulyo','Tarahan',11),
         ('Tarahan','Kalibalok', 22),
         ('Kalibalok','Sukarame',1.9),
         ('Branti','Natar',5.4),
         ('Sidomulyo','Merbau mataram',15),
         ('Merbau mataram','Tanjung Bintang',19),
         ('Tanjung Bintang','Sabah Balau', 8.1),
         ('Sabah Balau','ITERA', 6.4),
         ('Hajimena','Kedaton',6.4),
         ('Belambangan','Terbanggi Besar',29),
         ('Terbanggi Besar','Gunung Sugih',16),
         ('Gunung Sugih','Boemiratoe',14),
         ('Boemiratoe','Tegineneng',14),
         ('Belambangan','Bangunrejo',37),
         ('Bangunrejo','Tegineneng',19),
         ('Pasar Untung','Labuhan Ratu',1.9),
         ('Pasar Untung','Sukarame',5.2),
         ('Pasar Untung','Way Halim',4.4),
         ('Pringsewu','Tugu Coklat',30),
         ('Tugu Coklat','Universitas Malahayati',6.7),
         ('Universitas Malahayati','Hajimena',3.2),
         ('Tugu Coklat','Hajimena',7.3),
         ('Bukit Kemuning','Ulusemung',55),
         ('Ulusemung','Rumah Khaila',21),
         ('Tugu Coklat','Kalirejo',31),
         ('Kalirejo','Bangunrejo',14)
         ]

G.add_weighted_edges_from(edges)
G.edges()
G.edges(data=True)

position = {
    'ITERA' : (6, 0),
    'Rumah Bachtiar' : (5.12, 11),
    'Rumah Indri' : (5.25, -2.56),
    'Rumah Khaila' : (-15, 1.8),
    'Rumah Fiki' : (-12, 25),
    'Rumah Riki' : (16, -18),
    'Sukarame' : (3.59, -0.52),
    'Way Halim' : (-1.16, -1.262),
    'Sukadamai' : (4.839, 6.82),
    'Karang Anyar' : (2.9472, 3.567),
    'Metro Kibang' : (5.82, 8.9),
    'Sabah Balau' : (7.82, -0.83),
    'Tanjung Bintang' : (8.21, -4.3),
    'Merbau mataram' : (10.12, -9.2),
    'Sidomulyo' : (11, -12),
    'Tarahan' : (8.6523, -11.26),
    'Kalibalok' : (3.91, -3.92),
    'Tegineneng' : (-3.453, 10.2),
    'Trimurjo' : (2.707,10.487),
    'Hajimena' : (-5.17, 1.72),
    'Boemiratoe' : (-2.98, 14),
    'Bangunrejo' : (-6.5, 11),
    'Belambangan' : (-7.3, 23),
    'Ulusemung' : (-16.62, 7.159),
    'Bukit Kemuning' : (-15, 22.58),
    'Terbanggi Besar' : (-2.16, 23.85),
    'Gunung Sugih' : (-2.27, 18),
    'Labuhan Ratu' : (-3.72, 0.21),
    'Natar' : (-3.86, 5.52),
    'Kedaton' : (-5, -1.41),
    'Umbulan Pepanggar' : (12.84, -15.9302),
    'Branti' : (-3.86, 7.72),
    'Pasar Untung' : (-1.87, 0.9),
    'Universitas Malahayati' : (-8.289, 0.52),
    'Pringsewu' : (-12, 1.12),
    'Kalirejo' : (-8.5, 9.91),
    'Tugu Coklat' : (-9.8, 2)
}

rute_terpendek1 = nx.dijkstra_path(G, source='Rumah Bachtiar', target='ITERA', weight='weight')
rute_edges1 = list(zip(rute_terpendek1[:-1], rute_terpendek1[1:]))

rute_terpendek2 = nx.dijkstra_path(G, source='Rumah Fiki', target='ITERA', weight='weight')
rute_edges2 = list(zip(rute_terpendek2[:-1], rute_terpendek2[1:]))

rute_terpendek3 = nx.dijkstra_path(G, source='Rumah Riki', target='ITERA', weight='weight')
rute_edges3 = list(zip(rute_terpendek3[:-1], rute_terpendek3[1:]))

rute_terpendek4 = nx.dijkstra_path(G, source='Rumah Khaila', target='ITERA', weight='weight')
rute_edges4 = list(zip(rute_terpendek4[:-1], rute_terpendek4[1:]))

rute_terpendek5 = nx.dijkstra_path(G, source='Rumah Indri', target='ITERA', weight='weight')
rute_edges5 = list(zip(rute_terpendek5[:-1], rute_terpendek5[1:]))

pos = nx.spring_layout(G, pos=position, fixed=position.keys() , seed=42)

label_pos = {node: (x, y - 0.75) for node, (x, y) in pos.items()}
plt.figure(figsize=(20,20))
nx.draw(G, pos, node_color='black', edge_color='white', node_size=450, arrows=True)
nx.draw_networkx_edges(G, pos, edgelist=edges, arrowsize=25, arrowstyle='->')
nx.draw_networkx_nodes(G, pos, nodelist=['Rumah Bachtiar','Rumah Fiki','Rumah Riki','Rumah Khaila','Rumah Indri'], node_color='red')
nx.draw_networkx_nodes(G, pos, nodelist=['ITERA'], node_color='blue')
nx.draw_networkx_labels(G, label_pos, font_size=12)

nx.draw_networkx_edges(G, pos, edgelist=rute_edges1, edge_color='red', width=3,arrowsize=25, arrowstyle='->')
nx.draw_networkx_edges(G, pos, edgelist=rute_edges2, edge_color='green', width=3,arrowsize=25, arrowstyle='->')
nx.draw_networkx_edges(G, pos, edgelist=rute_edges3, edge_color='blue', width=3,arrowsize=25, arrowstyle='->')
nx.draw_networkx_edges(G, pos, edgelist=rute_edges4, edge_color='orange', width=3,arrowsize=25, arrowstyle='->')
nx.draw_networkx_edges(G, pos, edgelist=rute_edges5, edge_color='cyan', width=3,arrowsize=25, arrowstyle='->')
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))

data_rute = [
    ("Rumah Bachtiar", rute_terpendek1, nx.dijkstra_path_length(G, 'Rumah Bachtiar', 'ITERA', weight='weight'), 'red'),
    ("Rumah Fiki", rute_terpendek2, nx.dijkstra_path_length(G, 'Rumah Fiki', 'ITERA', weight='weight'), 'green'),
    ("Rumah Riki", rute_terpendek3, nx.dijkstra_path_length(G, 'Rumah Riki', 'ITERA', weight='weight'), 'blue'),
    ("Rumah Khaila", rute_terpendek4, nx.dijkstra_path_length(G, 'Rumah Khaila', 'ITERA', weight='weight'), 'orange'),
    ("Rumah Indri", rute_terpendek5, nx.dijkstra_path_length(G, 'Rumah Indri', 'ITERA', weight='weight'), 'cyan'),
]

legend_elements = [
    Line2D([0], [0],color='red', lw=2, label='Rumah Bachtiar -> ITERA'),
    Line2D([0], [0],color='green', lw=2, label='Rumah Fiki -> ITERA'),
    Line2D([0], [0],color='blue', lw=2, label='Rumah Riki -> ITERA'),
    Line2D([0], [0],color='orange', lw=2, label='Rumah Khaila -> ITERA'),
    Line2D([0], [0],color='cyan', lw=2, label='Rumah Indri -> ITERA'),
]

legend_rute = ("")
for asal, rute, jarak, warna in data_rute:
  if asal != 'Rumah Indri':
    legend_rute += f"  Jarak: {jarak:.2f} km\n"
  else:
    legend_rute += f"  Jarak: {jarak:.2f} km"

plt.legend(handles=legend_elements, loc='lower left')

plt.text(
    -15, -22.15,
    legend_rute,
    fontsize=12,
    bbox=dict(facecolor='white', alpha=0.8, edgecolor='black')
)

plt.title("Graf rute tercepat ke ITERA dari rumah masing-masing (berdasarkan bobot)")
plt.show()
