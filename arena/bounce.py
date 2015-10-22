'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from sys import stdin
from random import choice
from arena import *

class Ball(Actor):
    W, H = 20, 20
    SPEED = 5

    def __init__(self, arena, x, y):
        self._x, self._y = x, y
        self._dx, self._dy = self.SPEED, self.SPEED
        self._arena = arena
        arena.add(self)

    def move(self):
        arena_w, arena_h = self._arena.size()
        if not (0 <= self._x + self._dx < arena_w - self.W):
            self._dx = -self._dx
        if not (0 <= self._y + self._dy < arena_h - self.H):
            self._dy = -self._dy
        self._x += self._dx
        self._y += self._dy

    def collide(self, other):
        x, y, w, h = other.rect()
        if x < self._x:
            self._dx = self.SPEED
        else:
            self._dx = -self.SPEED
        if y < self._y:
            self._dy = self.SPEED
        else:
            self._dy = -self.SPEED
        
    def rect(self):
        return self._x, self._y, self.W, self.H

    def symbol(self):
        return 0


class Ghost(Actor):
    W, H = 20, 20

    def __init__(self, arena, x, y):
        self._x, self._y = x, y
        self._arena = arena
        arena.add(self)

    def move(self):
        dx = choice([-5, 0, 5])
        dy = choice([-5, 0, 5])
        arena_w, arena_h = self._arena.size()
        self._x = (self._x + dx) % arena_w
        self._y = (self._y + dy) % arena_h

    def collide(self, other):
        pass
        
    def rect(self):
        return self._x, self._y, self.W, self.H

    def symbol(self):
        return 0


class Turtle(Actor):
    W, H = 20, 20
    SPEED = 2

    def __init__(self, arena, x, y):
        self._x, self._y = x, y
        self._dx, self._dy = 0, 0
        self._arena = arena
        arena.add(self)

    def move(self):
        arena_w, arena_h = self._arena.size()
        self._y += self._dy
        if self._y < 0:
            self._y = 0
        elif self._y > arena_h - Turtle.H:
            self._y = arena_h - Turtle.H

        self._x += self._dx
        if self._x < 0:
            self._x = 0
        elif self._x > arena_w - Turtle.W:
            self._x = arena_w - Turtle.W

    def go_left(self):
        self._dx, self._dy = -Turtle.SPEED, 0
        
    def go_right(self):
        self._dx, self._dy = +Turtle.SPEED, 0

    def go_up(self):
        self._dx, self._dy = 0, -Turtle.SPEED
        
    def go_down(self):
        self._dx, self._dy = 0, +Turtle.SPEED

    def stay(self):
        self._dx, self._dy = 0, 0

    def collide(self, other):
        pass
        
    def rect(self):
        return self._x, self._y, self.W, self.H

    def symbol(self):
        return 0


def print_arena(arena):
    for a in arena.actors():
        print(type(a).__name__, '@', a.rect())

    
if __name__ == '__main__':
    arena = Arena(320, 240)
    Ball(arena, 40, 80)
    Ball(arena, 80, 40)
    Ghost(arena, 120, 80)
    print_arena(arena)

    for line in stdin:
        arena.move_all()
        print_arena(arena)
