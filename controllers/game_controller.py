"""Controleur principal du jeu"""
try:
    import pygame
    PYGAME_AVAILABLE = True
except ImportError:
    PYGAME_AVAILABLE = False
    print("Warning: pygame n'est pas installé")

from models import Robot

if PYGAME_AVAILABLE:
    from views import GameView


class GameController:
    """Gère la logique du jeu"""

    def __init__(self, width=400, height=400):
        if not PYGAME_AVAILABLE:
            raise ImportError("pygame requis")

        self.width = width
        self.height = height
        self.view = GameView(width, height, "Robot Simulation")
        self.robot = Robot(width // 2, height // 2)
        self.points = [(self.robot.x, self.robot.y)]

        # parametres du carre
        self.cote = 100
        self.steps = 40
        self.side = 0
        self.step = 0
        self.en_pause_rotation = False
        self.running = True

    def handle_events(self):
        """Gestion des evenements"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_r:
                    # reset
                    self.robot = Robot(self.width // 2, self.height // 2)
                    self.points = [(self.robot.x, self.robot.y)]
                    self.side = 0
                    self.step = 0
                    self.en_pause_rotation = False

    def update(self):
        """Update logique"""
        if self.side >= 4:
            return

        if self.step == 0 and not self.en_pause_rotation:
            self.robot.tourner(90)
            self.robot.vitesse = 0.0
            self.en_pause_rotation = True
        elif self.en_pause_rotation:
            self.en_pause_rotation = False
            self.step = 1
        elif self.step < self.steps:
            distance = self.cote / self.steps
            self.robot.avancer(distance, dt=1.0)
            self.points.append((self.robot.x, self.robot.y))
            self.step += 1
        else:
            self.step = 0
            self.side += 1

    def render(self):
        """Affichage"""
        self.view.clear()
        self.view.draw_path(self.points, color=(255, 0, 0), width=2)
        self.view.draw_robot(self.robot.x, self.robot.y, radius=5, color=(0, 0, 255))

        x, y, angle, vitesse = self.robot.get_location()
        self.view.draw_info(x, y, angle, vitesse)
        self.view.update()

    def run(self):
        """Boucle principale"""
        print("Robot Simulator")
        print("ESC pour quitter, R pour reset")

        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.view.delay(100)
            self.view.tick(60)

        self.view.quit()
