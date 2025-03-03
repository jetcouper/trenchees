import tkinter as tk
#Ajout pour voir les abilities dans le répertoire
import os

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
        self.vitesse = 0
        self.damage = 0
        self.rayon = 0
        self.cooldown = 0
        self.angle = 0
    
    def init_tower(self, f='main'):
        for file in os.listdir("abilities"):
            filename = os.path.splitext(file)
            # if(filename[0] = f):
                # print("fichier trouvé : ")
                # pass
        
        
    def tirer(self):
        self.angle = Modele.valider_tirs() ## Remplacer par le fonction qui tir dans la classe Modele
    
    def avaible_upgrade(self):
        pass
    
    def upgrade(self):
        pass
        


class Modele():
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        
    def valider_tirs():
        pass

class Controleur():
    def __init__(self):     
        self.modele = Modele(600,600)
        self.vue = Vue(self, self.modele.largeur, self.modele.hauteur)
        self.loop_jeu()
        
    def loop_jeu(self):
        self.vue.root.after(16, self.loop_jeu) # 16 pour 60 fps
    
if __name__ == "__main__":
    c = Controleur()
    c.vue.root.mainloop()