from pathlib import Path

# Absolute path = from hard drive to here
# Relative path = from file to other file

# No argument in Path() = current directory
path = Path()
# mkdir, rmdir, glob = getting files in directory
for file in path.glob('*.py'): #searches current directory for .py files
    print(file)