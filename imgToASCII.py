import imageio
from PIL import Image
import subprocess
import os

os.chdir("images")
subprocess.run(['powershell', 'ls'], shell=False) # displays the imgs in the images folder bc why not
os.chdir("..")

print("ONLY WORKS WITH JPEG FILES PLEASE I BEG YOU DO NOT USE .PNG RN ok thanks!!!!!!") # future me please make it PNG compatible as well
img = input("select the img you want: ") # probably should use a try and except block rn
background = input("are you displaying it on a dark or light background [d,l]?\n") # thank you ascii wiki

pic = imageio.imread(f'images/{img}.jpg')
im = Image.open(f'images/{img}.jpg')

def brightnessCheker(rgb_color):
    # this command:
    # return 'light' if luminance > 127.5 else 'dark'
    # is for basic colour operations, and it does the same thing as the functions current return
    # but idk why i like this more lmao
    brightness = sum(rgb_color) / 3
    return brightness

with open(f'artworks/{img.split(".")[0]}.txt', 'a') as file:
    # creates 
    file.write("\n")

    for h in range(pic.shape[0]):
        for w in range(pic.shape[1]):

            pixel_value = im.getpixel((w, h))
            light = brightnessCheker(pixel_value)

            if background == 'l':
                if light <= 50:
                    file.write("# ")
                elif light <= 75:
                    file.write("$ ")
                elif light <= 100:
                    file.write("& ")
                elif light <= 125:
                    file.write("! ")
                elif light <= 150:
                    file.write("% ")
                elif light <= 200:
                    file.write("* ")
                else:
                    file.write("^ ")

            if background == 'd':
                if light <= 50:
                    file.write(". ")
                elif light <= 75:
                    file.write("! ")
                elif light <= 100:
                    file.write("/ ")
                elif light <= 125:
                    file.write("v ")
                elif light <= 150:
                    file.write("J ")
                elif light <= 200:
                    file.write("m ")
                else:
                    file.write("# ")

        file.write("\n")

# basic properties of the image
print('Type of the image:', type(pic))
print('Shape of the image:', pic.shape)
print('Image Height:', pic.shape[0])
print('Image Width:', pic.shape[1])
print('Dimension of Image:', pic.ndim)
print('Image size:', pic.size)
print('Maximum RGB value in this image:', pic.max())
print('Minimum RGB value in this image:', pic.min())
