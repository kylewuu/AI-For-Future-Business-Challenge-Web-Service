import requests
import base64
import threading
from picamera import PiCamera

camera = PiCamera()
camera.start_preview()


def take_image():
    image = camera.capture('/home/pi/Desktop/image.jpg')
    return image


def encode_image(image_file):
    encoded_string = base64.b64encode(image_file.read())
    return encoded_string


def printit():
    threading.Timer(5.0, printit).start()
    image = take_image()
    encoded_image = encode_image(image)
    url = 'https://image-detection-docker.azurewebsites.net/status'
    myobj = {'image': encoded_image}

    requests.post(url, data=myobj)


printit()
