import math
import os
import json
import random
from PIL import Image, ImageTk

import threading
import time



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
            
    #antoine

    def tire(self, ennemis):
            if self.current_cooldown > 0:
                self.current_cooldown -= 1
                return None

            for ennemi in ennemis:
                distance = math.sqrt((ennemi.x - self.x)**2 + (ennemi.y - self.y)**2)
                
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
            self.cooldown_time *= 0.90
            print("Cooldown réduit de 10%")
        else:
            print("Type d'upgrade ompissbbbble")
            
            
# Dans modele.py, après la définition de la classe Tour

class TourRapide(Tour):
    def __init__(self, posX, posY):
        super().__init__(posX, posY, vitesse=10, damage=1, rayon=120, cooldown_time=5, on_cooldown=False, angle=0, price=50)
        self.image_path = "assets/tour1.png"
        self.projectile_image_path = "assets/fire-explosion.png"
        img = Image.open(self.projectile_image_path)
        img = img.resize((10, 10))
        self.projectile_photo = ImageTk.PhotoImage(img)

    def tire(self, ennemis):
        return super().tire(ennemis)


class TourRange(Tour):
    def __init__(self, posX, posY):
        super().__init__(posX, posY, vitesse=5, damage=5, rayon=180, cooldown_time=20, on_cooldown=False, angle=0, price=80)
        self.image_path = "assets/tour2.png"
        self.projectile_image_path = "assets/fire-explosion.png"
        img = Image.open(self.projectile_image_path)
        img = img.resize((10, 10))
        self.projectile_photo = ImageTk.PhotoImage(img)

    def tire(self, ennemis):
        return super().tire(ennemis)


class TourDamage(Tour):
    def __init__(self, posX, posY):
        super().__init__(posX, posY, vitesse=4, damage=8, rayon=150, cooldown_time=25, on_cooldown=False, angle=0, price=100)
        self.image_path = "assets/tour3.png"
        self.projectile_image_path = "assets/fire-explosion.png"
        img = Image.open(self.projectile_image_path)
        img = img.resize((10, 10))
        self.projectile_photo = ImageTk.PhotoImage(img)

    def tire(self, ennemis):
        return super().tire(ennemis)


class Tour4(Tour):
    def __init__(self, posX, posY):
        super().__init__(posX, posY, vitesse=12, damage=2, rayon=140, cooldown_time=6, on_cooldown=False, angle=0, price=60)
        self.image_path = "assets/tour4.png"
        self.projectile_image_path = "assets/fire-explosion.png"
        img = Image.open(self.projectile_image_path)
        img = img.resize((10, 10))
        self.projectile_photo = ImageTk.PhotoImage(img)

    def tire(self, ennemis):
        return super().tire(ennemis)


class TourProf(Tour):
    def __init__(self, posX, posY):
        super().__init__(posX, posY, vitesse=3, damage=7, rayon=200, cooldown_time=30, on_cooldown=False, angle=0, price=110)
        self.image_path = "assets/TOURULTIMEWOW.png"
        self.projectile_image_path = "assets/fire-explosion.png"
        img = Image.open(self.projectile_image_path)
        img = img.resize((10, 10))
        self.projectile_photo = ImageTk.PhotoImage(img)

    def tire(self, ennemis):
        return super().tire(ennemis)


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
        self.type = "tracing"
        self.TTL = tour.TTL
        
        try:
            self.tk_image = tour.projectile_photo
        except Exception as e:
            print("OULALA:", e)
            self.tk_image = None


class Partie():
    def __init__(self, largeur, hauteur, score=0, argent=500, life_joueur=100):
        self.largeur = largeur
        self.hauteur = hauteur
        
        self.default_score = score
        self.default_argent = argent
        self.default_life_joueur = life_joueur
        self.default_life_joueur = 1
        self.reset()
        self.countEnnemie = 0
        self.liste_ennemis = ["glace", "feu", "gaz", "avion", "tank" ]
        self.difficulte = 1
    
       
        self.path = [
            (75, -20),
            (75, 225),
            (575, 225),
            (575, 200),
            (725, 200),
            (725, 615),
            (150, 615),
            (150, 800)
        ]
        
        self.path2 = [
            (75, -20),
            (75, 225),
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
        self.nb_ennemis = 0
        self.score = self.default_score
        self.argent = self.default_argent
        self.life_joueur = self.default_life_joueur
        
    def placer_tour(self, x, y, type_tour="machinegun"):
        
        towers = {
            "machinegun": TourRapide,
            "mortar": TourRange,
            "antitank": TourDamage,
            "antiair": Tour4,
            "artillery": TourProf
        }
            
        if type_tour in towers:
            t = towers[type_tour](x, y)
        else:
            t = Tour(x, y, 5, 2, 150, 25, False, 0, 50)
        if t.price > self.argent:
            print("Pas assez d'argent")
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
                    print("Type d'upgrade pas possible")
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
        rnd_delay = 0

        if len(self.ennemis) > 0:
            print("Round Can not start")
            return
        else:
            #self.round_count+=1
            self.nb_ennemis = self.calculer_nbEnnemis()
            self.nb_ennemis = self.nb_ennemis * self.difficulte
            self.countEnnemie = self.nb_ennemis
            print("nb ennemis : " + str(self.nb_ennemis))
            
            thread = threading.Thread(target=self.ajout_ennemi)
            thread.daemon = True  # Permet au thread de se terminer quand le programme principal se termine
            thread.start()    
               
   
    def calculer_nbEnnemis(self):
        
        self.round_count+=1
        
        return int(3 * math.sqrt(self.round_count * 2))

    def calculer_tauxVie(self, bonus):

        return math.floor(5 * math.sqrt(self.round_count * 2) + bonus)
    # Antoine à reçu la malediction             
    
    
    # Monsieur le professeur ici est un test afin de verifier si vous liser reelement le code. Si oui veuiller me dire BONJOUR ANTOINE au prochain cours. -antoine



    def ajout_ennemi(self):
        
        for x in range(self.nb_ennemis):

            if len(self.ennemis) > 0:
                rnd_delay = random.random() * (x + 4)
                time.sleep(rnd_delay)
                # self.apparition_ennemis("glace")
                # self.apparition_ennemis("feu")
                # self.apparition_ennemis("gaz")
                # self.apparition_ennemis("avion")
                
                
            # choix = random.choice(self.liste_ennemis) 
            # index = self.liste_ennemis.index(choix) #indice de la liste ennemi pour retrouver le % 
            # print(choix)
            # print(index)
            
            if self.round_count == 1 and self.round_count < 10:
                
                probability1 = [0.5, 0.5, 0.3, 0, 0]
                current_ennemi = random.choices(self.liste_ennemis, weights = probability1, k = 1)[0]
            
            elif self.round_count > 10 and self.round_count < 20:
                
                probability2 = [0.3, 0.5, 0.4, 0, 0.01]
                current_ennemi = random.choices(self.liste_ennemis, weights = probability2, k = 1)[0]
                
            elif self.round_count > 20 and self.round_count < 30:    
                
                probability3 = [0.2, 0.4, 0.5, 0.1, 0.2]
                current_ennemi = random.choices(self.liste_ennemis, weights = probability3, k = 1)[0]
                
            elif self.round_count > 30 and self.round_count < 40:   
                probability4 = [0.1, 0.3, 0.4, 0.3, 0.3]
                current_ennemi = random.choices(self.liste_ennemis, weights = probability4, k = 1)[0]
            else:
                current_ennemi = random.choice(self.liste_ennemis)
                
            self.apparition_ennemis(current_ennemi)
              
            print(current_ennemi)






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
                
            
    
    def apparition_ennemis(self, type):
        
        # if type == None:
        #     ennemi = Ennemi(self.path[0][0], self.path[0][1])
        
        path_choisi = random.choice([self.path, self.path2])
        
        if type == "glace":
            ennemi = Ennemi_glace(self.path[0][0], path_choisi[0][1], path=path_choisi)
            ennemi.set_life(self.calculer_tauxVie(3))  
        elif type == "feu":
            ennemi = Ennemi_feu(self.path[0][0], path_choisi[0][1], path=path_choisi)
            ennemi.set_life(self.calculer_tauxVie(4))
        elif type == "gaz":
            ennemi = Ennemi_gaz(self.path[0][0], path_choisi[0][1], path=path_choisi)
            ennemi.set_life(self.calculer_tauxVie(2))
        elif type == "avion":
            ennemi = Ennemi_avion(self.path[0][0], path_choisi[0][1], path=path_choisi)
            ennemi.set_life(self.calculer_tauxVie(5))
        elif type == "tank":
            ennemi = Ennemi_tank(self.path[0][0], path_choisi[0][1], path=path_choisi)
            ennemi.set_life(self.calculer_tauxVie(7))

        else:
            return 
        # else:
        #     raise ValueError(f".Type d'ennemi inconnu: {type}")

        # ennemi.life = 2*math.sqrt(self.round_count)+3

        # int(ennemi.life + self.calculer_tauxVie()) #ajuste le taux de vie
        #print("taux vie : "+str(ennemi.life))
        self.ennemis.append(ennemi)
        

    def deplacer_ennemis(self):
        for ennemi in self.ennemis:
            ennemi_arrive = ennemi.deplacer()
            if not ennemi_arrive:
                ennemi.life = 0
                self.victoire_ennemi() # on enleve 1 pts de vie par bebitte tant que joueur a plus de 1 points de vie sinon crash le jeu ! 
                self.ennemis.remove(ennemi)
                self.countEnnemie = self.countEnnemie - 1
                # Je suis Alexandre :) -antoine D.
                
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
                self.countEnnemie = self.countEnnemie -1
    
    def victoire_ennemi(self):
        self.life_joueur -=1 
        if self.life_joueur <= 0:

            self.player_alive = False
            #quit()
            # ici vue et ferme loop
                 
                    
            

class Ennemi():
    def __init__(self, x, y, taille=1, type="normal", life=1, vitesse=1, path=0, index_path=0, score=15):
        self.x = x
        self.y = y
        self.taille = taille
        self.life = life
        self.max_life = self.life
        self.vitesse = vitesse
        self.path = path
        self.index_path = index_path
        self.score = score
        self.angle = 0
        self.type = type

    def set_life(self, life):
        self.life = life
        self.max_life = life

    def deplacer(self):
        try:
            if self.index_path >= (len(self.path) - 1):
                return False

            destination_X = self.path[self.index_path + 1][0]
            destination_Y = self.path[self.index_path + 1][1]
            distance = Helper.calcDistance(self.x, self.y, destination_X, destination_Y)
            

            self.angle = Helper.calcAngle(self.x, self.y, destination_X, destination_Y)
            
            if distance < self.vitesse:

                self.x = destination_X
                self.y = destination_Y
                self.index_path += 1
                

                if self.index_path < len(self.path) - 1:
                    next_destX = self.path[self.index_path + 1][0]
                    next_destY = self.path[self.index_path + 1][1]
                    self.angle = Helper.calcAngle(self.x, self.y, next_destX, next_destY)
                print("change_direction")
            else:

                posx = math.cos(self.angle) * self.vitesse
                posy = math.sin(self.angle) * self.vitesse
                self.x += posx
                self.y += posy

            return True

        except Exception as e:
            print(f"erreur: {e}")
            return False
        
class Ennemi_glace(Ennemi):
    def __init__(self, x, y, path):
        super().__init__(x, y, path=path, type="glace", life=3, vitesse=2, score=20)
        self.link_img = "assets/char_silver1.png"
        base_image = Image.open(self.link_img)
        base_image = base_image.resize((75, 50))
        self.image_base = base_image
        self.tk_image = ImageTk.PhotoImage(self.image_base)

    
class Ennemi_feu(Ennemi): #est immunisé contre les attaques de la tour de glace
    def __init__(self,x,y, path):
       
        super().__init__(x, y, path=path, type="feu", life=4, vitesse=3, score=25)
        self.link_img = "assets/tank_vert1.png"
        base_image = Image.open(self.link_img)
        base_image = base_image.resize((75, 50))  
        self.image_base = base_image
        self.tk_image = ImageTk.PhotoImage(self.image_base)
        # self.ennemi_photo = ImageTk.PhotoImage(image)             
    

class Ennemi_gaz(Ennemi): #diminue la visibilité du joueur sur la carte de jeu
    def __init__(self,x,y, path):
      
        super().__init__(x, y, path=path, type="gaz", life=2, vitesse=1, score=18)           
        self.link_img = "assets/char_silver1.png"
        base_image = Image.open(self.link_img)
        base_image = base_image.resize((75, 50))  
        self.image_base = base_image
        self.tk_image = ImageTk.PhotoImage(self.image_base) 
        # self.ennemi_photo = ImageTk.PhotoImage(image)   
    
class Ennemi_avion(Ennemi): #déplacement logique sur la carte de jeu
    def __init__(self,x,y, path):
       
        super().__init__(x, y, path=path, type="avion", life=5, vitesse=5, score=30) 
        self.link_img = "assets/avion.png"
        base_image = Image.open(self.link_img)
        base_image = base_image.resize((75, 50))   
        self.image_base = base_image
        self.tk_image = ImageTk.PhotoImage(self.image_base) 
        # self.ennemi_photo = ImageTk.PhotoImage(image)            
    
    
class Ennemi_tank(Ennemi): #déplacement logique sur la surface de jeu
    def __init__(self,x,y, path):
       
        super().__init__(x, y, path=path, type="tank", life=7, vitesse=2, score=35)  
        self.link_img = "assets/tank.png"
        base_image = Image.open(self.link_img)
        base_image = base_image.resize((75, 50)) 
        self.image_base = base_image
        self.tk_image = ImageTk.PhotoImage(self.image_base)
        # self.ennemi_photo = ImageTk.PhotoImage(image)           
    
# Antoine