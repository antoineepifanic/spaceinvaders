"""
 _______  _______  _______  _______  _______   _________ _                 _______  ______   _______  _______  _______ 
(  ____ \(  ____ )(  ___  )(  ____ \(  ____ \  \__   __/( (    /||\     /|(  ___  )(  __  \ (  ____ \(  ____ )(  ____ \
| (    \/| (    )|| (   ) || (    \/| (    \/     ) (   |  \  ( || )   ( || (   ) || (  \  )| (    \/| (    )|| (    \/
| (_____ | (____)|| (___) || |      | (__         | |   |   \ | || |   | || (___) || |   ) || (__    | (____)|| (_____ 
(_____  )|  _____)|  ___  || |      |  __)        | |   | (\ \) |( (   ) )|  ___  || |   | ||  __)   |     __)(_____  )
      ) || (      | (   ) || |      | (           | |   | | \   | \ \_/ / | (   ) || |   ) || (      | (\ (         ) |
/\____) || )      | )   ( || (____/\| (____/\  ___) (___| )  \  |  \   /  | )   ( || (__/  )| (____/\| ) \ \__/\____) |
\_______)|/       |/     \|(_______/(_______/  \_______/|/    )_)   \_/   |/     \|(______/ (_______/|/   \__/\_______)
                                                                                                                      

Armand de Pompignan
7/11 
Objectif création d'un jeu space invaders
"""

import tkinter as tk
import fonctions

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
fenetre.geometry("1000x700")

# Frame Menu (accueil boutons réglages et tout)
frame_menu = tk.Frame(fenetre)
canvas_menu = tk.Canvas(frame_menu, width=950, height=600, bg="lightblue")
canvas_menu.pack(pady=20)
bouton_quitter = tk.Button(frame_menu, text="Quitter", command=fenetre.quit, bg="red", fg="white")
bouton_quitter.place(relx=1, anchor="ne")
zone_texte = tk.Text(frame_menu, width=20, height=1)
zone_texte.place(anchor="nw")
meilleurscore = fonctions.record()
zone_texte.insert("1.0", f"Meilleur score={meilleurscore}")
bouton_demarrer = tk.Button(frame_menu, text="Démarrer Partie", command=demarrer_partie)
bouton_demarrer.pack(pady=20)

# Frame Partie (jeu)
frame_partie = tk.Frame(fenetre)
canvas_partie = tk.Canvas(frame_partie, width=950, height=600, bg="lightgreen")
canvas_partie.pack(pady=20)
label_score = tk.Label(frame_partie, text="Score : 0", font=("Arial", 16))
label_score.pack(pady=20)
bouton_retour_menu = tk.Button(frame_partie, text="Retour au menu", command=retourner_menu)
bouton_retour_menu.place(relx=1, anchor="ne")

# Affichage initial du menu
frame_menu.pack(fill="both", expand=True)
fenetre.mainloop()