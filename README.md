##  Contrastive Learning-based Nonlinear Optical Histopathology for Noninvasive Tissue Characterization

This project hosts the scripts for training and testing contrastive unregistered patchwise-learning translation (CUPT) network, as presented in our [Paper](assets/Manuscript.pdf).


## Introduction

Label-free nonlinear optical imaging (NLOI) modalities like multiphoton excited fluorescence, second harmonic generation, and stimulated Raman scattering microscopy show promise for high-resolution characterization of cancer morphology and heterogeneity without exogenous labels. However, interpreting these complex multidimensional datasets proves difficult. Here, we present nonlinear optical digital histopathology (NODH), integrating biophotonic nonlinear signals with a contrastive deep learning framework to generate diagnostic quality hematoxylin and eosin (H&E) slides comparable to conventional histopathology. A patch-wise contrastive training approach overcomes registration challenges between nonlinear optical and H&E images. We demonstrate NODH effectively transforms label-free nonlinear optical data from human brain and ovarian cancers into realistic virtual H&E slides closely paralleling standard histology. Quantitative analysis confirms NODH images accurately reproduce nuclear morphometric features across different cancer stages. Combining multimodal nonlinear signals also enhances diagnostic classification versus individual modalities. By generating rapid, non-destructive virtual histology directly from fresh tissues, NODH could help overcome current tradeoffs between imaging scalability, specificity, and histopathological interpretation. This platform may enable more accurate and multifaceted optical assessment of cancer morphology and heterogeneity at the microscopic scale.

<p align="center">
  <img src="image/NOCV.jpg">
</p>

## NLOI, NODH and histopathological staining workflows 
Label-free multi-contrast nonlinear imaging procedure for quantitative analysis and standard histopathological procedure for experienced examination and structural annotation. The MP and histopathological images were trained in the self-contrastive learning network. 
Top: neural network as bridge connects the MP imaging and the conventional histopathology with high accuracy and speed. 
Bottom: label-free MP image, inferred NODH image, and histopathological image of a normal ovarian tissue.

<p align="center">
  <img src="image/Supplementary video 1(compressed).gif">
</p>

## Network
📕 Dependencies and Installation

Python >= 3.7 (Recommend to use [Anaconda](https://www.anaconda.com/download/#linux) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html))
- [PyTorch >= 1.3](https://pytorch.org/)
- NVIDIA GPU + [CUDA](https://developer.nvidia.com/cuda-downloads)

1. Clone repo

    ```bash
    git clone https://github.com/shenblin/NODH.git
    ```

2. Install dependent packages

    ```bash
    pip install -r requirements.txt
    pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 -f https://download.pytorch.org/whl/torch_stable.html
    ```

## Train and Test
 
📕 Dataset Preparation

The input and ground truth paired images should have the same name.


⚡ **Training and testing commands**: For single gpu, use the following command as example:
1. **Training**
    ```bash
    python train.py --dataroot datasets/train_dataset/Brain_SRS/SRS --name SRS_to_HE --save_epoch_freq 1
    ```
   ```bash
    python train.py --dataroot datasets/train_dataset/Brain_SRS/SRS --name SRS_to_HE_cross_contrastive --save_epoch_freq 1 --nce_includes_all_negatives_from_minibatch True --batch_size 3
    ```
    ```bash
    python train.py --dataroot datasets/train_dataset/Ovarian/MP_to_HE/ovarian_RGB --name MP_to_HE
    ```
    ```bash
    python train.py --dataroot datasets/train_dataset/Ovarian/MP_to_HE/ovarian_RGB --name MP_to_HE_cross_contrastive --nce_includes_all_negatives_from_minibatch True --batch_size 2
    ```
3. **Testing**
    ```bash
    python test.py --dataroot datasets/test_dataset/Brain_SRS/002 --name SRS_to_HE --phase test --results_dir result_tiles/2/  --epoch 26
    ```
    ```bash
    python test.py --dataroot datasets/test_dataset/Brain_SRS/002 --name SRS_to_HE_cross_contrastive --phase test --results_dir result_tiles/2/  --epoch 25
    ```
    ```bash
    python test.py --dataroot datasets/test_dataset/Ovarian/MP_to_HE/ovarian_RGB/ovarian_1 --name MP_to_HE --phase test --results_dir result_tiles/1/ --epoch 80
    ```
    ```bash
    python test.py --dataroot datasets/test_dataset/Ovarian/MP_to_HE/ovarian_RGB/ovarian_1 --name MP_to_HE_cross_contrastive --phase test --results_dir result_tiles/1/ --epoch 80
    ```
    
## Results

<p align="center">
  <img src="image/Figure 2.jpg">
</p>

Label-Free neurosurgical pathology using NODH. 
a–c, g–i, Glioblastoma IV; d–f, j–l, Oligoastrocytoma II–III. The unstained SRS images (a,d,g,j) were merged by protein (green) and lipid (blue) image. The NODH network inferences (b,e,h,k) closely mirror the corresponding pathological morphology observed in the H&E histopathology. (c,f,i,l). Scale bar, 100 μm in a–f, 40 μm in g–l.

<p align="center">
  <img src="image/Fig. S1.jpg">
</p>
___________________________________________________________________________________________________________________________

Comparison of NODH results of different networks. 
a, The SRS spectrum of lipid (blue) and protein (green), which compose the SRS images. b, Cycle-consistent module which transforms images between the two domains. c, Self-contrastive loss associating the sampled query and its positive, in contrast to negatives within the same image. d, Cross-contrastive loss associating the sampled query and its positive, in contrast to negatives from different images. Second to fourth columns present the virtually histological results. e, Conventional H&E histology including fixing tissue slide in acetic acid, staining with hematoxylin and eosin mixture, dehydrating with ethanol, and cleaning with xylene. Second to fourth columns correspond to the bright-field H&E images for reference. Scale bar, 50 μm.


📢 **For more results and further analyses, please refer to our paper.**


## License

📜 This project is released under the [LICENSE](LICENSE).<br>

 ## Citation

If you find this work useful in your research, please consider citing the paper:

B. Shen, et al.

📧 Contact

If you have any questions, please email `shenblin@foxmail.com`.
