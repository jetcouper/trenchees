import tkinter as tk
#Ajout pour voir les abilities dans le répertoire
import os
import json
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
    def __init__(self, posX, posY, vitesse=0, damage=0, rayon=0, cooldown_time=0, on_cooldown=0, angle=0):
        self.x = posX
        self.y = posY
        self.vitesse = vitesse
        self.damage = damage
        self.rayon = rayon
        self.cooldown_time = cooldown_time # 1 secondes
        self.on_cooldown = on_cooldown # false
        self.angle = angle
        self.abilities= {}

    def init_tower(self, f='main'):
        for file in os.listdir("abilities"):
            filename = os.path.splitext(file)
            # if(filename[0] = f):
                # print("fichier trouvé : ")
                # pass
        
        
    def tire(self, ennemis):
        # passer ici le 
        if not self.on_cooldown:
            for ennemi in ennemis: # tire en fonction de qui est dans le rayon et le premier dans la liste
                distance = math.sqrt(abs(ennemi.x - self.x) * abs(ennemi.x - self.x) + abs(ennemi.y - self.y) * abs(ennemi.y - self.y))
                if distance <= self.rayon:
                    self.on_cooldown = True
                    return [ennemi, self]
                else:
                    return None
            return None
    
    def add_abilities(self, f='main'):
        for file in os.listdir("abilities"):
            filename = os.path.splitext(file)
            if(filename[0] == f):
                print(f'fichier trouvé : '+filename[0])
                with open(os.path.join("abilities", file), "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.damage = data["damage"] + self.damage
                    self.vitesse = data["vitesse"] + self.vitesse
                    self.cooldown_time = data["cooldown"] + self.cooldown_time
                    self.rayon = data["rayon"] + self.rayon
                    self.type = data["type"]
                    self.abilities[data["id"]] = data

    
    def avaible_upgrade(self):
        pass
    
    def upgrade(self):
        pass
        
class Ennemi():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Projectiles():
    def __init__(self, ennemi, tour):
        self.x = tour.x
        self.y = tour.y
        self.vitesse = tour.vitesse
        self.damage = tour.damage
        self.angle = tour.angle
        self.cible_x = ennemi.x
        self.cible_y = ennemi.y
        self.ennemi = ennemi
        self.type = "basic" # temporairement hardcoder on attend le type par la tour normalement.

class Modele():
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.projectiles = []
        self.tours = []
        self.ennemis = []
        
        ### Test ici ###
        e = Ennemi(150, 55)
        e1 = Ennemi(50, 45)
        t = Tour(20, 20, 0.1, 5, 300, 5000, False, 0)
        self.tours.append(t)
        self.ennemis.append(e)
        self.ennemis.append(e1)
    
    def valider_tirs(self):
        for tour in self.tours:
            # Le tirs contient lobject ennemi sur lequel il tir et la tour qui tir le projectile
            tirs = tour.tire(self.ennemis) # [ennemi, tour] 
            if tirs:
                self.creer_projectile(tirs)
    
    def creer_projectile(self, tirs):
        p = Projectiles(tirs[0], tirs[1]) # [ennemi, tour] 
        self.projectiles.append(p)
        
    def mouvement_projectiles(self):
        for projectile in self.projectiles:
            ### Methode pour chaque type de projectile
            
            # Pour missile de base ?
            if projectile.type == "basic":
                if projectile.cible_x >= projectile.x:
                    projectile.x += projectile.vitesse
                else:
                    projectile.x -= projectile.vitesse
                    
                if projectile.cible_y >= projectile.y:
                    projectile.y += projectile.vitesse
                else:
                    projectile.y -= projectile.vitesse
                
            # Pour missile qui suit
            # if projectile.type == "following":
            # if projectile.ennemi.x >= projectile.x:
            #     projectile.x += projectile.vitesse
            # else:
            #     projectile.x -= projectile.vitesse
                
            # if projectile.ennemi.y >= projectile.y:
            #     projectile.y += projectile.vitesse
            # else:
            #     projectile.y -= projectile.vitesse
            
            # delete le projectile si y touch et gerer la logique de damage ici et tout 
            # sort du rayon # timer
            print(projectile.x, projectile.y) 
        

class Controleur():
    def __init__(self):     
        self.modele = Modele(60,60)
        self.vue = Vue(self, self.modele.largeur, self.modele.hauteur)
        self.loop_jeu()
        
    def loop_jeu(self):
        self.modele.valider_tirs()
        self.modele.mouvement_projectiles()
        self.vue.root.after(16, self.loop_jeu) # 16 pour 60 fps
    
if __name__ == "__main__":
    c = Controleur()
    c.vue.root.mainloop()