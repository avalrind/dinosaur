import numpy as np
from PIL import Image , ImageDraw

def fig_to_np_array(fig):
    '''
    Convert Figure to Numpy Array

    Args :
    
        1) fig : Figure
            Figure to Convert

    Returns :
    
        1) buf : Numpy Array
            Numpy Array of the Figure
    '''
    
    fig.canvas.draw()

    w, h = fig.canvas.get_width_height()
    buf = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8)
    buf.shape = (h, w, 3)

    return buf

def norm(value , max_value , min_value) : 
    '''
    Normalize Value

    Args :

        1) value : Float
            Value to Normalize

        2) max_value : Float
            Maximum Value

        3) min_value : Float
            Minimum Value

    Returns :

        1) norm_value : Float
    '''

    return (value - min_value) / (max_value - min_value)

def get_png(figure) :
    '''
    Get PNG from Figure

    Args :

        1) figure : Figure
            Figure to Convert

    Returns :

        1) image : Image
            Image of the Figure
    '''

    figure = fig_to_np_array(figure)
    image = Image.new('RGB' , (figure.shape[1] , figure.shape[0]))
    draw = ImageDraw.Draw(image)

    for row in range(figure.shape[0]) :

        for col in range(figure.shape[1]) :

            if figure[row][col][0] != 0 : draw.point((col , row) , fill = (figure[row][col][0] , figure[row][col][1] , figure[row][col][2]))

    return image

def map_to_pixels(points , width , height , width_pad , height_pad , dpi) :
    '''
    Map Points to Pixels

    Args :

        1) points : List
            List of Points
        
        2) width : Int
            Width of the Image

        3) height : Int
            Height of the Image

        4) width_pad : Int
            Width Padding

        5) height_pad : Int
            Height Padding

        6) dpi : Int
            Dots per Inch
    '''

    x_points = [x for x , _ in points]
    y_points = [y for _ , y in points]
    x_max = max(x_points)
    y_max = max(y_points)
    x_min = min(x_points)
    y_min = min(y_points)

    x_max += 0.005 * x_max * dpi
    y_max += 0.005 * y_max * dpi

    pixel_points = []

    for x , y in points :

        x_norm = norm(x , x_max , x_min)
        y_norm = norm(y , y_max , y_min)

        x_scale = x_norm * width
        y_scale = y_norm * height

        y_scale = height - y_scale # PIL starts from top-left 

        x_scale += width_pad
        y_scale -= height_pad

        pixel_points.append((
            x_scale , 
            y_scale 
))

    return pixel_points

def get_pixels(point , 
               right_pad , left_pad , 
               up_pad , down_pad) : 
    '''
    Get Pixels

    Args :

        1) point : Tuple
            Point

        2) right_pad : Int
            Right Padding

        3) left_pad : Int
            Left Padding

        4) up_pad : Int
            Up Padding

        5) down_pad : Int
            Down Padding

    Returns :
    
            1) pixels : List
                List of Pixels
    '''

    pixels = [point]

    for padding in range(right_pad + 1) : pixels.append((point[0] + padding , point[1]))
    for padding in range(left_pad + 1) : pixels.append((point[0] - padding , point[1]))
    for padding in range(up_pad + 1) : pixels.append((point[0] , point[1] + padding))
    for padding in range(down_pad + 1) : pixels.append((point[0] , point[1] - padding))

    x_set = set([
        pixel[0]
        for pixel
        in pixels
    ])
    y_set = set([
        pixel[1]
        for pixel
        in pixels
    ])

    pixels = [
        (x_cor , y_cor)
        for x_cor in x_set
        for y_cor in y_set
    ]

    return pixels
