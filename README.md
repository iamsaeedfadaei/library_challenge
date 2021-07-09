# library_challenge
This project was done by me as a challenge.
Challenge statements:

Part I:

    1. Create User Profile, Author, Publisher, Book models.

Part II:

    by Django Rest Framework we have:
        1. Retrieve Publishers listings
        2. Retrieve Authors listings
        3. Retrieve Books Listings
        4. Retrieve any Author Books.
        5. Retrieve any Publisher Books.
        6. Create Books for any specific Author
        7. create Book for any specific Publisher
    
Additional Features:

    1. Any User Profile, Author, Book, Publisher can be created, edited and deleted from Admin Panel.
    2. Specific Author's Books can be filtered from Admin Panel.
    3. Specific Publisher's books can be filtered from Admin Panel.
    4. Books are searchable by title from Admin Panel.
    
Technologies Used:

    Python
    Django
    Jinja

Additional Python Modules Required:

    Django
    Django Rest Framework
    Pillow
    Asgiref
    Pytz
    Sqlparse
    

Note :

project can be used by:
    1. virtualenv virtual_env_name
    2. pip install -r requirements.txt
    3. python django_web_app/manage.py makemigrations
    4. python django_web_app/manage.py migrate
    5. python django_web_app/manage.py runserver
    
In your web browser enter these addresses : 
    http://localhost:8000 or http://127.0.0.1:8000/
    http://127.0.0.1:8000/management/book/
    http://127.0.0.1:8000/management/author/
    http://127.0.0.1:8000/management/publisher/
    http://127.0.0.1:8000/management/author/author_id/
    http://127.0.0.1:8000/management/publisher/publisher_id/
    
    
