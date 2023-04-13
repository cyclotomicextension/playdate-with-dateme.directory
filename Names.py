import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

names=pd.read_csv("/workspaces/codespaces-blank/names.csv")
# Create a numpy array of names
names_array = np.array(names["Names"])

# Initialize a dictionary to store the first names and their counts
name_dict = {}

# Loop over each name in the array
for name in names_array:
    # Split the name into first and last name
    first_name = name.split()[0]
    
    # Add the first name to the dictionary and increment its count
    if first_name in name_dict:
        name_dict[first_name] += 1
    else:
        name_dict[first_name] = 1

# Get the names and their counts as two separate lists
names = list(name_dict.keys())
counts = list(name_dict.values())

# Sort the names and counts in descending order by count
sorted_indices = np.argsort(counts)[::-1]
names = [names[i] for i in sorted_indices]
counts = [counts[i] for i in sorted_indices]

# Plot all names and their counts
fig, ax = plt.subplots(figsize=(20, 5))
ax.bar(names, counts)

# Highlight the most common name with a red bar
ax.bar(names[0], counts[0], color='r')

# Rotate the x-tick labels by 90 degrees
plt.xticks(rotation=90)

# Add labels to the axes and a title to the plot
ax.set_xlabel('Name')
ax.set_ylabel('Frequency')
ax.set_title('Names and Their Frequencies')

# Show the plot
plt.show()
