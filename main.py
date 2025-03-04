import tkinter as tk
import math

ENNEMIS_COLOR = "Green"

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
                                    ennemi.x + ennemi.taille, ennemi.y + 10, 
                                    fill=ENNEMIS_COLOR,tags="ennemi")
            
class Modele():
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.liste_ennemis = []
        self.path = [
            (0.0, 0.0),
            (25.0, 50.0),
            (50.0, 100.0),
            (75.0, 150.0),
            (100.0, 200.0),
            (120.0, 250.0),
            (140.0, 300.0),
            (160.0, 350.0),
            (180.0, 400.0),
            (200.0, 500.0),
            (20,20)
        ]
        
        self.path1 = [
            (0.0, 0.0),
            (10.0, 10.0),
            (160.0, 150.0),
            (50.0, 100.0),
            (100.0, 200.0),
            (75.0, 150.0),
            (120.0, 250.0),
            (140.0, 300.0),
            (180.0, 400.0),
            (200.0, 500.0),
            (20,20)
        ]

    def apparition_ennemis(self):
        ennemi = Ennemi(0, 0, 10, 5, 1, self.path, 0)
        ennemi2 = Ennemi(0, 0, 10, 5, 1, self.path1, 0)
        self.liste_ennemis.append(ennemi)
        self.liste_ennemis.append(ennemi2)

    def deplacer_ennemis(self):
        for ennemi in self.liste_ennemis:
            ennemi_arrive = ennemi.deplacer()
            if not ennemi_arrive:
                # lennemi a rentrer dans la base du joueur
                # faire perdre vie au joueur
                # ici faut delete lennemi
                self.liste_ennemis.remove(ennemi)
                print(self.liste_ennemis)

class Ennemi: #chemin

    def __init__(self, x, y, taille, life, vitesse, path, index_path = 0):
        self.x = x
        self.y = y
        self.taille = taille
        self.vitesse = vitesse
        self.life = life
        self.path = path
        self.index_path = index_path
    
    def deplacer(self):
        try:
            destination_X = self.path[self.index_path+1][0]
            destination_Y = self.path[self.index_path+1][1]
        
            if self.x != destination_X or self.y != destination_Y:
            
                if self.x < destination_X:
                    self.x += self.vitesse #déplace droit
                elif self.x > destination_X:
                    self.x -= self.vitesse #déplace gauche
                
                if self.y < destination_Y:
                    self.y += self.vitesse #déplace bas
                elif self.y > destination_Y:
                    self.y -= self.vitesse #déplace haut
                    
                print("pos_x:", math.floor(self.x), "pos_y:", math.floor(self.y), "NextPathPosX:", destination_X, "NextPathPosY", destination_Y)
                
            else:
                self.index_path +=1
                
        except:
            return False
            
        return True
        
        
class Controleur():
    def __init__(self):     
        self.modele = Modele(600,600)
        self.vue = Vue(self, self.modele.largeur, self.modele.hauteur)
        self.modele.apparition_ennemis()
        self.loop_jeu()
        
        
    def loop_jeu(self):
        self.vue.dessiner_ennemi(self.modele.liste_ennemis)
        self.modele.deplacer_ennemis()
        self.vue.root.after(16, self.loop_jeu) # 16 pour 60 fps
    
if __name__ == "__main__":
    c = Controleur()
    c.vue.root.mainloop()
