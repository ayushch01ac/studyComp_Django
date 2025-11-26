* * *


# 📚 Study Room – Django-Based Chat App

A full-stack web application where users can register, log in, create topic-based public rooms, and engage in real-time conversations. Built using Django's MVT architecture with custom user authentication and secure environment-based deployment.

---

## ✨ Features

- 🧑‍💼 User registration, login, and logout
- 💬 Create and join topic-based public chat rooms
- 📥 Post and view messages in real time (page refresh)
- 🔐 Custom user authentication with model-level validation
- 🛠️ Admin panel for managing topics, rooms, and users
- 🌐 Responsive UI with clean layout

---

## 🏗️ Tech Stack

- **Backend**: Django (MVT architecture)
- **Database**: PostgreSQL (via [Neon](https://neon.tech))
- **Frontend**: HTML, CSS (with Django templates)
- **Deployment**: [Render](https://render.com) (cloud deployment)
- **Version Control**: Git & GitHub

---

## 🚀 Getting Started

### 🔧 Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/ayushch01ac/studyComp_Django.git
   cd studyComp_Django
    ```

2.  **Create and activate a virtual environment**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    ```
3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Set environment variables**  
    Create a `.env` file and add:
    ```env
    SECRET_KEY=your_secret_key
    DEBUG=True
    DATABASE_URL=your_neon_postgres_connection_url
    ```
5.  **Apply migrations**
    ```bash
    python manage.py migrate
    ```
6.  **Run the server**
    ```bash
    python manage.py runserver
    ```

* * *

🧪 Usage
--------

*   Navigate to `http://localhost:8000`
*   Register a new user
*   Browse existing rooms or create a new one
*   Post and view messages in the chat

* * *

🌍 Live Demo
------------

*   🔗 GitHub: [studyComp\_Django](https://github.com/ayushch01ac/studyComp_Django)
*   🚀 Live App: https://chatroom-pa4f.onrender.com/
* * *

📄 License
----------

This project is licensed under the MIT License – see the LICENSE file for details.

* * *

👤 Author
---------

*   **Ayush Choudhary**  
    🔗 [GitHub](https://github.com/ayushch01ac)

* * *

🤝 Contributing
---------------

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

* * *
