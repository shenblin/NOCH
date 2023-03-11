<p align="center">
  <img src="image/sCUPT.jpg">
</p>

This project hosts the scripts for training and testing self-contrastive unregistered patchwise-learning translation (sCUPT) network, as presented in our paper: B. Shen, Y. Li, Y. Pan, Y. Guo, Y. Lu, R. Hu, J. Qu, L. Liu, Nonlinear optical imaging-based intelligent vision for fast intuitive label-free cancer diagnosis and tumor heterogeneous analysis.


## Introduction

Tumor heterogeneity is of crucial importance for cancer diagnosis and in-depth pathological analysis despite the near-an-hour invasive histopathological examination and tedious bio-structural discrimination. Nonlinear optical microscopy has emerged as a powerful tool for visualizing biological structure at the molecular scale and quantifying tumor heterogeneity. However, this technique is subjected to abnormal, unintuitive interpretation of tumor microenvironment. Here, we combine real-time multi-contrast optical-section nonlinear optical microscopy and self-contrastive learning network to realize histopathology-like visualization, structural mapping, and heterogeneous analysis of clinicopathological tissues. We demonstrate label-free histological translation with high authenticity, staged classification with high accuracy, and bio-structural segmentation with high specificity. These are challenging without stain collaboration. Further integration with high-speed image acquisition and network denoising boosts the above tasks with running time advantages. Thereby, the contrastive learning-based deep translation method builds a bridge to connect the data-rich optical microscopy and the intuitive histological examination and structural discrimination, and hence enables toilless biomedical diagnosis and tumor heterogeneous analysis.

<p align="center">
  <img src="image/NOCV.jpg">
</p>


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
    Breast
    ```bash
    python test.py --dataroot datasets/test_dataset/breast/Breast_RG/breast --name 2PA_SHG_to_HE --phase test --results_dir result_tiles/1/
     ```
    Skin
    ```bash
    python test.py --dataroot datasets/test_dataset/Skin/Skin_RG/Skin --name 2PA_SHG_to_HE --phase test --results_dir result_tiles/5/
     ```
    Segmentation
    ```bash
    python test.py --dataroot datasets/test_dataset/Nuclei_inpainting/Ovarian/ovarian_RGB_exp/ovarian_1 --name Nuclei_inpainting_MP --phase test --results_dir result_tiles
     ```
    Denoising
    ```bash
   python test.py --dataroot datasets/test_dataset/image_enhancement/resonant_4X/ovarian_1 --name image_enhancement --phase test --results_dir result_tiles
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
