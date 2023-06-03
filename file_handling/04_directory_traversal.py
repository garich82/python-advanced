import os

directory = input("Enter the directory path: ")

if not os.path.exists(directory):
    print("Error: The specified directory does not exist.")
    exit()

files = {}

try:
    for entry in os.scandir(directory):  # Getting the files in the main directory
        if entry.is_file():
            file_name = entry.name
            extension = os.path.splitext(file_name)[1]

            if extension not in files:
                files[extension] = []

            files[extension].append(file_name)

    subdirectories = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]

    for subdir in subdirectories:  # Getting the files in each of the immediate subdirectories
        subdir_path = os.path.join(directory, subdir)
        for entry in os.scandir(subdir_path):
            if entry.is_file():
                file_name = entry.name
                extension = os.path.splitext(file_name)[1]

                if extension not in files:
                    files[extension] = []

                files[extension].append(file_name)

    sorted_extensions = sorted(files.keys())

    with open(os.path.join(directory, 'report.txt'), 'w') as report_file:  # Generating the report file
        for extension in sorted_extensions:
            report_file.write(f"{extension}\n")
            files[extension].sort()
            for file_name in files[extension]:
                report_file.write(f"- - - {os.path.basename(file_name)}\n")
            report_file.write("\n")

    print("Report generated successfully.")

except FileNotFoundError:
    print("Error: The specified directory does not exist.")
