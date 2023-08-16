import sys

utils_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'utils.py')
from utils_path import run_command

working_directory = sys.argv[1]

try:
    # Install the doc framework and run link checker
    run_command('make install', working_directory)
    run_command('make linkcheck', working_directory)
except subprocess.CalledProcessError as e:
    print(f"Command '{e.cmd}' returned non-zero exit status {e.returncode}.")
    exit(1)