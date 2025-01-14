import os
import datetime

# Path to the directory containing the files
directory = r'C:\Users\'

# Get a list of files in the directory
files = os.listdir(directory)

# Create a list to hold tuples of (file name, creation time)
file_list = []

# Loop through the files and get their creation times
for file_name in files:
    file_path = os.path.join(directory, file_name)
    creation_time = os.path.getctime(file_path)
    file_list.append((file_name, creation_time))

# Sort the files by creation time
file_list.sort(key=lambda x: x[1])

# Rename the files in chronological order
for index, (file_name, creation_time) in enumerate(file_list):
    new_name = f'Exhibit {index + 1}{os.path.splitext(file_name)[1]}'
    os.rename(os.path.join(directory, file_name), os.path.join(directory, new_name))

print("Files renamed successfully in chronological order.")
