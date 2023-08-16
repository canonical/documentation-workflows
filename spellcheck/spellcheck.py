import subprocess

def run_command(command):
    subprocess.run(command, check=True, shell=True)

try:
    # Install Aspell
    run_command('sudo apt-get install aspell aspell-en')

    # Install the doc framework and run spelling checker
    run_command('make install')
    run_command('make spelling')
except subprocess.CalledProcessError as e:
    print(f"Command '{e.cmd}' returned non-zero exit status {e.returncode}.")
    exit(1)