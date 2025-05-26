import tkinter as tk
from PIL import Image, ImageTk, ImageSequence




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
        # Couleur de fond : gris foncé doux
        self.bg_color = "#2e2e2e"
        self.fg_color = "#f0f0f0"  # Couleur du texte

        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (self.largeur // 2)
        y = (screen_height // 2) - (self.hauteur // 2)
        self.root.geometry(f"{self.largeur}x{self.hauteur}+{x}+{y}")

        self.background_frame = tk.Frame(self.root, width=screen_width, height=screen_height)
        self.background_frame.pack()
        self.background_frame.pack_propagate(False)

        bg_img = Image.open("assets/couleur-fond.png")
        bg_img = bg_img.resize((screen_width, screen_height))
        self.bg = ImageTk.PhotoImage(bg_img)

        self.bg_canvas = tk.Canvas(self.background_frame, width=screen_width, height=screen_height,
                                   highlightthickness=0)
        self.bg_canvas.place(x=0, y=0)
        self.bg_canvas.create_image(0, 0, image=self.bg, anchor="nw", tags="background")
        self.bg_canvas.tag_lower("background")

        # Charger le GIF
        self.im = Image.open("assets/soldier.gif")
        self.frames = []

        # Définir la couleur de fond à rendre transparente (noir)
        fond_a_supprimer = (0, 0, 0)
        seuil = 10  # tolérance pour ne pas supprimer les traits noirs du personnage

        for frame in ImageSequence.Iterator(self.im):
            frame_rgba = frame.convert("RGBA")
            datas = frame_rgba.getdata()

            new_data = []
            for item in datas:
                # Si la couleur est proche du noir, on la rend transparente
                if all(abs(item[i] - fond_a_supprimer[i]) < seuil for i in range(3)):
                    new_data.append((0, 0, 0, 0))  # transparent
                else:
                    new_data.append(item)

            frame_rgba.putdata(new_data)
            frame_rgba = frame_rgba.resize((200, 200))
            self.frames.append(ImageTk.PhotoImage(frame_rgba))

        self.creer_cadre_credit(self.largeur, self.hauteur)

    def update(self,index):
        frame = self.frames[index]
        self.label_gauche.configure(image=frame)
        self.label_droite.configure(image=frame)
        self.root.after(100, self.update, (index + 1) % len(self.frames))



    def retour_menu(self):
        self.cacher()
        self.controleur.vue.afficher()

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

        # Créer la frame centrale (centrée)
        self.credit_frame = tk.Frame(
            self.background_frame,
            width=largeur,
            height=hauteur,
            highlightbackground="darkred",
            highlightcolor="darkred",
            highlightthickness=2,
            bg=self.bg_color
        )
        self.credit_frame.place(relx=0.5, rely=0.5, anchor="center")
        self.credit_frame.pack_propagate(False)


        # Calculer le centre Y en pixels (au milieu de l'écran)
        center_y = self.hauteur // 2  # Puisque credit_frame est de 800 px de haut

        # GIF gauche (à gauche de credit_frame, centré verticalement)
        self.label_gauche = tk.Label(self.credit_frame, image=self.frames[0], bg=self.bg_color)


        # GIF droite (à droite de credit_frame, centré verticalement)
        self.label_droite = tk.Label(self.credit_frame, image=self.frames[0], bg=self.bg_color)




        self.titre = tk.Label(
            self.credit_frame,
            text="TOWER DEFENSE",
            font=("Stencil", 30, "bold"),
            anchor="center",
            bg=self.bg_color,
            fg=self.fg_color)

        self.par = tk.Label(
            self.credit_frame,
            text="PAR",
            font=("Stencil", 30, "bold"),
            anchor="center",
            bg=self.bg_color,
            fg=self.fg_color)

        self.equipe = tk.Label(
            self.credit_frame,
            text="Momofat",
            font=("Stencil", 30, "bold"),
            anchor="center",
            bg=self.bg_color,
            fg=self.fg_color)

        self.fait = tk.Label(
            self.credit_frame,
            text="Fait au cégep du vieux Montréal",
            font=("Stencil", 30, "bold"),
            anchor="center",
            bg=self.bg_color,
            fg=self.fg_color)

        self.quitter = tk.Button(self.credit_frame, command=self.retour_menu, text="Menu", fg="black", bg="grey")

        self.antoine = tk.Button(self.credit_frame, command=lambda: self.afficher_fenetre_membre("Antoine"), text="Antoine", fg=self.fg_color, bg=self.bg_color, font=("Stencil", 30, "bold"))
        self.alexiane = tk.Button(self.credit_frame, command=lambda: self.afficher_fenetre_membre("Alexiane"),text="Alexiane", fg=self.fg_color, bg=self.bg_color,font=("Stencil", 30, "bold"))
        self.label_gauche.place(x=0, y=center_y, anchor="w")
        self.samuel = tk.Button(self.credit_frame, command=lambda: self.afficher_fenetre_membre("Samuel"),text="Samuel" ,fg=self.fg_color, bg=self.bg_color,font=("Stencil", 30, "bold"))
        self.jacques = tk.Button(self.credit_frame, command=lambda: self.afficher_fenetre_membre("Jacques"),text="Jacques", fg=self.fg_color, bg=self.bg_color,font=("Stencil", 30, "bold"))
        self.label_droite.place(x=self.largeur, y=center_y, anchor="e")

        self.titre.place(relx=0.5, rely=0.1, anchor="center")
        self.par.place(relx=0.5, rely=0.15, anchor="center")
        self.equipe.place(relx=0.5, rely=0.2, anchor="center")

        self.antoine.place(relx=0.1, rely=0.3, anchor="center")
        self.alexiane.place(relx=0.1, rely=0.7, anchor="center")
        self.samuel.place(relx=0.9, rely=0.3, anchor="center")
        self.jacques.place(relx=0.9, rely=0.7, anchor="center")

        self.fait.place(relx=0.5, rely=0.9, anchor="center")
        self.quitter.place(relx=0.5, rely=0.95, anchor="center")
        # Démarrer l'animation
        self.update(0)



    def afficher_fenetre_membre(self, nom):
        # Si une frame existe déjà, on la détruit
        if hasattr(self, "popup_frame") and self.popup_frame:
            self.popup_frame.destroy()

        self.popup_frame = tk.Frame(self.credit_frame, bg="#444", width=600, height=400, highlightbackground="white",
                                    highlightthickness=2)
        self.popup_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Choisir l'image et les infos selon le membre
        infos = {
            "Antoine": {
                "image": "assets/tour3.png",
                "Nom": "Antoine Dextraze",
                "Rôle": "Étudiant",
                "Cours": "420.B0",
                "Années": "2e année",
                "Spécialité":"Design du UI"
            },
            "Alexiane": {
                "image": "assets/tour4.png",
                "Nom": "Alexiane Chartrand",
                "Rôle": "",
                "Cours": "Canon laser",
                "Années": "Design des sprites et UI",
                "Spécialité": ""
            },
            "Jacques": {
                "image": "assets/tour2.png",
                "Nom": "Jacques Michel Caron",
                "Rôle": "",
                "Cours": "Tourelle Tesla",
                "Années": "Optimisation et correction de bugs",
                "Spécialité": ""
            },
            "Samuel": {
                "image": "assets/tour1.png",
                "Nom": "Samuel Bergeron-Lagacé",
                "Rôle": "",
                "Cours": "Sniper automatique",
                "Années": "Création des vagues ennemies",
                "Spécialité": ""
            }
        }
        data = infos.get(nom, {})
        image_path = data.get("image", "assets/couleur-fond.png")

        # Afficher l'image
        image = Image.open(image_path).resize((100, 100))
        self.membre_photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(self.popup_frame, image=self.membre_photo, bg="#444")
        image_label.pack(pady=10)

        # Titre
        label_nom = tk.Label(self.popup_frame, text=nom, font=("Arial", 18, "bold"), fg="white", bg="#444")
        label_nom.pack(pady=5)

        # Affichage des catégories
        for categorie, valeur in data.items():
            if categorie == "image":
                continue  # On n'affiche pas le chemin de l'image
            ligne = tk.Frame(self.popup_frame, bg="#444")
            ligne.pack(pady=2,anchor="w")
            cat_label = tk.Label(ligne, text=f"{categorie} :", font=("Arial", 12, "bold"), fg="#ddd", bg="#444",
                                 width=12, anchor="e")
            cat_label.pack(side="left")
            val_label = tk.Label(ligne, text=valeur, font=("Arial", 12), fg="white", bg="#444", anchor="w")
            val_label.pack(side="left")

        # Bouton de fermeture
        bouton_fermer = tk.Button(self.popup_frame, text="Fermer", command=self.popup_frame.destroy)
        bouton_fermer.pack(pady=15)





