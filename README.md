Space Invaders
Un jeu Space Invaders développé en Python avec Tkinter.

Description :
Ce jeu reprend les mécaniques classiques de Space Invaders :

Contrôlez un vaisseau qui peut se déplacer horizontalement et tirer
Détruisez tous les ennemis avant qu'ils n'atteignent votre position
Évitez ou détruisez les tirs ennemis
Des protections peuvent vous aider à bloquer les tirs ennemis
Un ennemi bonus apparaît périodiquement pour des points supplémentaires

Points et Score :

Ennemi standard : 25 points
Ennemi bonus (vert) : 150 points
Bonus fin de partie : 50 points par vie restante

Contrôles :

Flèche Gauche : Déplacer le vaisseau à gauche
Flèche Droite : Déplacer le vaisseau à droite
Espace : Tirer

Conditions de fin de partie
La partie se termine dans les cas suivants :

Victoire : Tous les ennemis sont détruits
Défaite :Le joueur perd ses 3 vies ou les ennemis atteignent la hauteur des protections

https://github.com/antoineepifanic/spaceinvaders

Structures demandées :

Un chargé de TD nous a dit que l'implémentation de piles et de files n'était pas obligatoire finalement. Il ne nous a pas paru pertinent,
dans le cadre de notre programme, d'en implanter, d'où leur absence.
Cependant, nous travaillons évidemment avec de nombreuses listes, notamment pour gérer les coordonnées, comme par exemple :

ligne 71 dans Ennemi.py

Tous les collisions sont gérées en analysant les coordonnées des éléments du jeu qui se trouvent elles-mêmes dans des listes,
comme par exemple :

ligne 112 dans Tir_Ennemi.py

NB IMPORTANT :

J'ai travaillé sous Mac et il semble que le placement et la taille des fenêtres ne sont pas toujours exactement les mêmes entre les 2 OS,
normalement la fenêtre de jeu devrai s'ouvrir et on devrait voir score et point de vie directement sans avoir à agrandir mais ce n'est pas 
forcément le cas sous windows, désolé !