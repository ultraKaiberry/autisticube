# autisticube(remove it if you want bleh)

import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 2000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rotating Cube")

vertices = [
    [-1, -1, -1],
    [ 1, -1, -1],
    [ 1,  1, -1],
    [-1,  1, -1],
    [-1, -1,  1],
    [ 1, -1,  1],
    [ 1,  1,  1],
    [-1,  1,  1]
]

edges = [
    [0, 1], [1, 2], [2, 3], [3, 0],
    [4, 5], [5, 6], [6, 7], [7, 4],
    [0, 4], [1, 5], [2, 6], [3, 7]
]


def project(x, y, z, scale=500):
    factor = scale / (z + 4)
    x_proj = x * factor + WIDTH / 2
    y_proj = -y * factor + HEIGHT / 2
    return x_proj, y_proj


def rotate(x, y, z, angle_x, angle_y, angle_z):
   
    temp_y = y * math.cos(angle_x) - z * math.sin(angle_x)
    temp_z = y * math.sin(angle_x) + z * math.cos(angle_x)
    y, z = temp_y, temp_z

    
    temp_x = x * math.cos(angle_y) + z * math.sin(angle_y)
    temp_z = -x * math.sin(angle_y) + z * math.cos(angle_y)
    x, z = temp_x, temp_z

    
    temp_x = x * math.cos(angle_z) - y * math.sin(angle_z)
    temp_y = x * math.sin(angle_z) + y * math.cos(angle_z)
    x, y = temp_x, temp_y

    return x, y, z


running = True
clock = pygame.time.Clock()

angle_x, angle_y, angle_z = 0, 0, 0
while running:
    screen.fill((0, 0, 0))  

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    rotated_vertices = []
    for vertex in vertices:
        x, y, z = vertex
        x, y, z = rotate(x, y, z, angle_x, angle_y, angle_z)
        rotated_vertices.append((x, y, z))

    
    projected_vertices = []
    for vertex in rotated_vertices:
        x, y, z = vertex
        x_proj, y_proj = project(x, y, z)
        projected_vertices.append((x_proj, y_proj))

   
    for edge in edges:
        start, end = edge
        pygame.draw.line(screen, (255, 255, 255), projected_vertices[start], projected_vertices[end], 2)
    
    pygame.display.flip()
    angle_x += 0.02
    angle_y += 0.03
    angle_z += 0.04
    clock.tick(60)
pygame.quit()
