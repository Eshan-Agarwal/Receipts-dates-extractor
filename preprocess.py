IMAGE_SIZE = 1800   # Image size to resize it
import tempfile
import sys
import cv2
import numpy as np
from PIL import Image
from PIL import ImageFile
from extract_dates import extract_dates # input as receipt image and output as date and time on images.
import pandas as pd


def process_image_for_ocr(file_path):
    # TODO : Implement using opencv
    

    # returns dates after set dpi value to 300,300.

    temp_filename = set_image_dpi(file_path)
    
    r = extract_dates(temp_filename)
   

    return r
    

# Optical Character Recognition (OCR) works well in case when dots per inch (DPI) is 300,300 
def set_image_dpi(file_path):



    """
    Args:
        take path of images
    Returns:
        save images at 300,300 DPI
    """

    ImageFile.LOAD_TRUNCATED_IMAGES = True
    im = Image.open(file_path)
    im = im.convert('RGB')
    length_x, width_y = im.size
    factor = max(1, int(IMAGE_SIZE / length_x))
    size = factor * length_x, factor * width_y
    # size = (1800, 1800)
    im_resized = im.resize(size, Image.ANTIALIAS)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
    temp_filename = temp_file.name
    im_resized.save(temp_filename, dpi=(300, 300))
    return temp_filename

