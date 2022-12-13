import nibabel as nib
import numpy as np
import os

# folder path
dir_path = '/home/rtm/scratch/rtm/ms_project/data/projectNeuromorphometrics/OASISLabels'
save_dir = '/home/rtm/scratch/rtm/data/MedImagepreprocess/ventricle_labels/OASISNeuromorphometrics'


for folder in os.listdir(dir_path):
    path = os.path.join(dir_path, folder,str(folder)+ '_seg.nii')
    image = (nib.load(path)).get_fdata()
    arr4 = np.where(image == 4, 50, 0)
    arr11 = np.where(image == 11, 100, 0)
    arr15 = np.where(image == 15, 150, 0)
    arr52 = np.where(image == 52, 200, 0)
    arr51 = np.where(image == 51, 250, 0)
    arr = arr4 + arr11 + arr15 + arr52 + arr51

    new_image = nib.Nifti1Image(arr, np.eye(4))
    save_path = os.path.join(save_dir, str(folder) + '_seg.nii')
    print('save_path', save_path)
    nib.save(new_image, save_path)



