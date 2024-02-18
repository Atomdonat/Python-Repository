import os
import shutil

# Specify the source directory path
source_directory_path = 'C:/Meine_Ablage/Uni Bochum/3_Semester/TheroretischeInformatik/WiSe2324/Heimübung/Informatik 3 - Theoretische Informatik (212002-WiSe23_24)_20240121_1731.zip'

# Specify the destination directory path
destination_directory_path = 'C:/Meine_Ablage/Uni Bochum/3_Semester/TheroretischeInformatik/WiSe2324/Heimübung/Abgaben'

# Iterate over all files in the source directory and its subdirectories
for root, dirs, files in os.walk(source_directory_path):
    for file_name in files:
        if file_name.endswith('.pdf'):
            # Create the full source file path
            source_file_path = os.path.join(root, file_name)

            # Create the full destination file path
            destination_file_path = os.path.join(destination_directory_path, file_name)

            # Copy the file to the destination directory
            shutil.copy(source_file_path, destination_file_path)