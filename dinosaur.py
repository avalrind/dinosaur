import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
from IPython.display import HTML
import numpy as np

def lineplot(x_data , y_data , x_label = '' , y_label = '' , title = '') : 

    figure , axes = plt.subplots()
    x_temp = []
    y_temp = []
    ln , = plt.plot(
        [] , 
        [] , 
        'y-' , 
        linewidth = 3
    )

    axes.spines['right'].set_visible(False)
    axes.spines['top'].set_visible(False)

    axes.spines['left'].set_linewidth(3)  # Set the thickness of the left spine
    axes.spines['bottom'].set_linewidth(3)  # Set the thickness of the bottom spine

    axes.spines['left'].set_position('zero')
    axes.spines['bottom'].set_position('zero')

    axes.xaxis.set_ticks_position('bottom')
    axes.yaxis.set_ticks_position('left')

    figure.set_facecolor('black')
    axes.set_facecolor('black')

    axes.spines['left'].set_color('white')
    axes.spines['bottom'].set_color('white')

    axes.tick_params(colors='white')

    def init() : 

        axes.set_xlim(0 , max(x_data))
        axes.set_ylim(0 , max(y_data))

        return ln ,

    def update(frame) : 

        x_temp.append(x_tempe[frame])
        y_temp.append(y_tempe[frame])

        axes.margins(x=0, y=0)

        ln.set_data(x_temp , y_temp)

        return ln,

    offsets = 5

    x_tempe = []
    y_tempe = []

    for index in range(len(x_data)) : 

        if index < offsets or index > len(x_data) - offsets : 
            
            x_tempe.extend([x_data[index]] * 5)
            y_tempe.extend([y_data[index]] * 5)

        else : 

            x_tempe.append(x_data[index])
            y_tempe.append(y_data[index])

    ani = FuncAnimation(
        figure , 
        update , 
        frames = range(len(x_tempe)) , 
        init_func = init , 
        blit = True , 
        interval = 200
    )

    return HTML(ani.to_jshtml())
