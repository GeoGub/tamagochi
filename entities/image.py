from PIL import Image, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

with Image.open("d:\\tamagochi\\entities\\IMG_5747.png") as img:
    imgSmall = img.resize((35,35), resample=Image.Resampling.BILINEAR)
    result = imgSmall.resize(img.size, Image.Resampling.NEAREST)
    # result.load()
    result = result.convert("L")
    result.show()
