
import tkinter as tk

import math
from PIL import Image, ImageTk



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
        self.dessiner_chemin(self.modele.path2, "gray")

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
        self.init_info_panel()


    def retour_menu(self):
        self.cacher()
        self.controleur.vue.afficher()

    def cacher(self):
        self.background_frame.pack_forget()
        self.cadrePrincipal.pack_forget()
        self.cadreSecondaire.pack_forget()

    def afficher(self):
        self.background_frame.pack(fill="both", expand=True)
        self.cadrePrincipal.pack(side="left", expand=True, padx=0, pady=0)
        self.cadreSecondaire.pack(side=tk.RIGHT, fill=tk.Y)
        self.cadrePrincipal.pack_propagate(False)
        self.cadreSecondaire.pack_propagate(False)
        #self.frame_parametres.pack(side=tk.RIGHT, fill=tk.Y)

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
            self.dessiner_chemin(self.controleur.modele.path2, "gray")


        self.hide_info_panel()

    def creer_info_panel(self):
        self.info_panel = tk.Frame(self.canevas, bg="#FFD580", bd=2, relief="raised",
                                   highlightbackground="black", highlightthickness=1)

        # Titre du panneau
        self.info_title = tk.Label(self.info_panel, text="Informations", font=("Stencil", 12, "bold"), bg="#FFD580")
        self.info_title.pack(pady=5)

        # Description
        self.info_desc = tk.Label(self.info_panel, text="", wraplength=180, justify="left", bg="#FFD580")
        self.info_desc.pack(pady=5, padx=5)

        # Stats (au besoin)
        self.info_stats = tk.Label(self.info_panel, text="", justify="left", bg="#FFD580")
        self.info_stats.pack(pady=5)

        # Bouton de fermeture
        self.info_close_btn = tk.Button(self.info_panel, text="Fermer", command=self.hide_info_panel)
        self.info_close_btn.pack(pady=5)

    def show_info_panel(self, title, description, stats=""):
        self.info_title.config(text=title)
        self.info_desc.config(text=description)
        self.info_stats.config(text=stats)

        # Position du panneau centrée mais légèrement décalée vers la droite
        panel_width = 400  # Largeur
        panel_height = 400  # Hauteur

        # Calcul de la position pour centrer le panneau
        canvas_width = self.canevas.winfo_width()
        canvas_height = self.canevas.winfo_height()

        # Si le canvas n'a pas encore de taille (première utilisation), utiliser les dimensions par défaut
        if canvas_width == 1:  # Le canvas retourne 1 s'il n'est pas encore rendu
            canvas_width = self.largeur
            canvas_height = self.hauteur

        # Position le panneau à droite du centre
        x_pos = (canvas_width // 2) - 100
        y_pos = (canvas_height // 2) - 100

        # Place le panneau sur le canvas
        self.info_panel.place(x=x_pos, y=y_pos, width=panel_width, height=panel_height)

    def hide_info_panel(self):
        self.info_panel.place_forget()

    def setup_button_info(self):
        # Dictionnaire des informations
        self.tower_info = {
            "machinegun": {
                "title": "Machine Gun",
                "description": "Tour rapide à cadence de tir élevée. Efficace contre les ennemis légers.",
                "stats": "Dégâts: 10\nPortée: 150\nVitesse: Rapide\nCoût: 100"
            },
            "mortar": {
                "title": "Mortar",
                "description": "Attaque de zone qui inflige des dégâts aux ennemis groupés.",
                "stats": "Dégâts: 25\nPortée: 200\nVitesse: Lente\nCoût: 200"
            },
            "antitank": {
                "title": "Anti-Tank",
                "description": "Spécialisée contre les ennemis blindés avec une forte pénétration d'armure.",
                "stats": "Dégâts: 50\nPortée: 175\nVitesse: Moyenne\nCoût: 250"
            },
            "antiair": {
                "title": "Anti-Air",
                "description": "Cible les ennemis aériens avec précision.",
                "stats": "Dégâts: 15\nPortée: 200\nVitesse: Rapide\nCoût: 200"
            },
            "artillery": {
                "title": "Artillery",
                "description": "Longue portée avec dégâts importants mais lente.",
                "stats": "Dégâts: 40\nPortée: 300\nVitesse: Très lente\nCoût: 300"
            }
        }

        # Informations pour améliorations
        self.upgrade_info = {
            "speed": {
                "title": "Amélioration: Vitesse",
                "description": "Augmente la vitesse d'attaque de la tour sélectionnée.",
                "stats": "Coût: 50\nBonus: +20% de vitesse"
            },
            "range": {
                "title": "Amélioration: Portée",
                "description": "Augmente la portée d'attaque de la tour sélectionnée.",
                "stats": "Coût: 75\nBonus: +15% de portée"
            },
            "damage": {
                "title": "Amélioration: Dégâts",
                "description": "Augmente les dégâts infligés par la tour sélectionnée.",
                "stats": "Coût: 100\nBonus: +25% de dégâts"
            },
            "cooldown": {
                "title": "Amélioration: Cooldown",
                "description": "Réduit le temps entre chaque attaque de la tour sélectionnée.",
                "stats": "Coût: 125\nBonus: -15% de temps de recharge"
            }
        }

    def configure_button_interactions(self):
        # Tours
        self.btn_machinegun.config(command=lambda: self.show_tower_info("machinegun"))
        self.btn_mortar.config(command=lambda: self.show_tower_info("mortar"))
        self.btn_antitank.config(command=lambda: self.show_tower_info("antitank"))
        self.btn_antiair.config(command=lambda: self.show_tower_info("antiair"))
        self.btn_artillery.config(command=lambda: self.show_tower_info("artillery"))

        # Améliorations
        self.btn_speed.config(command=lambda: self.show_upgrade_info("speed"))
        self.btn_range.config(command=lambda: self.show_upgrade_info("range"))
        self.btn_damage.config(command=lambda: self.show_upgrade_info("damage"))
        self.btn_cooldown.config(command=lambda: self.show_upgrade_info("cooldown"))

        # Vendre
        self.cadreBoutonBtnVendre.config(command=self.show_sell_info)
        # Start
        self.button.config(command=self.show_start_info)

    def show_tower_info(self, tower_type):
        info = self.tower_info.get(tower_type, {})
        self.show_info_panel(info.get("title", ""), info.get("description", ""), info.get("stats", ""))

    def show_upgrade_info(self, upgrade_type):
        info = self.upgrade_info.get(upgrade_type, {})
        self.show_info_panel(info.get("title", ""), info.get("description", ""), info.get("stats", ""))

    def show_sell_info(self):
        self.show_info_panel("Vendre Tour",
                             "Cliquez sur une tour placée pour la vendre et récupérer une partie de son coût.",
                             "Remboursement: 75% du coût")
    def show_start_info(self):
        self.show_info_panel("Star Round",
                             "Cliquez pour démarrer le round. Durant celui-ci vous pourrez ajouter des tours ou les vendre",
                             "Démarrage de la partie.")

    def init_info_panel(self):
        self.creer_info_panel()
        self.setup_button_info()
        self.configure_button_interactions()

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
        self.labelTutoriel = tk.Label(self.canevas, text="Tutoriel")
        self.labelTutoriel.config(font=("Stencil" , 30, "bold"), bg="green")
        self.labelTutoriel.pack(side="top", padx=10)
        self.labelTutorielInstruction = tk.Label(self.canevas, text="Appuyer sur les boutons pour voir les informations")
        self.labelTutorielInstruction.config(font=("Stencil", 20, "bold"), bg="green")
        self.labelTutorielInstruction.pack(side="top", padx=10)




        self.placeholder = 0

        self.cadreSecondaire = tk.Frame(self.background_frame, width=largeur * 0.2, height=hauteur, bg="orange", bd=0,
                                        highlightthickness=0)
        self.cadreSecondaire.pack(side="right", fill="y", padx=0, pady=0)

        self.UIinfo = tk.Canvas(self.cadreSecondaire, width=largeur * 0.2, height=hauteur, bg="orange", relief="ridge",
                                highlightthickness=0)
        self.UIinfo.pack_propagate(False)
        self.UIinfo.pack(padx=2)
        ## ajouter le stock et les bouttons ici
        self.boutonQuitter = tk.Button(self.UIinfo, text="Quitter",command=self.retour_menu)
        self.boutonQuitter.config(font=("Stencil", 10, "bold"))
        self.boutonQuitter.pack(side="top")


        self.label_score = tk.Label(self.UIinfo, text=("Info"), fg="black", font=("Stencil", 40), bg="orange", padx=2)
        self.label_score.pack(pady=10)

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


        # Dans la méthode creer_cadre_jeu() de votre classe Vue, après la création de self.UIinfo
        self.tower_selection_frame = tk.Frame(self.UIinfo, bg="orange")
        self.tower_selection_frame.pack(pady=10)

        self.btn_machinegun = tk.Button(self.tower_selection_frame,
                                        text="Machine Gun",
                                        width=12)
        self.btn_machinegun.pack(pady=5)

        self.btn_mortar = tk.Button(self.tower_selection_frame,
                                    text="Mortar",
                                    width=12)
        self.btn_mortar.pack(pady=5)

        self.btn_antitank = tk.Button(self.tower_selection_frame,
                                      text="Anti-Tank",
                                      width=12)
        self.btn_antitank.pack(pady=5)

        self.btn_antiair = tk.Button(self.tower_selection_frame,
                                     text="Anti-Air",
                                     width=12
                                     )
        self.btn_antiair.pack(pady=5)

        self.btn_artillery = tk.Button(self.tower_selection_frame,
                                       text="Artillery",
                                       width=12
                                       )
        self.btn_artillery.pack(pady=5)

        self.cadreBoutonBtnVendre = tk.Button(self.UIinfo, text="Vendre Tour", height=5, width=12, bg="green"
                                              )
        self.cadreBoutonBtnVendre.pack(padx=20, pady=10)

        self.button = tk.Button(Rframe, text="Start Round", activeforeground="black"
                                )
        self.button.pack()

        self.upgrade_frame = tk.Frame(self.UIinfo, bg="orange")
        self.upgrade_frame.pack(pady=10)

        self.btn_speed = tk.Button(self.upgrade_frame, text="Speed", width=8)
        self.btn_speed.pack(pady=3)  # par défaut, pack les widgets verticalement

        self.btn_range = tk.Button(self.upgrade_frame, text="Range", width=8)
        self.btn_range.pack(pady=3)

        self.btn_damage = tk.Button(self.upgrade_frame, text="Damage", width=8)
        self.btn_damage.pack(pady=3)

        self.btn_cooldown = tk.Button(self.upgrade_frame, text="Cooldown", width=8)
        self.btn_cooldown.pack(pady=3)

        self.label_Round_nbr = tk.Label(Rframe, text="Round : 1", fg="black", font=("Stencil", 20), bg="orange")
        self.label_Round_nbr.pack()

    def dessiner_chemin(self, path, couleur="gray"):
        if len(path) > 1:
            for i in range(len(path) - 1):
                x1, y1 = path[i]
                x2, y2 = path[i + 1]
                self.canevas.create_line(x1, y1, x2, y2, fill=couleur, width=5, tags=("chemin",))



