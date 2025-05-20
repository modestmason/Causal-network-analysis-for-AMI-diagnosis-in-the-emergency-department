import xml.etree.ElementTree as ET  # read xml
import networkx as nx
from causalnex.structure import StructureModel
from var_name import dict_CE

def parse_xml(filename):
    G = nx.DiGraph()
    # sm = StructureModel()
    root = ET.parse(filename)  # read and parse xml
    node_objs = root.find('./bnVariables')
    edge_objs = root.find('./parents')
    for node_obj in node_objs.findall('discreteVariable'):
        G.add_node(node_obj.attrib['name'])

    for edge_obj in edge_objs.findall('parentsFor'):
        dest_node = edge_obj.attrib['name']
        for source_obj in edge_obj.findall('parent'):
            source_node = source_obj.attrib['name']
            G.add_edge(source_node, dest_node)

    return G

def parse_xml_sm(filename):
    sm = StructureModel()
    root = ET.parse(filename)  # read and parse xml
    node_objs = root.find('./bnVariables')
    edge_objs = root.find('./parents')
    for node_obj in node_objs.findall('discreteVariable'):
        sm.add_node(node_obj.attrib['name'])

    for edge_obj in edge_objs.findall('parentsFor'):
        dest_node = edge_obj.attrib['name']
        for source_obj in edge_obj.findall('parent'):
            source_node = source_obj.attrib['name']
            sm.add_edge(source_node, dest_node)

    return sm

def parse_xml_node(filename):
    node = []
    root = ET.parse(filename)
    node_objs = root.find('./bnVariables')
    for node_obj in node_objs.findall('discreteVariable'):
        node.append(node_obj.attrib['name'])
    return node