##  Contrastive Learning-based Nonlinear Optical Histopathology for Noninvasive Tissue Characterization

This project hosts the scripts for training and testing contrastive unregistered patchwise-learning translation (CUPT) network, as presented in our paper: B. Shen, Y. Li, Y. Pan, Y. Guo, Y. Lu, R. Hu, J. Qu, L. Liu,  Contrastive Learning-based Nonlinear Optical Histopathology for Noninvasive Tissue Characterization.


## Introduction

Label-free nonlinear optical imaging modalities like multiphoton excited fluorescence, second harmonic generation, and stimulated Raman scattering microscopy show promise for high-resolution characterization of cancer morphology and heterogeneity without exogenous labels. However, interpreting these complex multidimensional datasets proves difficult. Here, we present nonlinear optical digital histopathology (NODH), integrating biophotonic nonlinear signals with a contrastive deep learning framework to generate diagnostic quality hematoxylin and eosin (H&E) slides comparable to conventional histopathology. A patch-wise contrastive training approach overcomes registration challenges between nonlinear optical and H&E images. We demonstrate NODH effectively transforms label-free nonlinear optical data from human brain and ovarian cancers into realistic virtual H&E slides closely paralleling standard histology. Quantitative analysis confirms NODH images accurately reproduce nuclear morphometric features across different cancer stages. Combining multimodal nonlinear signals also enhances diagnostic classification versus individual modalities. By generating rapid, non-destructive virtual histology directly from fresh tissues, NODH could help overcome current tradeoffs between imaging scalability, specificity, and histopathological interpretation. This platform may enable more accurate and multifaceted optical assessment of cancer morphology and heterogeneity at the microscopic scale.

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
    git clone https://github.com/shenblin/NOCV.git
    ```

2. Install dependent packages

    ```bash
    pip install -r requirements.txt
    pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 -f https://download.pytorch.org/whl/torch_stable.html
    ```
   
📕 Dataset Preparation

The input and ground truth paired images should have the same name.


⚡ Train and Test

- **Training and testing commands**: For single gpu, use the following command as example:
1. **Training**
    ```bash
    python train.py --dataroot datasets/train_dataset/MP_to_HE/Ovarian/ovarian_RGB --name MP_to_HE --no_flip
    ```
2. **Testing**
    ```bash
    python test.py --dataroot datasets/test_dataset/MP_to_HE/ --name MP_to_HE --phase test --results_dir result_tiles
    ```

    
📢 Results

For more results and further analyses, please refer to our paper.


📜 Acknowledgement

Thanks [paper](https://arxiv.org/pdf/2007.15651) authers for the wonderful open source project!


🌏 Citations

If you find this work useful in your research, please consider citing the paper:

B. Shen, et al.

📧 Contact

If you have any questions, please email `shenblin@foxmail.com`.
