import tkinter as tk

import math
from PIL import Image, ImageTk

ENNEMIS_COLOR = "Yellow"
TOURS_COLOR = "Blue"
PROJECTILES_COLOR = "Red"


class Vue():
    def __init__(self, controleur, largeur, hauteur, root):
        self.controleur = controleur
        self.root = root
        self.root.title("Tower Defense")
        self.largeur = largeur
        self.hauteur = hauteur

        self.root.minsize(largeur + 168, hauteur)
        self.switch = True

        ico = Image.open("assets/Machine_Gun.png")
        photo = ImageTk.PhotoImage(ico)
        self.root.wm_iconphoto(False, photo)

        self.mode_actif = "placement"
        self.info = []
        
        self.show_tour = (0,0,0)
        
        self.show_distance = True

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
        self.dessiner_chemin(self.modele.path2, "gray")
        
        self.tour_image1 = Image.open("assets/tour1.png")
        self.tour_image1 = self.tour_image1.resize((40,40))
        self.tour_photo1 = ImageTk.PhotoImage(self.tour_image1)
        
        self.tour_image2 = Image.open("assets/tour2.png")
        self.tour_image2 = self.tour_image2.resize((40,40))
        self.tour_photo2 = ImageTk.PhotoImage(self.tour_image2)
        
        self.tour_image3 = Image.open("assets/tour3.png")
        self.tour_image3 = self.tour_image3.resize((40,40))
        self.tour_photo3 = ImageTk.PhotoImage(self.tour_image3)
        
        self.tour_image4 = Image.open("assets/tour4.png")
        self.tour_image4 = self.tour_image4.resize((40,40))
        self.tour_photo4 = ImageTk.PhotoImage(self.tour_image4)

        self.placement_mode = False

    def afficher(self):
        # Configurer la fenêtre
        self.root.title("Tower Defense - Jeu")
        self.root.geometry(f"{self.largeur + 200}x{self.hauteur}")  # +200 pour la barre latérale
        
        # S'assurer que les frames sont visibles
        self.cadrePrincipal.grid(column=0, row=0)
        self.cadreSecondaire.grid(column=1, row=0, rowspan=2)
        
        # Redessiner les chemins au cas où
        if hasattr(self.controleur.modele, 'path'):
            self.dessiner_chemin(self.controleur.modele.path, "gray")
        if hasattr(self.controleur.modele, 'path2'):
            self.dessiner_chemin(self.controleur.modele.path2, "gray")


    #def afficherParametre(self):
    #    self.root.title("Tower Defense - Paramètre")
    #    self.root.geometry(f"{self.largeur + 200}x{self.hauteur}")

    #    self.cadrePrincipal.grid(column=0, row=0)
    #    self.cadreSecondaire.grid(column=1, row=0, rowspan=2)








    def cacher(self):
        # Cacher les frames principales
        self.cadrePrincipal.grid_remove()
        self.cadreSecondaire.grid_remove()

        
    def reset(self):
        self.canevas.delete("popup")
        self.canevas.delete("chemin")
        self.dessiner_chemin(self.modele.path, "gray")
        self.dessiner_chemin(self.modele.path2, "gray")
        self.button.config(state="normal")
        print("Message de Reset")

    def update_vue(self, vie, score, argent, round, nbennemis, message):
        self.info = [vie, score, argent, round, nbennemis, message]
        self.label_score.pack_forget
        self.score.pack_forget
        self.vie.pack_forget
        self.nbennemis.pack_forget
        self.label_Round_nbr.pack_forget
        self.score.config(text=(f"Vie {self.info[0]}"))
        self.message.pack_forget

        self.vie.config(text=(f"score {self.info[1]}"))

        self.Argent.config(text=(f"Argent {self.info[2]}"))
        
        self.label_Round_nbr.config(text=(f"Round: {self.info[3]}"))

        self.nbennemis.config(text=(f"Ennemis restant: {self.info[4]}"))
        
        self.message.config(text=(f"Message:\n\n{self.info[5]}"))

        self.label_score.pack(pady=10)

        self.vie.pack(anchor="w")

        self.score.pack(anchor="w")

        self.Argent.pack(anchor="w")
        
        self.nbennemis.pack(anchor="w")
        
        self.message.pack(anchor="w")
        
        self.label_Round_nbr.pack()
        if self.info[4] > 0:
            self.button.config(state="disabled")
            self.controleur.demarrerRound = True
        elif self.info[4] == 0 and self.controleur.demarrerRound == False:
            self.button.config(state="normal")

        ## boucle pour garde à jour le rayon des tours
        self.afficher_distance_tour(self.show_tour)

    def creer_cadre_jeu(self, largeur, hauteur, info):

        self.cadrePrincipal = tk.Frame(self.background_frame, width=largeur, height=hauteur, bd=0, highlightthickness=0)
        self.cadrePrincipal.pack(side="left", expand=True, padx=0, pady=0)

        self.map = Image.open("assets/map.png")
        self.map = self.map.resize((largeur, hauteur))
        self.map_photo = ImageTk.PhotoImage(self.map)

        self.canevas = tk.Canvas(self.cadrePrincipal, width=largeur, height=hauteur, highlightthickness=0, bd=0)
        self.canevas.bind("<Button-1>", self.afficher_coordonnees)
        self.canevas.pack(expand=True,fill="both", padx=0, pady=0)
        self.canevas.create_image(0, 0, anchor=tk.NW, image=self.map_photo)

        self.placeholder = 0

        self.cadreSecondaire = tk.Frame(self.background_frame, width=largeur * 0.2, height=hauteur, bg="orange", bd=0, highlightthickness=0)
        self.cadreSecondaire.pack(side="right", fill="y", padx=0, pady=0)

        self.UIinfo = tk.Canvas(self.cadreSecondaire, width=largeur * 0.2, height=hauteur, bg="orange", relief="ridge",highlightthickness=0)
        self.UIinfo.pack_propagate(False)
        self.UIinfo.pack(padx=2)
        ## ajouter le stock et les bouttons ici
        
        self.frame_parametres = tk.Frame(self.UIinfo, width=200, height=200, bg="orange")
        self.frame_parametres.pack(expand=True,side=tk.TOP,anchor="center")
        
        self.label_score = tk.Label(self.frame_parametres, text=(f"Info"), fg="black", font=("Stencil", 10), bg="orange", padx=2)
        self.label_score.pack(anchor="center")

        self.vie = tk.Label(self.UIinfo, text=(f"Vie 0"), fg="black", font=("Stencil", 10, "bold" ), bg="orange")
        self.vie.pack()

        self.score = tk.Label(self.UIinfo, text=(f"score 0"), fg="black", font=("Stencil", 10, "bold"), bg="orange")
        self.score.pack()

        self.Argent = tk.Label(self.UIinfo, text=(f"Argent 0"), fg="black", font=("Stencil", 10, "bold"), bg="orange")
        self.Argent.pack()
        
        self.nbennemis = tk.Label(self.UIinfo, text=(f"Ennemis restant 0"), fg="black", font=("Stencil", 10, "bold"),bg="orange")
        self.nbennemis.pack()
        
        self.message = self.label_score
        self.message.pack()
        
        # Boutton pour afficher ou ne pas afficher les cercles des distances des tours
        self.btndistance = tk.Button(self.UIinfo,text=(f"Rayon ON"),fg="green",font=("Italic0", 10, "bold") ,command=self.selection_show_distance)
        self.btndistance.pack()
        
        ### Initialisation de la frame Popup
        self.popup = tk.Frame(self.canevas, bg="gray", bd=2, relief="raised")
        tk.Label(self.popup, text="Game-OVER", font=("Stencil", 14), bg="gray").pack(pady=5)
        tk.Button(self.popup, text="Réessayer", font=("Stencil", 14), command=lambda: self.controleur.init_game_values()).pack(pady=5)

        

        Rframe = tk.Frame(self.UIinfo, width=largeur * 0.2, height=hauteur * 0.2, bg="orange")
        Rframe.pack(side="bottom", fill="x", padx=5, pady=5)

        # self.cadreBoutonBtnTour = tk.Button(self.UIinfo, text="Poser Tour", height=5, width=12, bg="red", command=self.selection_tour)
        # self.cadreBoutonBtnTour.pack(padx=20, pady=10)
        
        # Dans la méthode creer_cadre_jeu() de votre classe Vue, après la création de self.UIinfo
        self.tower_selection_frame = tk.Frame(self.UIinfo, bg="orange")
        self.tower_selection_frame.pack(pady=5)

        self.btn_machinegun = tk.Button(self.tower_selection_frame,
                                        font=("Stencil"),
                                        text="Machine Gun",
                                        width=8,
                                        command=lambda: self.selection_tower("machinegun"))
        self.btn_machinegun.pack(pady=5)

        self.btn_mortar = tk.Button(self.tower_selection_frame,
                                    font=("Stencil"),
                                    text="Mortar",
                                    width=8,
                                    command=lambda: self.selection_tower("mortar"))
        self.btn_mortar.pack(pady=2)

        self.btn_antitank = tk.Button(self.tower_selection_frame,
                                    font=("Stencil"),
                                    text="Anti-Tank",
                                    width=8,
                                    command=lambda: self.selection_tower("antitank"))
        self.btn_antitank.pack(pady=2)

        self.btn_antiair = tk.Button(self.tower_selection_frame,
                                    font=("Stencil"),
                                    text="Anti-Air",
                                    width=8,
                                    command=lambda: self.selection_tower("antiair"))
        self.btn_antiair.pack(pady=2)

        self.btn_artillery = tk.Button(self.tower_selection_frame,
                                    font=("Stencil"),
                                    text="Artillery",
                                    width=8,
                                    command=lambda: self.selection_tower("artillery"))
        self.btn_artillery.pack(pady=2)


        self.cadreBoutonBtnVendre = tk.Button(self.UIinfo, text="Vendre Tour", font=("Stencil"), height=1, width=12, bg="green", command=self.selection_sell)
        self.cadreBoutonBtnVendre.pack(padx=20, pady=2)

        self.button = tk.Button(Rframe, text="Start Round", font=("Stencil"), activeforeground="black",
                                command=self.controleur.start_Round)
        self.button.pack()
        
        self.upgrade_frame = tk.Frame(self.UIinfo, bg="orange")
        self.upgrade_frame.pack(pady=5)

        self.btn_speed = tk.Button(self.upgrade_frame, text="Speed", font=("Stencil"), width=8, command=self.selection_upgrade_speed)
        self.btn_speed.pack(pady=2)  # par défaut, pack les widgets verticalement

        self.btn_range = tk.Button(self.upgrade_frame, text="Range", font=("Stencil"), width=8, command=self.selection_upgrade_range)
        self.btn_range.pack(pady=2)

        self.btn_damage = tk.Button(self.upgrade_frame, text="Damage", font=("Stencil"), width=8, command=self.selection_upgrade_damage)
        self.btn_damage.pack(pady=2)
        
        self.btn_cooldown = tk.Button(self.upgrade_frame, text="Cooldown", font=("Stencil"), width=8, command=self.selection_upgrade_cooldown)
        self.btn_cooldown.pack(pady=2)



        self.label_Round_nbr = tk.Label(Rframe, text="Round : 0", fg="black", font=("Stencil"), bg="orange")
        self.label_Round_nbr.pack()

    def dessiner_ennemi(self, liste):
        self.canevas.delete("ennemi")
        self.canevas.delete("vie")
        self.canevas.delete("vie_max")

        for ennemi in liste:
            self.afficher_ennemi(ennemi)
            
    def afficher_ennemi(self, ennemi):
        
        degrees = -math.degrees(ennemi.angle)
        
        rotated_image = ennemi.image_base.rotate(degrees, expand=True)
        
        tk_image = ImageTk.PhotoImage(rotated_image)
        
        ennemi.tk_image = tk_image
        self.afficher_vie(ennemi)
        
        self.canevas.create_image(ennemi.x, ennemi.y, image=tk_image, tags="ennemi")

        self.afficher_vie(ennemi)
        
        
    def afficher_vie(self,ennemi):
        largeur_totale = 40
        pourcentage_vie = ennemi.life / ennemi.max_life
        largeur_actuelle = largeur_totale * pourcentage_vie
        largeurtemp = largeur_totale - largeur_actuelle
        
        
        if ennemi.life >= 1:
            self.canevas.create_rectangle(ennemi.x-20, ennemi.y-25, ennemi.x+20, ennemi.y-20, fill='gray', tag="vie_max")
            self.canevas.create_rectangle(ennemi.x-20, ennemi.y-25, ennemi.x+20-largeurtemp, ennemi.y-20, fill='green', tag="vie")
        
        #self.canvas.coords(self.barre_vie, ennemi.x-20, ennemi.y-25, ennemi.x-20, self.y-20)
        
        

    def dessiner_tours(self, tours):
        self.canevas.delete("tour")
        for tour in tours:
            if not hasattr(tour, "photo_image"):
                image = Image.open(tour.image_path)
                image = image.resize((40, 40))
                tour.photo_image = ImageTk.PhotoImage(image)
            self.canevas.create_image(tour.x, tour.y, image=tour.photo_image, anchor="center", tags=("tour"))
        

    def dessiner_projectiles(self, projectiles):
        self.canevas.delete("projectile")
        for projectile in projectiles:
            if hasattr(projectile, "tk_image") and projectile.tk_image is not None:
                self.canevas.create_image(projectile.x, projectile.y,
                                        image=projectile.tk_image,
                                        tags=("projectile",))

            # else:
            #     self.canevas.create_rectangle(projectile.x - 2, projectile.y - 2,
            #                                 projectile.x + 2, projectile.y + 2,
            #                                 fill=PROJECTILES_COLOR,
            #                                 tags=("projectile",))


    def dessiner_chemin(self, path, couleur="gray"):
        if len(path) > 1:
            for i in range(len(path) - 1):
                x1, y1 = path[i]
                x2, y2 = path[i + 1]
                self.canevas.create_line(x1, y1, x2, y2, fill="brown", width=25, tags=("chemin"), smooth=True , joinstyle=tk.BEVEL,capstyle=tk.ROUND)

                
    def selection_tour(self):
        self.placement_mode = not self.placement_mode
        print("Placement mode:", self.placement_mode)
        
        if self.placement_mode:
            self.canevas.bind("<Button-1>", self.afficher_coordonnees)
        else:
            self.canevas.unbind("<Button-1>")
            
    def selection_tower(self, tower_type):
        self.mode_actif = "placement"
        self.selected_tower = tower_type
        print(f"Tour sélectionnée : {tower_type}")


    def afficher_coordonnees(self, event):
        x, y = event.x, event.y

        if self.mode_actif == "placement":
            if self.verifier_emplacement(event):
                self.controleur.clic_dans_vue(x, y)
            else:
                print("Placement refusé.")
        elif self.mode_actif == "vente":
            if self.verifier_tour(event):
                self.controleur.clic_dans_vue_vendre(x, y)
            else:
                print("Aucune tour présente pour vente.")
        elif self.mode_actif == "upgrade":
            if self.verifier_tour(event):
                self.show_tour = self.controleur.clic_dans_vue_upgrade(x, y)
            else:
                print("Aucune tour présente pour upgrade.")
        else:
            print("Mode non défini.")
            
            ## Temporaire pour tester le draw circle
            if self.verifier_tour(event):
                self.show_tour = self.controleur.clic_dans_vue(x, y)
                # self.afficher_distance_tour(tour)
    
    def verifier_tour(self, event):
        items = self.canevas.find_overlapping(event.x - 10, event.y - 10, event.x + 10, event.y + 10)
        for item_id in items:
            tags = self.canevas.gettags(item_id)
            if "tour" in tags:
                return True
        return False

    def selection_tour(self):
        self.mode_actif = "placement"
        print("Mode placement")

    def selection_sell(self):
        self.mode_actif = "vente"
        print("Mode vente")

    def selection_upgrade_speed(self):
        self.mode_actif = "upgrade"
        self.upgrade_type = "speed"
        print("Mode upgrade activé: Speed")

    def selection_upgrade_range(self):
        self.mode_actif = "upgrade"
        self.upgrade_type = "range"
        print("Mode upgrade activé: Range")

    def selection_upgrade_damage(self):
        self.mode_actif = "upgrade"
        self.upgrade_type = "damage"
        print("Mode upgrade activé: Damage")
        
    def selection_upgrade_cooldown(self):
        self.mode_actif = "upgrade"
        self.upgrade_type = "cooldown"
        print("Mode upgrade activé: cooldown réduit de 5%")
        
        
    def selection_show_distance(self):
        self.mode_actif = "NOT_SET"
        
        if(self.show_distance):
            self.show_distance = False
            self.btndistance.config(text=(f"Range OFF"),fg="red")
            self.canevas.delete("cercle_tour")
        else:
            self.show_distance = True
            self.btndistance.config(text=(f"Range ON"),fg="green")
            
        
        print(f"Show distance est à {self.show_distance}")
        
    def afficher_distance_tour(self, tour):
        if(self.show_distance):
            self.canevas.delete("cercle_tour")
            #print(tour)
            if(tour != None):
                x,y,rayon = tour
                
                x1 = x-rayon
                y1 = y-rayon
                x2 = x+rayon
                y2 = y+rayon
                
                self.canevas.create_oval(x1,y1,x2,y2,outline="red",width=2,tags="cercle_tour")
            


        
    def afficher_game_over(self):
        popup_window = self.canevas.create_window(400, 300, window=self.popup, tags="popup")
        
    def verifier_emplacement(self, event):

        
        # https://tkinter-docs.readthedocs.io/en/latest/widgets/canvas.html
        # find_overlapping(x1, y1, x2, y2)
        # Returns every item overlapping the rectangular region given by x1, y1, x2, and y2. (x1, y1)
        # must be the top-left corner of the region and (x2, y2) the bottom-right.
        # The items are returned in stacking order, with the lowest item first.

        tempTour = self.canevas.find_overlapping(event.x - 10, event.y - 10, event.x + 10, event.y + 10)

        for item_id in tempTour:
            tags = self.canevas.gettags(item_id)
            if "tour" in tags or "chemin" in tags:
                
                return False

        if "tour" in tags:
            
            return False
        
        if "chemin" in tags:
            
            return False

        else:
            
            return True


