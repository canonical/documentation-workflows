import os
import sys
import subprocess
import argparse

def run_command(command, cwd):
    subprocess.run(command, check=True, shell=True, cwd=cwd)

parser = argparse.ArgumentParser()
parser.add_argument("working_dir")
parser.add_argument("--woke_target")
parser.add_argument("--makefile")
args = parser.parse_args()

woke_target = args.woke_target
makefile = args.makefile

try:
    # If the Makefile has not been specified, use the starter pack Makefile (and the corresponding
    # targets) if available. Otherwise, use "Makefile".
    if makefile == "use-default":
        if os.path.exists(os.path.join(args.working_dir, "Makefile.sp")):
            makefile = "Makefile.sp"
            woke_target = "sp-" + woke_target
        else:
            makefile = "Makefile"

    # Install the doc framework and run inclusive-language checker
    run_command(f"make -f {makefile} {woke_target} CONFIRM_SUDO=y", args.working_dir)
except subprocess.CalledProcessError as e:
    print(f"Command '{e.cmd}' returned non-zero exit status {e.returncode}.")
    exit(1)
