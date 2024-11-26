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
# coding: utf-8
import tkinter as tk
import fonctions
from Joueur import Joueur
from Ennemi import Ennemi
from PIL import Image, ImageTk

def demarrer_partie():
    frame_menu.pack_forget()  
    frame_partie.pack(fill="both", expand=True)
    fenetre.update_idletasks()

def retourner_menu():
    frame_partie.pack_forget()
    frame_menu.pack(fill="both", expand=True) 
    fenetre.update_idletasks()

fenetre = tk.Tk()
fenetre.title("Space Invaders")
fenetre.geometry("675x600")

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
label_titre = tk.Label(frame_menu, text="SPACE INVADERS", font=('Helvetica', 30))
label_titre.pack(side="top", pady=(40, 10))

frame_partie = tk.Frame(fenetre)
Width = 675
canvas_partie = tk.Canvas(frame_partie, width=Width, height=600)
canvas_partie.pack(pady=20)

background_image = Image.open("ressources/background.jpg")
background_image = background_image.resize((Width, 600))
background_photo = ImageTk.PhotoImage(background_image)
canvas_partie.create_image(0, 0, image=background_photo, anchor="nw")
canvas_partie.image = background_photo

label_score = tk.Label(frame_partie, text="Score : 0", font=("Arial", 16))
label_score.pack(pady=20)
bouton_retour_menu = tk.Button(frame_partie, text="Retour au menu", command=retourner_menu)
bouton_retour_menu.place(relx=1, anchor="ne")

animation = Ennemi(canvas_partie)

joueur = Joueur(canvas_partie)

frame_menu.pack(fill="both", expand=True)
fenetre.mainloop()