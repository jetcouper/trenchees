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
        self.x = posX
        self.y = posY
        self.vitesse = vitesse
        self.damage = damage
        self.rayon = rayon
        self.cooldown_time = cooldown_time  
        self.on_cooldown = on_cooldown  
        self.angle = angle
        self.abilities = {}
        self.TTL = rayon/vitesse if vitesse != 0 else 0
        self.price = price
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

    def upgrade(self, upgrade_type):
        if upgrade_type == "speed":
            self.vitesse += 1
            self.TTL = self.rayon/self.vitesse if self.vitesse != 0 else 0
            print("Speed upgrade effectué.")
        elif upgrade_type == "range":
            self.rayon += 20
            print("Range upgrade effectué.")
            self.TTL = self.rayon/self.vitesse if self.vitesse != 0 else 0
        elif upgrade_type == "damage":
            self.damage += 1
            self.TTL = self.rayon/self.vitesse if self.vitesse != 0 else 0
            print("Damage upgrade effectué.")
        elif upgrade_type == "cooldown":
            # Réduction du temps de cooldown de 5% (multiplication par 0.95)
            self.cooldown_time *= 0.95
            print("Cooldown réduit de 5%")
        else:
            print("Type d'upgrade invalide.")

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
            (0, -20),
            (75, -20),
            (75, 225),
            (575, 225),
            (575, 200),
            (725, 200),
            (725, 615),
            (150, 615),
            (150, 800)
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
        
    def placer_tour(self, x, y):
        
        # for tour in self.tours:
        #     if (x != tour.x and y != tour.y)
            
        t = Tour(x, y, 5, 2, 150, 25, False, 0, 50 )
        if t.price > self.argent:
            print("Too broke to play")
        else:
            self.argent -= t.price
            self.tours.append(t)
            print(self.argent)
            
    def vendre_tour(self, x, y):
        seuil = 20  
        for tour in self.tours:
            if abs(tour.x - x) < seuil and abs(tour.y - y) < seuil:
                self.tours.remove(tour)
                remboursement = int(tour.price * 0.75)
                self.argent += remboursement
                print(f"Tour vendue pour {remboursement} !")
                return
        print("AAAAAAAAAAAAAAAAAAAAAAAH")
        
    def upgrade_tour(self, x, y, upgrade_type):
        seuil = 20  # seuil de détection du clic sur la tour
        for tour in self.tours:
            if abs(tour.x - x) < seuil and abs(tour.y - y) < seuil:
                if upgrade_type == "speed":
                    cost = 30
                elif upgrade_type == "range":
                    cost = 40
                elif upgrade_type == "damage":
                    cost = 50
                elif upgrade_type == "cooldown":
                    cost = 40
                else:
                    print("Type d'upgrade invalide.")
                    return

                if self.argent >= cost:
                    self.argent -= cost
                    tour.upgrade(upgrade_type)
                    print(f"Tour améliorée ({upgrade_type}). Coût: {cost} - Argent restant: {self.argent}")
                    return
                else:
                    print("Argent insuffisant pour cet upgrade.")
                    return
        print("Aucune tour trouvée à cet emplacement pour upgrade.")


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
                
                
              

            # delete le projectile si y touch et gerer la logique de damage ici et tout 
            # sort du rayon # timer
    
    def apparition_ennemis(self, type):
        
        if type == None:
            ennemi = Ennemi(self.path[0][0], self.path[0][1])
        
        elif type == "glace":
            ennemi = Ennemi_glace(self.path[0][0], self.path[0][1])
        
        elif type == "feu":
            ennemi = Ennemi_feu(self.path[0][0], self.path[0][1])
        
        elif type == "gaz":
            ennemi = Ennemi_gaz(self.path[0][0], self.path[0][1])
        
        elif type == "avion":
            ennemi = Ennemi_avion(self.path[0][0], self.path[0][1])
        
        elif type == "tank":
            ennemi = Ennemi_tank(self.path[0][0], self.path[0][1])
        
        # else:
        #     raise ValueError(f".Type d'ennemi inconnu: {type}")
            
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
                 
                    
            

class Ennemi():
    def __init__(self, x, y, taille, type, life, vitesse, path, index_path=0, score=15):
        self.x = x
        self.y = y
        self.taille = taille
        self.life = life
        self.vitesse = vitesse
        self.path = path
        self.index_path = index_path
        self.score = score
        self.angle = 0
        self.type = type



    def deplacer(self):
        try:
            if self.index_path >= (len(self.path) - 1):
                return False

            destination_X = self.path[self.index_path + 1][0]
            destination_Y = self.path[self.index_path + 1][1]
            distance = Helper.calcDistance(self.x, self.y, destination_X, destination_Y)
            
            # Compute the angle toward the destination
            self.angle = Helper.calcAngle(self.x, self.y, destination_X, destination_Y)
            
            if distance < self.vitesse:
                # Snap enemy to destination and update path index
                self.x = destination_X
                self.y = destination_Y
                self.index_path += 1
                
                # Optionally, update angle for the next segment if available:
                if self.index_path < len(self.path) - 1:
                    next_destX = self.path[self.index_path + 1][0]
                    next_destY = self.path[self.index_path + 1][1]
                    self.angle = Helper.calcAngle(self.x, self.y, next_destX, next_destY)
                print("change_direction")
            else:
                # Increment position along the direction
                posx = math.cos(self.angle) * self.vitesse
                posy = math.sin(self.angle) * self.vitesse
                self.x += posx
                self.y += posy

            return True

        except Exception as e:
            print(f"erreur: {e}")
            return False

        
        
        
class Ennemi_glace(Ennemi): #ralentit la vitesse de projectile à proximité, donc diminue leur force d'impact de tirs? 
    def __init__(self):
       
        super().__init__(self, type="glace", life=3, vitesse=2, score=20)           
    
class Ennemi_feu(Ennemi): #est immunisé contre les attaques de la tour de glace
    def __init__(self):
       
        super.__init__(self, type="feu", life=4, vitesse=3, score=25)           
    

class Ennemi_gaz(Ennemi): #diminue la visibilité du joueur sur la carte de jeu
    def __init__(self):
      
        super.__init__(self, type="gaz", life=2, vitesse=1, score=18)           
    
class Ennemi_avion(Ennemi): #déplacement logique sur la carte de jeu
    def __init__(self):
       
        super.__init__(self, type="avion", life=5, vitesse=5, score=30)           
    
    
class Ennemi_tank(Ennemi): #déplacement logique sur la surface de jeu
    def __init__(self):
       
        super.__init__(self, type="tank", life=7, vitesse=2, score=35)           
    
