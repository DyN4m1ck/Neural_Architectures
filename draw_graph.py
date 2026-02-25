"""
Script to visualize the graph in Memgraph using Graphviz.
"""
import os
from py2neo import Graph
from graphviz import Digraph


def connect_to_memgraph():
    """
    Connect to Memgraph database
    """
    # Using py2neo to connect to Memgraph
    graph = Graph("bolt://localhost:7687")
    return graph


def get_graph_data(graph):
    """
    Get all nodes and relationships from the graph database
    """
    # Query to get all nodes and their properties
    nodes_query = """
    MATCH (n)
    RETURN id(n) AS id, labels(n) AS labels, properties(n) AS properties
    """
    
    # Query to get all relationships and their properties
    rels_query = """
    MATCH ()-[r]->()
    RETURN id(startNode(r)) AS start_id, 
           id(endNode(r)) AS end_id, 
           type(r) AS type,
           properties(r) AS properties
    """
    
    nodes = graph.run(nodes_query).data()
    relationships = graph.run(rels_query).data()
    
    return nodes, relationships


def draw_graph(nodes, relationships, output_file='graph_visualization'):
    """
    Draw the graph using Graphviz
    """
    dot = Digraph(comment='Graph Visualization', format='png')
    dot.attr(rankdir='TB', size='10,8')
    
    # Add nodes to the graph
    for node in nodes:
        node_id = str(node['id'])
        labels = ':'.join(node['labels']) if node['labels'] else 'Node'
        properties = node['properties']
        
        # Create label for the node with its properties
        node_label = f"{labels}\\nID: {node_id}"
        for key, value in properties.items():
            node_label += f"\\n{key}: {value}"
        
        # Different shapes/colors for different node types
        if 'Architecture' in node['labels']:
            dot.node(node_id, node_label, shape='box', style='filled', fillcolor='lightblue')
        elif 'ArchitectureCategory' in node['labels']:
            dot.node(node_id, node_label, shape='ellipse', style='filled', fillcolor='lightgreen')
        else:
            dot.node(node_id, node_label, shape='circle', style='filled', fillcolor='lightgray')
    
    # Add relationships to the graph
    for rel in relationships:
        start_id = str(rel['start_id'])
        end_id = str(rel['end_id'])
        rel_type = rel['type']
        properties = rel['properties']
        
        # Create label for the relationship
        rel_label = rel_type
        for key, value in properties.items():
            rel_label += f"\\n{key}: {value}"
        
        dot.edge(start_id, end_id, label=rel_label)
    
    # Render the graph
    dot.render(output_file, cleanup=True)
    print(f"Graph visualization saved as {output_file}.png")


def main():
    """
    Main function to run the graph visualization
    """
    try:
        # Connect to Memgraph
        graph = connect_to_memgraph()
        print("Connected to Memgraph successfully!")
        
        # Get graph data
        nodes, relationships = get_graph_data(graph)
        print(f"Fetched {len(nodes)} nodes and {len(relationships)} relationships from the database.")
        
        # Draw the graph
        draw_graph(nodes, relationships)
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")


if __name__ == "__main__":
    main()