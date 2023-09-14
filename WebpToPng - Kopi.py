from PIL import Image
import sys
import time
from pathlib import Path

if len(sys.argv) > 1:
    imagepath = sys.argv[1]
    im = Image.open(Path(imagepath))
    im.convert("RGB")
    png_path = imagepath.rsplit('.', 1)[0] + '.png'
    im.save(png_path, "PNG")
