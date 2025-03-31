from modele import *
from vue import Vue

class Controleur():
    def __init__(self):
        self.modele = Modele(800, 800)
        self.vue = Vue(self, self.modele.largeur, self.modele.hauteur)
        self.vue.dessiner_chemin(self.modele.path)
        #self.modele.apparition_ennemis() Start round dès le début
        self.loop_jeu()
        
    def clic_dans_vue(self, x, y):
        self.modele.placer_tour(x, y)

    def start_Round(self):
        self.modele.start_round()

    def loop_jeu(self):
        
        self.modele.valider_tirs()
        self.modele.mouvement_projectiles()
        self.vue.dessiner_ennemi(self.modele.ennemis)
        self.vue.dessiner_tours(self.modele.tours)
        self.vue.dessiner_projectiles(self.modele.projectiles)
        self.vue.update_vue( self.modele.score, self.modele.life_joueur,self.modele.argent, self.modele.round_count)
        
        self.modele.deplacer_ennemis()
        # self.modele.acheter_tour()
        self.modele.vie_restante_ennemi()
        self.modele.mort_ennemi()
        
        if(self.modele.player_alive):
            self.vue.root.after(16, self.loop_jeu)  # 16 pour 60 fps
        else:
            self.vue.afficher_game_over()
            
            
    def init_game_values(self):
        self.modele.reset()
        self.vue.reset()
        
        self.loop_jeu()

if __name__ == "__main__":
    c = Controleur()
    c.vue.root.mainloop()
    
    