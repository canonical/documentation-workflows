import os
import sys
import subprocess

def run_command(command, cwd):
    subprocess.run(command, check=True, shell=True, cwd=cwd)

working_directory = sys.argv[1]

try:
    # If the starter pack Makefile is available, use it
    makefile, prefix = "Makefile", ""
    if os.path.exists(os.path.join(working_directory, "Makefile.sp")):
        makefile, prefix = "Makefile.sp", "sp-"

    # Install the doc framework and run link checker
    run_command(f"make -f {makefile} {prefix}install", working_directory)
    run_command(f"make -f {makefile} {prefix}pa11y", working_directory)
except subprocess.CalledProcessError as e:
    print(f"Command '{e.cmd}' returned non-zero exit status {e.returncode}.")
    exit(1)
