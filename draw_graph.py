"""
Script to visualize the graph in Memgraph using PyVis for interactive visualization.
"""
import os
from pyvis.network import Network
from connection_manager import ConnectionManager


def connect_to_memgraph():
    """
    Connect to Memgraph database using ConnectionManager
    """
    # Using ConnectionManager to connect to Memgraph
    conn_manager = ConnectionManager()
    return conn_manager


def get_graph_data(conn_manager):
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

    nodes = conn_manager.run_query(nodes_query)
    relationships = conn_manager.run_query(rels_query)

    return nodes, relationships


def draw_graph(nodes, relationships, output_file='graph_visualization.html'):
    """
    Draw the graph using PyVis for interactive visualization
    """
    # Create network
    net = Network(height="800px", width="100%", bgcolor="#ffffff", font_color="black", directed=True)

    # Define colors for different node types
    color_map = {
        'Category': '#FF9999',      # Light red for categories
        'Architecture': '#99CCFF',  # Light blue for architectures
    }

    # Add nodes to the graph
    for node in nodes:
        node_id = str(node['id'])
        labels = node['labels'] if node['labels'] else ['Node']
        properties = node['properties']

        # Create label for the node with its properties
        primary_label = labels[0] if labels else 'Node'
        node_label = f"{primary_label}\\nID: {node_id}"
        for key, value in properties.items():
            if key != 'name':  # Don't duplicate the name property since we're using it as the title
                node_label += f"\\n{key}: {value}"

        # Determine color based on node type
        color = color_map.get(primary_label, '#D3D3D3')  # Default to light gray

        # Use name property as title if available, otherwise use the constructed label
        title = properties.get('name', node_label)

        # Add node to the network
        net.add_node(
            node_id,
            label=properties.get('name', primary_label)[:20] + ("..." if len(str(properties.get('name', primary_label))) > 20 else ""),
            title=title,
            color=color
        )

    # Add relationships to the graph
    for rel in relationships:
        start_id = str(rel['start_id'])
        end_id = str(rel['end_id'])
        rel_type = rel['type']
        properties = rel['properties']

        # Create title for the relationship
        rel_title = rel_type
        for key, value in properties.items():
            rel_title += f"\\n{key}: {value}"

        # Add edge to the network
        net.add_edge(start_id, end_id, label=rel_type, title=rel_title)

    # Set physics configuration for better layout
    net.set_options("""
    var options = {
      "physics": {
        "enabled": true,
        "stabilization": {"iterations": 100}
      }
    }
    """)

    # Save the network
    net.save_graph(output_file)
    print(f"Interactive graph visualization saved as {output_file}")


def main():
    """
    Main function to run the graph visualization
    """
    try:
        # Connect to Memgraph
        conn_manager = connect_to_memgraph()
        print("Connected to Memgraph successfully!")

        # Test connection
        if not conn_manager.test_connection():
            print("Failed to connect to Memgraph")
            return

        # Get graph data
        nodes, relationships = get_graph_data(conn_manager)
        print(f"Fetched {len(nodes)} nodes and {len(relationships)} relationships from the database.")

        # Draw the graph
        draw_graph(nodes, relationships)

        # Close connection
        conn_manager.close()

    except Exception as e:
        print(f"Error occurred: {str(e)}")


if __name__ == "__main__":
    main()