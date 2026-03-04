import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from matplotlib.widgets import Slider
from matplotlib.colors import ListedColormap
N=100
C=-2.4
T =2
grid=np.random.choice([0,1], size=(N,N))

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)
ax_slider = plt.axes(tuple([0.2, 0.1, 0.6, 0.03]))
ax_slider2 = plt.axes(tuple([0.2, 0.2, 0.7, 0.03]))
c_slider = Slider(ax_slider, "Chemical potential", -10, 10.0, valinit=C)
t_slider = Slider(ax_slider2, "Temperature",0.0, 4.0 , valinit=T)
cmpa = ListedColormap(['White', 'Orange'])

im = ax.imshow(grid, cmap =cmpa)
def update(frame):
        for i in range(N*N/2):
            i = np.random.randint(0,N-1)
            j = np.random.randint(0, N-1)
            C = c_slider.val
            T=t_slider.val
            energy=0
            energy_increment=-1
            #consider the probability of the particle's state being flipped
            #consider the energy if the particle exists
            if(i>0 and grid[i-1][j]==1):
                energy+=energy_increment
            if(i<N-1 and grid[i+1][j]==1):
                energy+=energy_increment
            if(j>0 and grid[i][j-1]==1):
                energy+=energy_increment
            if(j<N-1 and grid[i][j+1]==1):
                energy+=energy_increment
            if(i>0 and j>0 and grid[i-1][j-1]==1):
                energy+=energy_increment
            if(i>0 and j<N-1 and grid[i-1][j+1]==1):
                energy+=energy_increment
            if(i<N-1 and j>0 and grid[i+1][j-1]==1):
                energy+=energy_increment
            if(i<N-1 and j<N-1 and grid[i+1][j+1]==1):
                energy+=energy_increment
            probability_gradient = np.power(np.e, (-1*energy+C)/T)
            not_there= 1/(probability_gradient+1)
            x = np.random.random()
            if(x<not_there):
                grid[i,j] = 0
            else:
                grid[i,j] = 1
            


        im.set_array(grid)
        return grid


                
                



an1 = anim.FuncAnimation(fig=fig, func=update, frames=range(1000))
plt.show()

