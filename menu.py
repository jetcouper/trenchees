import tkinter as Tk
import math as M
from PIL import ImageTk,Image




class Menu():
    def __init__(self, controleur,root, largeur, hauteur):
        self.controleur = controleur
        self.root = root
        self.root.title("Tower Defense")
        self.root.geometry(f"{largeur}x{hauteur}")
        self.root.minsize(largeur, hauteur)
        ico = Image.open("assets/Machine_Gun.png")
        photo = ImageTk.PhotoImage(ico)
        self.root.wm_iconphoto(False, photo)
        # self.controleur = controleur
        # self.modele = modele
        self.largeur = largeur
        self.hauteur = hauteur
        
        # Configuration initiale
        self.create_mainFrame()
        self.create_menu_frame()


        
        
        
        
        self.node_image = [
            ImageTk.PhotoImage(Image.open(".\\assets\\icons\\play.png").resize((70,70))), #Image de Play
            ImageTk.PhotoImage(Image.open(".\\assets\\icons\\profil.png").resize((70,70))), #Image de profil
            ImageTk.PhotoImage(Image.open(".\\assets\\icons\\parameters.png").resize((120,120))), #Image de parametres
            ImageTk.PhotoImage(Image.open(".\\assets\\icons\\map.png").resize((70,70))), #Image de Map Maker
            ImageTk.PhotoImage(Image.open(".\\assets\\icons\\leave.png").resize((60,60))), #Image de Quitter
            ImageTk.PhotoImage(Image.open(".\\assets\\icons\\achievements.png").resize((70,70))), #Image de Achievement
            ImageTk.PhotoImage(Image.open(".\\assets\\icons\\credits.png").resize((80,80))), #Image de Crédits
            ImageTk.PhotoImage(Image.open(".\\assets\\icons\\tutorial.png").resize((80,80))), #Image de Tutorial
        ]
        
        
        
        self.node_types = [{"text": "Play !", "int": 0},
                           {"text": "Profil", "int": 1},
                           {"text": "Parameters", "int": 2},
                           {"text": "Map\nMaker", "int": 3},
                           {"text": "Exit", "int": 4},
                           {"text": "Achievements", "int": 5},
                           {"text": "Credits", "int": 6},
                           {"text": "Tutorial", "int": 7}]

        # Positions angulaires (en radians, partant de -π/2 pour le Nord, sens horaire)
        self.positions = [
            -M.pi/2,        # N
            -M.pi/4,        # NE
            0,              # E
            M.pi/4,         # SE
            M.pi/2,         # S
            3*M.pi/4,       # SW
            M.pi,           # W
            -3*M.pi/4       # NW
        ]
        
        
        
        # Variables d'animation
        self.current_rotation = 0  # Angle de rotation actuel
        self.is_animating = False  # Animation en cours?
        self.node_objects = []     # Liste des objets nœuds et textes
        self.target_position = None # Position cible pour la rotation
        
        # Créer le label central
        self.create_center_label()
        
        # Dessiner les nœuds
        self.draw_nodes()
        
    # Dans la classe Menu

    def afficher(self):
        # Afficher le frame principal
        self.main_frame.pack(expand=True, fill="both")
        self.menu_frame.pack(expand=True)
        self.menu_frame.pack_propagate(False)
        
    def cacher(self):
        # Cacher le frame principal
        self.main_frame.pack_forget()
        self.menu_frame.pack_forget()
        
    
    def create_mainFrame(self):
        self.main_frame = Tk.Frame(self.root, width=self.largeur, height=self.hauteur, bg="gray")
        self.main_frame.pack(expand=True, fill="both")
    
    def create_menu_frame(self):
        self.menu_frame = Tk.Canvas(self.main_frame, bg="green", width=self.largeur, height=self.hauteur, relief="flat", bd=0, highlightthickness=0)
        self.menu_frame.pack(expand=True)
        self.menu_frame.pack_propagate(False)
    
    def create_center_label(self):
        """Crée un label au centre indiquant le type de nœud sélectionné."""
        center_x = self.largeur / 2
        center_y = self.hauteur / 2
        
        # Cercle de fond
        self.center_circle = self.menu_frame.create_oval(
            center_x - 70, center_y - 70, 
            center_x + 70, center_y + 70, 
            fill="#333333",
            outline="black",
            width=2
        )
        
        # Label du type de nœud
        self.center_text = self.menu_frame.create_text(
            center_x, center_y,
            text=self.node_types[0]["text"],  # Utilise la clé "text" du dictionnaire node_types
            fill="white",
            font=("Arial", 14, "bold")
        )

        self.menu_frame.tag_bind(self.center_text, "<Button-1>", lambda event : self.click_center_label())
        self.menu_frame.tag_bind(self.center_circle, "<Button-1>", lambda event: self.click_center_label())

    
    def update_center_label(self):
        """Met à jour le texte du label central avec le type du nœud en position Nord."""
        # Trouver l'indice du nœud en position Nord
        north_index = 0  # Par défaut, le premier nœud est au Nord
        
        # Mettre à jour le texte
        self.menu_frame.itemconfig(self.center_text, text=self.node_types[north_index]["text"])

        
    def click_center_label(self):
        """Gérer le clic sur le label central."""
        
        match self.node_types[0]["int"]:
            case 0:
                print("Lancement du jeu !")
                self.controleur.clic_start()
                # self.root.destroy()
            case 1:
                print("Accéder au profil !")
            case 2:
                print("Accéder aux paramètres !")
                self.controleur.clic_parametre()
            case 3:
                print("Accéder au Map Maker !")
            case 4:
                print("Quitter le jeu !")
                self.validation_exit()
                # self.root.quit()
            case 5:
                print("Accéder aux réalisations !")
            case 6:
                print("Accéder aux crédits !")
                self.controleur.clic_credit()
            case 7:
                print("Accéder au tutoriel !")
                self.controleur.clic_tutoriel()
                
                
    def validation_exit(self):
        popup = Tk.Frame(self.main_frame, bg="gray", bd=2, relief="raised")
        Tk.Label(popup, text="Êtes vous sûr de vouloir quitter", font=("Arial", 14), bg="gray").pack(pady=10)
        Tk.Button(popup, text="NON", command= self.validation_exit2 ).pack(pady=10)
        Tk.Button(popup,text= "OUI",command= self.on_exit).pack(pady=10)
        popup_window = self.menu_frame.create_window(self.largeur/2, self.hauteur/2, window=popup, tags="popup")
        
    def validation_exit2(self):
        self.menu_frame.delete("popup")
        
    def on_exit(self):
        self.controleur.root.quit()
        
    
            
        
    
    def clear_nodes(self):
        """Efface tous les nœuds et textes existants."""
        
        
        for text_id in self.node_objects:
            # self.menu_frame.delete(node_id)
            self.menu_frame.delete(text_id)
        self.node_objects = []
    
    def draw_nodes(self):
        # Nettoyer tous les nœuds existants
        self.clear_nodes()
        
        center_x = self.largeur / 2
        center_y = self.hauteur / 2
        radius = 200    # Distance du centre
        node_size = 40  # Taille du nœud
        
        # Créer 8 nœuds avec leurs positions et étiquettes
        for i in range(8):
            # Position angulaire avec la rotation actuelle
            angle = self.positions[i] + self.current_rotation
            
            # Calculer les coordonnées
            x = center_x + radius * M.cos(angle)
            y = center_y + radius * M.sin(angle)
            
            
            text_id = self.menu_frame.create_image(
                x,y,
                image=self.node_image[i]
            )
            
            
            
            # Associer un gestionnaire d'événements au clic
            self.menu_frame.tag_bind(text_id, "<Button-1>", lambda event, idx=i: self.rotate_to_north(idx))
            
            # Stocker le nœud et son texte
            # self.node_objects.append((node_id, text_id))
            self.node_objects.append((text_id))
    
    def rotate_to_north(self, node_index):
        """Initie la rotation pour amener le nœud cliqué à la position Nord."""
        # if self.is_animating or self.rotation_active:
        #     return  # Éviter les clics multiples pendant une animation
        
        # Si le nœud est déjà en position Nord, rien à faire
        if node_index == 0:
            return
        
        # Enregistrer la position cible
        self.target_position = node_index
        
        # Calculer l'angle de rotation nécessaire pour mettre ce nœud au Nord
        target_angle = self.positions[node_index] + self.current_rotation
        
        # L'angle à tourner est l'opposé de la position angulaire du nœud cible
        # puisque nous voulons le ramener à -π/2 (position Nord)
        angle_to_rotate = -target_angle - M.pi/2
        
        # Normaliser l'angle entre 0 et 2π
        while angle_to_rotate < 0:
            angle_to_rotate += 2 * M.pi
        while angle_to_rotate >= 2 * M.pi:
            angle_to_rotate -= 2 * M.pi
        
        # Vérifier si c'est plus court de tourner dans l'autre sens
        if angle_to_rotate > M.pi:
            angle_to_rotate -= 2 * M.pi
        
        # Démarrer l'animation avec l'angle calculé
        self.start_rotation_animation(angle_to_rotate)
    
    def start_rotation_animation(self, total_angle):
        """Démarre l'animation de rotation avec un angle total donné."""
        self.is_animating = True
        self.total_angle_to_rotate = total_angle
        self.remaining_angle = abs(total_angle)
        self.rotate_direction = 1 if total_angle > 0 else -1
        self.animate_step()
    
    def animate_step(self):
        """Effectue une étape de l'animation de rotation."""
        if not self.is_animating:
            return
        
        # Vitesse de rotation (en radians par étape)
        step_size = 0.15
        
        # Si on est presque à la fin, ajuster précisément
        if self.remaining_angle < step_size:
            actual_step = self.remaining_angle * self.rotate_direction
            self.current_rotation += actual_step
            self.remaining_angle = 0
        else:
            # Sinon, faire un pas normal
            actual_step = step_size * self.rotate_direction
            self.current_rotation += actual_step
            self.remaining_angle -= step_size
        
        # Normaliser la rotation actuelle
        self.current_rotation = self.current_rotation % (2 * M.pi)
        
        # Redessiner les nœuds
        self.draw_nodes()
        
        # Continuer ou terminer
        if self.remaining_angle > 0:
            self.root.after(30, self.animate_step)
        else:
            self.finish_animation()
    
    def finish_animation(self):
        """Finalise l'animation en ajustant les tableaux de couleurs et positions."""
        self.is_animating = False
        
        if self.target_position is not None:
            # Déplacer la couleur et le type du nœud cliqué à la position Nord
            target = self.target_position
            
            self.node_types = self.node_types[target:] + self.node_types[:target]
            self.node_image = self.node_image[target:] + self.node_image[:target]
            self.target_position = None
        
        # Réinitialiser l'angle de rotation
        self.current_rotation = 0
        
        # Mettre à jour le label central
        self.update_center_label()
        
        # Redessiner les nœuds
        self.draw_nodes()
    
    

