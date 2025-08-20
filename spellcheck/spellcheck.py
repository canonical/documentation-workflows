import os
import sys
import subprocess
import argparse

def run_command(command, cwd):
    subprocess.run(command, check=True, shell=True, cwd=cwd)
parser = argparse.ArgumentParser()
parser.add_argument("working_dir")
parser.add_argument("--install_target")
parser.add_argument("--spelling_target")
parser.add_argument("--makefile")
args = parser.parse_args()

install_target = args.install_target
spelling_target = args.spelling_target
makefile = args.makefile

try:
    # Install Aspell
    run_command('sudo apt-get -y install aspell aspell-en', args.working_dir)
    
    # If the Makefile has not been specified, use the starter pack Makefile (and the corresponding
    # targets) if available. Otherwise, use "Makefile".
    if makefile == "use-default":
        if os.path.exists(os.path.join(args.working_dir, "Makefile.sp")):
            makefile = "Makefile.sp"
            install_target = "sp-" + install_target
            spelling_target = "sp-" + spelling_target
        else:
            makefile = "Makefile"

    # Install the doc framework and run spelling checker
    run_command(f"make -f {makefile} {install_target}", args.working_dir)
    run_command(f"make -f {makefile} {spelling_target}", args.working_dir)
except subprocess.CalledProcessError as e:
    print(f"Command '{e.cmd}' returned non-zero exit status {e.returncode}.")
    exit(1)
