from PIL import Image, ImageSequence, ImageDraw, ImageFont
import imageio.v2 as imageio
import shutil
import os

brightnessForChars = {
    'l': {
        range(0, 51): "#",
        range(51, 76): "$",
        range(76, 101): "&",
        range(101, 126): "!",
        range(126, 151): "%",
        range(151, 201): "*",
        range(201, 256): "^"
    },
    'd': {
        range(0, 51): ".",
        range(51, 76): "!",
        range(76, 101): "/",
        range(101, 126): "v",
        range(126, 151): "J",
        range(151, 201): "m",
        range(201, 256): "#"
    }
}

class imgToASCII:
    def __init__(self, fileName, background):
        self.fileName = fileName
        self.background = background

    def brightnessCheker(self, rgb_color):
        # this command:
        # return 'light' if luminance > 127.5 else 'dark'
        # is for basic colour operations, and it does the same thing as the functions current return
        # but idk why i like this more lmao
        brightness = sum(rgb_color) / 3
        return int(brightness)

    def checkFile(self):
        files = os.listdir('images')
        for file in files:
            if file.startswith(self.fileName):
                return file

    def ASCIIWrtier(self, background, brightness):
        for x, symbol in brightnessForChars[background].items():
            if brightness in x:
                return symbol

    def imageToASCII(self):
        pic = imageio.imread(f'images/{self.checkFile()}') # readiing frame with imageio

        currentImg = Image.open(f'images/{self.checkFile()}') # reading frame with pillow
        currentImg = currentImg.convert('RGB')

        with open(f'artworks/{self.fileName}.txt', 'a') as file:
            # creates
            for h in range(pic.shape[0]):
                for w in range(pic.shape[1]):

                    pixel_value = currentImg.getpixel((w, h))
                    brightness = self.brightnessCheker(pixel_value)

                    pixel = self.ASCIIWrtier(self.background, brightness)

                    file.write(pixel)

                file.write("\n")
