 echo "BUILD START"
 python3.9 -m pip install -r requirements.txt
 python3.9 manage.py collectstatic --noinput --clear
 python3.9 manage.py makemigrations
 python3.9 manage.py migrate
 python3.9 manage.py createsuperuser --username=apcoer --email=admin@example.com --noinput --password=apcoer@123
 echo "BUILD END"
