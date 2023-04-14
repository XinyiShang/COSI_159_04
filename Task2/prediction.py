import pandas as pd
import os
#import patoolib
from deepface import DeepFace

"""
Perform the prediction using deepface
the output should be stored in the fairface_val_predicted.csv
"""
# extract zip file
#patoolib.extract_archive("val.zip")

# Load FairFace validation dataset from CSV file
df_val = pd.read_csv('fairface_label_val.csv')

# Define function to predict age using Deepface on GPU
def predict_age(img_path):
    result = DeepFace.analyze(img_path, actions=['age'], enforce_detection=False, detector_backend='mtcnn')
    return result[0]['age']

# Predict age for each image in validation set
predicted_ages = []
for i in range(len(df_val)):
    img_num = str(i+1)
    img_path = os.path.join('val', img_num + '.jpg') #change to the directory of image
    predicted_age = predict_age(img_path)
    predicted_ages.append(predicted_age)
    print(i)
    
# Add predicted ages to validation dataset
df_val['predicted_age'] = predicted_ages

# Save predicted ages to CSV file
df_val.to_csv('fairface_val_predicted.csv', index=False)


# delete extracted directory
# os.system("rm -rf val")

