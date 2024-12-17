# **Quiz Application**

This is a multi-user quiz application built with Django. Users can create quiz sessions, answer randomly selected questions, save their progress, or submit the session to view results.

---

## **Features**

1. **Multi-User Support** - Users can register, login and logout. Users can create independent quiz sessions.

2. Randomized Questions - The app picks **10 random questions** from the database for each session.

3. Session Persistence - **Save Progress**: Users can save incomplete sessions and resume later.
4. **Abandon Session**: Unanswered sessions are stored without progress. 

5. **Submit Results**: Users can submit their answers to see their score.

6. Dynamic UI - Clean and responsive UI using **Bootstrap 4**.

## **Technologies Used**
1. Backend: Django (Python)
2. Frontend: HTML, CSS, Bootstrap 4
3. Database: Postgreql (render)
4. Deployment: Render 

## **To run this project locally, follow these steps:**

### **Pre-requisites**
- Python and pip should already be installed on your system.

---

### **Without Git Installed**

- **Download** the ZIP file of the project and extract its contents.  
- Open your terminal and navigate to the project directory.  
- Run the following commands:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py populate_questions
python manage.py runserver
```

### **With Git Installed**

- Fork and/or clone the repository. 
```bash
git clone https://github.com/YourGithubUsername/quiz-app.git
```
or
```bash
git clone https://github.com/AllenJonathan/quiz-app.git
```
and
```bash
cd quiz-app
```

- Run the following commands in your terminal

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py populate_questions
python manage.py runserver
```

Access the site at: `http://localhost:8000/`

Also available at: https://quiz-app-9kw7.onrender.com/

## Challenges Faced

- Adopting the right database relationship.
- Saving current session's progress for later.
