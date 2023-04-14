import pandas as pd

# Load FairFace validation dataset
df_val = pd.read_csv('fairface_val.csv')

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
predicted_ages = df_predicted['age'].tolist()

# Convert predicted ages to age ranges
predicted_age_ranges = [age_to_range(round(age)) for age in predicted_ages]

# Calculate accuracy for each gender and race category
categories = ['gender', 'race']
for category in categories:
    groupby_col = f'{category}_idx'
    grouped = df_val.groupby(groupby_col)
    for group_name, group_df in grouped:
        group_size = len(group_df)
        group_num_correct = 0
        for i in range(group_size):
            if group_df['age_range'].iloc[i] == predicted_age_ranges[group_df.index[i]]:
                group_num_correct += 1
        group_accuracy = group_num_correct / group_size
        print(f"Accuracy for {category} '{group_name}': {group_accuracy}")
