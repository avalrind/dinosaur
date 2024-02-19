import matplotlib.pyplot as plt
from moviepy.editor import ImageSequenceClip
from PIL import ImageDraw
import numpy as np
from copy import deepcopy

from helper import (
    get_png , 
    map_to_pixels , 
    get_pixels
)

import numpy as np

def lineplot(x_data , y_data = None ,
             linewidth = 3 , beautify = True ,
             figsize = (10 , 6) , dpi = 72 , fps = 25 ,
             right_pad = 0 , left_pad = 0 , up_pad = 0 , down_pad = 0 ,
             rgb = (255 , 255 , 255)) :
    
    '''
    Line Plot Animation Function for Dinosaur

    Args : 

        1) x_data : Iterable  
            X - Axis Data

        2) y_data : Iterable
            Y - Axis Data

        3) linewidth : int
            Width of the Axes Line

        4) beautify : bool
            If True , Beautify the Plot

        5) figsize : Tuple
            Size of the Figure

        6) dpi : int
            Dots per Inch

        7) fps : int
            Frames per Second

        8) right_pad : int
            Width to the Right of the Point

        9) left_pad : int
            Width to the Left of the Point

        10) up_pad : int
            Width to the Up of the Point

        11) down_pad : int 
            Width to the Down of the Point

        12) rgb : Tuple
            RGB Color of the Line
        
    Returns :
    
            1) Animation
                Line Plot Animation
    '''

    figure , axes = plt.subplots(figsize = figsize , dpi = dpi)

    if not y_data : y_data = list(range(len(x_data)))

    if beautify :
        axes.spines['right'].set_visible(False)
        axes.spines['top'].set_visible(False)

    axes.spines['left'].set_linewidth(linewidth)
    axes.spines['bottom'].set_linewidth(linewidth)

    axes.spines['left'].set_position('zero')
    axes.spines['bottom'].set_position('zero')

    axes.xaxis.set_ticks_position('bottom')
    axes.yaxis.set_ticks_position('left')

    figure.set_facecolor('black')
    axes.set_facecolor('black')

    axes.spines['left'].set_color('white')
    axes.spines['bottom'].set_color('white')

    axes.tick_params(colors='white')

    axes.set_xlim(0 , max(x_data))
    axes.set_ylim(0 , max(y_data))

    points = [
        (x , y)
        for x , y
        in zip(x_data , y_data)
    ]

    height = (figsize[0]) * dpi
    width = (figsize[1]) * dpi

    points = map_to_pixels(points , height , width , width_pad = (dpi * figsize[0]) / 7.2 , height_pad = (figsize[1] * dpi) / 8.64 , dpi = dpi)
    plane_mask = get_png(figure)

    anim_array = [plane_mask]

    for point in points  :

        temp_plane_mask = deepcopy(plane_mask)

        draw = ImageDraw.Draw(temp_plane_mask)

        pixels = get_pixels(point , right_pad , left_pad , up_pad , down_pad)

        for point in pixels : draw.point(point , fill = (rgb[0] , rgb[1] , rgb[2]))

        anim_array.append(temp_plane_mask)

        plane_mask = deepcopy(temp_plane_mask)

    anim_array = [np.array(val) for val in anim_array]

    images = [np.uint8(frame[..., ::-1]) for frame in anim_array]

    clip = ImageSequenceClip(images, fps=fps)

    del images , anim_array

    return clip.ipython_display(fps=10, autoplay=True, loop=True)
