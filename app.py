from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import subprocess  # Pour exécuter les scripts existants
import os

app = Flask(__name__)

# Chemin vers le dossier où sont stockés les fichiers générés
OUTPUT_DIR = 'output'
OUTPUT_HTML_FILE = 'paroles_album.html'

@app.route('/')
def index():
    # Rendre la page d'accueil avec le formulaire
    return render_template('index.html')

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

@app.route('/generate', methods=['POST'])
def generate():
    # Récupérer les valeurs du formulaire
    min_occurrences = request.form.get('min_occurrences', type=int)
    unique_albums = request.form.get('unique_albums') == 'on'
    colormap = request.form.get('colormap', 'bwr')

    # Exécuter le script pour générer le fichier d'occurrences
    subprocess.run(['python', 'generate_occurrences.py', str(min_occurrences), str(unique_albums)])

    # Exécuter le script pour générer le fichier HTML
    subprocess.run(['python', 'generate_html.py', colormap])

    # Rediriger vers le fichier HTML généré
    return redirect(url_for('serve_file'))

@app.route('/output')
def serve_file():
    # Servir le fichier HTML généré à partir du répertoire 'output'
    return send_from_directory(OUTPUT_DIR, OUTPUT_HTML_FILE)

if __name__ == '__main__':
    # Démarrer l'application Flask
    app.run(debug=True)
