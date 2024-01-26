from utils import randcell

class Helicopter:

    def __init__(self, w, h):
        rc = randcell(w, h)
        rx, ry = rc[0], rc[1]
        self.x = rx
        self.y = ry
        self.h = h
        self.w = w
        self.tank = 0
        self.mxtank = 1
        self.score = 0
        self.life = 20

    def move(self, dx, dy):
        nx = dx + self.x
        ny = dy + self.y
        if(nx >= 0 and ny >= 0 and nx < self.h and ny < self.w):
            self.x, self.y = nx, ny

    def print_stats(self):
        print("🍺 ", self.tank, " / " , self.mxtank, end=" \/ ")
        print("⚱️ ", self.score, " \/ ", "❤️ ", self.life)
    
    def export_data(self):
        return {"score":self.score,
                "lifes":self.life,
                "x":self.x, "y":self.y,
                "tank":self.tank, "maxtank":self.mxtank
                }
    
    def import_data(self, data):
        self.x = data["x"] or 0
        self.y = data["y"] or 0
        self.tank = data["tank"] or 1
        self.mxtank = data["maxtank"] or 2
        self.score = data["score"] or 500
        self.life = data["lifes"] or 10

