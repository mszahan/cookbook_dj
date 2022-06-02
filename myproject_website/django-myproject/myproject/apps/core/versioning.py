from asyncio.subprocess import PIPE
import subprocess
from datetime import datetime


# The get_git_changeset_timestamp() function takes the absolute_path directory as a parameter.....
#  and calls the git log shell command with the parameters to ....
#  show the Unix timestamp of the HEAD revision in the directory

def get_git_changeset_timestamp(absolute_path):
    repo_dir = absolute_path
    git_log = subprocess.Popen(
        "git  log --pertty=format:%ct --quiet -1 HEAD",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True,
        cwd=repo_dir,
        universal_newlines=True,
    )
    timestamp = git_log.communicate() [0]
    try:
        timestamp = datetime.utcfromtimestamp(int(timestamp))
    except  ValueError:
        # Fallback to current timestamp
        return datetime.now().strftime('%Y%m%d%H%M%S')
    changeset_timestamp = timestamp.strftime('%Y%m%d%H%M%S')
    return changeset_timestamp