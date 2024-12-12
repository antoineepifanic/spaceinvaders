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
from Protections import Protections

def afficher_a_propos():
    # Créer une nouvelle fenêtre
    fenetre_apropos = tk.Toplevel(fenetre)
    fenetre_apropos.title("À propos")
    fenetre_apropos.geometry("500x400")
    
    # Empêcher l'interaction avec la fenêtre principale
    fenetre_apropos.transient(fenetre)
    fenetre_apropos.grab_set()
    
    # Ajouter le texte
    texte_apropos = """Space Invaders
    
Version 1.0
    
Créé par Antoine et Armand les meilleurs élèves de la promotion 3ETI
    
Ce jeu est une réplique de Space Invaders,
développé pour le module CS-DEV
    
© 2024 - Aucun droits réservés"""
    
    label = tk.Label(fenetre_apropos, text=texte_apropos, justify=tk.LEFT, padx=20, pady=20)
    label.pack(expand=True)
    
    # Bouton pour fermer la fenêtre
    bouton_fermer = tk.Button(fenetre_apropos, text="Fermer", command=fenetre_apropos.destroy)
    bouton_fermer.pack(pady=20)

def demarrer_partie(event):
    canvas_menu.pack_forget()
    frame_partie.pack(fill="both", expand=True)
    fenetre.update_idletasks()
    global animation, joueur, protections
    animation = Ennemi(canvas_partie)
    joueur = Joueur(canvas_partie)
    fenetre.joueur = joueur  # Stocker le joueur comme attribut de la fenêtre
    protections = Protections(canvas_partie, width=Width, y_position=400)
    update_lives_display()

def retourner_menu():
    for item in canvas_partie.find_all():
        if "background" not in canvas_partie.gettags(item):
            canvas_partie.delete(item)
    frame_partie.pack_forget()
    canvas_menu.pack(fill="both", expand=True)
    fenetre.update_idletasks()

def update_lives_display():
    global lives_label
    lives_label.config(text=f"Vies: {joueur.vies}")
    if joueur.vies > 0:
        fenetre.after(100, update_lives_display)
    else:
        game_over()

def game_over():
    canvas_partie.create_text(
        Width // 2, 
        Height // 2, 
        text="GAME OVER", 
        font=('Helvetica', 36), 
        fill='red'
    )

# Initialisation de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Space Invaders")
fenetre.geometry("800x800")

# Menu principal
canvas_menu = tk.Canvas(fenetre, bg="black", width=800, height=650)
canvas_menu.pack(fill="both", expand=True)

# Texte "Quitter"
canvas_menu.create_text(780, 20, text="Quitter", fill="white", 
                       font=('Helvetica', 12), anchor="ne", tags="quitter")
canvas_menu.tag_bind("quitter", "<Button-1>", lambda e: fenetre.quit())

# Zone de texte pour le meilleur score
meilleurscore = fonctions.record()
canvas_menu.create_text(20, 20, text=f"Meilleur score={meilleurscore}", 
                       fill="white", font=('Helvetica', 12), anchor="nw")

# Texte "Démarrer Partie"
canvas_menu.create_text(400, 600, text="Démarrer Partie", 
                       fill="white", font=('Helvetica', 20), tags="demarrer")
canvas_menu.tag_bind("demarrer", "<Button-1>", demarrer_partie)

# Texte "À propos"
canvas_menu.create_text(400, 650, text="À propos", 
                       fill="white", font=('Helvetica', 20), tags="apropos")
canvas_menu.tag_bind("apropos", "<Button-1>", lambda e: afficher_a_propos())

# Chargement et positionnement de l'image du logo
logo_image = Image.open("ressources/logospaceinvaders.jpg")
logo_image = logo_image.resize((400, 200))
logo_photo = ImageTk.PhotoImage(logo_image)
canvas_menu.create_image(400, 250, image=logo_photo)

# Zone de jeu
frame_partie = tk.Frame(fenetre)
Width = 675
Height = 550

# Bouton de retour au menu
bouton_retour_menu = tk.Button(frame_partie, text="Retour au menu", 
                              command=retourner_menu)
bouton_retour_menu.pack(side="top", anchor="ne", pady=(10, 0), padx=(0, 10))

# Canvas de jeu
canvas_partie = tk.Canvas(frame_partie, width=Width, height=Height)
canvas_partie.pack(pady=(10, 20))

# Chargement de l'image d'arrière-plan
background_image = Image.open("ressources/background.jpg")
background_image = background_image.resize((Width, Height))
background_photo = ImageTk.PhotoImage(background_image)
background_id = canvas_partie.create_image(0, 0, image=background_photo, 
                                         anchor="nw", tags="background")
canvas_partie.image = background_photo

# Label pour le score
label_score = tk.Label(frame_partie, text="Score : 0", font=("Arial", 16))
label_score.pack(side="left", pady=(0, 20))

# Label pour le nombre de vies
lives_label = tk.Label(frame_partie, text="Vies: 3", font=("Arial", 16))
lives_label.pack(side="right", pady=(0, 20), padx=(20, 0))

fenetre.mainloop()