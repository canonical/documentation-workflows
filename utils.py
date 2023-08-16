import subprocess

def run_command(command, cwd):
    subprocess.run(command, check=True, shell=True, cwd=cwd)