"""
Ce script permet, pour chacun des mots du dernier album de Mitski, 
d'obtenir toutes les phrases contenant ces mots dans chacun des six albums
précédents. Le fichier texte créé est words_in_sentences.txt
"""


import re


####### FONCTIONS #######
""" Lecture d'un fichier texte et retour du texte en minuscule sans ponctuation"""
def read_file(filename):
    plain_text = ""
    with open(filename, "r") as f:
        for line in f:
            lowered = line.strip().lower() + "\n"
            if re.match(".*(\?|:|,|\"|\)|\().*", lowered):
                plain_text += re.sub("\?|:|,|\"|\(|\)", "", lowered)
            else:
                plain_text += lowered        
    return plain_text


"""Récupérer les mots uniques dans l'album de ref"""
def get_unique_words(filename):
    unique_words = []
    texte = read_file(filename)
    [unique_words.append(word) for word in texte.split() if word not in unique_words]
    return unique_words   
        
        
        
if __name__ == "__main__":
    dico = {}
    # récupérer les mots de l'album principal    
    unique_words = get_unique_words("data/album7.txt")
    for w in unique_words:
        dico[w] = {}
   
    # chercher les mots dans les autres albums
    for i in range(1, 7):
        # Sous-dictionnaire
        filename = f"data/album{i}.txt"
        # Lecture des fichiers
        plain_text = read_file(filename)
        
        # Ajout de chacune des phrases dans un dictionnaire
        for w in unique_words:
            nb_lines = len(plain_text.split('\n'))
            for j in range(0, nb_lines):
                line = plain_text.split('\n')[j]
                line_split = line.split()
                if w in line_split:
                    n_album = i
                    n_ligne = j + 1
                    if n_album not in dico[w]:
                        dico[w][n_album] = {}
                    dico[w][n_album][n_ligne] = line
                    
    # Ecriture du fichier de sortie
    with open("earlier_versions/outputs/words_in_sentences.txt", "w") as f_out:
        for word in dico:
            for n_album in dico[word]:
                for n_ligne in dico[word][n_album]:
                    f_out.write(f"{word} :\t{n_album}\t{n_ligne}\t{dico[word][n_album][n_ligne]}\n")
        
    

        
        
    