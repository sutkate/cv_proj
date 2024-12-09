from typing import BinaryIO

import cv2
import numpy as np

def grayscale(img):
    if img.shape[2] != 3:
        raise ValueError("Input image must have 3 channels (RGB).")
    r, g, b = img[:, :, 0], img[:, :, 1], img[:, :, 2]
    result = 0.299 * r + 0.587 * g + 0.114 * b
    return result.astype(np.uint8)



def resize(img, value):
    new_hght = int(img.shape[0] * value)
    new_wdth = int(img.shape[1] * value)

    if new_hght <= 0 or new_hght <= 0:
        raise ValueError("New image must have positive height and height.")
    hght, wdth, nchannels = img.shape

    scale = {'x': wdth / new_wdth, 'y': hght / new_hght}

    x_ind = np.clip(np.floor(np.arange(new_wdth) * scale['x']).astype(int), 0, wdth - 1)
    y_ind = np.clip(np.floor(np.arange(new_wdth) * scale['y']).astype(int), 0, hght - 1)

    result = img[y_ind[:, None], x_ind]
    return result



def sepia(img):
    result = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

    B = img[:, :, 0]
    G = img[:, :, 1]
    R = img[:, :, 2]

    result[:, :, 0] = np.clip(0.272 * R + 0.534 * G + 0.131 * B, 0, 255)
    result[:, :, 1] = np.clip(0.349 * R + 0.686 * G + 0.168 * B, 0, 255)
    result[:, :, 2] = np.clip(0.393 * R + 0.769 * G + 0.189 * B, 0, 255)

    return result

def vignette(img, radius):
    result = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    height, width, nchannels = img.shape
    x = img.shape[1] // 2
    y = img.shape[0] // 2

    y_val, x_val = np.indices((height, width))

    distance = np.sqrt((x_val - x) ** 2 + (y_val - y) ** 2)
    coef = np.clip(1 - distance / radius, 0, 1)
    result = (img * coef[:, :, np.newaxis]).astype(np.uint8)

    return result

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        param['drawing'] = True
        param['start_point'] = (x, y)

    elif event == cv2.EVENT_LBUTTONUP:
        if param['drawing']:
            param['end_point'] = (x, y)
            img_copy = param['image'].copy()
            cv2.rectangle(img_copy, param['start_point'], param['end_point'], (0, 255, 0), 2)
            cv2.imshow('selected', img_copy)

    elif event == cv2.EVENT_MOUSEMOVE:
        param['drawing'] = False
        param['end_point'] = (x, y)

def select_region(img):
    params = {'drawing': False, 'start_point': None, 'end_point': None, "image": img}
    cv2.imshow('Select region', img)
    cv2.setMouseCallback('Select region', mouse_callback, param=params)
    cv2.waitKey(0)
    cv2.destroyWindow('Select region')

    if params['start_point'] and params['end_point']:
        return (params['start_point'][0], params['start_point'][1],
                params['end_point'][0] - params['start_point'][0],
                params['end_point'][1] - params['start_point'][1])
    else:
        return None

def pixelate(img, pixel_size):
    print('select region')

    region = select_region(img)
    if region is None:
        print('no region selected')
        return None

    x, y , w, h = region
    result = np.copy(img)

    for i in range(y, y + h, pixel_size):
        for j in range(x, x + w, pixel_size):
            # Извлечение блока
            block = result[i:i + pixel_size, j:j + pixel_size]
            if block.size == 0:
                continue
            avg_color = block.mean(axis=(0, 1)).astype(np.uint8)
            result[i:i + pixel_size, j:j + pixel_size] = avg_color
    return result



