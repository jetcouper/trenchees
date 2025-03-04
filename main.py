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
        for ennemi in liste:
            self.canevas.delete("ennemi")
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
            (200.0, 500.0)
        ]

    
 
    def apparition_ennemis(self):
        ennemi = Ennemi(0, 0, 10, 5, 0.1, self.path, 0)
        self.liste_ennemis.append(ennemi)

    def deplacer_ennemis(self):
        for ennemi in self.liste_ennemis:
            ennemi.deplacer()
            #print(math.floor(ennemi.x), math.floor(ennemi.y))

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
        
        if len(self.path) <= self.index_path:
            pass # on arrive a la fin du path ici
        else:
            print(self.path[self.index_path])
            
            
            destination_X = self.path[self.index_path+1][0]
            destination_Y = self.path[self.index_path+1][1]
            
            if self.x != destination_X and self.y != destination_Y:
                
                if self.x < destination_X:
                    self.x += self.vitesse #déplace droit
                # elif self.x > destination_X:
                #     self.x -= self.vitesse #déplace gauche
                
                if self.y < destination_Y:
                    self.y += self.vitesse #déplace bas
                # elif self.y > destination_X:
                #     self.y -= self.vitesse #déplace haut
                
            else:
                self.index_path +=1
            
            # if coordonner destionation != coordonner self.path[self.index_path]
                # effectue ton mouvement vers la prochaine coord
                # self.x > self.path[index_path][0]:
                    # x+=1
                # self.y > self.path[index_path][1]:
                    # y+1
            #else:
                #self.index_path+=1
                
    #     def deplacer(self):
#         if self.index_path < len(self.path): #tant que le chemin n'est pas complété
#             destination_X, destination_Y = self.path[self.index_path] #on note la prochaine destination à atteindre
#             deplace_X = (destination_X - self.x)/self.vitesse # on vient chercher le rapport de déplacement des ennemis à chaque itération de rafraîchissement
#             deplace_Y = (destination_Y - self.y)/self.vitesse 
#             self.x += deplace_X #on ajoute cette valeur à chaque itération pour créer le déplacement
#             self.y += deplace_Y
            
            
        
        self.x += self.vitesse
        self.y += self.vitesse
        
        
class Controleur():
    def __init__(self):     
        self.modele = Modele(600,600)
        self.vue = Vue(self, self.modele.largeur, self.modele.hauteur)
        self.vue.dessiner_ennemi(self.modele.liste_ennemis)
        self.modele.apparition_ennemis()
        
        self.loop_jeu()
        
        
    def loop_jeu(self):
        self.modele.deplacer_ennemis()
        self.vue.root.after(16, self.loop_jeu) # 16 pour 60 fps
    
if __name__ == "__main__":
    c = Controleur()
    c.vue.root.mainloop()
    
    
    
    
    
    
    
    

    
# import time
# import tkinter as tk

# ENNEMIS_COLOR = "Green"

# class Vue():
#     def __init__(self, controleur, largeur, hauteur):
#         self.controleur = controleur
#         self.root = tk.Tk()
#         self.creer_cadre_jeu(largeur, hauteur)
        
        
#     def creer_cadre_jeu(self, largeur, hauteur):
#         self.cadrePrincipal = tk.Frame(self.root, width=largeur, height=hauteur)
#         self.cadrePrincipal.grid(column=0, row=0)
#         self.canevas = tk.Canvas(self.cadrePrincipal, width=largeur, height=hauteur, bg="white")
#         self.canevas.pack()
        
    
#     def dessiner_ennemi(self):
        
#         ennemi = self.modele.ennemi
#         self.canevas.delete("ennemi")
#         self.canevas.create_oval(ennemi.x - ennemi.taille, ennemi.y - ennemi.taille, 
#                                  ennemi.x + ennemi.taille, ennemi.y + 10, 
#                                  fill=ENNEMIS_COLOR,tags="ennemi")


#     # def update(self):
#     #     # pour mettre à jour le dessin des ennemis durant le jeu
        
#     #     self.canevas.delete("ennemi")
        
#     #     for ennemi in self.controleur.modele.liste_ennemis:
#     #         self.dessiner_ennemi(ennemi.x, ennemi.y)
            
            
# class Modele():
#     def __init__(self, largeur, hauteur):
#         self.largeur = largeur
#         self.hauteur = hauteur
#         self.liste_ennemis = []
#         self.path = [(0,0), (100, 200), (200, 500)]
    
 
#     def apparition_ennemis(self, nbEnnemis):
        
#         # création d'une liste pour générer les ennemis 
#         # ou importation de la liste via le fichier json 
        
#         # création d'une liste pour sauvegarder les positions des ennemis sur la carte 
        
#         for i in range(nbEnnemis): #initialiser la boucle et création des ennemis 
            
#             ennemi = Ennemi(0, 0, 10, 25, 2, self.path, 0) 
#             self.liste_ennemis.append(ennemi)

#     def deplacer_ennemis(self):
#         for ennemi in self.liste_ennemis:
#             ennemi.deplacer()
        
#     def supprimer_ennemis(self, ennemi): #pour mettre à jour la position des ennemis en fct de leur déplacement
#         self.liste_ennemis.remove(ennemi)
                 

# class Ennemi: #chemin

#     def __init__(self, x, y, taille, life, vitesse, path, index_path):
#         self.x = x
#         self.y = y
#         self.taille = taille
#         self.vitesse = vitesse
#         self.life = life
#         self.path = path
#         self.index_path = index_path
    
#         # tous les paramètres seront initialisés via le fichier json de la carte 
    
#     def deplacer(self):
#         if self.index_path < len(self.path): #tant que le chemin n'est pas complété
#             destination_X, destination_Y = self.path[self.index_path] #on note la prochaine destination à atteindre
#             deplace_X = (destination_X - self.x)/self.vitesse # on vient chercher le rapport de déplacement des ennemis à chaque itération de rafraîchissement
#             deplace_Y = (destination_Y - self.y)/self.vitesse 
#             self.x += deplace_X #on ajoute cette valeur à chaque itération pour créer le déplacement
#             self.y += deplace_Y
            
#         if abs(self.x - destination_X) < 1 and (self.y - destination_Y) < 1: #si on est rendu à la destination
#             self.index_path += 1 #on augmente l'indice de 1 afin de continuer le chemin 
        
#      #  target_x, target_y = self.path[self.index_path]
#         #     # Calcul du déplacement de l'ennemi vers le point suivant
#         #     step_x = (target_x - self.x) / self.vitesse
#         #     step_y = (target_y - self.y) / self.vitesse
#         #     self.x += step_x
#         #     self.y += step_y
#         #     if abs(self.x - target_x) < 1 and abs(self.y - target_y) < 1:
#         #         self.index_path += 1  # L'ennemi a atteint le point suivant du chemin
        
        
#     # def mouvementEnnemis (self, ennemi, liste_ennemis, positionX, positionY, path, index_path, fin_path):
        
#     #     self.positionX = positionX
#     #     self.positionY = positionY
#     #     self.path = path
#     #     self.index_path = index_path
        
#     #     while index_path < fin_path: #tant que l'ennemi n'est pas au bout du chemin, il avance de 1 
#     #         index_path += 1
            
#     #     if index_path > fin_path: # mort ou disparition des ennemis 
#     #         # le joueur perd une vie 
#     #         self.liste_ennemis.remove(ennemi)  
         

# # def bouger_ennemi(self):
# #     self.ennemi.mouvementEnnemis() 
    
# # def __init__(self, controleur):
# #     self.controleur = controleur
# #     self.path = {0:[[0,100],[300,100]],
# #                        1:[[300,100],[300,500]],
# #                        2:[[300,500],[800,500]]}
#     #self.ennemi = Modele.Ennemi(self.path)

# class Controleur():
#     def __init__(self):     
#         self.modele = Modele(600,600)
#         self.vue = Vue(self, self.modele.largeur, self.modele.hauteur)
#         self.vue.dessiner_ennemi()
#         self.modele.ennemi()
#         self.modele.apparition_ennemis()
#         self.modele.deplacer_ennemis()
#         self.modele.supprimer_ennemis()

        
#         self.loop_jeu()
        
        
#     def loop_jeu(self):
#         self.vue.root.after(16, self.loop_jeu) # 16 pour 60 fps
    
# if __name__ == "__main__":
#     c = Controleur()
#     c.vue.root.mainloop()