from PIL import Image, ImageFilter
from urllib.request import urlopen
from pathlib import Path

# Ask user to choose filter and image
print('This program supports:\n (1)BLUR\n (2)CONTOUR\n (3)DETAIL\n (4)EDGE_ENHANCE\n (5)EDGE_ENHANCE_MORE\n (6)EMBOSS\n (7)FIND_EDGES\n (8)SMOOTH\n (9)SMOOTH_MORE\n (10)SHARPEN.')
print()
filter = input('Type the number of a filter you would like to use: ')
print()
source = input('Type the image url or an absolute path to your image: ')

# Dictionary of available filters
filter_dict = {'1': ImageFilter.BLUR,
            '2': ImageFilter.CONTOUR,
            '3': ImageFilter.DETAIL,
            '4': ImageFilter.EDGE_ENHANCE,
            '5': ImageFilter.EDGE_ENHANCE_MORE,
            '6': ImageFilter.EMBOSS,
            '7': ImageFilter.FIND_EDGES,
            '8': ImageFilter.SMOOTH,
            '9': ImageFilter.SMOOTH_MORE,
            '10': ImageFilter.SHARPEN
            }

# Check if filter chosen by user if available
if filter not in filter_dict:
        raise ValueError("Unknown filter type.")

# Separate file name and its extension from the url or path input by the user
file_name = Path(source).stem
file_extension = Path(source).suffixes

# Choose how to open a file, then filter, then save, then show filtered image
if 'http' in source:
    with Image.open(urlopen(source)) as original:
        filtered = original.filter(filter_dict[filter])
        filtered.save(f'{file_name}_FILTERED{file_extension[0]}')
        filtered.show()
if not 'http' in source:
    with Image.open(source, 'r') as original:
        filtered = original.filter(filter_dict[filter])
        filtered.save(f'{file_name}_FILTERED{file_extension[0]}')
        filtered.show()