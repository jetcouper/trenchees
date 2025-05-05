from modele import *
from vue import Vue
from menu import Menu
import tkinter as tk

class Controleur():
    def __init__(self):
        # Création d'une fenêtre root unique
        self.root = tk.Tk()
        
        self.modele = Partie(1000, 800)  # Ajustez la largeur pour inclure le panneau latéral
        
        # Création du menu avec la référence au root
        self.vue = Menu(self, self.root, self.modele.largeur, self.modele.hauteur)
        
        # Initialisation de la variable pour stocker la vue du jeu plus tard
        self.vue_jeu = None
        
        self.demarrerRound = False

    def clic_start(self):
        # Cacher le menu
        self.vue.cacher()
        
        # Initialiser la vue du jeu si ce n'est pas déjà fait
        if self.vue_jeu is None:
            # S'assurer que le modèle a des paths définis avant de créer la vue
            if not hasattr(self.modele, 'path') or not self.modele.path:
                # Définir des chemins par défaut si nécessaire
                self.modele.path = [(100, 100), (700, 100), (700, 700), (100, 700)]
                self.modele.path2 = [(200, 200), (600, 200), (600, 600), (200, 600)]
            
            # Créer la vue du jeu avec des dimensions adaptées
            self.vue_jeu = Vue(self, self.modele.largeur, self.modele.hauteur, self.root)
            
            # Définir explicitement la taille de la fenêtre pour inclure la barre latérale
            self.root.geometry(f"{self.modele.largeur + 200}x{self.modele.hauteur}")  # +200 pour la barre latérale
            
            # Maintenant dessiner les chemins avec les paths du modèle
            self.vue_jeu.dessiner_chemin(self.modele.path, "gray")
            self.vue_jeu.dessiner_chemin(self.modele.path2, "blue")
        else:
            # Sinon, juste afficher la vue existante et redessiner les chemins
            self.vue_jeu.afficher()
            self.vue_jeu.dessiner_chemin(self.modele.path, "gray")
            self.vue_jeu.dessiner_chemin(self.modele.path2, "blue")
        
        # Démarrer la boucle de jeu
        self.loop_jeu()

    # Méthode pour revenir au menu si nécessaire
    def retour_menu(self):
        if self.vue_jeu:
            self.vue_jeu.cacher()
        self.vue.afficher()

    # Le reste des méthodes reste inchangé
    def clic_dans_vue(self, x, y):
        if self.vue_jeu.mode_actif == "placement":
            tower_type = getattr(self.vue_jeu, "selected_tower", "machinegun")
            self.modele.placer_tour(x, y, tower_type)
        elif self.vue_jeu.mode_actif == "vente":
            self.clic_dans_vue_vendre(x, y)
        elif self.vue_jeu.mode_actif == "upgrade":
            self.clic_dans_vue_upgrade(x, y)
            
    def clic_dans_vue_vendre(self, x, y):
        self.modele.vendre_tour(x, y)
        
    def clic_dans_vue_upgrade(self, x, y):
        self.modele.upgrade_tour(x, y, self.vue_jeu.upgrade_type)

    def start_Round(self):
        self.modele.start_round()

    def select_Tour(self):
        self.vue_jeu.verifier_emplacement()

    def loop_jeu(self):
        self.modele.valider_tirs()
        self.modele.mouvement_projectiles()
        self.vue_jeu.dessiner_ennemi(self.modele.ennemis)
        self.vue_jeu.dessiner_tours(self.modele.tours)
        self.vue_jeu.dessiner_projectiles(self.modele.projectiles)
        self.vue_jeu.update_vue(self.modele.life_joueur, self.modele.score, self.modele.argent, self.modele.round_count, len(self.modele.ennemis))

        self.modele.deplacer_ennemis()
        self.modele.vie_restante_ennemi()
        self.modele.mort_ennemi()
        
        if(self.modele.player_alive):
            self.root.after(16, self.loop_jeu)  # 16 pour 60 fps
        else:
            self.vue_jeu.afficher_game_over()

        if(self.modele.countEnnemie == 0):
            self.demarrerRound = False
        else:
            self.demarrerRound = True
            
    def init_game_values(self):
        self.modele.reset()
        if self.vue_jeu:
            self.vue_jeu.reset()
        self.loop_jeu()

if __name__ == "__main__":
    c = Controleur()
    c.root.mainloop()
