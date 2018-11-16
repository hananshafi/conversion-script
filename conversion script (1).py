from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
from glob import glob
import PIL
import sys
import os


path = "C:/Users/hgani/Desktop/finalimages1/"
path_originals = "C:/Users/hgani/Desktop/cert lab data/png images/DAIMLER_HIGH/"
if not os.path.exists(path):
    os.makedirs(path)

def compress_image(image, infile):
    size = 800, 480
    width = 800
    height = 480
    listing = os.listdir(path_originals)

    name = infile.split('.')
    first_name = path+'/'+name[0] + '.jpg'
    if image.size[0] > width and image.size[1] > height:
        image.thumbnail(size, Image.ANTIALIAS)
        image.save(first_name, quality=85)
    elif image.size[0] > width:
        wpercent = (width/float(image.size[0]))
        height = int((float(image.size[1])*float(wpercent)))
        image = image.resize((width,height), PIL.Image.ANTIALIAS)
        image.save(first_name,quality=85)
    elif image.size[1] > height:
        wpercent = (height/float(image.size[1]))
        width = int((float(image.size[0])*float(wpercent)))
        image = image.resize((width,height), PIL.Image.ANTIALIAS)
        image.save(first_name, quality=85)
    else:
        image.save(first_name, quality=85)


def processImage():
    listing = os.listdir(path_originals)
    for infile in listing:
        img = Image.open(path_originals+infile)
        name = infile.split('.')
        first_name = path+'/'+name[0] + '.jpg'

        if img.format == "JPEG":
            image = img.convert('RGB')
            compress_image(image, infile)
            img.close()

        elif img.format == "GIF":
            i = img.convert("RGBA")
            bg = Image.new("RGBA", i.size)
            image = Image.composite(i, bg, i)
            compress_image(image, infile)
            img.close()

        elif img.format == "PNG":
            try:
                image = Image.new("RGB", img.size, (255,255,255))
                image.paste(img,img)
                compress_image(image, infile)
            except ValueError:
                image = img.convert('RGB')
                compress_image(image, infile)
            img.close()

        elif img.format == "BMP":
            image = img.convert('RGB')
            compress_image(image, infile)
            img.close()

processImage()