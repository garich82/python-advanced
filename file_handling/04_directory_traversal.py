# This script generates a report of files in a specified directory and its immediate subdirectories.
# It collects files, categorizes them by their extensions, and generates a report file ('report.txt').
# If the specified directory does not exist, an error message is displayed.


from pathlib import Path

directory = input("Enter the directory path (. for current directory): ")
directory_path = Path(directory)

if not directory_path.exists():
    print("Error: The specified directory does not exist.")
    exit()

files = {}

try:
    # Getting the files in the main directory
    for entry in directory_path.iterdir():
        if entry.is_file():
            file_name = entry.name
            extension = entry.suffix

            if extension not in files:
                files[extension] = []

            files[extension].append(file_name)

    # Writing the immediate subdirectories in a list
    subdirectories = [subdir for subdir in directory_path.iterdir() if subdir.is_dir()]

    # Getting the files in each of the immediate subdirectories
    for subdir in subdirectories:
        for entry in subdir.iterdir():
            if entry.is_file():
                file_name = entry.name
                extension = entry.suffix

                if extension not in files:
                    files[extension] = []

                files[extension].append(file_name)

    sorted_extensions = sorted(files.keys())

    report_file_path = directory_path / "report.txt"
    with open(report_file_path, 'w') as report_file:  # Generating the report file
        for extension in sorted_extensions:
            report_file.write(f"{extension}\n")
            files[extension].sort()
            for file_name in files[extension]:
                report_file.write(f"- - - {Path(file_name).name}\n")
            report_file.write("\n")

    print("Report generated successfully.")

except FileNotFoundError:
    print("Error: The specified directory does not exist.")
