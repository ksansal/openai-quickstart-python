cd openai-quickstart-python
cp .env.example .env

python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
flask run