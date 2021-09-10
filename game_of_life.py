import copy
import random
from threading import Lock


class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances or args or kwargs:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class GameOfLife(metaclass=SingletonMeta):
    def __init__(self, width=20, height=20):
        self.__width = width
        self.__height = height
        self.world = None
        self.old_world = None
        self.generation = 0

    def form_new_generation(self):
        if self.generation == 0:
            self.world = self.generate_universe()
            self.old_world = [[0 for _ in range(self.__width)] for _ in range(self.__height)]
            self.generation += 1
            return

        self.old_world = copy.deepcopy(self.world)
        for i in range(len(self.world)):
            for j in range(len(self.world[0])):
                number_of_neighbors = self.__get_near(self.old_world, [i, j])
                if self.old_world[i][j]:
                    self.world[i][j] = int(number_of_neighbors in (2, 3))
                else:
                    self.world[i][j] = int(number_of_neighbors == 3)
        self.generation += 1

    def generate_universe(self):
        return [[random.randint(0, 1) for _ in range(self.__width)] for _ in range(self.__height)]

    @staticmethod
    def move(pos, shift):
        return pos[0] + shift[0], pos[1] + shift[1]

    @staticmethod
    def test_field(universe, pos):
        h, w = len(universe), len(universe[0])
        return universe[pos[0] % h][pos[1] % w]

    @staticmethod
    def __get_near(universe, pos, system=None):
        if system is None:
            system = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        return sum([GameOfLife.test_field(universe, GameOfLife.move(pos, shift)) for shift in system])
