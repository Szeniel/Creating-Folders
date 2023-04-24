import os

num_folders = int(input("Enter the number of folders to create: "))
folder_name = input("Enter the name of the folder: ")
folder_path = input("Enter the path where the folders should be created: ")

for i in range(1, num_folders+1):
    folder_full_path = os.path.join(folder_path, f'{folder_name}{i}')
    os.makedirs(folder_full_path, exist_ok=True)
    
print(f'Successfully created {num_folders} folders named {folder_name} at {folder_path}.')
