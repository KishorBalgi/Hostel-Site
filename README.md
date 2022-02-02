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
### Snapshots

![image](https://user-images.githubusercontent.com/75678927/152208348-ea4f05a7-691f-4fb3-a4a0-bdec6a01b2f0.png)

![image](https://user-images.githubusercontent.com/75678927/152208492-0c0def6c-ea76-4e6e-b04e-821923209df4.png)

![image](https://user-images.githubusercontent.com/75678927/152208558-270ef226-7861-4d93-9bcb-2241bf3bc5bc.png)

![image](https://user-images.githubusercontent.com/75678927/152208664-6b79a332-00f5-4996-9cb8-9a442608ae5f.png)
