# Tower Defense

# Introduction
- **Avertissement:** Ce jeux n'est qu'une version non-terminer(Béta), ceci ne représente pas la version finale. Il peut donc y avoir des bugs.

Ce document explique en parti comment ce projet est fait, par qui et avec quels moyens utilisés. Ce jeu est bassé sur un style 
Tower Defense dont le bût du joueur est d'empêcher l'ennemi d'atteindre la fin du chemin en placant des tours autour du chemin.

## Languages utilisés
- **Python:** Le language Python est utilisé principalement pour ce projet. Ce language peut être lu sur plusieurs appareils tel que Linux, Windows, 
macOS et si bien programmé, sur android.

- **JavaScript:** Le javaScript ou plus simplement les fichiers .json sont utilisés comme base de donnée pour contenir nos objects tel que les ennemis ou la carte elle-même.

## Structure
- **Logique MVC:** Le programme est conçu selon la norme MVC (Model-View-Controller) qui est un modèle d'architecture 
qui consiste à séparer la logique et calcule de la vue (Affichage logiciel), donc seul le contrôlleur devrait avoir accès à la vue et au modèle,
la vue ne doit pas communiquer directement avec modèle elle doit passer par le contrôlleur pour mettre à jour son interface.
- **Démarrage:** Le programme ne peut démarrer qu'à partir du contrôlleur.

## Comment jouer
- **Démarrage du jeu:** Au début vous verrez la carte, les informations du joueur et 2 boutons. Le bouton "Tours" va vous permettre de placer
des tours sur la carte dans le bût de vaincre l'ennemis, cependant vous devrez prendre en compte que les tours coûtent de l'argent, alors placer vos tours
de manière intélligente. Dans la barre à droit, nous avons les informations du jeu dont le score du joueur, ses vie, son argent et les ennemis restant sur
la carte.



## Comportement du jeu pour le joueur (V0.1) 

- **Début partie:** Lorsque vous appuyez sur le bouton "Start Round" la partie va démarrer et l'ennemis va avancer jusqu'à ce rendre à la fin.
Durant la partie, il 
- **Placement des tours:** Vous pourrez placer les tours dans les zones qui ne sont pas d'autres tours ou le chemin. Ils tireront des projectiles sur les ennemis à proximité.
- **Ennemis:** Des ennemis vont apparaitrent et seront plus nombreux chaque round et peut-être plus résistant(Plus de vie).

- **Gagné le round:** Lorsque vous remportez le round, il vous est possible de continuer à l'infini, jusqu'à ce que vous soyez vaincu ou que vous quittez la partie.

- **Perdu:** Lorsque vous perdez la partie,c'est à dire, s'il ne vous reste plus de vie un affichage GameOver apparaitra et tu auras le choix de recommencer
ou non.

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
