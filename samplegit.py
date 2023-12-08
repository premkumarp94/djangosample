import datetime
import subprocess

def get_current_datetime_string():
    now = datetime.datetime.now()
    return now.strftime("%Y%m%d%H%M%S")

# Call the function to get the current date and time in "yyyymmddhhmmss" format
current_datetime_string = get_current_datetime_string()


def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True)
        print(result)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while executing '{command}': {e}")
        raise

# Replace these variables with your own values
#repository_path = r'C:/prem/src/workspace1/python'
commit_message = "ec2in4_" + current_datetime_string

# Example Git commands
commands = [
    #f"cd /d {repository_path}",          # Change directory to the repository path
    f"git add .",                         # Stage all changes
    f'git commit -m "{commit_message}"', # Commit changes
    "git branch -M main",            # Pull from remote (optional)
    "git push -u origin main"             # Push to remote
]

# Run the commands in sequence
for command in commands:
    run_command(command)

print("Git commands executed successfully.")