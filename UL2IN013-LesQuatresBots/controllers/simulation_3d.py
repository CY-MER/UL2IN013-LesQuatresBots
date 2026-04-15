from vpython import *
from models.robot import Robot
import math
 
# La simulation
scene.title = "Simulation Robot 3D"
scene.width = 800
scene.height = 600

# Le sol
sol = box(pos=vector(0, -1, 0), size=vector(30, 0.5, 30), color=color.white)

robot2D = Robot(0, 0)

# objet 3D
robot3D = sphere(pos=vector(0, 0, 0), radius=0.5, color=color.blue)

# direction du robot
direction_arrow = arrow(pos=robot3D.pos, axis=vector(1,0,0), color=color.yellow)

# Les obstacles 
obstacles = [
    box(pos=vector(3, 0, 3), size=vector(2, 2, 2), color=color.red),
    box(pos=vector(-4, 0, 2), size=vector(3, 1, 2), color=color.green),
    sphere(pos=vector(2, 0, -4), radius=1, color=color.orange)
]

# Le carré
cote = 100
steps = 50
side = 0
step = 0

while True:
    rate(60)

    if side < 4:
        if step < steps:
            robot2D.avancer(2)
            step += 1
        else:
            robot2D.tourner(1)
            if robot2D.rotation % 90 < 2:
                side += 1
                step = 0

    # update physique robot
    robot2D.update()

    # récuperation de la position
    x, y, angle, _ = robot2D.get_location()

    # conversion 2D -> 3D
    robot3D.pos = vector(x/20, 0, y/20)

    # direction
    direction_arrow.pos = robot3D.pos
    direction_arrow.axis = vector(
        math.cos(math.radians(angle)),
        0,
        math.sin(math.radians(angle))
    )
