import sys
import os
import subprocess
import shlex
import re

def execute_command_in_shell(command: str, working_directory: str) -> bool:
    command_args = shlex.split(
        f'{command}'
    )

    execute_command = subprocess.run(command_args, shell=True, cwd=working_directory, stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE, text=True)

    if execute_command.returncode == 0:
        print(f"Command executed successfully. Output:\n{execute_command.stdout}")
        return True

    else:
        print(f"Command failed with error:\n{execute_command.stderr}")
        return False


def create_uml_class_diagram(target_directory: str, target_file: str, output_directory: str) -> str:
    target_filename = target_file.rsplit('.')[0]

    def create_dot_file():
        command_executed = execute_command_in_shell(
            command=f'C:/Users/buste/AppData/Roaming/Python/Python312/Scripts/pyreverse.exe {target_file} -o dot -d {output_directory}',
            working_directory=target_directory
        )
        if command_executed:
            execute_command_in_shell(
                command=f"ren classes.dot {target_filename}.dot",
                working_directory=output_directory
            )

            return f'{output_directory}/{target_filename}.dot'

    def create_svg_file():
        dot_file = create_dot_file()

        if dot_file is not None:
            execute_command_in_shell(
                command=f'dot -Tsvg {dot_file} > {output_directory}/{target_filename}.svg',
                working_directory=target_directory
            )

    create_svg_file()


if __name__ == '__main__':
    create_uml_class_diagram(
        target_directory='C:/Programmieren/SpotipyClient/',
        target_file='main.py',
        output_directory='C:/Programmieren/SpotipyClient/class_diagramms'
    )
