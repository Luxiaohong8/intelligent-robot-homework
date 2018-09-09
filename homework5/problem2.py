# coding=utf-8
#  Created by Liuyue on 2018-05-14

import random
import math
import bisect
import math
import turtle
import random

turtle.tracer(50000, delay=0)
turtle.register_shape("dot", ((-3,-3), (-3,3), (3,3), (3,-3)))
turtle.register_shape("tri", ((-3, -2), (0, 3), (3, -2), (0, 0)))
turtle.speed(0)
turtle.title("Simulation of CS401")

PARTICLE_COUNT = 6000   

UPDATE_EVERY = 0
DRAW_EVERY = 2

maze_data = ( ( 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1 ),
              ( 1, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,1),
              ( 1, 0, 1, 1, 0, 2, 1, 1, 0, 1 ,1),
              ( 1, 0, 1, 2, 0, 0, 0, 1, 0, 2 ,1),
              ( 1, 0, 0, 0, 2, 2, 0, 0, 0, 0 ,1),
              ( 1, 1, 1, 0, 1, 1, 1, 1, 1, 0 ,1),
              ( 1, 0, 0, 0, 0, 0, 1, 0, 1, 0 ,1),
              ( 1, 1, 0, 1, 1, 1, 1, 0, 0, 0 ,1),
              ( 1, 0, 0, 0, 0, 0, 0, 0, 2, 0 ,1),
              ( 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1))

ROBOT_HAS_COMPASS = True

def add_noise(level, *coords):
    return [x + random.uniform(-level, level) for x in coords]

def add_little_noise(*coords):
    return add_noise(0.02, *coords)

def add_some_noise(*coords):
    return add_noise(0.1, *coords)

sigma2 = 0.9 ** 2
def w_gauss(a, b):
    error = a - b
    g = math.e ** -(error ** 2 / (2 * sigma2))
    return g

def compute_mean_point(particles):
    m_x, m_y, m_count = 0, 0, 0
    for p in particles:
        m_count += p.w
        m_x += p.x * p.w
        m_y += p.y * p.w

    if m_count == 0:
        return -1, -1, False

    m_x /= m_count
    m_y /= m_count
    m_count = 0
    for p in particles:
        if world.distance(p.x, p.y, m_x, m_y) < 1:
            m_count += 1

    return m_x, m_y, m_count > PARTICLE_COUNT * 0.95

class WeightedDistribution(object):
    def __init__(self, state):
        accum = 0.0
        self.state = [p for p in state if p.w > 0]
        self.distribution = []
        for x in self.state:
            accum += x.w
            self.distribution.append(accum)

    def pick(self):
        try:
            return self.state[bisect.bisect_left(self.distribution, random.uniform(0, 1))]
        except IndexError:
            return None

class Maze(object):
    def __init__(self, maze):
        self.maze = maze
        self.width   = len(maze[0])
        self.height  = len(maze)
        turtle.setworldcoordinates(0, 0, self.width, self.height)
        self.blocks = []
        self.update_cnt = 0
        self.one_px = float(turtle.window_width()) / float(self.width) / 2

        self.beacons = []
        for y, line in enumerate(self.maze):
            for x, block in enumerate(line):
                if block:
                    nb_y = self.height - y - 1
                    self.blocks.append((x, nb_y))
                    if block == 2:
                        self.beacons.extend(((x, nb_y), (x+1, nb_y), (x, nb_y+1), (x+1, nb_y+1)))

    def draw(self):
        for x, y in self.blocks:
            turtle.color("#87CEEB")
            turtle.up()
            turtle.setposition(x, y)
            turtle.down()
            turtle.setheading(90)
            turtle.begin_fill()
            for _ in range(0, 4):
                turtle.fd(1)
                turtle.right(90)
            turtle.end_fill()
            turtle.up()

        turtle.color("#00ffff")
        for x, y in self.beacons:
            turtle.setposition(x, y)
            turtle.dot()
        turtle.update()

    def weight_to_color(self, weight):
        return "#%02x00%02x" % (int(weight * 255), int((1 - weight) * 255))

    def is_in(self, x, y):
        if x < 0 or y < 0 or x > self.width or y > self.height:
            return False
        return True

    def is_free(self, x, y):
        if not self.is_in(x, y):
            return False

        yy = self.height - int(y) - 1
        xx = int(x)
        return self.maze[yy][xx] == 0

    def show_mean(self, x, y, confident=False):
        if confident:
            turtle.color("#00AA00")
        else:
            turtle.color("#cccccc")
        turtle.setposition(x, y)
        turtle.shape("circle")
        turtle.stamp()

    def show_particles(self, particles):
        self.update_cnt += 1
        if UPDATE_EVERY > 0 and self.update_cnt % UPDATE_EVERY != 1:
            return

        turtle.clearstamps()
        turtle.shape('arrow')
        turtle.shapesize(0.1, 0.1, 0.1)
        draw_cnt = 0
        px = {}
        for p in particles:
            draw_cnt += 1
            if DRAW_EVERY == 0 or draw_cnt % DRAW_EVERY == 1:
                scaled_x = int(p.x * self.one_px)
                scaled_y = int(p.y * self.one_px)
                scaled_xy = scaled_x * 10000 + scaled_y
                if not scaled_xy in px:
                    px[scaled_xy] = 1
                    turtle.setposition(*p.xy)
                    turtle.setheading(90 - p.h)
                    turtle.color(self.weight_to_color(p.w))
                    turtle.stamp()

    def show_robot(self, robot):
        turtle.shapesize(1, 1, 1)
        turtle.color("blue")
        turtle.setposition(*robot.xy)
        turtle.setheading(90 - robot.h)
        turtle.stamp()
        turtle.update()

    def random_place(self):
        x = random.uniform(0, self.width)
        y = random.uniform(0, self.height)
        return x, y

    def random_free_place(self):
        while True:
            x, y = self.random_place()
            if self.is_free(x, y):
                return x, y

    def distance(self, x1, y1, x2, y2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def distance_to_nearest_beacon(self, x, y):
        d = 99999
        for c_x, c_y in self.beacons:
            distance = self.distance(c_x, c_y, x, y)
            if distance < d:
                d = distance
                d_x, d_y = c_x, c_y

        return d

class Particle(object):
    def __init__(self, x, y, heading=None, w=1, noisy=False):
        if heading is None:
            heading = random.uniform(0, 360)
        if noisy:
            x, y, heading = add_some_noise(x, y, heading)

        self.x = x
        self.y = y
        self.h = heading
        self.w = w

    def __repr__(self):
        return "(%f, %f, w=%f)" % (self.x, self.y, self.w)

    @property
    def xy(self):
        return self.x, self.y

    @property
    def xyh(self):
        return self.x, self.y, self.h

    @classmethod
    def create_random(cls, count, maze):
        return [cls(*maze.random_free_place()) for _ in range(0, count)]

    def read_sensor(self, maze):
        return maze.distance_to_nearest_beacon(*self.xy)

    def advance_by(self, speed, checker=None, noisy=False):
        h = self.h
        if noisy:
            speed, h = add_little_noise(speed, h)
            h += random.uniform(-3, 3) 
        r = math.radians(h)
        dx = math.sin(r) * speed
        dy = math.cos(r) * speed
        if checker is None or checker(self, dx, dy):
            self.move_by(dx, dy)
            return True
        return False

    def move_by(self, x, y):
        self.x += x
        self.y += y

class Robot(Particle):
    speed = 0.2

    def __init__(self, maze):
        super(Robot, self).__init__(*maze.random_free_place(), heading=90)
        self.chose_random_direction()
        self.step_count = 0

    def chose_random_direction(self):
        heading = random.uniform(0, 360)
        self.h = heading

    def read_sensor(self, maze):
        return add_little_noise(super(Robot, self).read_sensor(maze))[0]

    def move(self, maze):
        while True:
            self.step_count += 1
            if self.advance_by(self.speed, noisy=True,
                checker=lambda r, dx, dy: maze.is_free(r.x+dx, r.y+dy)):
                break

            self.chose_random_direction()

world = Maze(maze_data)
world.draw()

particles = Particle.create_random(PARTICLE_COUNT, world)
robbie = Robot(world)

while True:
    r_d = robbie.read_sensor(world)

    for p in particles:
        if world.is_free(*p.xy):
            p_d = p.read_sensor(world)
            p.w = w_gauss(r_d, p_d)
        else:
            p.w = 0

    m_x, m_y, m_confident = compute_mean_point(particles)

    world.show_particles(particles)
    world.show_mean(m_x, m_y, m_confident)
    world.show_robot(robbie)

    new_particles = []

    nu = sum(p.w for p in particles)
    if nu:
        for p in particles:
            p.w = p.w / nu

    dist = WeightedDistribution(particles)

    for _ in particles:
        p = dist.pick()
        if p is None:  
            new_particle = Particle.create_random(1, world)[0]
        else:
            new_particle = Particle(p.x, p.y,
                    heading=robbie.h if ROBOT_HAS_COMPASS else p.h,
                    noisy=True)
        new_particles.append(new_particle)

    particles = new_particles

    old_heading = robbie.h
    robbie.move(world)
    d_h = robbie.h - old_heading

    for p in particles:
        p.h += d_h 
        p.advance_by(robbie.speed)
