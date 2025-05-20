import tkinter as tk

import math
from PIL import Image, ImageTk




class Credit():
    def __init__(self, controleur, root):
        self.controleur = controleur
        self.root = root
        self.root.title("Tower Defense")
        self.largeur = 1200
        self.hauteur = 800
        self.root.minsize(self.largeur, self.hauteur)
        ico = Image.open("assets/Machine_Gun.png")
        photo = ImageTk.PhotoImage(ico)
        self.root.wm_iconphoto(False, photo)

        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (self.largeur // 2)
        y = (screen_height // 2) - (self.hauteur // 2)
        self.root.geometry(f"{self.largeur}x{self.hauteur}+{x}+{y}")

        self.background_frame = tk.Frame(self.root, width=self.largeur, height=self.hauteur)
        self.background_frame.pack(fill="both", expand=True)

        bg_img = Image.open("assets/couleur-fond.png")
        bg_img = bg_img.resize((screen_width, screen_height))  # Ajuster à la taille de la fenêtre
        self.bg = ImageTk.PhotoImage(bg_img)

        self.bg_canvas = tk.Canvas(self.background_frame, width=self.largeur, height=self.hauteur, highlightthickness=0)
        self.bg_canvas.place(x=0, y=0, relwidth=1, relheight=1)
        self.bg_canvas.create_image(0, 0, image=self.bg, anchor="nw", tags="background")

        self.creer_cadre_credit(self.largeur, self.hauteur)


    def afficherCredit(self):
        # Configurer la fenêtre
        self.root.title("Tower Defense - Jeu")
        self.root.geometry(f"{self.largeur}x{self.hauteur}")

        # S'assurer que les frames sont visibles
        self.background_frame.pack_propagate(False)

    def cacher(self):
        self.background_frame.pack_forget()

    def afficher(self):
        self.background_frame.pack(fill="both", expand=True)

    def creer_cadre_credit(self, largeur, hauteur):
        self.credit_frame = tk.Frame(self.background_frame, width=self.largeur, height=self.hauteur)
        self.credit_frame.config(highlightbackground = "red", highlightcolor= "red", highlightthickness=2)
        self.credit_frame.pack()
        self.titre = tk.Label(self.credit_frame, text="TOWER DEFENSE", font=("Stencil", 20, "bold"), anchor="center")
        self.par = tk.Label(self.credit_frame, text="PAR", font=("Stencil", 20, "bold"),anchor="center")


        self.titre.pack(side="top")
        self.par.pack(side="top")

