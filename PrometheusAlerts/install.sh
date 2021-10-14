#NOTE: This assumes "python3" maps to some reasonable 3.X version that will work with the script
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install -r flask-app/requirements.txt
