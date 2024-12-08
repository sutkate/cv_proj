import cv2
import numpy as np

def grayscale(img):
    if img.shape[2] != 3:
        raise ValueError("Input image must have 3 channels (RGB).")
    r, g, b = img[:, :, 0], img[:, :, 1], img[:, :, 2]
    result = 0.299 * r + 0.587 * g + 0.114 * b
    return result.astype(np.uint8)

def resize(img, new_wdth, new_hght):
    if new_hght <= 0 or new_hght <= 0:
        raise ValueError("New image must have positive height and height.")
    hght, wdth, nchannels = img.shape

    scale = {'x': wdth / new_wdth, 'y': hght / new_hght}

    x_ind = np.clip(np.floor(np.arange(new_wdth) * scale['x']).astype(int), 0, wdth - 1)
    y_ind = np.clip(np.floor(np.arange(new_wdth) * scale['y']).astype(int), 0, hght - 1)

    result = img[y_ind[:, None], x_ind]
    return result
