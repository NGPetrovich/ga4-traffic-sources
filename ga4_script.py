import subprocess
import os
import glob

# Define the list of commands to be executed
commands = [
    "cd step-0",
    "python fake_ga4.py",
    "python fake_backend.py",
    "python fake_app_ga4.py",
    "python fake_channels.py",
    "cd ..",
    "cd step-1",
    "python cleaner.py",
    "cd ..",
    "cd step-2",
    "python cleaner_backend.py",
    "cd ..",
    "cd step-3",
    "python merging_ga4.py",
    "cd ..",
    "cd step-4",
    "python ga4_cleaner.py",
    "cd ..",
    "cd step-5",
    "python cleaner_native.py",
    "cd ..",
    "cd step-6",
    "python completing_ga4.py",
    "cd ..",
    "cd step-7",
    "python final_ga4.py",
    "cd .."
]

# Execute each command in the list
for command in commands:
    # Split the command string into its components
    parts = command.split()
    if parts[0] == "cd":
        # Change directory
        os.chdir(parts[1])
    else:
        # Execute command
        subprocess.run(parts)

    # Print the command being executed
    print("Executing:", command)

def delete_files(file_pattern):
    # Get a list of files matching the pattern
    files = glob.glob(file_pattern)
    # Loop through and delete each file
    for file in files:
        try:
            os.remove(file)
            print(f"Deleted: {file}")
        except Exception as e:
            print(f"Failed to delete {file}: {e}")

# Navigate to each folder and delete .csv and .xlsx files
base_path = os.getcwd()
folders = [f"step-{i}" for i in range(1, 8)]
for folder in folders:
    os.chdir(os.path.join(base_path, folder))
    delete_files('*.csv')
    delete_files('*.xlsx')

print("All commands executed successfully.")
