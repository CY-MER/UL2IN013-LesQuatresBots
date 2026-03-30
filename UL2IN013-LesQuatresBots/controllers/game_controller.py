"""Controleur principal : orchestre vue + simulation"""

import pygame

from controllers.simulation_controller import SimulationController
from views import GameView


class GameController:
    """Coordonne la simulation et l'affichage"""

    def __init__(self, width=400, height=400):
        self.simulation = SimulationController(width, height)
        self.view = GameView(width, height, "Robot Simulation")
        self.running = True

    def handle_events(self):
        """Gestion des événements utilisateur"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_r:
                    self.simulation.reset()

    def run(self):
        """Boucle principale"""
        print("Robot Simulator")
        print("ESC pour quitter, R pour reset")

        while self.running:
            self.handle_events()
            self.simulation.update()

            data = self.simulation.get_robot_info()
            self.view.render_simulation(data)

            self.view.delay(100)
            self.view.tick(60)

        self.view.quit()