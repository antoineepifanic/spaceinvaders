# coding: utf-8
import tkinter as tk
from PIL import Image, ImageTk

def afficher_a_propos(fenetre):
    fenetre_apropos = tk.Toplevel(fenetre)
    fenetre_apropos.title("À propos")
    fenetre_apropos.geometry("400x300")
    
    fenetre_apropos.transient(fenetre)
    fenetre_apropos.grab_set()
    
    texte_apropos = """Space Invaders
    
Version 1.0
    
Créé par Armand et Antoine les meilleurs étudiants de la promotion 3ETI.
    
Ce jeu est une réplique de Space Invaders,
développé pour le module CS-DEV.
    
© 2024 - Aucun droits réservés"""
    
    label = tk.Label(fenetre_apropos, text=texte_apropos, justify=tk.LEFT, padx=20, pady=20)
    label.pack(expand=True)
    
    bouton_fermer = tk.Button(fenetre_apropos, text="Fermer", command=fenetre_apropos.destroy)
    bouton_fermer.pack(pady=20)

def creer_menu_principal(fenetre, canvas_menu, Width, Height):
    # Texte "Quitter"
    canvas_menu.create_text(780, 20, text="Quitter", fill="white", 
                       font=('Helvetica', 12), anchor="ne", tags="quitter")
    
    # Logo
    logo_image = Image.open("ressources/logospaceinvaders.jpg")
    logo_image = logo_image.resize((400, 200))
    logo_photo = ImageTk.PhotoImage(logo_image)
    canvas_menu.create_image(400, 250, image=logo_photo)
    canvas_menu.logo = logo_photo  # Garder une référence
    
    # Texte "Démarrer Partie"
    canvas_menu.create_text(400, 600, text="Démarrer Partie", 
                       fill="white", font=('Helvetica', 20), tags="demarrer")
    
    # Texte "À propos"
    canvas_menu.create_text(400, 650, text="À propos", 
                       fill="white", font=('Helvetica', 20), tags="apropos")

def creer_zone_jeu(frame_partie, canvas_partie, Width, Height):
    # Chargement de l'image d'arrière-plan
    background_image = Image.open("ressources/background.jpg")
    background_image = background_image.resize((Width, Height))
    background_photo = ImageTk.PhotoImage(background_image)
    background_id = canvas_partie.create_image(0, 0, image=background_photo, 
                                         anchor="nw", tags="background")
    canvas_partie.background = background_photo  # Garder une référence
    
    # Bouton retour menu
    bouton_retour = tk.Button(frame_partie, text="Retour au menu")
    bouton_retour.pack(side="top", anchor="ne", pady=(10, 0), padx=(0, 10))
    
    return bouton_retour

def creer_labels(frame_partie):
    # Label pour le score
    label_score = tk.Label(frame_partie, text="Score : 0", font=("Arial", 16))
    label_score.pack(side="left", pady=(0, 20))
    
    # Label pour le nombre de vies
    lives_label = tk.Label(frame_partie, text="Vies: 3", font=("Arial", 16))
    lives_label.pack(side="right", pady=(0, 20), padx=(20, 0))
    
    return label_score, lives_label