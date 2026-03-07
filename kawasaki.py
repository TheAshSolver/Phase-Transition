import taichi as ti
import taichi.math as tm
import numpy as np
N=1000
##initialize taichi to use custom gpu
ti.init(arch=ti.gpu)
T=2

##For ising model
#we need a two 2d grid
array = ti.field( dtype=ti.f32, shape=(N,N))
array.from_numpy(np.random.choice([0,1], size=(N,N)).astype(np.int32))

rgb = ti.Vector.field(3, dtype=ti.types.f32, shape=(N,N))

offsets=[(-1,0), (1,0), (0,1), (0,-1)]  

@ti.kernel
def update():
    for i, j in array:
        #compute swap
        row= ti.random(dtype=int)%N
        column = ti.random(dtype=int)%N
        while array[i,j] == array[row, column]:
           row= ti.random(dtype=int)%N
           column = ti.random(dtype=int)%N
        neighbours=0
        
        for k_idx in ti.static(range(len(offsets))):
           k= offsets[k_idx]
           (m,n)= (i+k[0], j+k[1])
           if(0<=m<N and 0<=n<N):
               neighbours-=array[m,n]*array[i,j]
           (m,n) = (row+k[0], column+k[1])
           if(0<=m<N and 0<=n<N):
               neighbours-=array[m,n]*array[row,column]
        for k_idx in ti.static(range(len(offsets))):
           k= offsets[k_idx]
           (m,n)= (i+k[0], j+k[1])
           if(0<=m<N and 0<=n<N):
               neighbours+=array[m,n]*(1-array[i,j])
           (m,n) = (row+k[0], column+k[1])
           if(0<=m<N and 0<=n<N):
               neighbours+=array[m,n]*(1-array[row,column])
        probability_ratio = 1/(1+tm.exp(neighbours/T))
        random_number = ti.random(dtype=ti.f32)
        if(random_number>probability_ratio):
            array[i, j] = 1-array[i,j]
            array[row, column] = 1-array[row, column]
        rgb[i, j] =ti.Vector([array[i,j], 0, 0])
        rgb[row, column] = ti.Vector([array[row, column], 0,0])


gui = ti.GUI("Kawasaki", res=(N,N), fast_gui = True)

while gui.running:
    update()

    gui.set_image(rgb)
   

    gui.show()

           
        
        


        
       
               

