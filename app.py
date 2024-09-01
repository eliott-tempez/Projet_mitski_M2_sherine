from flask import Flask, render_template, request, redirect, url_for
import subprocess  # Pour exécuter les scripts existants
import os

app = Flask(__name__)

# Chemin vers les fichiers générés
OUTPUT_HTML_PATH = 'output/paroles_album.html'

@app.route('/')
def index():
    # Rendre la page d'accueil avec le formulaire
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    # Récupérer les valeurs du formulaire
    min_occurrences = request.form.get('min_occurrences', 1, type=int)
    unique_albums = request.form.get('unique_albums') == 'on'
    colormap = request.form.get('colormap', 'bwr')

    # Exécuter le script pour générer le fichier d'occurrences
    subprocess.run(['python', 'generate_occurrences.py', str(min_occurrences), str(unique_albums)])

    # Exécuter le script pour générer le fichier HTML
    subprocess.run(['python', 'generate_html.py', colormap])

    # Rediriger vers le fichier HTML généré
    return redirect(url_for('output'))

@app.route('/output')
def output():
    # Afficher le fichier HTML généré
    return render_template(OUTPUT_HTML_PATH)

if __name__ == '__main__':
    # Démarrer l'application Flask
    app.run(debug=True)
