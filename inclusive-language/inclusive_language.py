import sys

def run_command(command, cwd):
    subprocess.run(command, check=True, shell=True, cwd=cwd)

working_directory = sys.argv[1]

try:
    # Install the doc framework and run inclusive-language checker
    run_command('make install', working_directory)
    run_command('make woke', working_directory)
except subprocess.CalledProcessError as e:
    print(f"Command '{e.cmd}' returned non-zero exit status {e.returncode}.")
    exit(1)