
#########################################################     self_contrastive learning        ########################################################

#python train.py --dataroot datasets/train_dataset/Brain_SRS/SRS --name SRS_to_HE --save_epoch_freq 1
python test.py --dataroot datasets/test_dataset/Brain_SRS/001 --name SRS_to_HE --phase test --results_dir result_tiles/1/  --epoch 26
python test.py --dataroot datasets/test_dataset/Brain_SRS/002 --name SRS_to_HE --phase test --results_dir result_tiles/2/  --epoch 26
python test.py --dataroot datasets/test_dataset/Brain_SRS/003 --name SRS_to_HE --phase test --results_dir result_tiles/3/  --epoch 26
python test.py --dataroot datasets/test_dataset/Brain_SRS/004 --name SRS_to_HE --phase test --results_dir result_tiles/4/  --epoch 26
python test.py --dataroot datasets/test_dataset/Brain_SRS/005 --name SRS_to_HE --phase test --results_dir result_tiles/5/  --epoch 26
python test.py --dataroot datasets/test_dataset/Brain_SRS/006 --name SRS_to_HE --phase test --results_dir result_tiles/6/  --epoch 26
python test.py --dataroot datasets/test_dataset/Brain_SRS/007 --name SRS_to_HE --phase test --results_dir result_tiles/7/  --epoch 26
python test.py --dataroot datasets/test_dataset/Brain_SRS/008 --name SRS_to_HE --phase test --results_dir result_tiles/8/  --epoch 26
python test.py --dataroot datasets/test_dataset/Brain_SRS/009 --name SRS_to_HE --phase test --results_dir result_tiles/9/  --epoch 26
python test.py --dataroot datasets/test_dataset/Brain_SRS/010 --name SRS_to_HE --phase test --results_dir result_tiles/10/  --epoch 26


#########################################################     cross_contrastive learning        ########################################################

#python train.py --dataroot datasets/train_dataset/Brain_SRS/SRS --name SRS_to_HE_cross_contrastive --save_epoch_freq 1 --nce_includes_all_negatives_from_minibatch True --batch_size 3
python test.py --dataroot datasets/test_dataset/Brain_SRS/001 --name SRS_to_HE_cross_contrastive --phase test --results_dir result_tiles/1/  --epoch 26
python test.py --dataroot datasets/test_dataset/Brain_SRS/002 --name SRS_to_HE_cross_contrastive --phase test --results_dir result_tiles/2/  --epoch 26
python test.py --dataroot datasets/test_dataset/Brain_SRS/003 --name SRS_to_HE_cross_contrastive --phase test --results_dir result_tiles/3/  --epoch 26
python test.py --dataroot datasets/test_dataset/Brain_SRS/004 --name SRS_to_HE_cross_contrastive --phase test --results_dir result_tiles/4/  --epoch 26
python test.py --dataroot datasets/test_dataset/Brain_SRS/005 --name SRS_to_HE_cross_contrastive --phase test --results_dir result_tiles/5/  --epoch 26
python test.py --dataroot datasets/test_dataset/Brain_SRS/006 --name SRS_to_HE_cross_contrastive --phase test --results_dir result_tiles/6/  --epoch 26
python test.py --dataroot datasets/test_dataset/Brain_SRS/007 --name SRS_to_HE_cross_contrastive --phase test --results_dir result_tiles/7/  --epoch 26
python test.py --dataroot datasets/test_dataset/Brain_SRS/008 --name SRS_to_HE_cross_contrastive --phase test --results_dir result_tiles/8/  --epoch 26
python test.py --dataroot datasets/test_dataset/Brain_SRS/009 --name SRS_to_HE_cross_contrastive --phase test --results_dir result_tiles/9/  --epoch 26
python test.py --dataroot datasets/test_dataset/Brain_SRS/010 --name SRS_to_HE_cross_contrastive --phase test --results_dir result_tiles/10/  --epoch 26
