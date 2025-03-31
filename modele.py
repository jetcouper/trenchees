import math
import os
import json
import random


class Helper(object):
    def getAngledPoint(angle,longueur,cx,cy):
        x = (math.cos(angle)*longueur)+cx
        y = (math.sin(angle)*longueur)+cy
        return (x,y)
    getAngledPoint = staticmethod(getAngledPoint)
    
    def calcAngle(x1,y1,x2,y2):
         dx = x2-x1
         dy = y2-y1
         #angle = (math.atan2(dy,dx) % (2*math.pi)) * (180/math.pi)
         angle = (math.atan2(dy,dx) ) #% (2*math.pi)) * (180/math.pi)
         return angle
    calcAngle = staticmethod(calcAngle)
    
    def calcDistance(x1,y1,x2,y2):
         dx = abs(x2-x1)**2
         dy = abs(y2-y1)**2
         distance=math.sqrt(dx+dy)
         return distance
    calcDistance = staticmethod(calcDistance)

    
class Tour():
    def __init__(self, posX, posY, vitesse=0, damage=0, rayon=0, cooldown_time=0, on_cooldown=0, angle=0, price=50):
        #self.id = random()
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
        self.price = price # coût de la tour
        self.current_cooldown = 0

    def init_tower(self, f='main'):
        for file in os.listdir("abilities"):
            filename = os.path.splitext(file)
            # if(filename[0] = f):
            # print("fichier trouvé : ")
            # pass

    def tire(self, ennemis):
            if self.current_cooldown > 0:
                self.current_cooldown -= 1
                return None

            for ennemi in ennemis:
                distance = math.sqrt((ennemi.x - self.x)**2 + (ennemi.y - self.y)**2)
                #distance = Helper.calcDistance(self.x, self.y,ennemi.x,ennemi.y)
                
                if distance <= self.rayon:
                    self.current_cooldown = self.cooldown_time
                    return [ennemi, self]
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
    def __init__(self, largeur, hauteur, score=0, argent=500, life_joueur=100):
        self.largeur = largeur
        self.hauteur = hauteur
        
        self.default_score = score
        self.default_argent = argent
        self.default_life_joueur = life_joueur
        
        
        self.reset()
        
        ### NE PAS MERGE
        #self.life_joueur = 1#nb de vies initiales du joueur
        #self.experience_joueur = 1 #expérience initiale du joueur ???????
        #self.selectON = False
        
       
        self.path = [
            (0.0, 50.0),
            (150.0, 50.0),
            (150.0, 200.0),
            (50.0, 200.0),
            (50.0, 350.0),
            (250.0, 350.0),
            (250.0, 150.0),
            (400.0, 150.0),
            (400.0, 300.0),
            (300.0, 300.0),
            (300.0, 500.0),
            (500.0, 500.0),
            (500.0, 400.0),
            (650.0, 400.0),
            (650.0, 650.0),
            (800.0, 650.0),
        ]


        
    ### Méthode pour remettre à 0 les varaiables de jeu    
    def reset(self):
        self.player_alive = True
        self.projectiles = []
        self.tours = []
        self.ennemis = []
        self.round_count = 0
        self.score = self.default_score
        self.argent = self.default_argent
        self.life_joueur = self.default_life_joueur
        self.life_joueur = 1
        
        
        
    def placer_tour(self, x, y):
        
        # for tour in self.tours:
        #     if (x != tour.x and y != tour.y)
            
        t = Tour(x, y, 1, 2, 150, 25, False, 0, 50 )
        if t.price > self.argent:
            print("Too broke to play")
        else:
            self.argent -= t.price
            self.tours.append(t)
            print(self.argent)

    def start_round(self):
        if len(self.ennemis) > 0:
            print("Round Can not start")
        else:
            self.round_count+=1
            for x in range(self.round_count):
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
            # if projectile.type == "basic":
            #     angle = Helper.calcAngle(projectile.x,projectile.y,projectile.cible_x,projectile.cible_y)
            #     pasx = math.cos(angle) * projectile.vitesse
            #     pasy = math.sin(angle) * projectile.vitesse
                
            #     projectile.x += pasx
            #     projectile.y += pasy
                
            if projectile.type == "tracing":
                cible_x = projectile.ennemi.x
                cible_y = projectile.ennemi.y
            else:

                cible_x = projectile.cible_x
                cible_y = projectile.cible_y
                
            distance = Helper.calcDistance(projectile.x, projectile.y, cible_x, cible_y)
                
            if distance < projectile.vitesse:
                projectile.x = cible_x
                projectile.y = cible_y
            else:
                angle = Helper.calcAngle(projectile.x, projectile.y, cible_x, cible_y)
                pasx = math.cos(angle) * projectile.vitesse
                pasy = math.sin(angle) * projectile.vitesse
                projectile.x += pasx
                projectile.y += pasy
                
                
                # if projectile.cible_x >= projectile.x:
                #     projectile.x += projectile.vitesse
                # else:
                #     projectile.x -= projectile.vitesse

                # if projectile.cible_y >= projectile.y:
                #     projectile.y += projectile.vitesse
                # else:
                #     projectile.y -= projectile.vitesse

            # Pour missile qui suit
            # if projectile.type == "tracing":
                # if projectile.ennemi.x >= projectile.x:
                #     projectile.x += projectile.vitesse
                # else:
                #     projectile.x -= projectile.vitesse

                # if projectile.ennemi.y >= projectile.y:
                #     projectile.y += projectile.vitesse
                # else:
                #     projectile.y -= projectile.vitesse

            # delete le projectile si y touch et gerer la logique de damage ici et tout 
            # sort du rayon # timer
    
    def apparition_ennemis(self):
        ennemi = Ennemi(self.path[0][0], self.path[0][1], 10, 5, 1, self.path, 0)
        self.ennemis.append(ennemi)

    def deplacer_ennemis(self):
        for ennemi in self.ennemis:
            ennemi_arrive = ennemi.deplacer()
            if not ennemi_arrive:
                ennemi.life = 0
                self.victoire_ennemi() # on enleve 1 pts de vie par bebitte tant que joueur a plus de 1 points de vie sinon crash le jeu ! 
                self.ennemis.remove(ennemi)
                
    def vie_restante_ennemi(self):
        for ennemi in self.ennemis:
            tolerance = 3
            for projectile in self.projectiles:
                if abs(int(ennemi.x) - projectile.x) <= tolerance and abs(int(ennemi.y) - projectile.y) <= tolerance:
                    ennemi.life -= projectile.damage
                    self.projectiles.remove(projectile)
                    
                if ennemi.life <= 0:
                    self.mort_ennemi()
        
                
    def mort_ennemi(self):
        for ennemi in self.ennemis:
            if (ennemi.life < 0): #si l'ennemi est vaincu
                self.score += ennemi.score # le joueur augmente son score selon le nb de points donnés par l'ennemi 
                self.argent += ennemi.score
                self.ennemis.remove(ennemi)
        
    # def selection_tour(self):
    #     for tour in self.tours:
    #         if (tour == self.tours[i])         
                
    # def acheter_tour(self):
        
    #         if (self.score >= self.tours[self.selection_tour].price): # si le joueur peut acheter la tour avec son pointage, on soustrait du solde le montant de la tour 
    #             self.score -= self.tours[self.selection_tour].price
            
    #         if (self.score < self.tours[self.selection_tour].price): # si le joueur n'a pas assez de fonds, un message avertit le joueur qu'il ne peut procéder à l'achat 
    #             print("Pas assez de fonds pour l'achat de cette tour")
    
    def victoire_ennemi(self):
        self.life_joueur -=1 
        if self.life_joueur <= 0:
            print("game terminer on ferme le loop ici") ## ici faut crash le jeu
            self.player_alive = False
            #quit()
            # ici vue et ferme loop
                 
                    
            

class Ennemi():  # chemin
    def __init__(self, x, y, taille, life, vitesse, path, index_path=0, score=15):
        self.x = x
        self.y = y
        self.taille = taille
        self.vitesse = vitesse
        #### Ne pas merge ceci
        self.life = 100000000000
        ### 
        self.path = path
        self.index_path = index_path
        self.score = score

    def deplacer(self):
        try:
            destination_X = self.path[self.index_path + 1][0]
            destination_Y = self.path[self.index_path + 1][1]

            if self.x != destination_X or self.y != destination_Y:
                
                # if self.x > destination_X and self.y > destination_Y:
                #     self.x -= self.vitesse * 0.70
                #     self.y -= self.vitesse * 0.70
                    
                # if self.x > destination_X and self.y < destination_Y:
                #     self.x -= self.vitesse * 0.70
                #     self.y += self.vitesse * 0.70
                    
                # if self.x < destination_X and self.y < destination_Y:
                #     self.x += self.vitesse * 0.70
                #     self.y += self.vitesse * 0.70
                    
                # if self.x < destination_X and self.y > destination_Y:
                #     self.x += self.vitesse * 0.70
                #     self.y -= self.vitesse * 0.70

                if self.x < destination_X:
                    self.x += self.vitesse  # déplace droit
                elif self.x > destination_X:
                    self.x -= self.vitesse  # déplace gauche

                if self.y < destination_Y:
                    self.y += self.vitesse  # déplace bas
                elif self.y > destination_Y:
                    self.y -= self.vitesse  # déplace haut

            else:
                self.index_path += 1

        except:
            return False

        return True
    
            
        
    
    
