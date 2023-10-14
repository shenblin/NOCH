import os
import glob
import cv2

# input_folder = 'MP_to_HE/Ovarian/ovarian_RGB'
# input_folder = 'MP_to_HE/Ovarian/ovarian_R'
# input_folder = 'MP_to_HE/Ovarian/ovarian_G_R'
# input_folder = 'MP_to_HE/Ovarian/ovarian_B_R'
# input_folder = 'MP_to_HE/Ovarian/ovarian_B_G'
# input_folder = 'MP_to_HE/Ovarian/ovarian_B'
# input_folder = 'MP_to_HE/Ovarian/subtract_G-R'
# input_folder = 'MP_to_HE/Ovarian/ovarian_3P2H2P'
# GT_folder = 'MP_to_HE/Ovarian/ovarian_GT'


tile_pixel = 544


input_imgs_path = 'datasets/{}'.format(input_folder)
input_tiles_path = 'datasets/train_dataset/{}/trainA'.format(input_folder)
GT_imgs_path = 'datasets/{}'.format(GT_folder)
GT_tiles_path = 'datasets/train_dataset/{}/trainB'.format(input_folder)


overlap = 0

def crop_im(imgs_path, tiles_path, overlap, reverse_color='fault', RGB2gray='fault'):
    im_files = sorted(list(glob.glob(os.path.join(imgs_path, '*.tif'))))
    n_tiles = 0
    for k, im_file0 in enumerate(im_files):
        im_file = os.path.split(im_file0)[-1].split('.')[0]
        im = cv2.imread(im_file0)
        if reverse_color == 'true':
            # reverse color
            im = 255 - im

        h, w = im.shape[0:2]
        h_num = h//tile_pixel
        w_num = w//tile_pixel
        print('Image tile number: %.2f x %.2f' % (h/tile_pixel, w/tile_pixel))

        for i in range(h_num):
            for j in range(w_num):
                num = w_num*i+j
                if i==0:
                    h_start = tile_pixel * i
                elif i==h_num-1:
                    h_start = tile_pixel * i - 2 * overlap
                else:
                    h_start = tile_pixel * i - overlap
                if j==0:
                    w_start = tile_pixel * j
                elif j==w_num-1:
                    w_start = tile_pixel * j - 2 * overlap
                else:
                    w_start = tile_pixel * j - overlap
                if i==h_num-1:
                    h_end = tile_pixel * (i + 1)
                elif i==0:
                    h_end = tile_pixel * (i + 1) + 2 * overlap
                else:
                    h_end = tile_pixel * (i + 1) + overlap
                if j==w_num-1:
                    w_end = tile_pixel * (j + 1)
                elif j==0:
                    w_end = tile_pixel * (j + 1) + 2 * overlap
                else:
                    w_end = tile_pixel * (j + 1) + overlap
                image_tile = im[h_start:h_end, w_start:w_end]

                if not os.path.exists(tiles_path):
                    os.makedirs(tiles_path)
                n_tiles += 1
                new_im_path = os.path.join(tiles_path, (str(n_tiles) + '.tif'))

                if RGB2gray == 'true':
                    # convert RGB image into gray
                    image_tile = cv2.cvtColor(image_tile, cv2.COLOR_RGB2GRAY)
                cv2.imwrite(new_im_path, image_tile)


crop_im(input_imgs_path, input_tiles_path, overlap, 'true')
crop_im(GT_imgs_path, GT_tiles_path, overlap)


print('done!')
