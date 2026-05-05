# Projet Robot - Groupe Les Quatres Bots

## 👥 Équipe

Ce projet est réalisé par :
- [Anis-tak](https://github.com/Anis-tak)
- [liliasophia2006](https://github.com/liliasophia2006)
- [yasmineboukercha75-droid](https://github.com/yasmineboukercha75-droid)

**main** : version finale du projet 
**anis-tak-patch1** : branche de développement utilisée pour tester et implémenter les fonctionnalités avant intégration

---
## 📖 Sommaire

- À propos du projet  
- Architecture & Conception  
- Fonctionnalités  
- Structure du projet  
- Installation & Lancement  

---

## 🎯 À propos du projet

Ce projet consiste à concevoir un mini-robot autonome capable de se déplacer dans un environnement avec des obstacles.

Une simulation 2D (Pygame) a été développée afin de tester les comportements du robot avant leur exécution sur un robot réel.

L’objectif principal est de pouvoir utiliser les mêmes stratégies de déplacement en simulation et sur le robot physique grâce à une architecture modulaire.

---


## 🏗 Architecture & Conception

Le projet repose sur une architecture modulaire basée sur deux design patterns principaux :

### 🔁 Pattern Strategy : Comportement du robot

Les comportements du robot sont définis sous forme de stratégies :

- Avancer  
- Tourner  
- Stop  
- Séquence de stratégies (ex : tracer un carré)

Chaque stratégie implémente les méthodes `update()` et `fini()`.

---

### 🔄 Pattern Adapter : Lien simulation / réel

Le `RobotAdapter` permet d’utiliser les mêmes commandes :

- en simulation (Pygame)  
- sur le robot réel (API)

👉 Cela évite de modifier le code des stratégies.

---

## ⚙️ Fonctionnalités

- Déplacement autonome du robot  
- Gestion des vitesses des roues  
- Détection et évitement d’obstacles  
- Simulation en temps réel avec Pygame  
- Stratégies de déplacement (ex : tracer un carré)  
- Exécution sur robot réel  

---

## 📂 Structure du projet
PROJET-ROBOT/
├── src/
│ ├── model/ # Robot, Vecteur2D, Point , Obstacles
│ ├── strategy/ # Stratégies (Pattern Strategy)
│ ├── adapter/ # RobotAdapter (Pattern Adapter)
│ ├── view/ # Simulation Pygame
│ ├── controller/ # SimulationController
│ └── main.py # Lancement du programme
│
└── README.md
│
└── rapport_projett.pdf

## 🚀 Installation & Lancement

### Prérequis

- Python 3

### Installation

```bash
pip install pygame
Lancer la simulation : python main.py

