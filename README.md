# Hostel-Site
1. Backend Framework: **Django**
2. Front-end Framework: **Bootstrap**

## Installation 

1. Fork and Clone
    <ol>
    <li>Fork Hostel-Site Repo</li>
    <li>Clone the repo to your computer.</li>
    </ol>

2. Create a Virtual Environment for the Project

    In Windows
    ```bash
    python -m venv env
    
    env\Scripts\activate
    ```

    In Ubuntu/MacOS
    ```bash
    python -m virtualenv env
    
    source env/bin/activate
    ```
   
   If you are giving a different name then `env`, then please mention it in `.gitigonre` first

3. Install all the requirements

    ```bash
    pip install -r requirements.txt
    ```

4. Make migrations/ Create db.sqlite3

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
5. Run server
    ```bash
    python manage.py runserver
    ```