import pandas as pd

# Create dummy data


survey_dict = {'language': ['C++', 'VB.NET', 'Go', 'PHP', 'Perl'],
               'avg_salary': [80, 75, 70, 90, 80],
               'num_candidates': [122, 154, 138, 120, 145]
               }
# Build the Pandas DataFrame
survey = pd.DataFrame(survey_dict)

df = pd.DataFrame({
    'name': ['Alice', 'Bob'],
    'age': [25, 30],
    'sage': [225, 320]
})

dft = pd.DataFrame(columns=['asd', 'asfasd', 'fff'])
# create a dictionary for the new row
new_row = {'name': 'Charlie', 'sage': 35}

new_df = pd.DataFrame(new_row, index=[0])

# append the new row to the dataframe
df = pd.concat([df, new_df], ignore_index=True)
dft = pd.concat([dft, new_df], ignore_index=True)

new_row = {'name': 'aCharlie', 'age': 35}

new_df = pd.DataFrame(new_row, index=[0])

# append the new row to the dataframe
df = pd.concat([df, new_df], ignore_index=True)
dft = pd.concat([dft, new_df], ignore_index=True)

new_row = {'name': 'aaCharlie'}

new_df = pd.DataFrame(new_row, index=[0])

# append the new row to the dataframe
df = pd.concat([df, new_df], ignore_index=True)
dft = pd.concat([dft, new_df], ignore_index=True)

print(dft)
dft = dft.fillna(0)
print(dft)
