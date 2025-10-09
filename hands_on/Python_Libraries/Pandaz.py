import pandas as pd  # We give the elder a short, respectful nickname 'pd'

# The scribe creates a table from a dictionary
data = {'Name': ['Lebo', 'Thando', 'Sipho'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)

# Display the beautiful table
print(df)

# Calculate the average age of the village
print(f"\nThe average age is: {df['Age'].mean()} Summers")

#Add a new column for Occupation
df['Occupation'] = ['Farmer', 'Blacksmith', 'Doctor']
print("\nUpdated Table with Occupation:")
print(df)   
# Filter villagers older than 28
Adults = df[df['Age'] > 28]
print("\nVillagers Adults:")     
print(Adults)

# Sort villagers by Age
Sorted_by_Age = df.sort_values(by='Age')
print("\nVillagers Sorted by Age:") 
print(Sorted_by_Age)

# Save the table to a CSV file
df.to_csv('villagers.csv', index=False)
print("\nThe villagers' data has been saved to 'villagers.csv'.")
