import os, sys
import Image
import numpy as np
import scipy.misc

files = os.listdir("./imgs")
files = [f for f in files if "marker" not in f and (".png" in f or ".jpg" in f)]
file_pairs = [[f, "marker_{}.png".format(f.split("_")[0])] for f in sorted(files)]

if not os.path.exists("combined"):
    os.makedirs("combined")

for file_pair in file_pairs:

    list_im = file_pair
    imgs = [scipy.misc.imread(i, flatten=False, mode='RGB') for i in list_im]

    # pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
    min_shape = (350, 350)
    imgs_comb = np.vstack((scipy.misc.imresize(i, min_shape) for i in imgs))

    # save that beautiful picture
    imgs_comb = Image.fromarray(imgs_comb)
    print(''.join(file_pair[0].split("_")[1:]))
    imgs_comb.save("combined/{}".format(''.join(file_pair[0].split("_")[1:])))
