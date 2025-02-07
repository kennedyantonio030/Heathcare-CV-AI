from PIL import Image
import numpy as np
import nibabel as nib
import os

# Open the TIFF file
tiff_image_path = os.path.abspath('test.tif')
print(os.path.abspath('test.tif'))
tiff_image = Image.open(tiff_image_path)
# Convert the image to a NumPy array
image_array = np.array(tiff_image)

# Create a NIfTI image from the NumPy array
nifti_image = nib.Nifti1Image(image_array, affine=np.eye(4))

# Save the NIfTI image to a file
nib.save(nifti_image, 'test.nii')