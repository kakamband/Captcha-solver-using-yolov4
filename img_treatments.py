from PIL import Image
import numpy as np
import cv2

UPLOADED_TREATED_DIR = 'uploaded treated/'


# -------------------
#    Treatment 1
#
#  Remove Background
# -------------------


def treatment1(img_path):
    # Read image as RGBA
    im = Image.open(img_path)
    # print(pic)
    im = im.convert('RGBA')
    data = np.array(im)

    # just use the rgb values for comparison
    rgb = data[:, :, :3]
    color = [192, 192, 192]  # Original value - color to be changed
    white = [255, 255, 255, 255]  # Color to change - new color
    mask = np.all(rgb == color, axis=-1)

    # change all pixels that match color to white
    data[mask] = white

    # set of colors to change
    rgb = data[:, :, :3]
    color = [240, 248, 255]  # Original value
    mask = np.all(rgb == color, axis=-1)
    data[mask] = white
    new_im = Image.fromarray(data)

    rgb = data[:, :, :3]
    color = [190, 190, 190]  # Original value
    mask = np.all(rgb == color, axis=-1)
    data[mask] = white
    new_im = Image.fromarray(data)

    rgb = data[:, :, :3]
    color = [191, 191, 191]  # Original value
    mask = np.all(rgb == color, axis=-1)
    data[mask] = white
    new_im = Image.fromarray(data)

    rgb = data[:, :, :3]
    color = [253, 245, 230]  # Original value
    mask = np.all(rgb == color, axis=-1)
    data[mask] = white
    new_im = Image.fromarray(data)

    rgb = data[:, :, :3]
    color = [1, 255, 255]  # Original value
    mask = np.all(rgb == color, axis=-1)
    data[mask] = white
    new_im = Image.fromarray(data)

    rgb = data[:, :, :3]
    color = [1, 254, 254]  # Original value
    mask = np.all(rgb == color, axis=-1)
    data[mask] = white
    new_im = Image.fromarray(data)

    rgb = data[:, :, :3]
    color = [1, 253, 253]  # Original value
    mask = np.all(rgb == color, axis=-1)
    data[mask] = white
    new_im = Image.fromarray(data)

    rgb = data[:, :, :3]
    color = [224, 255, 255]  # Original value
    mask = np.all(rgb == color, axis=-1)
    data[mask] = white
    new_im = Image.fromarray(data)

    rgb = data[:, :, :3]
    color = [240, 248, 255]  # Original value
    mask = np.all(rgb == color, axis=-1)
    data[mask] = white
    new_im = Image.fromarray(data)

    rgb = data[:, :, :3]
    color = [255, 228, 225]  # Original value
    mask = np.all(rgb == color, axis=-1)
    data[mask] = white
    new_im = Image.fromarray(data)

    rgb = data[:, :, :3]
    color = [240, 248, 255]  # Original value
    mask = np.all(rgb == color, axis=-1)
    data[mask] = white
    new_im = Image.fromarray(data)

    rgb = data[:, :, :3]
    color = [252, 244, 229]  # Original value
    mask = np.all(rgb == color, axis=-1)
    data[mask] = white
    new_im = Image.fromarray(data)

    rgb = data[:, :, :3]
    color = [218, 112, 146]  # Original value
    mask = np.all(rgb == color, axis=-1)
    data[mask] = white
    new_im = Image.fromarray(data)

    rgb = data[:, :, :3]
    color = [156, 188, 156]  # Original value
    mask = np.all(rgb == color, axis=-1)
    data[mask] = white
    new_im = Image.fromarray(data)

    rgb = data[:, :, :3]
    color = [254, 247, 219]  # Original value
    mask = np.all(rgb == color, axis=-1)
    data[mask] = white
    new_im = Image.fromarray(data)

    rgb = data[:, :, :3]
    color = [0, 255, 255]  # Original value
    mask = np.all(rgb == color, axis=-1)
    data[mask] = white
    new_im = Image.fromarray(data)

    rgb = data[:, :, :3]
    color = [0, 254, 254]  # Original value
    mask = np.all(rgb == color, axis=-1)
    data[mask] = white
    new_im = Image.fromarray(data)

    rgb = data[:, :, :3]
    color = [251, 243, 228]  # Original value
    mask = np.all(rgb == color, axis=-1)
    data[mask] = white
    new_im = Image.fromarray(data)

    rgb = data[:, :, :3]
    color = [230, 230, 230]  # Original value
    mask = np.all(rgb == color, axis=-1)
    data[mask] = white
    new_im = Image.fromarray(data)

    rgb = data[:, :, :3]
    color = [173, 173, 173]  # Original value
    mask = np.all(rgb == color, axis=-1)
    data[mask] = white
    new_im = Image.fromarray(data)

    rgb = data[:, :, :3]
    color = [254, 227, 224]  # Original value
    mask = np.all(rgb == color, axis=-1)
    data[mask] = white
    new_im = Image.fromarray(data)

    rgb = data[:, :, :3]
    color = [223, 254, 254]  # Original value
    mask = np.all(rgb == color, axis=-1)
    data[mask] = white
    new_im = Image.fromarray(data)

    rgb = data[:, :, :3]
    color = [239, 247, 254]  # Original value
    mask = np.all(rgb == color, axis=-1)
    data[mask] = white
    new_im = Image.fromarray(data)

    rgb = data[:, :, :3]
    color = [255, 248, 220]  # Original value
    mask = np.all(rgb == color, axis=-1)
    data[mask] = white
    new_im = Image.fromarray(data)

    rgb = data[:, :, :3]
    color = [217, 111, 146]  # Original value
    mask = np.all(rgb == color, axis=-1)
    data[mask] = white
    new_im = Image.fromarray(data)

    rgb = data[:, :, :3]
    color = [253, 246, 218]  # Original value
    mask = np.all(rgb == color, axis=-1)
    data[mask] = white
    new_im = Image.fromarray(data)

    rgb = data[:, :, :3]
    color = [238, 246, 253]  # Original value
    mask = np.all(rgb == color, axis=-1)
    data[mask] = white
    new_im = Image.fromarray(data)

    rgb = data[:, :, :3]
    color = [219, 112, 147]  # Original value
    mask = np.all(rgb == color, axis=-1)
    data[mask] = white
    new_im = Image.fromarray(data)
    new_im.save(UPLOADED_TREATED_DIR + img_path.split('/')[1])
    new_im = cv2.imread(UPLOADED_TREATED_DIR + img_path.split('/')[1])

    return new_im


# -------------------
#    Treatment 4
#
#  Isolate letters and numbers
# -------------------


def treatment4(img):

    lower = np.array([230, 230, 230])
    upper = np.array([255, 255, 255])
    my_mask = cv2.inRange(img, lower, upper)

    gray = cv2.threshold(my_mask, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    gray = cv2.medianBlur(gray, 3)

    return gray



