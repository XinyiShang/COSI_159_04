# COSI_159_04
 COSI 159 Assignment 4

## Task 1 Paper Reading

#### write-up link
https://github.com/XinyiShang/COSI_159_04/blob/ce175483ca0d29f8445d94088bd696a0ce2d0a6b/Task1/Task1_WriteUp.pdf

## Task 2 Measure the bias in deepface

In this section, I used DeepFace to predict the age of individuals in the Fairface dataset and measured the accuracy of the predictions. Additionally, I analyzed the potential bias of the DeepFace model with respect to gender and race.

#### Code

##### prediction.py
Run the deepface to predict the age

##### evaluation.py
Perform the evaluation and compute the accuracy

##### evaluation_GenderRace.py
Perform the evaluation for each subgroups (Race & Gender), and compute the accuracy and standard deviation

#### write-up link
https://github.com/XinyiShang/COSI_159_04/blob/ce175483ca0d29f8445d94088bd696a0ce2d0a6b/Task2/Task2_WriteUp.pdf


## References
[1]K. Ucla, J. Jungseock, and Ucla, “FairFace: Face Attribute Dataset for Balanced Race, Gender, and Age for Bias Measurement and Mitigation.” Available: https://openaccess.thecvf.com/content/WACV2021/papers/Karkkainen_FairFace_Face_Attribute_Dataset_for_Balanced_Race_Gender_and_Age_WACV_2021_paper.pdf

[2]S. I. Serengil and A. Ozpinar, “LightFace: A Hybrid Deep Face Recognition Framework,” IEEE Xplore, Oct. 01, 2020. https://ieeexplore.ieee.org/document/9259802
