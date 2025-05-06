import tkinter as tk
from tkinter import ttk

from PIL import ImageTk,Image


class Parametre():
    def __init__(self, controleur, root, largeur, hauteur):
        self.controleur = controleur
        self.root = root
        self.root.title("Tower Defense")
        self.root.geometry(f"{largeur}x{hauteur}")
        self.root.minsize(largeur + 200, hauteur)
        # self.controleur = controleur
        # self.modele = modele
        self.largeur = largeur
        self.hauteur = hauteur

        # Configuration initiale
        #self.create_mainFrame()
        #self.create_parameter_frame()
        # Création du canvas principal
        self.canvas = tk.Canvas(self.root, width=largeur, height=hauteur, bg="black")

        # Création du frame pour les widgets des paramètres
        self.frame_parametres = tk.Frame(self.root, width=200, bg="lightgray")

        # Bouton pour retourner au menu
        self.btn_retour = tk.Button(self.frame_parametres, text="Retour au menu",
                                    command=self.retour_menu)

        # Ces éléments ne sont pas encore placés dans la fenêtre

    def afficherParametre(self):
        """Initialise et affiche tous les éléments de la vue paramètres"""
        # Placement du canvas principal
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Placement du frame latéral avec les paramètres
        self.frame_parametres.pack(side=tk.RIGHT, fill=tk.Y)
        self.frame_parametres.pack_propagate(False)  # Empêche le redimensionnement du frame

        # Ajout des widgets de paramètres
        self.btn_retour.pack(pady=10)

        # Ajout d'autres widgets pour les paramètres du jeu
        tk.Label(self.frame_parametres, text="Paramètres du jeu", bg="lightgray", font=("Arial", 12, "bold")).pack(
            pady=10)

        # Exemple: Difficulté
        tk.Label(self.frame_parametres, text="Difficulté:", bg="lightgray").pack(anchor="w", padx=5, pady=5)
        difficulte = tk.StringVar(value="normale")
        tk.Radiobutton(self.frame_parametres, text="Facile", variable=difficulte, value="facile", bg="lightgray").pack(
            anchor="w", padx=15)
        tk.Radiobutton(self.frame_parametres, text="Normale", variable=difficulte, value="normale",
                       bg="lightgray").pack(anchor="w", padx=15)
        tk.Radiobutton(self.frame_parametres, text="Difficile", variable=difficulte, value="difficile",
                       bg="lightgray").pack(anchor="w", padx=15)

        # Exemple: Volume sonore
        tk.Label(self.frame_parametres, text="Volume:", bg="lightgray").pack(anchor="w", padx=5, pady=5)
        volume_scale = tk.Scale(self.frame_parametres, from_=0, to=100, orient=tk.HORIZONTAL, bg="lightgray")
        volume_scale.set(50)
        volume_scale.pack(fill=tk.X, padx=15)

        # Bouton pour appliquer les changements
        tk.Button(self.frame_parametres, text="Appliquer", command=self.appliquer_parametres).pack(pady=10)

    def afficher(self):
        """Réaffiche la vue des paramètres si elle a été cachée"""
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.frame_parametres.pack(side=tk.RIGHT, fill=tk.Y)

    def cacher(self):
        """Cache la vue des paramètres"""
        self.canvas.pack_forget()
        self.frame_parametres.pack_forget()

    def retour_menu(self):
        """Retourne au menu principal"""
        self.cacher()
        self.controleur.vue.afficher()

    def appliquer_parametres(self):
        """Applique les paramètres sélectionnés"""
        # Ici vous pourriez récupérer les valeurs des widgets et les appliquer au modèle
        print("Paramètres appliqués")