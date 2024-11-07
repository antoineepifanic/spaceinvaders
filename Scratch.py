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
Objectif création d'un jeu space invader
"""

import tkinter as tk

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Exemple de Canvas Tkinter")

# Définir les dimensions de la fenêtre
fenetre.geometry("400x400")

# Créer un canvas
canvas = tk.Canvas(fenetre, width=300, height=300, bg="lightblue")
canvas.pack(pady=20)

bouton_quitter = tk.Button(fenetre, text="Quitter", command=fenetre.quit, bg ="red", fg="white")
bouton_quitter.place(x=350, y=10)


# Lancer la boucle principale
fenetre.mainloop()
