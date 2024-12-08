import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i', '--input',
        help='path to input image',
        type=str,
        dest='input',
    )
    parser.add_argument(
        '-o', '--output',
        help='path to output image',
        type=str,
        dest='output',
        default='output.jpg',
    )
    parser.add_argument(
        '-m', '--mode',
        help='Mode (\'image\', \'gray\', \'resize\', \'sepia\', \'vignette\', \'pixelate\')',
        type=str,
        dest='mode',
        default='image',
    )
    parser.add_argument(
        '-v', '--value',
        help='input strength of filter',
        type=float,
        dest='value',
        default=1,
    )
    parser.add_argument(
        '-r', '--radius',
        help='radius of filter',
        type=int,
        dest='radius',
        default=150,
    )
    parser.add_argument(
        '-p', '--pixelate',
        help='pixelate',
        type=int,
        dest='pixelate',
        default=15,
    )
    args = parser.parse_args()
    return args