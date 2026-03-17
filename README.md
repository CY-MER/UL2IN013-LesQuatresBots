# ProjetRobotG4

## Description
Projet de simulation de robot avec affichage Pygame.

## Branches
- `main`: code principal
- `dev1`: code avec pygame

## Structure

```
├── models/              # Classes du robot
│   ├── robot.py
│   ├── robot_vecteur.py
│   ├── point.py
│   ├── vecteur2D.py
│   └── obstacle.py
│
├── views/               # Affichage
│   └── game_view.py
│
├── controllers/         # Logique
│   ├── game_controller.py
│   └── mouvements.py
│
├── tests/               # Tests
│   └── test_robot.py
│
└── main.py
```

## Utilisation

```bash
# Lancer le programme
python main.py

# Tests
python tests/test_robot.py

# Demo mouvements
python demo_mouvements.py
```

Contrôles: ESC pour quitter, R pour reset

## UserStory

En tant qu'utilisateur j'ai besion d'un robot capable de faire des deplacements prédefinis, le robot doit aussi être capable de detecter les obstacles et les éviter, éventuellement suivre une balise ou autre fonctionnalités nécessaires.

On attendra enfin une nouvelle fonctionnalité du robot lui permettant d'effectuer un crénaux en autonomie.

## Fonctionnalités

- Simulation robot avec pygame
- Mouvements: carre, rectangle, triangle, cercle, aller-retour
- Detection obstacles
- Capteurs
- Tests unitaires
