import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
"""
\33[34m                ▄▄▄▄▄▄▄▄\33[0m
\33[34m           ▄████████████████▄\33[0m
\33[34m          ▐██   ▐█████████████\33[0m
\33[34m          ▐███▄▄██████████████\33[0m
\33[34m           ▀▀▀▀▀▀▀▀▀██████████\33[0m
\33[34m   ▄▄█████████████████████████\33[0m \33[33m██████\33[0m
\33[34m ▄████████████████████████████\33[0m \33[33m████████\33[0m
\33[34m▐█████████████████████████████\33[0m \33[33m█████████\33[0m
\33[34m████████████████████████████▀\33[0m  \33[33m█████████\33[0m
\33[34m███████████▀▀\33[0m                \33[33m▟██████████\33[0m
\33[34m█████████▌\33[0m  \33[33m████████████████████████████\33[0m
\33[34m▐████████\33[0m  \33[33m█████████████████████████████\33[0m
\33[34m ▀███████\33[0m  \33[33m████████████████████████████\33[0m
\33[34m   ▀█████\33[0m  \33[33m██████████████████████████\33[0m
\33[33m           █████████\33[0m
\33[33m           ███████████████████\33[0m
\33[33m           █████████████   ▐██\33[0m
\33[33m            █████████████████\33[0m
\33[33m                   ███\33[0m
"""

def initialize_git(project_directory):
    """
    Initialize the git repo.

    Args:
        project_directory:
    """
    import subprocess

    result = subprocess.run(
        ["git", "init"], cwd=project_directory, encoding="utf8", capture_output=True
    )
    if result.returncode != 0:
        print("Unable to initialize the git repo.")
        print(result.stdout, result.stderr)

    result = subprocess.run(
        ["git", "add", "."], cwd=project_directory, encoding="utf8", capture_output=True
    )
    if result.returncode != 0:
        print("Unable to add all files into the git repo.")
        print(result.stdout, result.stderr)

    result = subprocess.run(
        ["git", "commit", '-m"Initial commit"'],
        cwd=project_directory,
        encoding="utf8",
        capture_output=True,
    )
    if result.returncode != 0:
        print("Unable to make the initial commit.")
        print(result.stdout, result.stderr)

    result = subprocess.run(
        ["git", "tag", "0.1.0"],
        cwd=project_directory,
        encoding="utf8",
        capture_output=True,
    )
    if result.returncode != 0:
        print("Unable to tag the initial commit.")
        print(result.stdout, result.stderr)


initialize_git(PROJECT_DIRECTORY)
