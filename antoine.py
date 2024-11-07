import tkinter as tk
import fonctions 

fenetre = tk.Tk()
fenetre.title("Affichage du Score")

label = tk.Label(fenetre, text="Space invaders")
label.pack()


score_initial = fonctions.obtenir_score()
label_score = tk.Label(fenetre, text=f"Score : {score_initial}", font=("Arial", 16))
label_score.pack(pady=20)

fenetre.mainloop()