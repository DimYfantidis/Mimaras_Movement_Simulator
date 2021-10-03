import pygame
import random


class ParticlePrinciple:
    PARTICLE_EVENT = pygame.USEREVENT + 1

    def __init__(self):
        self.particles = []

    def emit(self, screen: pygame.display, color):
        if self.particles:
            self.delete_particles()
            for particle in self.particles:
                particle[0][1] += particle[2][0]  # x coordinate
                particle[0][0] += particle[2][1]  # y coordinate
                particle[1] -= 0.2  # particle radius
                pygame.draw.circle(screen, color, particle[0], int(particle[1]))

    def add_particles(self, emitting_obj: pygame.Rect):
        # Particle follows the mouse
        pos_x = emitting_obj.x + emitting_obj.size[0] / 2
        pos_y = emitting_obj.y + emitting_obj.size[1] / 2
        radius = 10
        direction_x = random.uniform(-1, 1)
        direction_y = random.uniform(-1, 1)
        particle_circle = [[pos_x, pos_y], radius, [direction_x, direction_y]]
        self.particles.append(particle_circle)

    def delete_particles(self):
        particle_copy = [particle for particle in self.particles if particle[1] > 0]
        self.particles = particle_copy


pygame.time.set_timer(ParticlePrinciple.PARTICLE_EVENT, 30)


class Entity(pygame.Rect):
    def __init__(self,
                 scr: pygame.display,
                 spawn_x: float, spawn_y: float,
                 width: float, height: float, color,
                 label: str = '',
                 l_font: pygame.font.Font = pygame.font.Font('freesansbold.ttf', 13)):
        super().__init__(spawn_x, spawn_y, width, height)
        self.screen = scr
        self.name = label
        self.color = color
        self.speed = 0
        self.dx = 0
        self.dy = 0
        self.particles = ParticlePrinciple()
        self.font = l_font
        self.visual_label = self.font.render(self.name, True, self.color)

    def show(self):
        self.particles.emit(self.screen, self.color)
        self.screen.blit(self.visual_label, (self.x - 12, self.y - 20))
        pygame.draw.rect(self.screen, self.color, self)

    def set_font(self, l_font: pygame.font.Font):
        self.font = l_font
        self.visual_label = self.font.render(self.name, True, self.color)

    def add_particles(self):
        self.particles.add_particles(self)

    def __str__(self):
        return f'{self.name}: speed={self.speed}, size=({self.size[0]}, {self.size[1]}), color={self.color}'
