import math
import os
import json

class Tour():
    def __init__(self, posX, posY, vitesse=0, damage=0, rayon=0, cooldown_time=0, on_cooldown=0, angle=0, TTL=0):
        self.x = posX
        self.y = posY
        self.vitesse = vitesse
        self.damage = damage
        self.rayon = rayon
        self.cooldown_time = cooldown_time  # 1 secondes
        self.on_cooldown = on_cooldown  # false
        self.angle = angle
        self.abilities = {}
        self.TTL = rayon/vitesse

    def init_tower(self, f='main'):
        for file in os.listdir("abilities"):
            filename = os.path.splitext(file)
            # if(filename[0] = f):
            # print("fichier trouvé : ")
            # pass

    def tire(self, ennemis):
        # passer ici le 
        if not self.on_cooldown:
            for ennemi in ennemis:  # tire en fonction de qui est dans le rayon et le premier dans la liste
                distance = math.sqrt(
                    abs(ennemi.x - self.x) * abs(ennemi.x - self.x) + abs(ennemi.y - self.y) * abs(ennemi.y - self.y))
                if distance <= self.rayon:
                    self.on_cooldown = True
                    return [ennemi, self]
                else:
                    return None
            return None

    def add_abilities(self, f='main'):
        for file in os.listdir("abilities"):
            filename = os.path.splitext(file)
            if (filename[0] == f):
                print(f'fichier trouvé : ' + filename[0])
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
        self.type = "tracing"  # temporairement hardcoder on attend le type par la tour normalement.
        self.TTL = tour.TTL


class Modele():
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.count = 1
        self.projectiles = []
        self.tours = []
        self.ennemis = []
        self.path = [
            (0.0, 100.0),
            (100.0, 100.0),
            (200, 200),
            (200, 400),
            (300, 400),
            (300, 300),
            (400, 300),
            (400, 400),
            (800.0, 800.0),
        ]

        ### Test ici ###
        t = Tour(500, 300, 1, 2, 100, 0, False, 0, 6000)
        self.tours.append(t)

    def start_round(self):
        if len(self.ennemis) > 0:
            print("Round Can not start")
        else:
            self.count+=1
            for x in range(self.count):
                print(x)
                self.ennemis.append(Ennemi(self.path[0][0]-(x)*20, self.path[0][1], 10, 5, 1, self.path, 0))


    def valider_tirs(self):
        for tour in self.tours:
            # Le tirs contient lobject ennemi sur lequel il tir et la tour qui tir le projectile
            tirs = tour.tire(self.ennemis)  # [ennemi, tour] 
            if tirs:
                self.creer_projectile(tirs)

    def creer_projectile(self, tirs):
        p = Projectiles(tirs[0], tirs[1])  # [ennemi, tour] 
        self.projectiles.append(p)

    def mouvement_projectiles(self):
        for projectile in self.projectiles:
            ### Methode pour chaque type de projectile

            projectile.TTL -= 1
            if projectile.TTL <= 0:
                self.projectiles.remove(projectile)

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
            if projectile.type == "tracing":
                if projectile.ennemi.x >= projectile.x:
                    projectile.x += projectile.vitesse
                else:
                    projectile.x -= projectile.vitesse

                if projectile.ennemi.y >= projectile.y:
                    projectile.y += projectile.vitesse
                else:
                    projectile.y -= projectile.vitesse

            # delete le projectile si y touch et gerer la logique de damage ici et tout 
            # sort du rayon # timer

    def apparition_ennemis(self):
        ennemi = Ennemi(self.path[0][0], self.path[0][1], 10, 5, 1, self.path, 0)
        self.ennemis.append(ennemi)

    def deplacer_ennemis(self):
        for ennemi in self.ennemis:
            ennemi_arrive = ennemi.deplacer()
            if not ennemi_arrive:
                # lennemi a rentrer dans la base du joueur
                # faire perdre vie au joueur
                # ici faut delete lennemi
                self.ennemis.remove(ennemi)
                print(self.ennemis)


class Ennemi:  # chemin
    def __init__(self, x, y, taille, life, vitesse, path, index_path=0):
        self.x = x
        self.y = y
        self.taille = taille
        self.vitesse = vitesse
        self.life = life
        self.path = path
        self.index_path = index_path

    def deplacer(self):
        try:
            destination_X = self.path[self.index_path + 1][0]
            destination_Y = self.path[self.index_path + 1][1]

            if self.x != destination_X or self.y != destination_Y:

                if self.x < destination_X:
                    self.x += self.vitesse  # déplace droit
                elif self.x > destination_X:
                    self.x -= self.vitesse  # déplace gauche

                if self.y < destination_Y:
                    self.y += self.vitesse  # déplace bas
                elif self.y > destination_Y:
                    self.y -= self.vitesse  # déplace haut

                # print("pos_x:", math.floor(self.x), "pos_y:", math.floor(self.y), "NextPathPosX:", destination_X, "NextPathPosY", destination_Y)

            else:
                self.index_path += 1

        except:
            return False

        return True
