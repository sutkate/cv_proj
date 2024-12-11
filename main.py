import filters
import cv2
import os
from parser import parse_args


def main():
    args = parse_args()
    if args.input == None:
        raise ValueError("Input path is None")

    img = cv2.imread(args.input)
    try:
        if args.mode == 'gray':
            result = filters.grayscale(img)
        elif args.mode == 'resize':
            if args.value is None:
                raise ValueError("Value is None")
            result = filters.resize(img, args.value)
        elif args.mode == 'sepia':
            result = filters.sepia(img)
        elif args.mode == 'vignette':
            if args.value is None:
                raise ValueError("Value is None")
            result = filters.vignette(img, int(args.value))
        elif args.mode == 'pixelate':
            if args.value is None:
                raise ValueError("Value is None")
            result = filters.pixelate(img, int(args.value))

        if args.output is not None:
            output_path = os.path.join(
                os.path.dirname(args.output),
                args.mode + "_" + os.path.basename(args.input)
            )
        else:
            output_path = os.path.join(
                os.path.dirname(args.input),
                args.mode + os.path.basename(args.input)
            )

        if result is not None:
            cv2.imwrite(output_path, result)

            cv2.imshow('Init image', img)
            cv2.imshow('Output image', result)
            cv2.waitKey(0)
        else:
            raise "variable result is None"
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()