<h1 align="center">Laundry Services Booking & Management System</h1>

<p align="center">
A full-stack **Laundry Services Web Application** built using **Django**, designed to manage laundry services, products, blogs, and customer interactions.  
The project is deployed live and accessible online.
</p>

---

  <p align="center" >
    <img src="https://i0.wp.com/htmlcodex.com/wp-content/uploads/2020/12/dryme.jpg?w=800&ssl=1"/>
  </p> 

---



🌐 **Live Demo:**  
👉 https://anurag7.pythonanywhere.com

---

## 🚀 Features

- 🏠 Clean and responsive home page
- 🧾 Service and product management
- 📰 Blog articles section
- 📩 Contact form for customer queries
- 🛠️ Django Admin Panel
- 📦 Static files handling
- 🔐 Secure backend with Django ORM

---

## 🛠️ Tech Stack

- **Backend:** Python, Django  
- **Frontend:** HTML, CSS, JavaScript  
- **Database:** SQLite (development)  
- **Deployment:** PythonAnywhere  
- **Version Control:** Git & GitHub  

---

## ⚙️ Installation & Setup (Local)

Follow these steps to run the project locally:

```bash
# Clone the repository
git clone https://github.com/anuragtiwari8010-sys/laundry_services.git

# Move into project directory
cd laundry_services

# Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
