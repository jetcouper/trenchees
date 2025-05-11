import tkinter as tk
from tkinter import ttk

from PIL import ImageTk,Image


class Parametre():
    def __init__(self, controleur, root, largeur, hauteur):
        self.controleur = controleur
        self.root = root
        self.root.title("Tower Defense")
        self.root.geometry(f"{largeur}x{hauteur}")
        self.root.minsize(largeur, hauteur)
        # self.controleur = controleur
        # self.modele = modele
        self.largeur = largeur
        self.hauteur = hauteur
        self.difficulte = 0



        # Création du frame pour les widgets des paramètres
        self.frame_parametres = tk.Frame(self.root, width=largeur, height=hauteur, bg="#81392a")

        # Bouton pour retourner au menu
        self.btn_retour = tk.Button(self.frame_parametres, text="Retour au menu",
                                    command=self.retour_menu)

        # Ces éléments ne sont pas encore placés dans la fenêtre

    def afficherParametre(self):
        """Initialise et affiche tous les éléments de la vue paramètres"""
        # Placement du canvas principal

        # Placement du frame latéral avec les paramètres
        self.frame_parametres.pack(fill="both", expand=True)
        self.frame_parametres.config(bg="#81392a")
        self.frame_parametres.pack_propagate(False)  # Empêche le redimensionnement du frame

        # Ajout des widgets de paramètres


        # Ajout d'autres widgets pour les paramètres du jeu
        tk.Label(self.frame_parametres, text="Paramètres du jeu", bg="#81392a", font=("Stencil", 40, "bold")).pack(
            pady=10)

        self.fontCustomiserRadio = ("Stencil", 40 ,"bold")
        self.fontCustomiserButton = ("Stencil", 30, "bold")
        # Exemple: Difficulté
        tk.Label(self.frame_parametres, text="Difficulté:", bg="#81392a", font=self.fontCustomiserRadio).pack(anchor="w", padx=5, pady=5)

        self.var_difficulte = tk.IntVar(value=self.controleur.modele.difficulte)

        tk.Radiobutton(self.frame_parametres, text="Facile", variable=self.var_difficulte, value=1, bg="#81392a", font=self.fontCustomiserRadio).pack(
            anchor="w", padx=15)
        tk.Radiobutton(self.frame_parametres, text="Normale", variable=self.var_difficulte, value=2,
                       bg="#81392a", font=self.fontCustomiserRadio).pack(anchor="w", padx=15)
        tk.Radiobutton(self.frame_parametres, text="Difficile", variable=self.var_difficulte, value=3,
                       bg="#81392a", font=self.fontCustomiserRadio).pack(anchor="w", padx=15)

        # Exemple: Volume sonore
        tk.Label(self.frame_parametres, text="Volume:", bg="#81392a").pack(anchor="w", padx=5, pady=5)
        volume_scale = tk.Scale(self.frame_parametres, from_=0, to=100, orient=tk.HORIZONTAL, bg="#81392a")
        volume_scale.set(50)
        volume_scale.config(state="disabled")
        volume_scale.pack(fill=tk.X, padx=15)

        # Bouton pour appliquer les changements
        self.btn_appliquer = tk.Button(self.frame_parametres, text="Appliquer", command=self.appliquer_parametres, font=self.fontCustomiserButton)


        self.btn_appliquer.pack(side="left",pady=10, padx=75)

        self.btn_retour = tk.Button(self.frame_parametres, text="Retour au menu",
                                    command=self.retour_menu, font=self.fontCustomiserButton)
        self.btn_retour.pack(side="right",pady=10, padx=75)

    def afficher(self):
        """Réaffiche la vue des paramètres si elle a été cachée"""
        self.frame_parametres.pack(side=tk.RIGHT, fill=tk.Y)

    def cacher(self):
        """Cache la vue des paramètres"""
        self.frame_parametres.pack_forget()

    def retour_menu(self):
        """Retourne au menu principal"""
        self.cacher()
        self.controleur.vue.afficher()

    def appliquer_parametres(self):
        """Applique les paramètres sélectionnés"""
        difficulte = self.var_difficulte.get()
        print("Difficulté choisie :", difficulte)
        self.controleur.application_nouveau_parametre(difficulte)
        # Ici vous pourriez récupérer les valeurs des widgets et les appliquer au modèle
