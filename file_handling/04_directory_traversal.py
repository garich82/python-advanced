import os

# Variant 1 - Manual entry of the directory
# directory = "c:\\Users\\....."  # Replace with your chosen directory path

# Variant 2 - Directory is by default the directory of the current .py file
directory = os.path.dirname(os.path.abspath(__file__))

files = {}

try:
    for entry in os.scandir(directory):
        if entry.is_file():
            file_name = entry.name
            extension = os.path.splitext(file_name)[1]

            if extension not in files:
                files[extension] = []

            files[extension].append(file_name)

    sorted_extensions = sorted(files.keys())

    with open(os.path.join(directory, 'report.txt'), 'w') as report_file:

        for extension in sorted_extensions:
            report_file.write(f"{extension}\n")
            files[extension].sort()
            for file_name in files[extension]:
                report_file.write(f"- - - {file_name}\n")
            report_file.write("\n")

    print("Report generated successfully.")

except FileNotFoundError:
    print("Error: The specified directory does not exist.")



