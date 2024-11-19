"""
 _______  _______  _______  _______  _______   _________ _                 _______  ______   _______  _______  _______ 
(  ____ \(  ____ )(  ___  )(  ____ \(  ____ \  \__   __/( (    /||\     /|(  ___  )(  __  \ (  ____ \(  ____ )(  ____ \
| (    \/| (    )|| (   ) || (    \/| (    \/     ) (   |  \  ( || )   ( || (   ) || (  \  )| (    \/| (    )|| (    \/
| (_____ | (____)|| (___) || |      | (__         | |   |   \ | || |   | || (___) || |   ) || (__    | (____)|| (_____ 
(_____  )|  _____)|  ___  || |      |  __)        | |   | (\ \) |( (   ) )|  ___  || |   | ||  __)   |     __)(_____  )
      ) || (      | (   ) || |      | (           | |   | | \   | \ \_/ / | (   ) || |   ) || (      | (\ (         ) |
/\____) || )      | )   ( || (____/\| (____/\  ___) (___| )  \  |  \   /  | )   ( || (__/  )| (____/\| ) \ \__/\____) |
\_______)|/       |/     \|(_______/(_______/  \_______/|/    )_)   \_/   |/     \|(______/ (_______/|/   \__/\_______)
                                                                                                                      

Armand de Pompignan et Antoine Epifanic
7/11 
Objectif création d'un jeu space invaders
"""

import tkinter as tk
import fonctions
from RectangleControle import RectangleControle

# Fonction pour afficher la partie
def demarrer_partie():
    frame_menu.pack_forget()  
    frame_partie.pack(fill="both", expand=True)  

# Fonction pour revenir au menu
def retourner_menu():
    frame_partie.pack_forget()  
    frame_menu.pack(fill="both", expand=True) 

# Fenêtre de jeu globale (contient le menu et tout)
fenetre = tk.Tk()
fenetre.title("Space Invaders")
fenetre.geometry("675x600")

# Frame Menu (accueil boutons réglages et tout)
frame_menu = tk.Frame(fenetre)
frame_bouton = tk.Frame(frame_menu, height=25)
frame_bouton.pack(fill="x", side="top")
bouton_quitter = tk.Button(frame_bouton, text="Quitter", command=fenetre.quit, bg="red", fg="white")
bouton_quitter.place(relx=1, anchor="ne")
zone_texte = tk.Text(frame_bouton, width=20, height=1)
zone_texte.place(anchor="nw")
meilleurscore = fonctions.record()
zone_texte.insert("1.0", f"Meilleur score={meilleurscore}")
bouton_demarrer = tk.Button(frame_menu, text="Démarrer Partie", command=demarrer_partie)
bouton_demarrer.pack(side="bottom")
label_titre = tk.Label(frame_menu, text="SP4C3 INV4D3R$", font=('Helvetica', 30))
label_titre.pack(side="top", pady=(40, 10))

# Frame Partie (jeu)
frame_partie = tk.Frame(fenetre)
canvas_partie = tk.Canvas(frame_partie, width=950, height=600, bg="lightgreen")
canvas_partie.pack(pady=20)
label_score = tk.Label(frame_partie, text="Score : 0", font=("Arial", 16))
label_score.pack(pady=20)
bouton_retour_menu = tk.Button(frame_partie, text="Retour au menu", command=retourner_menu)
bouton_retour_menu.place(relx=1, anchor="ne")

# Ajouter l'animation au canevas de jeu
animation = fonctions.Animation(canvas_partie)  # Passer le canevas existant

# Ajouter le rectangle bleu contrôlé
rectangle_controle = fonctions.RectangleControle(canvas_partie)
print(canvas_partie.coords(rectangle_controle.rect))
rectangle_controle.rect

# Affichage initial du menu
frame_menu.pack(fill="both", expand=True)
fenetre.mainloop()
