import os
os.system('pip3 install virtualenv')
os.system('virtualenv venv')
os.system('source venv/bin/activate')
os.system('pip3 install -r requirements.txt')
os.system('python3 -m app')
