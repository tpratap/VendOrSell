**1. Create a folder backend and push all files in backend folder**

**2. Install Virtual Environment**

pip install virtualenvwrapper-win

**3. Create Virtual Environment**

python -m venv <env_name>

**4. Activate virtual Environment**

source <env_name>/Scripts/activate

**5. Install all dependencies**
cd backend
pip install -r requirements.txt 

**6. Install Postgres, Create Database in pgAdmin**

**7. Connect to Database by entering same credentials as settings.py Databases section** 

**8. Make database ready for migrations** 

python manage.py makemigrations

**9. Migrate database**

python manage.py migrate

**10. Run server**

python manage.py runserver

**API End Points**

    admin/
    signup/ [name='authemail-signup']
    signup<drf_format_suffix:format> [name='authemail-signup']
    signup/verify/ [name='authemail-signup-verify']
    signup/verify<drf_format_suffix:format> [name='authemail-signup-verify']
    login/ [name='authemail-login']
    login<drf_format_suffix:format> [name='authemail-login']
    logout/ [name='authemail-logout']
    logout<drf_format_suffix:format> [name='authemail-logout']
    password/reset/ [name='authemail-password-reset']
    password/reset<drf_format_suffix:format> [name='authemail-password-reset']
    password/reset/verify/ [name='authemail-password-reset-verify']
    password/reset/verify<drf_format_suffix:format> [name='authemail-password-reset-verify']
    password/reset/verified/ [name='authemail-password-reset-verified']
    password/reset/verified<drf_format_suffix:format> [name='authemail-password-reset-verified']
    email/change/ [name='authemail-email-change']
    email/change<drf_format_suffix:format> [name='authemail-email-change']
    email/change/verify/ [name='authemail-email-change-verify']
    email/change/verify<drf_format_suffix:format> [name='authemail-email-change-verify']
    password/change/ [name='authemail-password-change']
    password/change<drf_format_suffix:format> [name='authemail-password-change']
    users/me/ [name='authemail-me']
    users/me<drf_format_suffix:format> [name='authemail-me']

