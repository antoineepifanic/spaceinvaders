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


fenetre = tk.Tk()
fenetre.title("Warzone")
fenetre.geometry("1000x700")
canvas = tk.Canvas(fenetre, width=950, height=600, bg="lightblue")
canvas.pack(pady=20)
bouton_quitter = tk.Button(fenetre, text="Quitter", command=fenetre.quit, bg ="red", fg="white")
bouton_quitter.place(relx=1, anchor="ne")  
zone_texte = tk.Text(fenetre, width=20, height=1)
zone_texte.place( anchor="nw")
a=1000
zone_texte.insert("1.0","score=",a)
fenetre.mainloop()
