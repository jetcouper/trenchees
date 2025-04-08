import tkinter as tk
from PIL import Image, ImageTk

ENNEMIS_COLOR = "Yellow"
TOURS_COLOR = "Blue"
PROJECTILES_COLOR = "Red"


class Vue():
    def __init__(self, controleur, largeur, hauteur):
        self.controleur = controleur
        self.root = tk.Tk()
        self.root.title("Tower Defense")
        ico = Image.open("assets/Machine_Gun.png")
        photo = ImageTk.PhotoImage(ico)
        self.root.wm_iconphoto(False, photo)
        self.info = []
        self.creer_cadre_jeu(largeur, hauteur, self.info)
        self.switch = True; 
        self.ennemi_image1 = Image.open("assets/avion.png")
        self.ennemi_image1 = self.ennemi_image1.resize((30, 30))
        self.ennemi_photo1 = ImageTk.PhotoImage(self.ennemi_image1)
        
        self.ennemi_image2 = Image.open("assets/ennemi2.png")
        self.ennemi_image2 = self.ennemi_image2.resize((30, 30))
        self.ennemi_photo2 = ImageTk.PhotoImage(self.ennemi_image2)
        
        self.placement_mode = False
        
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

        
        
        
    def reset(self):
        self.canevas.delete("popup")
        print("Message de Reset")

    def update_vue(self, vie, score, argent, round, nbennemis):
        self.info = [vie, score, argent, round, nbennemis]
        self.label_score.pack_forget
        self.score.pack_forget
        self.vie.pack_forget
        self.nbennemis.pack_forget
        self.label_Round_nbr.pack_forget
        self.score.config(text=(f"Vie {self.info[1]}"))

        self.vie.config(text=(f"score {self.info[0]}"))

        self.Argent.config(text=(f"Argent {self.info[2]}"))
        
        self.label_Round_nbr.config(text=(f"Round: {self.info[3]}"))

        self.nbennemis.config(text=(f"Ennemis restant: {self.info[4]}"))

        self.label_score.pack(pady=50)

        self.vie.pack(anchor="w")

        self.score.pack(anchor="w")

        self.Argent.pack(anchor="w")
        
        self.nbennemis.pack(anchor="w")
        
        self.label_Round_nbr.pack()
        if self.info[4] > 0:
            self.button.config(state="disabled")
        else:
            self.button.config(state="normal")

    def creer_cadre_jeu(self, largeur, hauteur, info):

        self.cadrePrincipal = tk.Frame(self.root, width=largeur, height=hauteur)
        self.cadrePrincipal.grid(column=0, row=0)
        self.map = Image.open("assets/map.png")
        self.map = self.map.resize((largeur, hauteur))
        self.map_photo = ImageTk.PhotoImage(self.map)
        self.canevas = tk.Canvas(self.cadrePrincipal, width=largeur, height=hauteur)
        self.canevas.bind("<Button-1>", self.afficher_coordonnees)
        self.canevas.pack()
        self.canevas.create_image(0, 0, anchor=tk.NW, image=self.map_photo)
        self.placeholder = 0

        self.cadreSecondaire = tk.Frame(self.root, width=largeur * 0.2, height=hauteur, bg="orange")
        self.cadreSecondaire.grid(column=1, row=0, rowspan=2)
        self.UIinfo = tk.Canvas(self.cadreSecondaire, width=largeur * 0.2, height=hauteur, bg="orange", relief="ridge",highlightthickness=0)
        self.UIinfo.pack_propagate(False)
        self.UIinfo.pack(padx=2)
        ## ajouter le stock et les bouttons ici
        
        
        
        self.label_score = tk.Label(self.UIinfo, text=("Info"), fg="black", font=("Italic", 40), bg="orange", padx=2)
        self.label_score.pack(pady=50)

        self.vie = tk.Label(self.UIinfo, text=(f"Vie 0"), fg="black", font=("Italic", 13, "bold" ), bg="orange")
        self.vie.pack()

        self.score = tk.Label(self.UIinfo, text=(f"score 0"), fg="black", font=("Italic", 13, "bold"), bg="orange")
        self.score.pack()

        self.Argent = tk.Label(self.UIinfo, text=(f"Argent 0"), fg="black", font=("Italic", 13, "bold"), bg="orange")
        self.Argent.pack()
        
        self.nbennemis = tk.Label(self.UIinfo, text=(f"Ennemis restant 0"), fg="black", font=("Italic", 13, "bold"),bg="orange")
        self.nbennemis.pack()
        
        
        ### Initialisation de la frame Popup
        self.popup = tk.Frame(self.canevas, bg="gray", bd=2, relief="raised")
        tk.Label(self.popup, text="Game-OVER", font=("Arial", 14), bg="gray").pack(pady=10)
        tk.Button(self.popup, text="Réessayer", command=lambda: self.controleur.init_game_values()).pack(pady=10)

        

        Rframe = tk.Frame(self.UIinfo, width=largeur * 0.2, height=hauteur * 0.2, bg="orange")
        Rframe.pack(side="bottom", fill="x", padx=5, pady=5)

        self.cadreBoutonBtnTour = tk.Button(self.UIinfo, text="Tours", height=5, width=12, bg="red", command=self.selection_tour)
        #self.cadreBoutonBtnTour.bind("<Button-1>", self.selection_tour)
        self.cadreBoutonBtnTour.pack(padx=20, pady=100)

        self.button = tk.Button(Rframe, text="Start Round", activeforeground="black",
                                command=self.controleur.start_Round)
        self.button.pack()

        self.label_Round_nbr = tk.Label(Rframe, text="Round : 0", fg="black", font=("Italic", 20), bg="orange")
        self.label_Round_nbr.pack()

    def dessiner_ennemi(self, liste):
        self.canevas.delete("ennemi")
        for ennemi in liste:
            self.canevas.create_image(ennemi.x, ennemi.y, image=self.ennemi_photo1, tags="ennemi")
            self.deplacer_ennemi
            
    def deplacer_ennemi(self):
        print("angle")
        
        self.angle += 90
        
        self.ennemi_photo1.rotate(self.angle)
         

    def dessiner_tours(self, tours):
        self.canevas.delete("tour")
        for tour in tours:
            self.canevas.create_image(tour.x, tour.y, image=self.tour_photo2, anchor="center", tags=("tour"))
            

    def dessiner_projectiles(self, projectiles):
        self.canevas.delete("projectile")
        for projectile in projectiles:
            self.canevas.create_rectangle(projectile.x - 2, projectile.y - 2,
                                          projectile.x + 2, projectile.y + 2,
                                          fill=PROJECTILES_COLOR, tags=("projectile",))

    def dessiner_chemin(self, path):
        self.canevas.delete("chemin")
        if len(path) > 1:
            for i in range(len(path) - 1):
                x1, y1 = path[i]
                x2, y2 = path[i + 1]
                self.canevas.create_line(x1, y1, x2, y2, fill="gray", width=5, tags=("chemin",))
                
    def selection_tour(self):
        self.placement_mode = not self.placement_mode
        print("Placement mode:", self.placement_mode)
        
        if self.placement_mode:
            self.canevas.bind("<Button-1>", self.afficher_coordonnees)
        else:
            self.canevas.unbind("<Button-1>")

        
    
    def afficher_coordonnees(self, event):
        x, y = event.x, event.y

        if self.placement_mode:
            if self.verifier_emplacement(event):
                self.controleur.clic_dans_vue(x, y)
            else:
                print("Placement refusé.")
        else:
            print("Mode placement non actif.")

            
    
        
    def afficher_game_over(self):
        popup_window = self.canevas.create_window(400, 300, window=self.popup, tags="popup")
        
    def verifier_emplacement(self, event):

        print("ici")
        # https://tkinter-docs.readthedocs.io/en/latest/widgets/canvas.html
        # find_overlapping(x1, y1, x2, y2)
        # Returns every item overlapping the rectangular region given by x1, y1, x2, and y2. (x1, y1)
        # must be the top-left corner of the region and (x2, y2) the bottom-right.
        # The items are returned in stacking order, with the lowest item first.

        tempTour = self.canevas.find_overlapping(event.x - 10, event.y - 10, event.x + 10, event.y + 10)

        for item_id in tempTour:
            tags = self.canevas.gettags(item_id)
            if "tour" in tags or "chemin" in tags:
                print("not good")
                return False

        print("okay")
       

        if "tour" in tags:
            print("tour")
            return False
        
        if "chemin" in tags:
            print("chemin")
            return False

        else:
            print("okay")
            return True


