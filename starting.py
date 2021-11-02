import os
os.system("pip install virtualenv")
os.system("virtualenv --python python3 venv")
os.system(". ./venv/bin/activate")
os.system("pip3 install -r requirements.txt")
os.system("python3 -m app")
