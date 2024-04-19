import os
import sys
import subprocess

def run_command(command, cwd):
    subprocess.run(command, check=True, shell=True, cwd=cwd)

working_directory = sys.argv[1]

try:
    # Install Aspell
    run_command('sudo apt-get install aspell aspell-en', working_directory)

    # If the starter pack Makefile is available, use it
    makefile = "Makefile"
    if os.path.exists(os.path.join(working_directory, "Makefile.sp")):
        makefile = "Makefile.sp"

    # Install the doc framework and run spelling checker
    run_command(f"make -f {makefile} install", working_directory)
    run_command(f"make -f {makefile} spelling", working_directory)
except subprocess.CalledProcessError as e:
    print(f"Command '{e.cmd}' returned non-zero exit status {e.returncode}.")
    exit(1)