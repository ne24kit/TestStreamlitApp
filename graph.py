import matplotlib.pyplot as plt
import time
from pyvis.network import Network
import streamlit as st
import streamlit.components.v1 as components
import json

with open('example.json', encoding="UTF-8") as json_file:
    data = json.load(json_file)


net = Network(notebook=True, directed=True, cdn_resources='in_line')
for elem in data:
    net.add_node(elem["data"], level=elem["level"])



for elem in data:
    if elem["prev_num"] is None:
        continue
    for prev_node in data:
        if prev_node["num"] == elem["prev_num"] and elem["level"] - 1 == prev_node["level"]:
            net.add_edge(prev_node["data"], elem["data"])


    
# print(net.get_adj_list())



# hide_1_level_node(data[1]["data"], True)
print('-'*20)




def hide_1_level_node(node_name, hide):
    net.get_node(node_name)["hidden"] = hide
    childern = net.get_adj_list()[node_name]
    
    for node_ch in childern:
        net.get_node(node_ch)["hidden"] = hide
    
def click_button(name):
    st.session_state[name] = not st.session_state[name]





names = net.get_nodes()
for name in names[1:6]:
    if name not in st.session_state:
        st.session_state[name] = False

    st.button(name, on_click=click_button, args=[name])
    hide_1_level_node(name, st.session_state[name])


st.title("Graph Visualization")

# print(net.get_node('Предложение 0 после узла 0'))

components.html(net.generate_html(), height=600)

