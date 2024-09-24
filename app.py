from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, static_folder='assets', static_url_path='/assets')

def get_categories_and_graphs(cancer_type, category_type):
    folder_path = os.path.join('assets', 'graph', f'{category_type}_{cancer_type}')
    graphs = []
    if os.path.exists(folder_path):
        for filename in os.listdir(folder_path):
            if filename.endswith('.html'):
                # No need to remove the prefix anymore, just clean up underscores and the extension
                graph_name = filename.replace('_', ' ').replace('.html', '')
                graphs.append((graph_name, filename))  # Keep both clean name and actual filename
    return graphs

# Homepage route
@app.route('/')
def index():
    return render_template('index.html')

# Cancer type selection route
@app.route('/<cancer_type>')
def cancer_type(cancer_type):
    return render_template('cancer_type.html', cancer_type=cancer_type)

# Category type selection route (e.g., causes, treats)
@app.route('/<cancer_type>/<category_type>')
def category_type(cancer_type, category_type):
    graphs = get_categories_and_graphs(cancer_type, category_type)
    return render_template('category.html', cancer_type=cancer_type, category_type=category_type, graphs=graphs)

# Graph display route
@app.route('/<cancer_type>/<category_type>/<graph>')
def graph(cancer_type, category_type, graph):
    # Construct the correct path based on cancer_type and category_type
    graph_path = f'assets/graph/{category_type}_{cancer_type}/{graph}'
    
    # No need to modify the filename; just pass the clean name for display
    clean_filename = graph.replace('_', ' ').replace('.html', '')
    
    return render_template('graph.html', graph_path=graph_path, filename=clean_filename)



# Serve the graph HTML files from the correct directory
@app.route('/assets/graph/<category>/<filename>')
def serve_graph(category, filename):
    folder_path = os.path.join('assets', 'graph', category)
    return send_from_directory(folder_path, filename)


if __name__ == '__main__':
    app.run(debug=True)
