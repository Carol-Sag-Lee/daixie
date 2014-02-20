# -*- coding: utf-8 -*-

import os
import re
from hashlib import md5
from PIL import Image, ImageOps
from werkzeug.utils import secure_filename

from heji import app, db


#
# common
#
def format_format(format):
    format = format.lower()
    if format in ['jpg', 'jpeg']:
        return 'jpg'
    return format

#
# photo
# get photo path with pid
#

def photo_path(id, create=False):
	folder = '%s/%s' % (app.config['DIR_IMAGES'], id)
	if create and not os.path.isdir(folder):
		os.makedirs(folder)

	return folder

def photo_name(name, format='jpg'):
	format = format_format(format)
	return secure_filename(name + '.' + format)

def save_photo(id, photo_pil, photo_name):
	path = photo_path(id, create=True)
	photo_path_and_photo_name = os.path.join(path, photo_name)
	photo_pil.save(photo_path_and_photo_name)
	return photo_path_and_photo_name

def save_photo_with_certificate(id, photo):
	photo.seek(0)
	photo_pil = Image.open(photo)
	name = photo_name('photo_with_certificate', format=photo_pil.format)
	return save_photo(id, photo_pil, name)

def save_photo_with_stu_card(id ,photo):
	photo.seek(0)
	photo_pil = Image.open(photo)
	name = photo_name('photo_with_stu_card', format=photo_pil.format)
	return save_photo(id, photo_pil, name)