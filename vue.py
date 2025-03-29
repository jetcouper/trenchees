import tkinter as tk

ENNEMIS_COLOR = "Yellow"
TOURS_COLOR = "Blue"
PROJECTILES_COLOR = "Red"


class Vue():
    def __init__(self, controleur, largeur, hauteur):
        self.controleur = controleur
        self.root = tk.Tk()
        self.info = []
        self.creer_cadre_jeu(largeur, hauteur, self.info)

    def update_vue(self,vie, score, argent, round):
        self.info = [vie, score, argent, round]
        self.label_score.pack_forget
        self.score.pack_forget
        self.vie.pack_forget
        self.label_Round_nbr.pack_forget
        self.score.config(text=(f"Vie {self.info[1]}"))
        
        self.vie.config(text=(f"score {self.info[0]}"))
        
        self.Argent.config(text=(f"Argent {self.info[2]}"))
        
        self.label_Round_nbr.config(text=(f"Round: {self.info[3]}"))
        
   
        self.label_score.pack(pady=50)
        
        self.vie.pack(anchor="w")

        self.score.pack(anchor="w")
  
        self.Argent.pack(anchor="w")
        self.label_Round_nbr.pack()

    def creer_cadre_jeu(self, largeur, hauteur, info):
        
        self.cadrePrincipal = tk.Frame(self.root, width=largeur, height=hauteur)
        self.cadrePrincipal.grid(column=0, row=0)
        self.canevas = tk.Canvas(self.cadrePrincipal, width=largeur, height=hauteur, bg="green")
        self.canevas.pack()
        self.canevas.bind("<Button-1>", self.afficher_coordonnees)
        self.placeholder = 0
        
        self.cadreSecondaire = tk.Frame(self.root, width=largeur*0.2, height=hauteur, bg="orange")
        self.cadreSecondaire.grid(column=1, row=0, rowspan=2)
        self.UIinfo = tk.Canvas(self.cadreSecondaire, width=largeur*0.2, height=hauteur, bg="orange")
        self.UIinfo.pack_propagate(False)
        self.UIinfo.pack()
        ## ajouter le stock et les bouttons ici
        self.label_score = tk.Label(self.UIinfo, text=("Info"), fg="black",font=("Italic", 40), bg="orange", padx=2)
        self.label_score.pack(pady=50)
        
        self.vie = tk.Label(self.UIinfo, text=(f"Vie 0"), fg="black",font=("Italic", 20), bg="orange")
        self.vie.pack()
        
        self.score = tk.Label(self.UIinfo, text=(f"score 0"), fg="black",font=("Italic", 20), bg="orange")
        self.score.pack()
        
        self.Argent = tk.Label(self.UIinfo, text=(f"Argent 0"), fg="black",font=("Italic", 20), bg="orange")
        self.Argent.pack()

        
        
        Rframe = tk.Frame(self.UIinfo, width=largeur*0.2, height=hauteur*0.2, bg="orange")
        Rframe.pack(side="bottom",fill="x", padx=5, pady=5)
        
        
        button = tk.Button(Rframe, text="Start Round", activeforeground="black", command=self.controleur.start_Round)
        button.pack()
        
        self.label_Round_nbr = tk.Label(Rframe, text="Round : 0", fg="black",font=("Italic", 20), bg="orange")
        self.label_Round_nbr.pack()



    def dessiner_ennemi(self, liste):
        self.canevas.delete("ennemi")
        for ennemi in liste:
            self.canevas.create_oval(ennemi.x - ennemi.taille, ennemi.y - ennemi.taille,
                                     ennemi.x + ennemi.taille, ennemi.y + ennemi.taille,
                                     fill=ENNEMIS_COLOR, tags="ennemi")

    def dessiner_tours(self, tours):
        self.canevas.delete("tour")
        for tour in tours:
            self.canevas.create_rectangle(tour.x - 20 / 2, tour.y - 20 / 2,
                                          tour.x + 20, tour.y + 20,
                                          fill=TOURS_COLOR, tags=("tour"))

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
        
    def afficher_coordonnees(self, event):
        x, y = event.x, event.y
        
        if (self.verifier_emplacement(event)):
            self.controleur.clic_dans_vue(x, y)
        else:
            print("Not allowed")
        
                    
    def verifier_emplacement(self, event):   
        
        # https://tkinter-docs.readthedocs.io/en/latest/widgets/canvas.html
        # find_overlapping(x1, y1, x2, y2)
        # Returns every item overlapping the rectangular region given by x1, y1, x2, and y2. (x1, y1) 
        # must be the top-left corner of the region and (x2, y2) the bottom-right. 
        # The items are returned in stacking order, with the lowest item first.
        
        tempTour = self.canevas.find_overlapping(event.x - 20 / 2, event.y - 20 / 2, event.x + 20, event.y + 20)
        
        tags = self.canevas.gettags(tempTour) #vérifie s'il existe des tags à l'emplacement cliqué sur le canevas, selon le format des carrés/tours 
        
        if "tour" in tags or "chemin" in tags:
            print("not good")
            return False
            
        else:
            print("okay")
            return True
            
        
