from deepface import DeepFace
import pandas as pd

import pandas as pd

# Load FairFace validation dataset
df_val = pd.read_csv('fairface_label_val.cs')

# Define function to convert age to age range
def age_to_range(age):
    if age < 2:
        return "0-2"
    elif age < 10:
        return "3-9"
    elif age < 20:
        return "10-19"
    elif age < 30:
        return "20-29"
    elif age < 40:
        return "30-39"
    elif age < 50:
        return "40-49"
    elif age < 60:
        return "50-59"
    elif age < 70:
        return "60-69"
    else:
        return "more than 70"

# Define tolerance interval
tolerance = 2

# Load predicted ages from FairFace validation set
df_predicted = pd.read_csv('fairface_val_predicted.csv')
predicted_ages = df_predicted['predicted_age'].tolist()

# Convert predicted ages to age ranges
predicted_age_ranges = [age_to_range(round(age)) for age in predicted_ages]

# Calculate number of correct predictions
num_correct = 0
for i in range(len(df_val)):
    actual_age_range = df_val['age'][i]
    predicted_age_range = predicted_age_ranges[i]
    if actual_age_range == predicted_age_range:
        num_correct += 1

# Calculate accuracy
accuracy = num_correct / len(df_val)
print(f"Accuracy: {accuracy}")
