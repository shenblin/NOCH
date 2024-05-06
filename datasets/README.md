# Data download guide

The data for training and testing NODH, as well as the pre-training weights in the paper can be downloaded from: https://doi.org/10.5281/zenodo.10020760

The MP data were captured by our multiphoton microscope with two aligned scanners: galvo-resonant scanning for high-speed acquisition and dual-galvo scanning for high-quality imaging. The H&E data were captured by a wide-field microscope.
Since the background of MP images (black) is opposite to the that of bright-field histopathological images (white), we inverted the color channels of the NLOI image by I_input=|L-I_raw | to avoid content mismatching during image splitting, where L is the dynamic range of the image (e.g. 255 for 8-bit).

After inference, stitch image tiles into origin size:

SRS to H&E:

brain_SRS_Stitch_Tiles.py

MP to H&E:

Stitch_Tiles_Ovary.py and stitch_tiles.py

