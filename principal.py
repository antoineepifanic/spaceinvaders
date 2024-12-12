"""
principal.py
Fichier principal du jeu Space Invaders

Ce fichier gère le lancement et la gestion principale du jeu Space Invaders.
Il contient la configuration initiale, le menu principal et la gestion des parties.

Date de création : Décembre 2024
Auteur : Antoine & Armand
"""

import tkinter as tk
import fonctions
from Joueur import Joueur
from Ennemi import Ennemi
from PIL import Image, ImageTk
from Protections import Protections
from Boss import Ennemi_bonus
import interface


def demarrer_partie(event):
    """Initialise et démarre une nouvelle partie"""
    canvas_menu.pack_forget()
    frame_partie.pack(fill="both", expand=True)
    fenetre.update_idletasks()
    
    global animation, joueur, protections
    fenetre.score = 0
    update_score()
    animation = Ennemi(canvas_partie)
    joueur = Joueur(canvas_partie)
    fenetre.joueur = joueur
    protections = Protections(canvas_partie, width=Width, y_position=400)
    update_lives_display()


def retourner_menu():
    """Retourne au menu principal et réinitialise la zone de jeu"""
    for item in canvas_partie.find_all():
        if "background" not in canvas_partie.gettags(item):
            canvas_partie.delete(item)
    frame_partie.pack_forget()
    canvas_menu.pack(fill="both", expand=True)
    meilleurscore = fonctions.record()
    for item in canvas_menu.find_all():
        if "score" in canvas_menu.gettags(item):
            canvas_menu.delete(item)
    canvas_menu.create_text(20, 20, text=f"Meilleur score={meilleurscore}", 
                       fill="white", font=('Helvetica', 12), anchor="nw", tags="score")
    fenetre.update_idletasks()


def update_lives_display():
    """Met à jour l'affichage des vies restantes"""
    global lives_label
    lives_label.config(text=f"Vies: {joueur.vies}")
    if joueur.vies > 0:
        fenetre.after(100, update_lives_display)
    else:
        game_over()


def update_score():
    """Met à jour l'affichage du score"""
    label_score.config(text=f"Score : {fenetre.score}")


def game_over():
    """Gère la fin de partie et affiche le score final"""
    for item in canvas_partie.find_all():
        if "background" not in canvas_partie.gettags(item):
            canvas_partie.delete(item)
    
    global animation, joueur, protections
    
    # Ajoute le bonus pour les vies restantes
    if joueur and joueur.vies > 0:
        fenetre.score += joueur.vies * 50
        
    animation = None
    joueur = None
    protections = None
    
    fonctions.sauvegarder_record(fenetre.score)
    
    canvas_partie.create_text(
        Width // 2, 
        Height // 2, 
        text="GAME OVER", 
        font=('Helvetica', 36), 
        fill='red'
    )
    
    canvas_partie.create_text(
        Width // 2,
        (Height // 2) + 50,
        text=f"Score final : {fenetre.score}",
        font=('Helvetica', 24),
        fill='white'
    )


# Configuration de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Space Invaders")
fenetre.geometry("800x800")
fenetre.score = 0
fenetre.update_score = update_score
fenetre.game_over = game_over

# Dimensions du jeu
Width = 675
Height = 550

# Création du menu principal
canvas_menu = tk.Canvas(fenetre, bg="black", width=800, height=650)
canvas_menu.pack(fill="both", expand=True)

# Configuration de l'interface
interface.creer_menu_principal(fenetre, canvas_menu, Width, Height)

# Affichage du meilleur score
meilleurscore = fonctions.record()
canvas_menu.create_text(20, 20, text=f"Meilleur score={meilleurscore}", 
                       fill="white", font=('Helvetica', 12), 
                       anchor="nw", tags="score")

# Configuration de la zone de jeu
frame_partie = tk.Frame(fenetre)
canvas_partie = tk.Canvas(frame_partie, width=Width, height=Height)
canvas_partie.pack(pady=(10, 20))

# Configuration de l'interface de jeu
bouton_retour_menu = interface.creer_zone_jeu(frame_partie, canvas_partie, Width, Height)
bouton_retour_menu.config(command=retourner_menu)

# Création des labels de score et de vies
label_score, lives_label = interface.creer_labels(frame_partie)

# Configuration des événements
canvas_menu.tag_bind("quitter", "<Button-1>", lambda e: fenetre.quit())
canvas_menu.tag_bind("demarrer", "<Button-1>", demarrer_partie)
canvas_menu.tag_bind("apropos", "<Button-1>", lambda e: interface.afficher_a_propos(fenetre))

# Lancement du jeu
fenetre.mainloop()