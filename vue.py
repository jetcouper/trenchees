import tkinter as tk

ENNEMIS_COLOR = "Green"
TOURS_COLOR = "Blue"
PROJECTILES_COLOR = "Red"


class Vue():
    def __init__(self, controleur, largeur, hauteur):
        self.controleur = controleur
        self.root = tk.Tk()
        self.creer_cadre_jeu(largeur, hauteur)

    def creer_cadre_jeu(self, largeur, hauteur):
        self.cadrePrincipal = tk.Frame(self.root, width=largeur, height=hauteur)
        self.cadrePrincipal.grid(column=0, row=0)
        self.canevas = tk.Canvas(self.cadrePrincipal, width=largeur, height=hauteur, bg="white")
        self.canevas.pack()
        self.canevas.bind("<Button-1>", self.afficher_coordonnees)
        
        self.cadreSecondaire = tk.Frame(self.root, width=largeur*0.2, height=hauteur, bg="white")
        self.cadreSecondaire.grid(column=1, row=0, rowspan=2)
        self.UIinfo = tk.Canvas(self.cadreSecondaire, width=largeur*0.2, height=hauteur, bg="white")
        self.UIinfo.pack_propagate(False)
        self.UIinfo.pack()
        ## ajouter le stock et les bouttons ici
        button = tk.Button(self.UIinfo, text="Start Round", foreground="lightgrey", activeforeground="black", command=self.controleur.modele.start_round) 
        button.pack()   

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
                                          fill=TOURS_COLOR, tags="tour")

    def dessiner_projectiles(self, projectiles):
        self.canevas.delete("projectile")
        for projectile in projectiles:
            self.canevas.create_rectangle(projectile.x - 2, projectile.y - 2,
                                          projectile.x + 2, projectile.y + 2,
                                          fill=PROJECTILES_COLOR, tags="projectile")

    def dessiner_chemin(self, path):
        self.canevas.delete("chemin")
        if len(path) > 1:
            for i in range(len(path) - 1):
                x1, y1 = path[i]
                x2, y2 = path[i + 1]
                self.canevas.create_line(x1, y1, x2, y2, fill="gray", width=5, tags="chemin")
        
        
    def afficher_coordonnees(self, event):
        x, y = event.x, event.y
        self.controleur.clic_dans_vue(x, y)
        
