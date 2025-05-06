
import tkinter as tk

import math
from PIL import Image, ImageTk


class TutorialArrow:
    def __init__(self, canvas, from_x, from_y, to_x, to_y, text, color="#FF6600", arrow_width=2):
        self.canvas = canvas
        self.from_x = from_x
        self.from_y = from_y
        self.to_x = to_x
        self.to_y = to_y
        self.text = text
        self.color = color
        self.arrow_width = arrow_width
        self.arrow_id = None
        self.text_box_id = None
        self.text_id = None

    def draw(self):
        # Dessiner la flèche
        self.arrow_id = self.canvas.create_line(
            self.from_x, self.from_y, self.to_x, self.to_y,
            arrow=tk.LAST, width=self.arrow_width, fill=self.color
        )

        # Calculer la position de la boîte de texte (au milieu de la flèche)
        text_x = (self.from_x + self.to_x) / 2
        text_y = (self.from_y + self.to_y) / 2

        # Décaler légèrement pour éviter que la boîte ne couvre la flèche
        angle = math.atan2(self.to_y - self.from_y, self.to_x - self.from_x)
        offset = 20
        text_x += math.sin(angle) * offset
        text_y -= math.cos(angle) * offset

        # Créer un rectangle pour la boîte de texte
        text_width = len(self.text) * 6 + 10  # Estimation approximative de la largeur
        text_height = 25

        self.text_box_id = self.canvas.create_rectangle(
            text_x - text_width / 2, text_y - text_height / 2,
            text_x + text_width / 2, text_y + text_height / 2,
            fill="white", outline=self.color, width=2
        )

        # Ajouter le texte
        self.text_id = self.canvas.create_text(
            text_x, text_y, text=self.text,
            font=("Stencil", 10), fill="black"
        )

        # Assurer que la boîte de texte et le texte sont au-dessus de la flèche
        self.canvas.tag_raise(self.text_box_id, self.arrow_id)
        self.canvas.tag_raise(self.text_id, self.text_box_id)

    def hide(self):
        if self.arrow_id:
            self.canvas.delete(self.arrow_id)
            self.arrow_id = None
        if self.text_box_id:
            self.canvas.delete(self.text_box_id)
            self.text_box_id = None
        if self.text_id:
            self.canvas.delete(self.text_id)
            self.text_id = None

    def show(self):
        if not self.arrow_id:
            self.draw()


# Modification de la classe Tutoriel pour intégrer les flèches et boîtes de texte
def add_to_Tutoriel_class():
    """
    Cette fonction contient le code à ajouter à la classe Tutoriel
    """

    def initialiser_tutoriel(self):
        """
        Initialise les flèches et boîtes de texte pour le tutoriel
        À ajouter comme méthode à la classe Tutoriel
        """
        self.tutorial_arrows = []
        self.tutorial_active = False

        # Créer des flèches pour chaque bouton important
        # Pour Machine Gun
        btn_coords = self.get_widget_coords(self.btn_machinegun)
        arrow = TutorialArrow(
            self.canevas,
            self.largeur - 40, self.hauteur // 4,  # Point de départ de la flèche
            btn_coords[0], btn_coords[1],  # Point d'arrivée (bouton)
            "Machine Gun: Attaque rapide"
        )
        self.tutorial_arrows.append(arrow)

        # Pour Mortar
        btn_coords = self.get_widget_coords(self.btn_mortar)
        arrow = TutorialArrow(
            self.canevas,
            self.largeur - 40, self.hauteur // 4 + 50,
            btn_coords[0], btn_coords[1],
            "Mortar: Dégâts de zone"
        )
        self.tutorial_arrows.append(arrow)

        # Pour Anti-Tank
        btn_coords = self.get_widget_coords(self.btn_antitank)
        arrow = TutorialArrow(
            self.canevas,
            self.largeur - 40, self.hauteur // 4 + 100,
            btn_coords[0], btn_coords[1],
            "Anti-Tank: Contre blindés"
        )
        self.tutorial_arrows.append(arrow)

        # Pour Anti-Air
        btn_coords = self.get_widget_coords(self.btn_antiair)
        arrow = TutorialArrow(
            self.canevas,
            self.largeur - 40, self.hauteur // 4 + 150,
            btn_coords[0], btn_coords[1],
            "Anti-Air: Contre aériens"
        )
        self.tutorial_arrows.append(arrow)

        # Pour Artillery
        btn_coords = self.get_widget_coords(self.btn_artillery)
        arrow = TutorialArrow(
            self.canevas,
            self.largeur - 40, self.hauteur // 4 + 200,
            btn_coords[0], btn_coords[1],
            "Artillery: Longue portée"
        )
        self.tutorial_arrows.append(arrow)

        # Pour le bouton Vendre Tour
        btn_coords = self.get_widget_coords(self.cadreBoutonBtnVendre)
        arrow = TutorialArrow(
            self.canevas,
            self.largeur - 40, self.hauteur // 2 + 50,
            btn_coords[0], btn_coords[1],
            "Vendre une tour"
        )
        self.tutorial_arrows.append(arrow)

        # Pour le bouton Start Round
        btn_coords = self.get_widget_coords(self.button)
        arrow = TutorialArrow(
            self.canevas,
            self.largeur - 40, self.hauteur - 100,
            btn_coords[0], btn_coords[1],
            "Démarrer la vague"
        )
        self.tutorial_arrows.append(arrow)

        # Pour les boutons d'amélioration
        upgrades = [
            (self.btn_speed, "Vitesse de tir"),
            (self.btn_range, "Portée de tir"),
            (self.btn_damage, "Dégâts"),
            (self.btn_cooldown, "Temps de recharge")
        ]

        for i, (btn, text) in enumerate(upgrades):
            btn_coords = self.get_widget_coords(btn)
            arrow = TutorialArrow(
                self.canevas,
                self.largeur - 40, self.hauteur // 2 + 120 + i * 30,
                btn_coords[0], btn_coords[1],
                f"Améliorer: {text}"
            )
            self.tutorial_arrows.append(arrow)

    def get_widget_coords(self, widget):
        """
        Obtient les coordonnées globales d'un widget
        À ajouter comme méthode à la classe Tutoriel
        """
        widget.update_idletasks()  # Assure que la géométrie est à jour
        x = widget.winfo_rootx() - self.root.winfo_rootx()
        y = widget.winfo_rooty() - self.root.winfo_rooty()
        width = widget.winfo_width()
        height = widget.winfo_height()

        # Retourne le centre du widget
        return (x + width // 2, y + height // 2)

    def show_tutorial(self):
        """
        Affiche toutes les flèches du tutoriel
        À ajouter comme méthode à la classe Tutoriel
        """
        self.tutorial_active = True
        for arrow in self.tutorial_arrows:
            arrow.draw()

        # Ajouter un bouton pour fermer le tutoriel
        self.close_tutorial_btn = tk.Button(
            self.canevas,
            text="Fermer le tutoriel",
            command=self.hide_tutorial,
            bg="#FF6600",
            fg="white",
            font=("Stencil", 12, "bold")
        )
        self.close_tutorial_btn.place(x=20, y=20)

    def hide_tutorial(self):
        """
        Cache toutes les flèches du tutoriel
        À ajouter comme méthode à la classe Tutoriel
        """
        self.tutorial_active = False
        for arrow in self.tutorial_arrows:
            arrow.hide()

        if hasattr(self, 'close_tutorial_btn'):
            self.close_tutorial_btn.destroy()

    def toggle_tutorial(self):
        """
        Bascule l'affichage du tutoriel
        À ajouter comme méthode à la classe Tutoriel
        """
        if self.tutorial_active:
            self.hide_tutorial()
        else:
            self.show_tutorial()


# Modification de afficherTutoriel pour intégrer notre tutoriel
def modified_afficherTutoriel(self):
    # Configurer la fenêtre
    self.root.title("Tower Defense - Jeu")
    self.root.geometry(f"{self.largeur + 200}x{self.hauteur}")  # +200 pour la barre latérale

    # S'assurer que les frames sont visibles
    self.cadrePrincipal.pack_propagate(False)
    self.cadreSecondaire.pack(side=tk.RIGHT, fill=tk.Y)

    # Redessiner les chemins au cas où
    if hasattr(self.controleur.modele, 'path'):
        self.dessiner_chemin(self.controleur.modele.path, "gray")
    if hasattr(self.controleur.modele, 'path2'):
        self.dessiner_chemin(self.controleur.modele.path2, "blue")

    # Initialiser et afficher le tutoriel si pas déjà fait
    if not hasattr(self, 'tutorial_arrows'):
        self.initialiser_tutoriel()

    # Ajouter un bouton pour afficher/masquer le tutoriel dans l'interface principale
    self.tutorial_toggle_btn = tk.Button(
        self.UIinfo,
        text="Afficher tutoriel",
        bg="#FF6600",
        fg="white",
        font=("Stencil", 12, "bold"),
        command=self.toggle_tutorial
    )
    self.tutorial_toggle_btn.pack(pady=10, before=self.label_score)


# Modification de la méthode __init__ pour intégrer le tutoriel
def modified_init(self, controleur, root, largeur, hauteur):
    # Le code existant reste inchangé
    # ...

    # À la fin de la méthode __init__, ajouter:
    self.tutorial_arrows = []
    self.tutorial_active = False



class Tutoriel():

    def __init__(self, controleur, root, largeur, hauteur):
        self.controleur = controleur
        self.root = root
        self.root.title("Tower Defense")
        self.largeur = largeur
        self.hauteur = hauteur

        self.root.minsize(largeur + 168, hauteur)
        self.switch = True;

        ico = Image.open("assets/Machine_Gun.png")
        photo = ImageTk.PhotoImage(ico)
        self.root.wm_iconphoto(False, photo)

        self.mode_actif = "placement"
        self.info = []

        # Utiliser controleur.modele au lieu de self.modele
        # Ou ajouter cette ligne si vous préférez accéder directement au modèle
        self.modele = self.controleur.modele

        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (largeur // 2)
        y = (screen_height // 2) - (hauteur // 2)
        self.root.geometry(f"{largeur}x{hauteur}+{x}+{y}")

        self.background_frame = tk.Frame(self.root, width=largeur + 168, height=hauteur)
        self.background_frame.pack(fill="both", expand=True)

        bg_img = Image.open("assets/couleur-fond.png")
        bg_img = bg_img.resize((screen_width, screen_height))  # Ajuster à la taille de la fenêtre
        self.bg = ImageTk.PhotoImage(bg_img)

        self.bg_canvas = tk.Canvas(self.background_frame, width=largeur + 168, height=hauteur, highlightthickness=0)
        self.bg_canvas.place(x=0, y=0, relwidth=1, relheight=1)
        self.bg_canvas.create_image(0, 0, image=self.bg, anchor="nw", tags="background")

        self.creer_cadre_jeu(largeur, hauteur, self.info)

        self.dessiner_chemin(self.modele.path, "gray")
        self.dessiner_chemin(self.modele.path2, "blue")

        self.tour_image1 = Image.open("assets/tour1.png")
        self.tour_image1 = self.tour_image1.resize((40, 40))
        self.tour_photo1 = ImageTk.PhotoImage(self.tour_image1)

        self.tour_image2 = Image.open("assets/tour2.png")
        self.tour_image2 = self.tour_image2.resize((40, 40))
        self.tour_photo2 = ImageTk.PhotoImage(self.tour_image2)

        self.tour_image3 = Image.open("assets/tour3.png")
        self.tour_image3 = self.tour_image3.resize((40, 40))
        self.tour_photo3 = ImageTk.PhotoImage(self.tour_image3)

        self.tour_image4 = Image.open("assets/tour4.png")
        self.tour_image4 = self.tour_image4.resize((40, 40))
        self.tour_photo4 = ImageTk.PhotoImage(self.tour_image4)

        self.placement_mode = False

        self.tutorial_arrows = []
        self.tutorial_active = False

    def afficherTutoriel(self):
        # Configurer la fenêtre
        self.root.title("Tower Defense - Jeu")
        self.root.geometry(f"{self.largeur + 200}x{self.hauteur}")  # +200 pour la barre latérale

        # S'assurer que les frames sont visibles
        self.cadrePrincipal.pack_propagate(False)
        self.cadreSecondaire.pack(side=tk.RIGHT, fill=tk.Y)

        # Redessiner les chemins au cas où
        if hasattr(self.controleur.modele, 'path'):
            self.dessiner_chemin(self.controleur.modele.path, "gray")
        if hasattr(self.controleur.modele, 'path2'):
            self.dessiner_chemin(self.controleur.modele.path2, "blue")

    def creer_cadre_jeu(self, largeur, hauteur, info):

        self.cadrePrincipal = tk.Frame(self.background_frame, width=largeur, height=hauteur, bd=0, highlightthickness=0)
        self.cadrePrincipal.pack(side="left", expand=True, padx=0, pady=0)

        self.map = Image.open("assets/map.png")
        self.map = self.map.resize((largeur, hauteur))
        self.map_photo = ImageTk.PhotoImage(self.map)

        self.canevas = tk.Canvas(self.cadrePrincipal, width=largeur, height=hauteur, highlightthickness=0, bd=0)
        #self.canevas.bind("<Button-1>", self.afficher_coordonnees)
        self.canevas.pack(expand=True, fill="both", padx=0, pady=0)
        self.canevas.create_image(0, 0, anchor=tk.NW, image=self.map_photo)

        self.placeholder = 0

        self.cadreSecondaire = tk.Frame(self.background_frame, width=largeur * 0.2, height=hauteur, bg="orange", bd=0,
                                        highlightthickness=0)
        self.cadreSecondaire.pack(side="right", fill="y", padx=0, pady=0)

        self.UIinfo = tk.Canvas(self.cadreSecondaire, width=largeur * 0.2, height=hauteur, bg="orange", relief="ridge",
                                highlightthickness=0)
        self.UIinfo.pack_propagate(False)
        self.UIinfo.pack(padx=2)
        ## ajouter le stock et les bouttons ici

        self.label_score = tk.Label(self.UIinfo, text=("Info"), fg="black", font=("Stencil", 40), bg="orange", padx=2)
        self.label_score.pack(pady=50)

        self.vie = tk.Label(self.UIinfo, text=(f"Vie 100"), fg="black", font=("Stencil", 13, "bold"), bg="orange")
        self.vie.pack()

        self.score = tk.Label(self.UIinfo, text=(f"score 0"), fg="black", font=("Stencil", 13, "bold"), bg="orange")
        self.score.pack()

        self.Argent = tk.Label(self.UIinfo, text=(f"Argent 0"), fg="black", font=("Stencil", 13, "bold"), bg="orange")
        self.Argent.pack()

        self.nbennemis = tk.Label(self.UIinfo, text=(f"Ennemis restant 5"), fg="black", font=("Stencil", 13, "bold"),
                                  bg="orange")
        self.nbennemis.pack()

        ### Initialisation de la frame Popup
        self.popup = tk.Frame(self.canevas, bg="gray", bd=2, relief="raised")
        tk.Label(self.popup, text="Game-OVER", font=("Stencil", 14), bg="gray").pack(pady=10)
        tk.Button(self.popup, text="Réessayer", command=lambda: self.controleur.init_game_values()).pack(pady=10)

        Rframe = tk.Frame(self.UIinfo, width=largeur * 0.2, height=hauteur * 0.2, bg="orange")
        Rframe.pack(side="bottom", fill="x", padx=5, pady=5)

        # self.cadreBoutonBtnTour = tk.Button(self.UIinfo, text="Poser Tour", height=5, width=12, bg="red", command=self.selection_tour)
        # self.cadreBoutonBtnTour.pack(padx=20, pady=10)

        # Dans la méthode creer_cadre_jeu() de votre classe Vue, après la création de self.UIinfo
        self.tower_selection_frame = tk.Frame(self.UIinfo, bg="orange")
        self.tower_selection_frame.pack(pady=10)

        self.btn_machinegun = tk.Button(self.tower_selection_frame,
                                        text="Machine Gun",
                                        width=12
                                        ,
                                        command=lambda: self.afficherTutoriel()
                                        )
        self.btn_machinegun.pack(pady=5)

        self.btn_mortar = tk.Button(self.tower_selection_frame,
                                    text="Mortar",
                                    width=12
                                    #,
                                    #command=lambda: self.selection_tower("mortar")
                                    )
        self.btn_mortar.pack(pady=5)

        self.btn_antitank = tk.Button(self.tower_selection_frame,
                                      text="Anti-Tank",
                                      width=12
                                      #,
                                      #command=lambda: self.selection_tower("antitank")
                                      )
        self.btn_antitank.pack(pady=5)

        self.btn_antiair = tk.Button(self.tower_selection_frame,
                                     text="Anti-Air",
                                     width=12
                                     #,
                                     #command=lambda: self.selection_tower("antiair")
                                     )
        self.btn_antiair.pack(pady=5)

        self.btn_artillery = tk.Button(self.tower_selection_frame,
                                       text="Artillery",
                                       width=12
                                       #,
                                       #command=lambda: self.selection_tower("artillery")
                                       )
        self.btn_artillery.pack(pady=5)

        self.cadreBoutonBtnVendre = tk.Button(self.UIinfo, text="Vendre Tour", height=5, width=12, bg="green"
                                              #,
                                              #command=self.selection_sell
                                              )
        self.cadreBoutonBtnVendre.pack(padx=20, pady=10)

        self.button = tk.Button(Rframe, text="Start Round", activeforeground="black"
                                #,
                                #=self.controleur.start_Round
                                )
        self.button.pack()

        self.upgrade_frame = tk.Frame(self.UIinfo, bg="orange")
        self.upgrade_frame.pack(pady=10)

        self.btn_speed = tk.Button(self.upgrade_frame, text="Speed", width=8
                                   #, command=self.selection_upgrade_speed
                                   )
        self.btn_speed.pack(pady=3)  # par défaut, pack les widgets verticalement

        self.btn_range = tk.Button(self.upgrade_frame, text="Range", width=8
                                   #, command=self.selection_upgrade_range
                                   )
        self.btn_range.pack(pady=3)

        self.btn_damage = tk.Button(self.upgrade_frame, text="Damage", width=8
                                    #, command=self.selection_upgrade_damage
                                    )
        self.btn_damage.pack(pady=3)

        self.btn_cooldown = tk.Button(self.upgrade_frame, text="Cooldown", width=8
                                      #,
                                      #command=self.selection_upgrade_cooldown
                                      )
        self.btn_cooldown.pack(pady=3)

        self.label_Round_nbr = tk.Label(Rframe, text="Round : 1", fg="black", font=("Stencil", 20), bg="orange")
        self.label_Round_nbr.pack()

    def dessiner_chemin(self, path, couleur="gray"):
        if len(path) > 1:
            for i in range(len(path) - 1):
                x1, y1 = path[i]
                x2, y2 = path[i + 1]
                self.canevas.create_line(x1, y1, x2, y2, fill=couleur, width=5, tags=("chemin",))



