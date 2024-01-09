from io import BytesIO
from PIL import Image, ImageDraw, ImageOps, ImageCms

def rounded_image(filename:str, folder:str, size:tuple=(450, 450)):
    try:
        image = Image.open(filename)
    except FileNotFoundError:
        return False
    
    image = remove_icc(image)

    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + size, fill=255)

    output = ImageOps.fit(image, mask.size, centering=(0.5, 0.5))
    output.putalpha(mask)

    name = filename.split('/')[-1].split('.')
    name = name[0] + '.png'
    new_filename = folder + name
    output.save(new_filename)

    return new_filename

def remove_icc(image: Image.Image) -> Image.Image:

    icc_bytes = image.info.get("icc_profile") or b""
    if not icc_bytes:
        return image.copy()

    orig_icc = ImageCms.getOpenProfile(BytesIO(icc_bytes)).profile
    srgb_icc = ImageCms.createProfile("sRGB")

    mode = image.mode
    tmp_image = None
    if mode == "CMYK":
        mode = "RGB"
    elif mode == "P":
        mode = "RGBA"
        tmp_image = image.convert("RGBA")

    try:
        result = ImageCms.profileToProfile(
            tmp_image or image, orig_icc, srgb_icc, outputMode=mode
        )
    finally:
        if tmp_image is not None:
            tmp_image.close()

    result.info.pop("icc_profile")

    if image.info.get("exif"):
        result.info["exif"] = image.info["exif"]

    return result