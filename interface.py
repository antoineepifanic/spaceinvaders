"""
interface.py
Gestion de l'interface utilisateur du jeu Space Invaders

Ce module contient toutes les fonctions liées à la création et la gestion
de l'interface graphique : menus, labels, fenêtres et éléments visuels.

Date de création : Décembre 2024
Auteur : Antoine & Armand
"""

import tkinter as tk
from PIL import Image, ImageTk

def afficher_a_propos(fenetre):
    """Affiche la fenêtre 'À propos' avec les informations du jeu"""
    fenetre_apropos = tk.Toplevel(fenetre)
    fenetre_apropos.title("À propos")
    fenetre_apropos.geometry("400x300")
    
    fenetre_apropos.transient(fenetre)
    fenetre_apropos.grab_set()
    
    texte_apropos = """Space Invaders
    
Version 1.0
    
Créé par Antoine et Armand
Module CS-DEV - 3ETI
    
Un jeu inspiré du classique Space Invaders
avec quelques fonctionnalités modernes ajoutées.
    
© 2024"""
    
    label = tk.Label(fenetre_apropos, text=texte_apropos, justify=tk.LEFT, padx=20, pady=20)
    label.pack(expand=True)
    
    bouton_fermer = tk.Button(fenetre_apropos, text="Fermer", command=fenetre_apropos.destroy)
    bouton_fermer.pack(pady=20)

def creer_menu_principal(fenetre, canvas_menu, Width, Height):
    """Crée les éléments du menu principal du jeu"""
    # Bouton Quitter
    canvas_menu.create_text(780, 20, text="Quitter", fill="white", 
                       font=('Helvetica', 12), anchor="ne", tags="quitter")
    
    # Logo du jeu
    logo_image = Image.open("ressources/logospaceinvaders.jpg")
    logo_image = logo_image.resize((400, 200))
    logo_photo = ImageTk.PhotoImage(logo_image)
    canvas_menu.create_image(400, 250, image=logo_photo)
    canvas_menu.logo = logo_photo  # Référence pour éviter la collecte de déchets
    
    # Options de menu
    canvas_menu.create_text(400, 600, text="Démarrer Partie", 
                       fill="white", font=('Helvetica', 20), tags="demarrer")
    
    canvas_menu.create_text(400, 650, text="À propos", 
                       fill="white", font=('Helvetica', 20), tags="apropos")

def creer_zone_jeu(frame_partie, canvas_partie, Width, Height):
    """Configure la zone de jeu et ses éléments graphiques"""
    # Configuration de l'arrière-plan
    background_image = Image.open("ressources/background.jpg")
    background_image = background_image.resize((Width, Height))
    background_photo = ImageTk.PhotoImage(background_image)
    background_id = canvas_partie.create_image(0, 0, image=background_photo, 
                                         anchor="nw", tags="background")
    canvas_partie.background = background_photo  # Référence pour éviter la collecte de déchets
    
    # Création du bouton retour
    bouton_retour = tk.Button(frame_partie, text="Retour au menu")
    bouton_retour.pack(side="top", anchor="ne", pady=(10, 0), padx=(0, 10))
    
    return bouton_retour

def creer_labels(frame_partie):
    """Crée les labels pour le score et les vies"""
    # Label score
    label_score = tk.Label(frame_partie, text="Score : 0", font=("Arial", 16))
    label_score.pack(side="left", pady=(0, 20))
    
    # Label vies
    lives_label = tk.Label(frame_partie, text="Vies: 3", font=("Arial", 16))
    lives_label.pack(side="right", pady=(0, 20), padx=(20, 0))
    
    return label_score, lives_label