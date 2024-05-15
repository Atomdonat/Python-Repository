import os
import shutil


def copy_a_to_b(source_directory_path, destination_directory_path, operator: dict):
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

def move_a_to_b(source_directory_path, destination_directory_path, operator: dict):
    # Iterate over all files in the source directory and its subdirectories
    for root, dirs, files in os.walk(source_directory_path):
        # if 'type' in operator and
        for file_name in files:
            if file_name.endswith('.lbr'):
                # Create the full source file path
                source_file_path = os.path.join(root, file_name)

                # Create the full destination file path
                destination_file_path = os.path.join(destination_directory_path, file_name)

                # Copy the file to the destination directory
                shutil.move(src=source_file_path, dst=destination_file_path)


if __name__ == '__main__':
    source_path = "C:/Users/buste/Downloads/eagle-lbr-master/eagle-lbr-master"
    dest_path = "C:/Users/buste/Downloads/eagle-lbr-master"
    operations = {'type': 'file', 'name': '.lbr'}

    move_a_to_b(source_directory_path=source_path, destination_directory_path=dest_path, operator=operations)
