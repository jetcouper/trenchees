import math
import os
import json

class Tour():
    def __init__(self, posX, posY, vitesse=0, damage=0, rayon=0, cooldown_time=0, on_cooldown=0, angle=0, TTL=100, price=50):
        self.x = posX
        self.y = posY
        self.vitesse = vitesse
        self.damage = damage
        self.rayon = rayon
        self.cooldown_time = cooldown_time  # 1 secondes
        self.on_cooldown = on_cooldown  # false
        self.angle = angle
        self.abilities = {}
        self.TTL = TTL
        self.price = price # coût de la tour 

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
    def __init__(self, largeur, hauteur, score=250, life_joueur=100):
        self.largeur = largeur
        self.hauteur = hauteur
        self.score = score #score initial du joueur
        self.life_joueur = life_joueur #nb de vies initiales du joueur
        #self.experience_joueur = 1 #expérience initiale du joueur ???????
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

        # self.path1 = [
        #     (0.0, 0.0),
        #     (10.0, 10.0),
        #     (160.0, 150.0),
        #     (50.0, 100.0),
        #     (100.0, 200.0),
        #     (75.0, 150.0),
        #     (120.0, 250.0),
        #     (140.0, 300.0),
        #     (180.0, 400.0),
        #     (200.0, 500.0),
        #     (20, 20)
        # ]

        ### Test ici ###
        t = Tour(250, 300, 1, 2, 300, 5000, False, 0, 6000)
        self.tours.append(t)

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
        ennemi = Ennemi(0, 100, 10, 5, 1, self.path, 0, 25)
        ennemi2 = Ennemi(0, 100, 10, 5, 1, self.path, 0, 20)
        self.ennemis.append(ennemi)
        self.ennemis.append(ennemi2)

    def deplacer_ennemis(self):
        for ennemi in self.ennemis:
            ennemi_arrive = ennemi.deplacer()
            if not ennemi_arrive:
                # lennemi a rentrer dans la base du joueur
                # faire perdre vie au joueur
                # ici faut delete lennemi
                #self.ennemis.remove(ennemi) #vers la méthode mort ennemi 
                self.mort_ennemi()
                print(self.ennemis)
                
    def vie_restante_ennemi(self):
        
        for ennemi in self.ennemis:
            
            for projectile in self.projectiles: 
                if (ennemi.x == projectile.x and ennemi.y == projectile.y):
                        ennemi.life -= projectile.damage
            
                if (ennemi.life < 0):
                    ennemi.life = 0
                    self.mort_ennemi() # call la fonction mort de l'ennemi 
        
        print(ennemi.life) #pour vérifier le damage sur ennemi
                
    def mort_ennemi(self):
        
        for ennemi in self.ennemis:
            if (ennemi.life == 0): #si l'ennemi est vaincu
                self.score += ennemi.score # le joueur augmente son score selon le nb de points donnés par l'ennemi 
                self.ennemis.remove(ennemi)
        
        print(self.score)   #affiche le nouveau score du joueur            
                
    def acheter_tour(self, tour):
        
        if (self.score >= tour.price): # si le joueur peut acheter la tour avec son pointage, on soustrait du solde le montant de la tour 
            self.score -= tour.price
            
        if (self.score < tour.price): # si le joueur n'a pas assez de fonds, un message avertit le joueur qu'il ne peut procéder à l'achat 
            print("Pas assez de fonds pour l'achat de cette tour")
    
    def victoire_ennemi(self):
        for ennemi in self.ennemis:
            if (ennemi.x == self.path[len(self.path) - 1] and ennemi.y == self.path[len(self.path) - 1]): #si un ennemi traverse tout le chemin
                self.score -= ennemi.score

                if (self.score < 0):
                    self.score = 0
                    
    def fin_partie(self):   
        
        if (self.score == 0):
            print("Fin de la partie") #fin du loop 
                 
                    
            

class Ennemi:  # chemin
    def __init__(self, x, y, taille, life, vitesse, path, index_path=0, score=15):
        self.x = x
        self.y = y
        self.taille = taille
        self.vitesse = vitesse
        self.life = life
        self.path = path
        self.index_path = index_path
        self.score = score

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
    
            
        
    
    
