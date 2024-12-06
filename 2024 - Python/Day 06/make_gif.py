from os import listdir
from os.path import isfile, join

import imageio.v2 as imageio

fp_in = "images/"
files = [join(fp_in, f)  for f in listdir(fp_in) if isfile(join(fp_in, f))]

fp_out = "day06_test.gif"
with imageio.get_writer(fp_out, mode='I', fps=265) as writer:
    for filename in files:
        print(filename)
        image = imageio.imread(filename)
        writer.append_data(image)

# import glob
# import contextlib
# from PIL import Image
#
# # filepaths
# fp_in = "images/*.jpg"
# fp_out = "day06.gif"
#
# # use exit stack to automatically close opened images
# with contextlib.ExitStack() as stack:
#
#     # lazily load images
#     imgs = (stack.enter_context(Image.open(f))
#             for f in sorted(glob.glob(fp_in)))
#
#     # extract  first image from iterator
#     img = next(imgs)
#
#     # https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif
#     img.save(fp=fp_out, format='GIF', append_images=imgs,
#              save_all=True, duration=1, loop=0)