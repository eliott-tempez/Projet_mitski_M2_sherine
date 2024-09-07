### Explication des codes

**Le répertoire *earlier_versions* contient les scripts et outputs utilisés pour construire l'édition papier de Shérine.**

Le script *generate_occurrences.py* est la base du travail ; il retourne deux fichiers texte (*mots_alphab.txt* et *mots_decroissant.txt*) répertoriant tous les mots présents dans tous les albums de Mitski, ainsi que le nombre de fois qu'ils sont retrouvés, classés selon les mots les plus retrouvés globalement aux moins retrouvés, ou classés alphabétiquement. Ce nombre d'occurrences est donné parmi tous les albums cumulés, ainsi que par album individuel. Voici les étapes de ce script : 
* ouverture des fichiers texte des paroles pour chacun des albums et stockage du texte
* suppression des stop words (déterminants, auxilliaires, ...) et de la ponctuation
* comptage des mots dans chacun des albums
* addition de ce compte pour créer un nombre d'occurrences global ainsi que par album
* écriture des résultats dans les fichiers texte

Le script *search_sentences.py* permet, pour chacun des mots du dernier album de Mitski, de rechercher toutes les occurrences de ce mot dans le reste des six albums, et d'afficher chacune des phrases dans lesquelles nous les retrouvons. Il écrit le résultat dans le fichier *words_in_sentences.txt*, c'est à dire le mot recherchée, la phrase retrouvée, ainsi que le numéro de l'album dans lequel elle a été trouvée et le numéro de la ligne correspondante.


**Les scripts dans le dossier principal permettent de créer l'application dynamique qui invitent l'utilisateur à choisir ses propres paramètres pour la coloration des mots selon leur occurrence**

* Le script *app.py* affiche visuellement le contenu du template *index.html* pour laisser l'utilisateur choisir les paramètres de recherche des occurrences des mots dans les albums, et renvoie ces choix aux deux scripts suivants. Lorsque les deux scripts suivants ont fini leur exécution, il affiche le document html généré à l'écran.
* Le script *generate_occurrences.py* est une version modifié du script du même nom décrit précédemment, et renvoie le fichier texte de la liste des occurrences selon ce que l'utilisateur a choisi comme critères.
* Le script *generate_html.py* prend le fichier de sortie de *generate_occurrences.py* et génère la visualisation html souhaitée, selon la palette de couleurs choisie par l'utilisateur.