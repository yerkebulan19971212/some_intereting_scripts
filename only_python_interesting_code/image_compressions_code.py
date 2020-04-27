from PIL import Image


def from_jpeg_to_webp():
    image = Image.open('/home/abyer/Downloads/download.jpeg')
    image.convert('RGB')
    image.save('/home/abyer/Desktop/test.webp', 'webp')


from_jpeg_to_webp()
