from collections import Counter
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
import re
import sys

####### VARIABLES #######
NB_ALBUMS = 7
# Enlever les mots contenant des apostrophes ?
CLEAN = False
# Nombre de mots minimum dans tous les albums
THRESHOLD = int(sys.argv[1])
# Besoin de trouver le mot dans au moins 2 albums différents ?
EPARSE = sys.argv[2]


####### FONCTIONS #######
""" Correction du bug des e mal codés"""
def replace_e(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    corrected_text = content.replace('е', 'e')
    with open(filename, "w", encoding="utf-8") as f:
        f.write(corrected_text)


""" Lecture d'un fichier texte et retour du texte brut sans retour à la ligne"""
def read_file(filename):
    plain_text = ""
    with open(filename, "r") as f:
        for line in f:
            plain_text += (line.strip() + " ")
    return plain_text


""" Division d'un texte brut en mots et suppression des stopwords et de la ponctuation"""
def clean_words(text, is_clean):
    # Division du texte en mots individuels
    tokens_brut = text.split(" ")
    tokens = []
    for word in tokens_brut:
        if "/" in word:
            mots = word.split("/")
            for mot in mots:
                tokens.append(mot)
        else:
            tokens.append(word)
    # Suppression de la ponctuation (?/,/:/"")
    sans_punct = []
    for word in tokens:
        if re.match(".*(\?|:|,|\"|\)|\().*", word):
            sans_punct.append(re.sub("\?|:|,|\"|\(|\)", "", word.lower()))
        else:
            sans_punct.append(word.lower())
    # Suppression des stopwords
    stop_words = set(stopwords.words('english'))
    sans_stop = [word.lower() for word in sans_punct if word.lower() not in stop_words and word != ""]
    if is_clean:
        sans_stop = [word for word in sans_stop if "'" not in word or word.startswith("'")]
    return sans_stop


"""Ecrire un compteur dans l'ordre choisi : alphabétique (a) ou décroissant(d)"""
def write_dict(word_count, order):
    text = ""
    if order == "d":
        sorted_counter = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
        for word, count in sorted_counter:
            text += f"{word}: {count}\n"
    elif order == "a":
        sorted_counter = sorted(word_count.items(), key=lambda x: x[0])
        for word, count in sorted_counter:
            text += f"{word}: {count}\n"
    return text


"""Ne garder les mots présents qu'une quantité prédéfinie"""
def keep_words(dict, threshold, nb_albums, eparse):
    words_to_keep = []
    new_dict = {}
    for word, count in dict[0].items():
        if count >= threshold:
            if eparse:
                nb_diff_albums = 0
                for i in range(1, nb_albums + 1):
                    if word in list(dict[i].keys()):
                        nb_diff_albums += 1
                if nb_diff_albums > 1:
                    words_to_keep.append(word)
            else:
                words_to_keep.append(word)
    for key in dict:
        new_dict[key] = Counter()
        for word, count in dict[key].items():
            if word in words_to_keep:
                new_dict[key][word] = count
    return new_dict
        
        
        
####### MAIN #######
if __name__ == "__main__":
    # Dictionnaire de comptage
    count_dict = {}
    count_dict[0] = Counter()
    # Parcours des albums
    for i in range(1, NB_ALBUMS + 1):
        # Sous-dictionnaire
        filename = f"./albums/Album{i}.txt"
        # Correction de l'affichage du e 
        replace_e(filename)
        # Lecture des fichiers
        plain_text = read_file(filename)
        # Nettoyage des mots
        words = clean_words(plain_text, CLEAN)
        # Remplissage du dictionnaire
        count_dict[i] = Counter(words)
        # Ajout au dictionnaire général
        count_dict[0] += count_dict[i]
        
    # Ne garder que les mots avec un fréquence supérieure au seuil
    count_dict = keep_words(count_dict, THRESHOLD, NB_ALBUMS, EPARSE)
    # Ecriture des fichiers
    # Ordre décroissant
    with open("./counter/mots_decroissant.txt", "w") as f:
        for i in range(NB_ALBUMS + 1):
            f.write(f"###### Album {i} ######\n{write_dict(count_dict[i], 'd')}\n")
    
    # Ordre alphabétique
    with open("./counter/mots_alphab.txt", "w") as f:
        for i in range(NB_ALBUMS + 1):
            f.write(f"###### Album {i} ######\n{write_dict(count_dict[i], 'a')}\n")

        
        