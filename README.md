# TIGER
TIGER (Three dimensional Image GeneratoR) is a 3D reconstruction framework capable of generating point clouds from 2D images similar to LIDAR, but using SfM algorithm with OpenCV.

(Still in early development, results are premature)

## Inputs

Example images used for testing purposes:

![image](https://github.com/matjsz/tiger/assets/54675543/af2bb80f-7bd7-434a-8f33-c9d9f5dda70e)

## Results:

The results got from this version are still premature and may have some wrong calculations, but they are already returning a 3D object from a 2D image, which is the goal here. The next step is to improve the algorithm and the calculations made on the KNN step and the radius of the triangle mesh that builds the OBJ file after the PLY (point clouds) generation.

Result got from the project's actual version:

![image](https://github.com/matjsz/tiger/assets/54675543/b9afa984-daa6-46fb-8538-138cebe838dd)

# The future of the project

I personally prefer to work with neural networks, the SfM algorithm is just a simple image analysis algorithm that can pinpoint depth through motion, that is, many images from the same object. I'm planning on bulding a deep learning model that can infer depth using the SfM's schema, but with more dense point clouds and concise triangle mesh generation through ball pivoting, getting the radius of each sphere during the OBJ generation by faster and more accurate KNN algorithms. In the mean time I'll be playing with the tools I already have by now.
