from tkinter import *
import tkinter as tk

class Vue():
    def __init__(self, controleur,modele, largeur, hauteur):
        self.controleur = controleur
        self.modele = modele
        self.largeur_pincipale = largeur
        self.hauteur_principale = hauteur
        self.root = tk.Tk()
        self.root.geometry(f'{largeur}x{hauteur}')
        self.root.title("Projet Tower Defense (Trenches)")
        
        self.frame_list = {}
        self.grid_cells = []
        
        self.init_frames()
        self.set_gameFrames()
        self.creer_grille_cases()
        
    def afficher_jeu(self):
        creep = self.modele.ennemi
        self.canvas.delete("ennemi")
        self.canvas.create_oval(creep.x - creep.taille,
                                     creep.y - creep.taille,
                                     creep.x + creep.taille,
                                     creep.y + creep.taille,
                                     fill = "red",
                                     tags=("ennemi"))    
    
    def init_frames(self):
        self.creer_cadre_principal()
        self.creer_cadre_jeu()
        self.creer_cadre_sidebar()
        
    def set_gameFrames(self):
        # self.canvas.grid()  # Supprimé car self.canvas est déjà pack()
        self.frame_list["Frame_sidebar"].grid()
        
    def creer_cadre_principal(self):
        self.cadrePrincipal = tk.Frame(self.root, width=self.largeur_pincipale, height=self.hauteur_principale , bg="gray")
        self.cadrePrincipal.pack(expand=True)
        self.cadrePrincipal.grid_propagate(False)

    # Configuration correcte des colonnes
        self.cadrePrincipal.grid_columnconfigure(0, weight=4) 
        self.cadrePrincipal.grid_columnconfigure(1, weight=1) 
        
    def creer_cadre_jeu(self):
        self.frame_list["Frame_Terrain"] = tk.Frame(self.cadrePrincipal, width=self.largeur_pincipale*0.8, height=self.hauteur_principale)
        self.frame_list["Frame_Terrain"].grid(column=0, row=0, sticky="nsew")
        
        self.canvas = tk.Canvas(self.frame_list["Frame_Terrain"], bg="blue", scrollregion=(0,0,32*50,32*50))
        self.canvas.pack(fill="both", expand=True)
        
        self.scroll_x = tk.Scrollbar(self.frame_list["Frame_Terrain"], orient="horizontal", command=self.canvas.xview)
        # self.scroll_x.pack(side="bottom", fill="x")  # Désactivé pour masquer la barre horizontale
        self.scroll_y = tk.Scrollbar(self.frame_list["Frame_Terrain"], orient="vertical", command=self.canvas.yview)
        # self.scroll_y.pack(side="right", fill="y")  # Désactivé pour masquer la barre verticale
        
        self.canvas.configure(xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)
        self.canvas.bind("<ButtonPress-1>", self.debut_scroll)
        self.canvas.bind("<B1-Motion>", self.defilement)
        
    def creer_cadre_sidebar(self):
        sidebar = tk.Canvas(self.cadrePrincipal,background="green",width=self.largeur_pincipale*0.2, height=self.hauteur_principale)
        sidebar.grid(column=1,row=0,sticky="nsew")
        self.frame_list["Frame_sidebar"] = sidebar
        
    def loadFrame(self, nom):
        self.frame_list[nom].grid()
        
    def creer_grille_cases(self):
        taille_case = 32
        nombre_cases = 50
        
        for row in range(nombre_cases):
            for col in range(nombre_cases):
                case = self.canvas.create_rectangle(
                    col * taille_case, row * taille_case,
                    (col + 1) * taille_case, (row + 1) * taille_case,
                    fill="white", outline="black", tags=f"cell_{row}_{col}")
                
                self.canvas.tag_bind(f"cell_{row}_{col}", "<ButtonPress-1>", lambda event, r=row, c=col: self.changer_couleur(r, c))
                self.canvas.tag_bind(f"cell_{row}_{col}", "<ButtonRelease-1>", lambda event, r=row, c=col: self.reinitialiser_couleur(r, c))
        
    def changer_couleur(self, row, col):
        self.canvas.itemconfig(f"cell_{row}_{col}", fill="gray")
        
    def reinitialiser_couleur(self, row, col):
        self.canvas.itemconfig(f"cell_{row}_{col}", fill="white")
        
    def debut_scroll(self, event):
        self.canvas.scan_mark(event.x, event.y)
        
    def defilement(self, event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)
        
    def loop_jeu(self,evt):
        self.controleur.loop_jeu()    
        
class Modele():
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.ennemi = Ennemie()
        
    def bougerEnnemie(self):
        self.ennemi.bougerEnnemie()
    
class Ennemie():
    def __init__(self):
        self.x = 0
        self.y = 100
        self.taille = 10
        self.vitesse = 5
        
    def bougerEnnemie(self):
        self.x += self.vitesse
        
class Controleur():
    def __init__(self):     
        self.modele = Modele(800,600)
        self.vue = Vue(self, self.modele ,self.modele.largeur, self.modele.hauteur)
        self.vue.root.mainloop()
        
    def loop_jeu(self):
        self.modele.bougerEnnemie()
        self.vue.afficher_jeu()
        self.vue.root.after(16, self.loop_jeu)
    
if __name__ == "__main__":
    c = Controleur()
