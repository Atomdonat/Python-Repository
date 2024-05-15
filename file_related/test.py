import os
import re

def get_dir_names(source_directory_path):
    for root, dirs, files in os.walk(source_directory_path):
        if re.search(pattern=r'\d{1,2}\s[a-zA-Z]', string=root) and not re.search(pattern=r'\\', string=root[119:]):
            print(re.match(pattern=r'^.*?(?=\()', string=root[119:]).group())


if __name__ == '__main__':
    print(len("C:/Meine_Ablage/Uni Bochum/3_Semester/SoftwareEngineering/WiSe2324/Software Engineering (212000-WS 23_24)_2024037_0946"))
    get_dir_names('C:/Meine_Ablage/Uni Bochum/3_Semester/SoftwareEngineering/WiSe2324/Software Engineering (212000-WS 23_24)_2024037_0946')