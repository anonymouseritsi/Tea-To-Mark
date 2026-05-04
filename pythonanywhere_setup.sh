# PythonAnywhere Deployment Commands
# Run these commands in your PythonAnywhere bash console

# 1. Navigate to your project directory
cd ~/milk_tea_shop

# 2. Create and activate virtual environment
python3.11 -m venv venv
source venv/bin/activate

# 3. Install requirements
pip install -r requirements.txt

# 4. Set up Django settings for production
export DJANGO_SETTINGS_MODULE=config.settings
export SECRET_KEY='your-secret-key-here-change-this'

# 5. Run database migrations
python manage.py migrate

# 6. Initialize product data
python initialize_db.py

# 7. Collect static files
python manage.py collectstatic --noinput

# 8. Test the application
python manage.py runserver 0.0.0.0:8000