import numpy as npy
import matplotlib.pyplot as plty
from matplotlib.animation import FuncAnimation

class AnimatedRadialBtn:
    def __init__(self):
        self.fig, self.ax = plty.subplots()
        self.circle = plty.Circle((0, 0), 0.1, color='red', animated=True)
        self.ax.add_artist(self.circle)
        self.ax.set_aspect('equal', 'box')
        self.ax.set_xlim(-1, 1)
        self.ax.set_ylim(-1, 1)
        self.anim = FuncAnimation(self.fig, self.update, init_func=self.init_animation, frames=200, interval=50, blit=True)
        
    def init_animation(self):
        self.circle.center = (0, 0)
        self.ax.add_artist(self.circle)
        return self.circle,
    
    def update(self, frame):
        radius = npy.abs(npy.sin(npy.radians(frame * 3))) * 0.5
        self.circle.set_radius(radius)
        return self.circle,
    
    def start_animation(self):
        plty.show()
        

if __name__ == "__main__":
    radialBtn = AnimatedRadialBtn()
    radialBtn.start_animation()