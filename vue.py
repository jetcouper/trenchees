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
