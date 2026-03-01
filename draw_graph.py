"""
Script to visualize the graph in Memgraph using PyVis for interactive visualization.
Fixed deduplication logic for both nodes and edges.
"""
import os
from pyvis.network import Network
from connection_manager import ConnectionManager


def connect_to_memgraph():
    """
    Connect to Memgraph database using ConnectionManager
    """
    conn_manager = ConnectionManager()
    return conn_manager


def get_graph_data(conn_manager):
    """
    Get all nodes and relationships from the graph database
    """
    nodes_query = """
    MATCH (n)
    RETURN id(n) AS id, labels(n) AS labels, properties(n) AS properties
    """

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
    Draw the graph using PyVis for interactive visualization.
    Includes logic to merge duplicate nodes and edges.
    """
    net = Network(height="800px", width="100%", bgcolor="#ffffff", font_color="black", directed=True)

    color_map = {
        'Category': '#FF9999',
        'Architecture': '#99CCFF',
    }

    # --- NODE DEDUPLICATION ---
    canonical_nodes = {}
    id_redirect_map = {}
    valid_canonical_ids = set()
    
    duplicates_count = 0

    for node in nodes:
        db_id = str(node['id'])
        labels = node['labels'] if node['labels'] else ['Node']
        properties = node['properties']
        primary_label = labels[0]
        name = properties.get('name', None)

        if name:
            business_key = (primary_label, name)
        else:
            business_key = (primary_label, db_id)

        if business_key in canonical_nodes:
            canonical_node_data = canonical_nodes[business_key]
            canonical_id = str(canonical_node_data['id'])
            id_redirect_map[db_id] = canonical_id
            duplicates_count += 1
        else:
            canonical_nodes[business_key] = node
            id_redirect_map[db_id] = db_id
            valid_canonical_ids.add(db_id)

    if duplicates_count > 0:
        print(f"Warning: Detected {duplicates_count} duplicate nodes. Merged them for visualization.")

    # Add unique (canonical) nodes to the graph
    for node in canonical_nodes.values():
        node_id = str(node['id'])
        labels = node['labels'] if node['labels'] else ['Node']
        properties = node['properties']

        primary_label = labels[0] if labels else 'Node'
        
        node_label = f"{primary_label}\\nID: {node_id}"
        for key, value in properties.items():
            if key != 'name':
                node_label += f"\\n{key}: {value}"

        color = color_map.get(primary_label, '#D3D3D3')
        title = properties.get('name', node_label)
        
        display_name = properties.get('name', primary_label)
        short_label = str(display_name)[:20] + ("..." if len(str(display_name)) > 20 else "")

        net.add_node(
            node_id,
            label=short_label,
            title=title,
            color=color
        )

    # --- EDGE DEDUPLICATION ---
    # Track added edges to avoid duplicates: (start_id, end_id, rel_type)
    added_edges = set()
    
    edges_added = 0
    edges_skipped_self_loop = 0
    edges_skipped_duplicate = 0
    edges_skipped_invalid = 0
    
    for rel in relationships:
        original_start = str(rel['start_id'])
        original_end = str(rel['end_id'])
        
        start_id = id_redirect_map.get(original_start)
        end_id = id_redirect_map.get(original_end)

        if start_id is None or end_id is None:
            edges_skipped_invalid += 1
            continue
            
        if start_id not in valid_canonical_ids or end_id not in valid_canonical_ids:
            edges_skipped_invalid += 1
            continue
            
        if start_id == end_id:
            edges_skipped_self_loop += 1
            continue

        rel_type = rel['type']
        properties = rel['properties']

        # Create unique key for edge deduplication
        edge_key = (start_id, end_id, rel_type)
        
        if edge_key in added_edges:
            edges_skipped_duplicate += 1
            continue
        
        added_edges.add(edge_key)

        rel_title = rel_type
        for key, value in properties.items():
            rel_title += f"\\n{key}: {value}"

        net.add_edge(start_id, end_id, label=rel_type, title=rel_title)
        edges_added += 1

    print(f"Added {edges_added} edges to visualization.")
    print(f"Skipped: {edges_skipped_duplicate} duplicates, {edges_skipped_self_loop} self-loops, {edges_skipped_invalid} invalid.")

    # Set physics configuration for better layout
    net.set_options("""
    var options = {
      "physics": {
        "enabled": true,
        "stabilization": {"iterations": 150},
        "barnesHut": {
          "gravitationalConstant": -2000,
          "centralGravity": 0.3,
          "springLength": 95
        }
      }
    }
    """)

    net.save_graph(output_file)
    print(f"Interactive graph visualization saved as {output_file}")


def main():
    """
    Main function to run the graph visualization
    """
    try:
        conn_manager = connect_to_memgraph()
        print("Connected to Memgraph successfully!")

        if not conn_manager.test_connection():
            print("Failed to connect to Memgraph")
            return

        nodes, relationships = get_graph_data(conn_manager)
        print(f"Fetched {len(nodes)} nodes and {len(relationships)} relationships from the database.")

        draw_graph(nodes, relationships)

        conn_manager.close()

    except Exception as e:
        print(f"Error occurred: {str(e)}")


if __name__ == "__main__":
    main()