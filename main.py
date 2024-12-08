import filters
import cv2 as cv
from parser import parse_args


def main():
    args = parse_args()

    if args.input == None:
        raise ValueError("Input path is None")

    img = cv.imread(args.input)

    if args.mode == 'gray':
        result = filters.grayscale(img)
    elif args.mode == 'resize':
        result = filters.resize(img, args.value)
    elif args.mode == 'sepia':
        return None
    elif args.mode == 'vignette':
        return None
    elif args.mode == 'pixelate':
        return None
    else:
        raise 'Unsupported \'mode\' value'

    cv.imshow('Init image', img)
    cv.imshow('Output image', result)
    cv.waitKey(0)

if __name__ == '__main__':
    main()