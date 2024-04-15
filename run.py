import subprocess
import os

# Define the path to your bash script
script_path = './chure.sh'

os.system(script_path)
'''
try:
    # Run the bash script
    result = subprocess.run([script_path], capture_output=True, text=True, check=True)
    print("stdout:", result.stdout)
except subprocess.CalledProcessError as e:
    print("An error occurred while trying to execute the script.")
    print("stderr:", e.stderr)
except FileNotFoundError:
    print(f"The script {script_path} does not exist.")
except Exception as e:
    print("An unexpected error occurred:", str(e))
'''

