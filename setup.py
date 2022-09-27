import subprocess

subprocess.run('python -m venv ./fbgroupphotoenv')
subprocess.run('./fbgroupphotoenv/scripts/python -m pip install -r requirements.txt')