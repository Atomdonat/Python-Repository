import re

def format_into_table(unformatted_table_file: str):
    # Lesen Sie den Inhalt der Datei
    with open(unformatted_table_file, "r", encoding="utf-8") as file:
        content = file.read()

    # Ersetzen Sie die Muster in der Datei und fügen Sie \\ hinzu
    formatted_content = re.sub(pattern=r'Aufbau',              repl=r'    Aufbau:              &', string=content)
    formatted_content = re.sub(pattern=r'Formeln',             repl=r'    Formeln:             &', string=formatted_content)
    formatted_content = re.sub(pattern=r'Erklärung',           repl=r'    Erklärung:           &', string=formatted_content)
    formatted_content = re.sub(pattern=r'Angriffsart',         repl=r'    Angriffsart:         &', string=formatted_content)
    formatted_content = re.sub(pattern=r'Sicherheitsziele',    repl=r'    Sicherheitsziele:    &', string=formatted_content)
    formatted_content = re.sub(pattern=r'Benötigte Variablen', repl=r'    Benötigte Variablen: &', string=formatted_content)
    formatted_content = re.sub(pattern=r'Verhinderbar durch',  repl=r'    Verhinderbar durch:  &', string=formatted_content)

    # Fügen Sie \\ am Ende jeder Zeile hinzu
    formatted_lines = [line + " \\\\[10pt]" for line in formatted_content.split('\n')]

    # Schreiben Sie den bearbeiteten Inhalt zurück in die Datei
    with open(unformatted_table_file, "w", encoding="utf-8") as file:
        file.write("\n".join(formatted_lines))

def reformat_latex(input_file: str):
    with open(input_file, 'r+') as file:
        lines = file.readlines()  # Lese alle Zeilen der Datei

        # Setze den Dateizeiger auf den Anfang der Datei
        file.seek(0)

        for line in lines:
            # Lösche "\textbf{" und "}" aus der Zeile
            modified_line = line.replace(r'\textbf{', '').replace('}', '')

            # Ersetze "\\ \hline" durch "[10pt]"
            modified_line = modified_line.replace(r'\\ \hline', '\\\\[10pt]')

            # Schreibe die modifizierte Zeile zurück in die Datei
            file.write(modified_line)

        # Schneide den restlichen Inhalt ab, falls die neue Datei kürzer ist als die vorherige
        file.truncate()

if __name__ == "__main__":
    format_into_table("C:/Programmieren/Github_Repos/Python-Repository/input.txt")
    # reformat_latex("C:/Programmieren/Github_Repos/Python-Repository/input.txt")
