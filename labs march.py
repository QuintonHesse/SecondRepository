

def calc_pyramid_volume(length,width,height):
    base_area = length*width
    volume = base_area*height*1/3
    return volume

length = float(input('length'))
width = float(input('width'))
height = float(input('height'))
print('Volume for', length, width, height, "is:", calc_pyramid_volume(length, width, height))