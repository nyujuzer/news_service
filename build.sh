set -a
source .env
set +a
pip install -r requirements.txt
python manage.py make_admin --username $USERNAME --password $PASSWORD --email $EMAIL --noinput
python manage.py makemigrations
python manage.py migrate