 echo "BUILD START"
 python3.9 -m pip install -r requirements.txt
 python3.9 manage.py collectstatic --noinput --clear
 echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('apcoer', '', 'apcoer@123')" | python manage.py shell
 python3.9 manage.py makemigrations
 python3.9 manage.py migrate
 echo "BUILD END"
