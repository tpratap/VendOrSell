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

