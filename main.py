import time
import tkinter as tk

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

class Modele():
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        
class Ennemi: #chemin
    
    def __init__(self, id, x, y, life, vitesse, path, index_path):
        self.id = id
        self.x = x
        self.y = y
        self.vitesse = vitesse
        self.life = life
        self.path = path
        self.index_path = index_path
        
        # tous les paramètres seront initialisés via le fichier json de la carte 
        
    def apparition_ennemi(self, id, liste_ennemis, nbEnnemis, departX, departY, path, index_path):
        
        # création d'une liste pour générer les ennemis 
        # ou importation de la liste via le fichier json 
        
        # création d'une liste pour sauvegarder les positions des ennemis sur la carte 
        
        self.id = id; 
        self.liste_ennemis = []
        self.departX = departX
        self.departY = departY
        self.ennemi = ennemi #1 individuel
        
        self.nbEnnemis = nbEnnemis
        i = 1
        
        for i in range(nbEnnemis): #initialiser la boucle et création des ennemis 
            
            # ajouter un tag sur l'ennemi pour être capable de l'identifier 
            ennemi = Ennemi(id, liste_ennemis, i, departX, departY, path, 0) #self, id, liste_ennemis, nbEnnemis, departX, departY, path, index_path
            self.liste_ennemis.append(ennemi)
            time.sleep(1)
       
    
    def mouvementEnnemis (self, ennemi, liste_ennemis, positionX, positionY, path, index_path, fin_path):
        
        self.positionX = positionX
        self.positionY = positionY
        self.path = path
        self.index_path = index_path
        
        while index_path < fin_path: #tant que l'ennemi n'est pas au bout du chemin, il avance de 1 
            index_path += 1
            
        if index_path > fin_path: # mort ou disparition des ennemis 
            # le joueur perd une vie 
            liste_ennemis.pop(ennemi)
    
    
    
           
            
            
        
        
        
            
            
           
            
        
        
        
    
                
            
           
    
    
         
        

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