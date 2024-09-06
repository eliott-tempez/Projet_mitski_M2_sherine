# When memories snow
## Shérine AZOUG
## en collaboration avec Eliott TEMPEZ

Ce github a été créé dans le cadre du projet de M2 de Shérine, et a pour but d'explorer les thèmes des albums de l'artiste Mitski, et particulièrement de son dernier album *the land is inhospitable and so are we*. L'application Flask créée permet de lire les paroles de cet album en prenant en compte les termes retrouvés dans les albums précédents selon des critères à choisir par l'utilisateur. Le dossier earlier_versions donne accès aux codes utilisés par Shérine pour créer son objet.

Pour charger l'application de chez vous :
* Placez vous dans le répertoire courant
* Si besoin, installez l'environnement conda avec la ligne de commande
```conda env create -f environment.yaml```
* Activez l'environnement conda 
```conda activate projet_mitski```
* Lancez l'application
```python app.py```
* Ouvrez un navigateur et tapez l'url http://127.0.0.1:5000/