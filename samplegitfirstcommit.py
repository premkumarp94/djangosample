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
#repository_path = r'C:/prem/src/workspace1'
commit_message = "ec2instance4" + current_datetime_string

# Example Git commands
commands = [
    #f"cd /d {repository_path}",          # Change directory to the repository path
    "git init",
    "git add .",                         # Stage all changes
    #"git add README.md",   
    f'git config --global --add safe.directory C:/Users/Administrator/Downloads/bkpdj',
    f'git config --global user.email "prex1994@gmail.com"',
    f'git config --global user.name "premkumarp94"',
    f'git commit -m "first commit a5"', # Commit changes
    "git branch -M main",            # Pull from remote (optional)
    "git remote add origin https://github.com/premkumarp94/djangosample.git",
    "git push -u origin main"             # Push to remote
]

try:
    run_command("git remote remove origin")
except Exception as e:
    pass

# Run the commands in sequence
for command in commands:
    run_command(command)

print("Git commands executed successfully.")