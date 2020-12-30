import numpy as np


N_ROWS = 15
N_COLS = 13
class GameMap():
    def __init__(self):
        self.map = np.zeros( [N_ROWS,N_COLS])