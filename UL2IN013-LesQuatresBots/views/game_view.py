"""Vue pour l'affichage pygame"""
import pygame
import math


class GameView:
    """Gere l'affichage pygame"""

    def __init__(self, width=400, height=400, title="Robot"):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.font = pygame.font.Font(None, 20)
        self.clock = pygame.time.Clock()

    def clear(self, color=None):
        """Efface l'ecran"""
        if color is None:
            color = (255, 255, 255)
        self.screen.fill(color)

    def draw_grid(self, cell_size=50, color=(200, 200, 200)):
        """Dessine une grille"""
        for x in range(0, self.width, cell_size):
            pygame.draw.line(self.screen, color, (x, 0), (x, self.height), 1)
        for y in range(0, self.height, cell_size):
            pygame.draw.line(self.screen, color, (0, y), (self.width, y), 1)

    def draw_path(self, points, color=(255, 0, 0), width=2):
        """Dessine le chemin du robot"""
        if len(points) > 1:
            pygame.draw.lines(
                self.screen,
                color,
                False,
                [(int(p[0]), int(p[1])) for p in points],
                width
            )
        
    def draw_obstacles(self, obstacles):
        for obstacle in obstacles:
            color = obstacle.couleur  # <- prend la couleur de l'obstacle
            if obstacle.type == "cercle":
                cx, cy, rayon = obstacle.data
                pygame.draw.circle(self.screen, color, (int(cx), int(cy)), rayon)
            elif obstacle.type == "rectangle":
                x, y, largeur, hauteur = obstacle.data
                pygame.draw.rect(self.screen, color, (x, y, largeur, hauteur))
            elif obstacle.type == "triangle":
                p1, p2, p3 = obstacle.data
                pygame.draw.polygon(self.screen, color, [p1, p2, p3])
        
    #changement de la couleur du robot pour le destinguer de son path 
    def draw_robot(self, x, y, angle=0, radius=5, color=(255, 255, 0)):
        pygame.draw.circle(self.screen, color, (int(x), int(y)), radius)
        
        # direction
        longueur = 15
        dx = longueur * math.cos(math.radians(angle))
        dy = longueur * math.sin(math.radians(angle))

        pygame.draw.line(
            self.screen,
            (0, 0, 0),
            (int(x), int(y)),
            (int(x + dx), int(y + dy)),
            2
        )

   
    def draw_info(self, x, y, angle, vitesse):
        """Affiche les infos du robot"""
        info_lines = [
            f"Position: ({x:.1f}, {y:.1f})",
            f"Angle: {angle % 360}",
            f"Vitesse: {vitesse:.2f}"
        ]

        for i, line in enumerate(info_lines):
            text = self.font.render(line, True, (0, 0, 0))
            self.screen.blit(text, (10, 10 + i * 25))

    
    def render_simulation(self, simulation_data):
        """affiche tout à partir des donées de la simulation"""
        self.clear()
        self.draw_grid()
        self.draw_obstacles(simulation_data["obstacles"])
        self.draw_path(simulation_data["points"])
        self.draw_robot(simulation_data["x"], simulation_data["y"], simulation_data["angle"])
        self.draw_info(
            simulation_data["x"],
            simulation_data["y"],
            simulation_data["angle"],
            simulation_data["vitesse"]
        )
        self.update()


    def draw_text(self, text, x, y, color=(0, 0, 0)):
        """Affiche du texte"""
        surface = self.font.render(text, True, color)
        self.screen.blit(surface, (x, y))

    def update(self):
        """MAJ affichage"""
        pygame.display.flip()

    def tick(self, fps=60):
        """Controle FPS"""
        self.clock.tick(fps)

    def delay(self, milliseconds):
        """Delai"""
        pygame.time.delay(milliseconds)

    def quit(self):
        """Ferme pygame"""
        pygame.quit()
