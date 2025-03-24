import tkinter as tk

ENNEMIS_COLOR = "Green"
TOURS_COLOR = "Blue"
PROJECTILES_COLOR = "Red"


class Vue():
    def __init__(self, controleur, largeur, hauteur):
        self.controleur = controleur
        self.root = tk.Tk()
        self.creer_cadre_jeu(largeur, hauteur)
        self.dessiner_btn_Round()

    def creer_cadre_jeu(self, largeur, hauteur):
        self.cadrePrincipal = tk.Frame(self.root, width=largeur, height=hauteur)
        self.cadrePrincipal.grid(column=0, row=0)
        self.canevas = tk.Canvas(self.cadrePrincipal, width=largeur, height=hauteur, bg="white")
        self.canevas.pack()
        self.canevas.bind("<Button-1>", self.afficher_coordonnees)

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
                
    def dessiner_btn_Round(self):
        btn_test = tk.Button(self.cadrePrincipal,text="Start Round", command=self.controleur.modele.start_round)
        btn_test.pack(anchor="sw")
        
    def afficher_coordonnees(self, event):
        x, y = event.x, event.y
        
        if (self.verifier_emplacement(x,y)):
            self.controleur.clic_dans_vue(x, y)
        else:
            print("Not allowed")
        
        
    def identifier_tour(self, x, y):
        
        if ([x,y] == self.canevas.gettags("tour")):
            print("tour")
                    
    def verifier_emplacement(self, x, y):
        
        self.identifier_tour(x,y)
        
        if ([x,y] != self.canevas.gettags("chemin") and [x,y] != self.canevas.gettags("tour")):
            return True
        
