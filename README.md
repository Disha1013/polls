# Django – (Polls App)

**Day 1 Task:**
This contains my **Day 1 work**  
The goal of this task was to set up a Django application, create a basic **Polls App**, define models, configure URLs, and push the code to GitHub.

## What is delivered
- Django application running locally on **port 8000**
- Polls app created 
- Basic model defined and migrated
- URL routing configured
- Project pushed to personal GitHub repository
  
## Tech Stack
- **Python**
- **Django**
- **SQLite** (default Django database)
  
## How to run this project
1. Clone the repository: 
git clone <repository-url> , 
cd Week1-django
2. Create and activate virtual environment: 
python -m venv venv , 
venv\Scripts\activate
3. Install dependencies: 
pip install -r requirements.txt
4. Apply migrations:  
cd mysite , 
python manage.py migrate
5. Run the server: 
python manage.py runserver
6. Open in browser:
http://127.0.0.1:8000/

## LOOM VIDEO:
https://www.loom.com/share/60934a41dc444ef4a6b56c1f0f1b999a


**Day 2 Task:** 
This contains my **Day-2** work

## What I Implemented
- Defined Django models using the ORM:
  - `Question` model to store poll questions
  - `Choice` model to store choices related to a question
- Created a **one-to-many relationship** between `Question` and `Choice` using `ForeignKey`
- Used Django migrations to create/update Database tables
- Verified everything using Django Admin and Django ORM

## Loom Video:
https://www.loom.com/share/e1f32bee5a244223a10062741b8b9003



