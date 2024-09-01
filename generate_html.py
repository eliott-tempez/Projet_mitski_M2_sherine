import re
import matplotlib.pyplot as plt
import numpy as np
from jinja2 import Template

# lire occurences à partir du fichier
word_counts = {}
with open("mots_alphab.txt", "r") as f_in:
    f_in.readline()
    for line in f_in:
        if not re.match("^[a-z|'].*", line):
            break     
        else:
            mot = line.split()[0][:-1].strip()
            occ = int(line.split()[1].strip())
            word_counts[mot] = occ
            
# Charger le texte depuis le fichier Album7.txt
with open('./albums/Album7.txt', 'r', encoding='utf-8') as file:
    album_text = file.read()

# Trouver le nombre maximum et minimum d'occurrences
max_count = max(word_counts.values())
min_count = min(word_counts.values())

# Fonction pour générer une couleur entre bleu et rouge
def word_to_color(count, min_count, max_count):
    # Normalisation de la fréquence du mot entre 0 et 1
    norm = (count - min_count) / (max_count - min_count) if max_count > min_count else 0
    # Génération de la couleur RGB du bleu au rouge
    color = plt.cm.gist_rainbow.reversed()(norm)  # bwr est un gradient de bleu à rouge
    return f'rgb({int(color[0] * 255)}, {int(color[1] * 255)}, {int(color[2] * 255)})'

# Générer un dictionnaire de mots avec leurs couleurs
word_colors = {word: word_to_color(count, min_count, max_count) for word, count in word_counts.items()}

# Couleur par défaut pour les mots non trouvés dans le compteur
default_color = 'rgb(0, 0, 0)'  # Gris foncé

# Préparation du texte avec les couleurs et mise en forme
formatted_text = []
for line in album_text.splitlines():  # Conserver les retours à la ligne
    formatted_line = []
    for word in line.split():
        # Retirer la ponctuation autour des mots
        word_cleaned = word.strip(",.?!;:\"'")
        # Déterminer la couleur
        color = word_colors.get(word_cleaned.lower(), default_color)
        # Mettre le mot en couleur et en gras
        formatted_line.append(f'<span style="color: {color};">{word}</span>')
    # Joindre les mots de la ligne et ajouter un saut de ligne HTML
    formatted_text.append(" ".join(formatted_line))
formatted_text = "<br>".join(formatted_text)  # Conserver les retours à la ligne

# Template HTML avec style CSS
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        @font-face {
            font-family: 'AvaraBlack';  /* Nom de la police pour l'utilisation dans le CSS */
            src: url('./static/Avara-Black.otf') format('opentype');  /* Chemin vers le fichier de police */
        }
        body {
            font-family: 'AvaraBlack', sans-serif; 
        }
        .word {
            display: inline-block;
            margin: 2px;
        }
    </style>
    <title>When memories snow</title>
</head>
<body>
    <h1>The land is inhospitable and so are we</h1>
    <p>
    {{ formatted_text | safe }}
    </p>
</body>
</html>
"""

# Générer le HTML final en utilisant Jinja2
template = Template(html_template)
html_output = template.render(formatted_text=formatted_text, font_family="Garamond")  # Remplacez "Arial" par votre choix de police

# Sauvegarder le HTML dans un fichier
with open('./output/paroles_album.html', 'w', encoding='utf-8') as file:
    file.write(html_output)
