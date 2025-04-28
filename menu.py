import tkinter as Tk
import math as M

class controleur():
    def __init__(self):
        self.root = Tk.Tk()
        self.root.title("Jeu de la vie")
        self.modele = Modele(800, 600)
        self.vue = Vue(self, self.modele, self.modele.largeur, self.modele.hauteur, self.root)
        self.root.mainloop()

class Vue():
    def __init__(self, controleur, modele, largeur, hauteur, root):
        self.root = root
        self.root.geometry(f"{largeur}x{hauteur}")
        self.root.minsize(largeur, hauteur)
        self.controleur = controleur
        self.modele = modele
        self.largeur = largeur
        self.hauteur = hauteur
        
        # Configuration initiale
        self.create_mainFrame()
        self.create_menu_frame()
        
        # Couleurs des nœuds
        self.node_colors = [
            "#FF0000",  # Rouge (N)
            "#FF7F00",  # Orange (NE)
            "#FFFF00",  # Jaune (E)
            "#00FF00",  # Vert (SE)
            "#0000FF",  # Bleu (S)
            "#4B0082",  # Indigo (SW)
            "#9400D3",  # Violet (W)
            "#FF1493"   # Rose (NW)
        ]
        
        # Types/noms des nœuds (association avec les couleurs)
        self.node_types = ["Créer", "Modifier", "Supprimer", "Déplacer", "Copier", "Coller", "Option", "Aide"]
        
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
        
        # Noms des positions
        self.position_names = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
        
        # Variables d'animation
        self.current_rotation = 0  # Angle de rotation actuel
        self.is_animating = False  # Animation en cours?
        self.node_objects = []     # Liste des objets nœuds et textes
        self.target_position = None # Position cible pour la rotation
        
        # Créer le label central
        self.create_center_label()
        
        # Dessiner les nœuds
        self.draw_nodes()
        
        # Bouton rotation continue
        self.rotation_active = False
        self.toggle_button = Tk.Button(self.main_frame, text="Rotation Continue", command=self.toggle_continuous_rotation)
        self.toggle_button.pack(side=Tk.BOTTOM, pady=10)
    
    def create_mainFrame(self):
        self.main_frame = Tk.Frame(self.root, bg="blue")
        self.main_frame.pack(expand=True, fill="both")
    
    def create_menu_frame(self):
        self.menu_frame = Tk.Canvas(self.main_frame, bg="green", width=self.largeur, height=self.hauteur, relief="flat")
        self.menu_frame.pack(expand=True)
        self.menu_frame.pack_propagate(False)
    
    def create_center_label(self):
        """Crée un label au centre indiquant le type de nœud sélectionné."""
        center_x = self.largeur / 2
        center_y = self.hauteur / 2
        
        # Cercle de fond
        self.center_circle = self.menu_frame.create_oval(
            center_x - 50, center_y - 50, 
            center_x + 50, center_y + 50, 
            fill="#333333",
            outline="white",
            width=2
        )
        
        # Label du type de nœud
        self.center_text = self.menu_frame.create_text(
            center_x, center_y,
            text=self.node_types[0],  # Type du nœud en position Nord
            fill="white",
            font=("Arial", 14, "bold")
        )
    
    def update_center_label(self):
        """Met à jour le texte du label central avec le type du nœud en position Nord."""
        # Trouver l'indice du nœud en position Nord
        north_index = 0  # Par défaut, le premier nœud est au Nord
        
        # Mettre à jour le texte
        self.menu_frame.itemconfig(self.center_text, text=self.node_types[north_index])
    
    def clear_nodes(self):
        """Efface tous les nœuds et textes existants."""
        for node_id, text_id in self.node_objects:
            self.menu_frame.delete(node_id)
            self.menu_frame.delete(text_id)
        self.node_objects = []
    
    def draw_nodes(self):
        # Nettoyer tous les nœuds existants
        self.clear_nodes()
        
        center_x = self.largeur / 2
        center_y = self.hauteur / 2
        radius = 200    # Distance du centre
        node_size = 25  # Taille du nœud
        
        # Créer 8 nœuds avec leurs positions et étiquettes
        for i in range(8):
            # Position angulaire avec la rotation actuelle
            angle = self.positions[i] + self.current_rotation
            
            # Calculer les coordonnées
            x = center_x + radius * M.cos(angle)
            y = center_y + radius * M.sin(angle)
            
            # Créer le nœud
            node_id = self.menu_frame.create_oval(
                x - node_size, y - node_size,
                x + node_size, y + node_size,
                fill=self.node_colors[i],
                outline="black",
                width=2
            )
            
            # Ajouter l'étiquette de position
            text_id = self.menu_frame.create_text(
                x, y,
                text=self.position_names[i],
                fill="white",
                font=("Arial", 12, "bold")
            )
            
            # Associer un gestionnaire d'événements au clic
            self.menu_frame.tag_bind(node_id, "<Button-1>", lambda event, idx=i: self.rotate_to_north(idx))
            
            # Stocker le nœud et son texte
            self.node_objects.append((node_id, text_id))
    
    def rotate_to_north(self, node_index):
        """Initie la rotation pour amener le nœud cliqué à la position Nord."""
        if self.is_animating or self.rotation_active:
            return  # Éviter les clics multiples pendant une animation
        
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
        step_size = 0.05
        
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
            self.node_colors = self.node_colors[target:] + self.node_colors[:target]
            self.node_types = self.node_types[target:] + self.node_types[:target]
            self.target_position = None
        
        # Réinitialiser l'angle de rotation
        self.current_rotation = 0
        
        # Mettre à jour le label central
        self.update_center_label()
        
        # Redessiner les nœuds
        self.draw_nodes()
    
    def toggle_continuous_rotation(self):
        """Active/désactive la rotation continue."""
        self.rotation_active = not self.rotation_active
        
        if self.rotation_active:
            self.toggle_button.config(text="Arrêter Rotation")
            self.continuous_rotation()
        else:
            self.toggle_button.config(text="Rotation Continue")
    
    def continuous_rotation(self):
        """Effectue une rotation continue des nœuds."""
        if not self.rotation_active:
            return
        
        # Incrémenter l'angle de rotation
        self.current_rotation = (self.current_rotation + 0.05) % (2 * M.pi)
        
        # Redessiner les nœuds
        self.draw_nodes()
        
        # Programmer la prochaine étape
        self.root.after(30, self.continuous_rotation)

class Modele():
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

if __name__ == "__main__":
    c = controleur()