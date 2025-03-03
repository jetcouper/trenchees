import tkinter as tk
import math

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
    def __init__(self,posX, posY):
        self.x = posX
        self.y = posY
        self.vitesse = 1
        self.damage = 1
        self.rayon = 10
        self.cooldown = 100
        self.angle = 0
        
    def tirer(self):
        self.angle = Modele.valider_tirs() ## Remplacer par le fonction qui tir dans la classe Projectile


class Tour():
    def __init__(self, x, y, vitesse, damage, rayon, cooldown_time, on_cooldown, angle):
        self.x = x
        self.y = y
        self.vitesse = vitesse
        self.damage = damage
        self.rayon = rayon
        self.cooldown_time = cooldown_time # 1 secondes
        self.on_cooldown = on_cooldown # false
        self.angle = angle
        
    def tire(self, ennemis):
        for ennemi in ennemis:
            distance = math.sqrt(abs(ennemi.x - self.x) * abs(ennemi.x - self.x) + abs(ennemi.y - self.y) * abs(ennemi.y - self.y))
            if distance <= self.rayon:
                print(distance)
            
        
class Ennemi():
    def __init__(self, x, y):
        self.x = x
        self.y = y

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
        self.tours = []
        self.ennemis = []
        e = Ennemi(20, 250)
        t = Tour(20, 20, 1, 5, 20, 5000, False, 0)
        self.tours.append(t)
        self.ennemis.append(e)
        
    def valider_tirs(self):
        for tour in self.tours:
            tour.tire(self.ennemis)
            
            

class Controleur():
    def __init__(self):     
        self.modele = Modele(600,600)
        self.vue = Vue(self, self.modele.largeur, self.modele.hauteur)
        self.loop_jeu()
        
    def loop_jeu(self):
        self.modele.valider_tirs()
        self.vue.root.after(16, self.loop_jeu) # 16 pour 60 fps
        
    
if __name__ == "__main__":
    c = Controleur()
    c.vue.root.mainloop()