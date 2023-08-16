import sys
import subprocess

def run_command(command, cwd):
    subprocess.run(command, check=True, shell=True, cwd=cwd)

working_directory = sys.argv[1]

try:
    # Install Aspell
    run_command('sudo apt-get install aspell aspell-en', working_directory)

    # Install the doc framework and run spelling checker
    run_command('make install', working_directory)
    run_command('make spelling', working_directory)
except subprocess.CalledProcessError as e:
    print(f"Command '{e.cmd}' returned non-zero exit status {e.returncode}.")
    exit(1)