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

# coding: utf-8
import tkinter as tk
import fonctions
from Joueur import Joueur
from Ennemi import Ennemi
from PIL import Image, ImageTk

def demarrer_partie(event):
    canvas_menu.pack_forget()
    frame_partie.pack(fill="both", expand=True)
    fenetre.update_idletasks()
    global animation, joueur
    animation = Ennemi(canvas_partie)
    joueur = Joueur(canvas_partie)

def retourner_menu():
    for item in canvas_partie.find_all():
        if "background" not in canvas_partie.gettags(item):
            canvas_partie.delete(item)
    frame_partie.pack_forget()
    canvas_menu.pack(fill="both", expand=True)
    fenetre.update_idletasks()

fenetre = tk.Tk()
fenetre.title("Space Invaders")
fenetre.geometry("675x600")

# Menu principal
canvas_menu = tk.Canvas(fenetre, bg="black", width=675, height=600)
canvas_menu.pack(fill="both", expand=True)

# Texte "Quitter"
canvas_menu.create_text(650, 20, text="Quitter", fill="white", font=('Helvetica', 12), anchor="ne", tags="quitter")
canvas_menu.tag_bind("quitter", "<Button-1>", lambda e: fenetre.quit())

# Zone de texte pour le meilleur score
meilleurscore = fonctions.record()
canvas_menu.create_text(20, 20, text=f"Meilleur score={meilleurscore}", fill="white", font=('Helvetica', 12), anchor="nw")

# Texte "Démarrer Partie"
canvas_menu.create_text(337, 550, text="Démarrer Partie", fill="white", font=('Helvetica', 20), tags="demarrer")
canvas_menu.tag_bind("demarrer", "<Button-1>", demarrer_partie)

# Chargement et positionnement de l'image du logo
logo_image = Image.open("ressources/logospaceinvaders.jpg")
logo_image = logo_image.resize((400, 200))  # Redimensionnement de l'image
logo_photo = ImageTk.PhotoImage(logo_image)
canvas_menu.create_image(337, 200, image=logo_photo)

# Zone de jeu
frame_partie = tk.Frame(fenetre)
Width = 675

# Bouton de retour au menu
bouton_retour_menu = tk.Button(frame_partie, text="Retour au menu", command=retourner_menu)
bouton_retour_menu.pack(side="top", anchor="ne", pady=(10, 0), padx=(0, 10))

# Canvas de jeu
canvas_partie = tk.Canvas(frame_partie, width=Width, height=550)
canvas_partie.pack(pady=(10, 20))

# Chargement de l'image d'arrière-plan
background_image = Image.open("ressources/background.jpg")
background_image = background_image.resize((Width, 550))
background_photo = ImageTk.PhotoImage(background_image)
background_id = canvas_partie.create_image(0, 0, image=background_photo, anchor="nw", tags="background")
canvas_partie.image = background_photo

# Label pour le score
label_score = tk.Label(frame_partie, text="Score : 0", font=("Arial", 16))
label_score.pack(pady=(0, 20))

fenetre.mainloop()