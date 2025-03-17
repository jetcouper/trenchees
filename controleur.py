from modele import *
from vue import Vue

class Controleur():
    def __init__(self):
        self.modele = Modele(800, 1000)
        self.vue = Vue(self, self.modele.largeur, self.modele.hauteur)
        self.vue.dessiner_chemin(self.modele.path)
        self.modele.apparition_ennemis()
        self.loop_jeu()

    def loop_jeu(self):
        self.modele.valider_tirs()
        self.modele.mouvement_projectiles()
        self.vue.dessiner_ennemi(self.modele.ennemis)
        self.vue.dessiner_tours(self.modele.tours)
        self.vue.dessiner_projectiles(self.modele.projectiles)
        self.modele.deplacer_ennemis()
        self.modele.acheter_tour()
        self.modele.vie_restante_ennemi()
        self.modele.mort_ennemi()
        self.vue.root.after(16, self.loop_jeu)  # 16 pour 60 fps


if __name__ == "__main__":
    c = Controleur()
    c.vue.root.mainloop()