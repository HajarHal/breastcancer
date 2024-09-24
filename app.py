<<<<<<< HEAD
from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, static_folder='assets', static_url_path='/assets')

def get_categories_and_graphs(cancer_type, category_type):
    folder_path = os.path.join('assets', 'graph', f'{category_type}_{cancer_type}')
    graphs = []
    if os.path.exists(folder_path):
        for filename in os.listdir(folder_path):
            if filename.endswith('.html'):
                # Clean up the filename to display as a proper name in the frontend
                graph_name = filename.replace(f'{category_type}_{cancer_type}_', '').replace('_', ' ').replace('.html', '')
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
    graph_path = f'assets/graph/{category_type}_{cancer_type}/{graph}'
    clean_filename = graph.replace(f'{category_type}_{cancer_type}_', '').replace('_', ' ').replace('.html', '')
    return render_template('graph.html', graph_path=graph_path, filename=clean_filename)


@app.route('/causes_sta')
def causes_sta():
    # Paths to the frequency graphs
    frequencies = {
        'female': 'stat/causes_female',
        'male': 'stat/causes_male',
        'recurrent': 'stat/causes_reccu'
    }
    return render_template('causes_sta.html', frequencies=frequencies)

# Serve the graph HTML files
@app.route('/assets/graph/<path:filename>')
def serve_graph(filename):
    return send_from_directory('assets/graph', filename)

if __name__ == '__main__':
    app.run(debug=True)
=======
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
>>>>>>> c3bdb7549e5d8e1bf7dc50010c8da1db4a8a606a
