import tkinter as tk
import time

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

class Tour():
    def __init__(self, x, y, vitesse, damage, rayon, cooldown, angle):
        self.x = x
        self.y = y
        self.vitesse = vitesse
        self.damage = damage
        self.rayon = rayon
        self.cooldown = cooldown
        self.angle = angle
        

class Projectiles():
    def __init__(self, tour):
        self.x = tour.x
        self.y = tour.y
        self.vitesse = tour.vitesse
        self.damage = tour.damage
        self.angle = tour.angle

class Modele():
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.projectiles = []
        self.t = Tour(20, 20, 1, 5, 20, 5000, 0)

class Controleur():
    def __init__(self):     
        self.modele = Modele(600,600)
        self.vue = Vue(self, self.modele.largeur, self.modele.hauteur)
        self.loop_jeu()
        
    def loop_jeu(self):
        time.sleep(1)
        print(self.modele.t)
        self.vue.root.after(16, self.loop_jeu) # 16 pour 60 fps
        
    
if __name__ == "__main__":
    c = Controleur()
    c.vue.root.mainloop()