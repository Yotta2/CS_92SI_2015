"""
Image manipulation library for CS 92SI: The Python Programming Language

You probably shouldn't modify this file.

@author sredmond
@date 10-19-15
"""
from PIL import Image
from pathlib import Path


def load_image(filename):
    """Returns a 2D array of pixels in column-major order
    from the image specified by filename."""
    with Image.open(filename, 'r') as image:
        image = image.convert('RGBA')
    return _swap_major(_unflatten(list(image.getdata()), image.width, image.height))


def save_image(data2D, filename):
    """Saves a PNG of the image data to disk
    under the given filename"""
    data2D = _swap_major(data2D)
    image = _to_image(data2D)
    image.save(filename, format='PNG')


def _swap_major(data2D):
    """Swaps the major ordering of a 2D list"""
    width, height = len(data2D[0]), len(data2D)
    columns = []
    for i in range(width):
        columns.append([data2D[j][i] for j in range(height)])
    return columns


def _flatten(data2D):
    """Flattens a 2D list"""
    data1D = []
    for row in data2D:
        data1D.extend(row)
    return data1D


def _unflatten(data1D, width, height):
    """Unflattens a 1D list into a width x height 2D list"""
    assert len(data1D) == width * height
    length = len(data1D)
    return [data1D[i:i+width] for i in range(0, length, width)]


def _to_image(data2D):
    """Converts 2D pixels to a PIL.Image"""
    size = len(data2D[0]), len(data2D)
    image = Image.new('RGBA', size)
    data1D = _flatten(data2D)
    image.putdata(data1D)
    return image


def show_image(data2D):
    """Opens a preview of the image data
    - useful for debugging"""
    data2D = _swap_major(data2D)
    image = _to_image(data2D)
    image.show()

def show_all_images(slc, *rest, buffer_width=1):
    """Draws all vertical slices in one image with a black buffer
    between slices buffer_width pixels wide. Useful for debugging"""
    width, height = len(slc), len(slc[0])
    slices = []
    slices += slc
    for chunk in rest:
        slices += [[(0, 0, 0, 0) for _ in range(height)] for _ in range(buffer_width)]
        slices += chunk
    show_image(slices)


class FileSystemException(Exception): pass


def files_in_directory(dirname):
    """Returns a list of filenames in the given directory"""
    p = Path(dirname)
    if not p.is_dir():
        raise FileSystemException("`{dir}` is not a valid directory".format(dir=dirname))
    return [str(child) for child in p.iterdir() if child.is_file()]


__all__ = ['load_image', 'show_image', 'show_all_images', 'save_image', 'files_in_directory']
