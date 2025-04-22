from modele import *
from vue import Vue


class Controleur():
    def __init__(self):
        self.modele = Modele(800, 800)
        self.vue = Vue(self, self.modele.largeur, self.modele.hauteur)
        self.vue.dessiner_chemin(self.modele.path, "gray")
        self.vue.dessiner_chemin(self.modele.path2, "blue")
        # self.modele.apparition_ennemis() Start round dès le début
        self.demarrerRound = False
        self.loop_jeu()

    def clic_dans_vue(self, x, y):
        if self.vue.mode_actif == "placement":
            tower_type = getattr(self.vue, "selected_tower", "machinegun")
            self.modele.placer_tour(x, y, tower_type)
        elif self.vue.mode_actif == "vente":
            self.clic_dans_vue_vendre(x, y)
        elif self.vue.mode_actif == "upgrade":
            self.clic_dans_vue_upgrade(x, y)

            
    def clic_dans_vue_vendre(self, x, y):
        self.modele.vendre_tour(x, y)
        
    def clic_dans_vue_upgrade(self, x, y):
        # Antoine
        self.modele.upgrade_tour(x, y, self.vue.upgrade_type)

    def start_Round(self):
        self.modele.start_round()

    def select_Tour(self):
        self.vue.verifier_emplacement()

    def loop_jeu(self):
        self.modele.valider_tirs()
        self.modele.mouvement_projectiles()
        self.vue.dessiner_ennemi(self.modele.ennemis)
        self.vue.dessiner_tours(self.modele.tours)
        self.vue.dessiner_projectiles(self.modele.projectiles)
        self.vue.update_vue(self.modele.score, self.modele.life_joueur, self.modele.argent, self.modele.round_count,len(self.modele.ennemis))

        self.modele.deplacer_ennemis()
        # self.modele.acheter_tour()
        self.modele.vie_restante_ennemi()
        self.modele.mort_ennemi()
        
        if(self.modele.player_alive):
            self.vue.root.after(16, self.loop_jeu)  # 16 pour 60 fps
        else:
            self.vue.afficher_game_over()

        if(self.modele.countEnnemie == 0):
            self.demarrerRound = False
        else:
            self.demarrerRound = True

            
            
    def init_game_values(self):
        self.modele.reset()
        self.vue.reset()
        
        self.loop_jeu()

if __name__ == "__main__":
    c = Controleur()
    c.vue.root.mainloop()

# ! APPEL DU SCRUM !