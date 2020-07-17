

from urllib.parse import urlparse
import requests
import os
import platform
from PIL import Image, ExifTags, ImageFont, ImageDraw, ImageFilter

from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse


def is_valid(url):
    """
    Checks whether `url` is a valid URL.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


def get_all_images(url):
    """
    Returns all image URLs on a single `url`
    """
    soup = bs(requests.get(url).content, "html.parser")
    urls = []
    for img in soup.find_all("img"):
        img_url = img.attrs.get("src")
        if not img_url:
            # if img does not contain src attribute, just skip
            continue
        # make the URL absolute by joining domain with the URL that is just extracted
        img_url = urljoin(url, img_url)
        # remove URLs like '/hsts-pixel.gif?c=3.2.5'
        try:
            pos = img_url.index("?")
            img_url = img_url[:pos]
        except ValueError:
            pass
        # finally, if the url is valid
        if is_valid(img_url):
            urls.append(img_url)
    return urls


def download(url, pathname):
    """
    Downloads a file given an URL and puts it in the folder `pathname`
    """
    # if path doesn't exist, make that path dir
    if not os.path.isdir(pathname):
        os.makedirs(pathname)
    # download the body of response by chunk, not immediately
    response = requests.get(url, stream=True)

    # get the total file size
    file_size = int(response.headers.get("Content-Length", 0))

    # get the file name
    filename = os.path.join(pathname, url.split("/")[-1])

    # progress bar, changing the unit to bytes instead of iteration (default by tqdm)
    progress = response.iter_content(1024)
    with open(filename, "wb") as f:
        for data in progress:
            # write data read to the file
            f.write(data)


def main(url, path):
    # get all images
    imgs = get_all_images(url)
    for img in imgs:
        # for each img, download it
        download(img, path)


def insertText(imageOBJ, title, picture):
    """Insert the Text of JobTitle to Image

    Args:
        imageOBJ (PIL): [image]
        title (string): [job title string]
        picture (string): [picture path string]
    """
    imageOBJ = Image.open(os.path.join('output_images', picture))
    draw_text = ImageDraw.Draw(imageOBJ)
    #Selects Font
    font = ImageFont.truetype("fonts/Syne-Regular.otf", 14)
    draw_text.text((50, 400), str(title), (26, 0, 0), font)
    #Saves Image after writing
    newPath = os.path.join('output_images', picture)
    imageOBJ.save(newPath, quality=100)


def findAllTitles(url):
    """Finds all Job Titles on Web page

    Args:
        url (string): URL of web page

    Returns:
        [list]: [list of job titles]
    """
    titlesList = []
    soup = bs(requests.get(url).content, "html.parser")
    titles = soup.findAll('h5')
    for title in titles:
        val = title.getText()
        titlesList.append(val)
    return titlesList


def getImagesPath():
    try:
        my_system = platform.system()

        if my_system == "Windows":
            root_fs = "C:\\Git\IT414-VictorIfezue\week10Assignment"
        else:
            root_fs = "/Git/IT414-VictorIfezue/week10Assignment"

        final_filepath = os.path.join(root_fs, "images")
        return final_filepath
    except Exception as error:
        print(error)


def zipdir(path, ziph):
    """Zip File and places in folder

    Args:
        path (): [description]
        ziph ([type]): [description]
    """
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

