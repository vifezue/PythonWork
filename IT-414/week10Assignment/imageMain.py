import re
import requests
from bs4 import BeautifulSoup
from PIL import Image, ExifTags, ImageFont, ImageDraw, ImageFilter
from functions.functionLibrary import *
import zipfile


imagesPath = getImagesPath()

# site URL
siteURL = "https://ool-content.walshcollege.edu/CourseFiles/IT/IT414/MASTER/Week10/WI20-Assignment/employees/index.php"

# Delete existing files
filesToDelete = [i for i in os.listdir(imagesPath)]
if len(filesToDelete) > 0:
    for file in filesToDelete:
        os.remove(os.path.join(imagesPath, file))

# fetch all images and save to folder
main(siteURL, "images")

# get job titles
jobTitles = findAllTitles(siteURL)

# get files from images folder
files = [i for i in os.listdir(imagesPath)]

for picture in files:
    logoImage = Image.open(
        'images/xsoftware_inc_logo.png.pagespeed.ic.sYxoMulhaS.png')
    image1 = Image.open(os.path.join(imagesPath, picture))

    back_im = image1.copy()
    back_im.paste(logoImage, (50, 415),mask = logoImage)

    newPath = os.path.join('output_images', picture)
    back_im.save(newPath, quality=100)
    # Find Match for Image Text by file name
    for title in jobTitles:
        keywordStr = str(title).split(' ')
        pictureStr = str(picture).split('_')
        pictureStr = str(pictureStr[0]).replace('x', '')
        if keywordStr[0].lower() in pictureStr.lower():
            # Insert Title To Images
            insertText(image1, title, picture)

zf = zipfile.ZipFile("images/myOutputZipfile.zip", "w")
for dirname, subdirs, files in os.walk("output_images"):
    zf.write(dirname)
    for filename in files:
        zf.write(os.path.join(dirname, filename))
zf.close()

