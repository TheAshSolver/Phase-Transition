import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
N=100
grid=np.zeros(shape=(N, N), dtype= int)
for i in range(10000):
    x= np.random.randint(1, 99, 1)
    y= np.random.randint(1, 99, 1)
    grid[x,y]=1

fig, ax = plt.subplots()
ax.matshow(grid)
def update(frame):
    for i in range(N):
        for j in range(N):
            if
    ax.matshow(grid)
    return grid


                
                



an1 = anim.FuncAnimation(fig=fig, func=update, frames=range(1000))
plt.show()

