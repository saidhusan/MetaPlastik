from django.core.files.storage import FileSystemStorage
import os
from PIL import Image
from django.conf import settings

# Compress a new Uploaded image to smaller size
def UploadImage(image,bottleCode):

    media_root = settings.MEDIA_ROOT       # url that includes root of computer
    media_url = settings.MEDIA_URL           # realtive media path

    fs = FileSystemStorage()
    fs.save(image.name, image)   # safe date from POST
    uploaded_file_url = os.path.join( media_root,image.name ) # place where file saved

    fileNewName = bottleCode + os.path.splitext(image.name)[1]           #get extension of new file
    compressedFileUrl = os.path.join(media_root,fileNewName)   # place where new compresed image would be saved

    FixImageSize(uploaded_file_url,compressedFileUrl) #create new image with new size

    os.remove(uploaded_file_url)    # deleted old big picture
    relativePath = os.path.join(media_url,fileNewName)   # place where new compresed image would be saved

    return relativePath


def FixImageSize(uploaded_file_url,newUrl):

    newImage = Image.open(uploaded_file_url)  # Object of Image
    size = newImage.size

    if (size[0] > size[1]):  # check if photo is in album version and fixes it
        newImage = newImage.rotate(-90, Image.NEAREST, expand=1)

    newImage = newImage.resize((960, 1280), Image.ANTIALIAS)  # resize Object
    newImage.save(newUrl, optimize=True, quality=95)  # saves new image
