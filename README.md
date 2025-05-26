# Tower Defense



# Introduction
- **Avertissement:** Ce jeux est une version préliminaire (Béta). 

Ce document explique comment ce projet est fait, par qui et avec quels moyens utilisés. 
Ce jeu est basé sur un style Tower Defense dont le but du joueur est d'empêcher l'ennemi d'atteindre la fin du chemin en placant des tours sur la carte.

## Mise à jour V0.3
- ### **Interface**
  - Possibilité de cliquer sur les tours pour afficher leur rayon d'attaque
  - Bouton pour activé ou désactivé la visibilité du rayon d'attaque
  - Ajout d'une police dans la thématique
  - Modification de l'apparence visuelle du GUI
  - Ajout d'un menu
      - Ajout de la page Tutorial
          - Possibilité de cliqué sur les éléments visible pour savoir comment jouer.
      - Ajout de la page Crédits
          - Possibilité de cliqué sur les noms des devs
      - Ajout de la page parametre
          - Possibilité de modifier la difficulté du jeu.
      Ajout de la fonction exit depuis le menu
- ### **Mécanique de jeu**
  - Réctification de la hitbox des ennemis
  - Effets des tours sur les ennemis.
  - Diminution du temps d'attente entre chaque spawn d'ennemi pendant un vague


- ### **Tours**
  Effets des tours

  ##### **Machine Gun**
    - **Ralentit les ennemis**
  ##### **Mortar**
    - **Coups critiques**
  ##### **Anti-Tank**
    - **Fait reculer les ennemis**
  ##### **Anti-Air**
    - **Plus de dégats sur le temps**
  ##### **Artillery**
    - **Gagne 2$ par coups porté**



## Mise à jour V0.2
- ### **Interface**
    Boutons de tours pour séléctionner les nouvelles tours ajoutées.\
    Boutons de habileté pour améliorer les tours.\
    Bouton pour vendre une tour.
    Barre de vie pour afficher la vie des ennemis.

- ### **Mécanique de jeu**

    **Choix tours:**\
    Pour placer les tours, il faut cliqué sur le bouton concerné et puis on choisi l'endroit où le placer avec un autre clique.

    **Choix amélioration:**\
    Pour améliorer une tour, il faut cliqué sur l'habileté concerné et ensuite choisi sur quelle tour appliqué l'habileté en cliquant dessus.

    **Vendre des tours:**\
    Pour vendre une tour, il suffit de cliqué sur le bouton et cliqué sur la tour à effacer.\
    **/!\ Attention**: Une fois cliqué, il faut réappuyer sur un autre bouton pour désactiver la fonctionnalité.

    **Difficulté progressive:**\
    Au fur et à mesure des rounds, les ennemis augmente leurs capacité (ex. leur vie et leur nombres.)

    **Dynamisme des déplacement des ennemis**\
    Les ennemis peuvent choisir un chemin pour donner des nouvelles possibilité de stratégie de jeu.


- ### **Ennemis**
  Nouveaux ennemis ajoutés.

  **Ennemi de Glace:** Caractéristiques de base\
  ![value](./assets/info/value.png)    -> **20** (Valeurs en crédit)\
  ![speed](./assets/info/speed.png) -> **2** (vitesse, par pixel)\
  ![life](./assets/info/life.png)      ->  **3**(point de valeur de vie)\
  **Ennemi de Feu** \
  ![value](./assets/info/value.png)-> **25**\
  ![speed](./assets/info/speed.png)-> **3**\
  ![life](./assets/info/life.png)  ->  **4**\
  **Ennemi de gaz** \
  ![value](./assets/info/value.png)-> **18**\
  ![speed](./assets/info/speed.png)-> **1**\
  ![life](./assets/info/life.png)->  **2**\
  **Avions**\
  ![value](./assets/info/value.png)-> **30**\
  ![speed](./assets/info/speed.png)-> **5**\
  ![life](./assets/info/life.png)->  **5**\
  **Tank**\
  ![value](./assets/info/value.png)-> **35**\
  ![speed](./assets/info/speed.png)-> **2**\
  ![life](./assets/info/life.png)->  **7**


- ### **Tours**
  Nouvelles Tours

  **Machine Gun**\
  ![speed](./assets/info/speed.png) ->**10** (vitesse, en pixel)\
  ![strenght](./assets/info/strength.png) -> **1** (dégats, en points de dégats)\
  **Mortar**\
  ![speed](./assets/info/speed.png) ->**5**\
  ![strenght](./assets/info/strength.png) -> **5**\
  **Anti-Tank**\
  ![speed](./assets/info/speed.png) ->**4**\
  ![strenght](./assets/info/strength.png) -> **8**\
  **Anti-Air**\
  ![speed](./assets/info/speed.png) ->**12**\
  ![strenght](./assets/info/strength.png) -> **2**\
  **Artillery**\
  ![speed](./assets/info/speed.png) ->**3**\
  ![strenght](./assets/info/strength.png) -> **7**



## Languages utilisés
- **Python:** Le language Python est utilisé principalement pour ce projet. Ce language peut être lu sur plusieurs appareils tel que Linux, Windows, 
macOS et si bien programmé, sur Android.

- **JavaScript:** Le javaScript ou plus simplement les fichiers .json sont utilisés comme base de donnée pour contenir nos objects tel que les ennemis ou la carte elle-même.

## Structure
- **Logique MVC:** Le programme est conçu selon le modèle MVC (Modèle-Vue-Contrôleur). Ce modèle d'architecture consiste à séparer la logique et les calculs (Modèle) de l'affichage du logiciel(Vue). Le contrôleur agit à titre d'intermédiaire entre la Vue et le Modèle puisque ceux-ci ne communiquent pas entre eux. 
- **Démarrage:** Le programme ne peut démarrer qu'à partir du contrôleur.

## Comment jouer
- **Démarrage du jeu:** Au début, vous verrez la carte s'afficher avec un tableau de bord dans la barre à droite. Le tableau contient les informations statistiques du joueur (score, argent, vie, ennemis restants sur la carte) ainsi que 2 boutons (Tours et Start Round). Le bouton "Tours" va vous permettre de placer des tours sur la carte dans le but de vaincre les ennemis. Cependant, vous devrez prendre en compte que les tours coûtent de l'argent, alors placez vos tours de manière stratégiques. Le bouton Start Round permet de commencer le jeu en envoyant les vagues d'ennemis. 


## Comportement du jeu pour le joueur (V0.1) 

- **Début partie:** Lorsque vous appuyez sur le bouton "Start Round", la partie va démarrer et l'ennemi va avancer jusqu'à se rendre à la fin du chemin. 

- **Placement des tours:** Vous pourrez placer les tours dans sur la carte, sauf sur les zones réservées pour les tours et le chemin. Le tours tireront des projectiles sur les ennemis à proximité.

- **Ennemis:** Des ennemis vont apparaîtrent à chaque début de round et seront plus nombreux à chaque vague. 

- **Gagner le round:** Lorsque vous remportez le round, il vous est possible de continuer à l'infini, jusqu'à ce que vous soyez vaincu ou que vous quittiez la partie.

- **Perdu:** Lorsque vous perdez la partie, c'est à dire, s'il ne vous reste plus de vie, un affichage GameOver apparaîtra et vous aurez le choix de recommencer une nouvelle partie ou non. 

  - *Valeurs des objets(De base):* 
    - Tours: 50$
    - Ennemis: vie de base = 5
    - Projectile: Dégât = 2

  
# Pour télécharger
1. Télécharger le code
2. Placer le dans un dossier de votre choix
3. Ouvrir un terminal dans le dossier du projet
4. Executer la commande suivante pour mettre à jours pip
* > pip install --upgrade pip
5. Executer le jeu
* > python controleur.py


---
# Pour les développeurs
## Naming Conventions
- **Variables and Functions:** Use `snake_case` (e.g., `my_variable`, `calculate_sum`).
- **Classes:** Use `PascalCase` (e.g., `MyClass`, `DataProcessor`).
- **Constants:** Use `UPPER_CASE` (e.g., `MAX_COUNT`, `DEFAULT_TIMEOUT`).

## Code Formatting
- **Indentation:** Use 4 spaces per indentation level.
- **Line Length:** Limit lines to 79 characters.
- **Imports:** Group imports in the following order:
  1. Standard library imports
  2. Third-party imports
  3. Local application/library-specific imports

## Comments and Documentation
- Use inline comments sparingly and clearly.
- Write docstrings for modules, classes, and functions following [PEP 257](https://www.python.org/dev/peps/pep-0257/).
- Focus comments on explaining *why* something is done rather than *what* is done.

## Best Practices
- Follow the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide.
- Keep functions and classes focused on a single task.
- Use virtual environments to manage project dependencies.
- Ensure your code is clean, readable, and well-documented.

## Branching Strategy
- **Base Branch:** Always create new branches from the `dev` branch.
- **Branch Naming:** Each sprint item should be developed in its own branch using the pattern: `/feature/name-of-feature`  
  - *Example:* `/feature/user-authentication`
- **Pull Requests:** When a feature is ready, open a pull request targeting the `dev` branch for integration.
  - This ensures all new features are reviewed and tested before being merged into the development stream.

## Best Practices
- Follow the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide.
- Keep functions and classes focused on a single task.
- Use virtual environments to manage project dependencies.
- Ensure your code is clean, readable, and well-documented.

Happy coding!
