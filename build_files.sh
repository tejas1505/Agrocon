 echo "BUILD START"
 python3.9 -m pip install -r requirements.txt
 pip install sqlite3
 python3.9 manage.py collectstatic --noinput --clear
 python3.9 manage.py makemigrations
 python3.9 manage.py migrate
 echo "BUILD END"
