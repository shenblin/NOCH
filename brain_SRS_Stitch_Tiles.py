import os
import glob
import cv2
import re
import numpy as np

epoch = '26'
# epoch = 'latest'

num_imgs = 10
name = 'SRS_to_HE'
# name = 'SRS_to_HE_cross_contrastive'
# name = 'SRS_to_HE_self_patch3'
# name = 'SRS_to_HE_unpaired'
# name = 'SRS_to_HE_stylegan2'


overlap = 136
file = open("brain_SRS_split_num.txt", "r")


def stitch_image_tiles(tiles_path, stitched_imgs_path, img_name, rev_color='fault'):
    if not os.path.exists(stitched_imgs_path):
        os.makedirs(stitched_imgs_path)
    im_files = sorted(list(glob.glob(os.path.join(tiles_path, '*.png'))))
    im_names = [os.path.split(im_file0)[-1].split('.')[0] for im_file0 in im_files]
    im_names_files = {}
    im_names_ = []
    for im_name, im_file in zip(im_names, im_files):
        im_names_files[im_name] = im_file
        im_names_.append(im_name)
    im_names = im_names_

    h_s, w_s = -1, -1
    for i_, im_name in enumerate(im_names):
        im_file0 = im_names_files[im_name]
        im = cv2.imread(im_file0)
        im_num = int(im_name.split('_')[-1])
        i = im_num // w_num  # i row idx
        j = im_num % w_num  # j col idx
        if overlap != 0:
            # if i == 0:
            #     im = im[:-2 * overlap, :]
            # elif i == h_num - 1:
            #     im = im[2 * overlap:, :]
            # else:
            #     im = im[overlap:-overlap, :]
            # if j == 0:
            #     im = im[:, :-2 * overlap]
            # elif j == w_num - 1:
            #     im = im[:, 2 * overlap:]
            # else:
            im = im[overlap:-overlap, overlap:-overlap]
        h, w = im.shape[0:2]
        if i_ % (h_num * w_num) == 0:
            h_s, w_s = h, w
            h_t, w_t = h_num * h_s, w_num * w_s
            im_t = np.zeros(shape=(h_t, w_t, 3))
        assert h == h_s, w == w_s
        im_t[h_s * i:h_s * (i + 1), w_s * j:w_s * (j + 1)] = im
        if (i_ + 1) % (h_num * w_num) == 0:
            if rev_color == 'true':
                # reverse color
                im_t = 255 - im_t
            im_name_t_path = os.path.join(stitched_imgs_path, (img_name + '.png'))
            cv2.imwrite(im_name_t_path, im_t)


for i in range(num_imgs):
    line = file.readline()
    numbers = re.findall(r'\d+', line)
    h_num, w_num = numbers
    h_num = int(h_num)
    w_num = int(w_num)
    print('saving im %d ' % (i+1), h_num, 'x', w_num)

    result_imgs_path = 'results/{}/stitched_epoch_{}'.format(name, epoch)

    sample = 'brain_{}_SRS'.format(str(i + 1))
    imgs_path = 'result_tiles/{}/{}/test_{}/images/real_A'.format(str(i + 1), name, epoch)
    stitch_image_tiles(imgs_path, result_imgs_path, sample, 'true')

    sample = 'brain_{}_NODH'.format(str(i + 1))
    imgs_path = 'result_tiles/{}/{}/test_{}/images/fake_B'.format(str(i + 1), name, epoch)
    stitch_image_tiles(imgs_path, result_imgs_path, sample)

    sample = 'brain_{}_HE'.format(str(i + 1))
    imgs_path = 'result_tiles/{}/{}/test_{}/images/real_B'.format(str(i + 1), name, epoch)
    stitch_image_tiles(imgs_path, result_imgs_path, sample)


file.close()
print('done!')
