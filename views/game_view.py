"""Vue pour l'affichage pygame"""
import pygame


class GameView:
    """Gere l'affichage pygame"""

    def __init__(self, width=400, height=400, title="Robot"):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.font = pygame.font.Font(None, 24)
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

    def draw_robot(self, x, y, radius=5, color=(0, 0, 0)):
        """Dessine le robot"""
        pygame.draw.circle(self.screen, color, (int(x), int(y)), radius)

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
