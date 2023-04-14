import pandas as pd
import numpy as np

# Load FairFace validation dataset
df_val = pd.read_csv('fairface_label_val.csv')

# Load predicted ages from FairFace validation set
df_predicted = pd.read_csv('fairface_val_predicted.csv')

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

# Convert actual ages to age ranges
df_val['age_range'] = df_val['age']

# Convert predicted ages to age ranges
df_predicted['predicted_age_range'] = df_predicted['predicted_age'].apply(age_to_range)

# Define tolerance interval
#tolerance = 2
df_val['age_prediction_correct'] = 0


# Add age prediction accuracy to validation dataset
for i in range(len(df_val)):
    actual_age_range = df_val['age'][i]
    predicted_age_range = df_predicted['predicted_age_range'][i]
    if actual_age_range == predicted_age_range:
        df_val['age_prediction_correct'][i] = 1
    else:
        df_val['age_prediction_correct'][i] = 0

# Group data by gender and race and calculate accuracy for each group
groups = df_val.groupby(['gender', 'race'])
for group, data in groups:
    gender, race = group
    num_correct = data['age_prediction_correct'].sum()
    num_total = len(data)
    accuracy = num_correct / num_total
    print(f"Gender: {gender}, Race: {race}, Accuracy: {accuracy}")

"""
# Calculate accuracy by race
race_groups = df_val.groupby('race')
for race, data in race_groups:
    num_correct = data['age_prediction_correct'].sum()
    num_total = len(data)
    accuracy = num_correct / num_total
    print(f"Race: {race}, Accuracy: {accuracy}")

# Calculate accuracy by gender
gender_groups = df_val.groupby('gender')
for gender, data in gender_groups:
    num_correct = data['age_prediction_correct'].sum()
    num_total = len(data)
    accuracy = num_correct / num_total
    print(f"Gender: {gender}, Accuracy: {accuracy}")
"""
# Calculate accuracy by race and standard deviation of ages for each race
accuracy_race= []
race_groups = df_val.groupby('race')
for race, data in race_groups:
    num_correct = data['age_prediction_correct'].sum()
    num_total = len(data)
    accuracy = num_correct / num_total
    #std_age = df_predicted['predicted_age'].std()
    accuracy_race.append(accuracy)
    print(f"Race: {race}, Accuracy: {accuracy}")

std_dev = np.std(accuracy_race)

print(f"Standard deviation across gender: {std_dev}")


# Calculate accuracy by gender and standard deviation of ages for each gender
accuracy_gender = []
gender_groups = df_val.groupby('gender')
for gender, data in gender_groups:
    num_correct = data['age_prediction_correct'].sum()
    num_total = len(data)
    accuracy = num_correct / num_total
    accuracy_gender.append(accuracy)
    #std_age = df_predicted['predicted_age'].std()
    print(f"Gender: {gender}, Accuracy: {accuracy}")
    
std_dev = np.std(accuracy_gender)

print(f"Standard deviation across gender: {std_dev}")