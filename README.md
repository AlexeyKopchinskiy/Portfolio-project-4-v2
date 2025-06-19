# Booking System for Restaurants

## 🏡 About the Project
A web application allowing users to manage restaurant bookings effortlessly. Users can create, update, and delete their reservations while accessing personalized booking history.^

## 🔗 Live Demo  
Try the live version here: [Live Demo](https://portfolio-project-4-1f0987e45403.herokuapp.com/)  

## 📷 Screenshots  
Here are some previews of the app in action:

**Start page**
![Home Page](/static/images/screenshots/screenshot-start-page.jpg)  

**Booking page**
![Booking Page](/static/images/screenshots/screenshot-booking-page.jpg)  

## 🚀 Features
- Secure **user authentication**.
- **User-specific** booking history.
- Seamless **reservation management** (create, update, delete).
- Intuitive **admin panel** for restaurant staff.
- Administrator interface

This project uses a custom Django model architecture to handle restaurant bookings with flexibility, accessibility, and administrative clarity in mind.

## 📘 Models

**BookingStatus**
Represents the current state of a reservation (e.g., Pending, Confirmed, Cancelled).
| Field | Type | Description | 
| status | CharField | Unique name for the status | 


**Location**
Defines different seating areas in the restaurant, such as “Terrace” or “Window Booth”.
| Field | Type | Description | 
| location | CharField | Name of the area | 


**Table**
Each table is a reservable unit, assigned to a Location. Tables are annotated with features for better matching.
| Field | Type | Description | 
| size | SmallInteger | Number of seats | 
| smoking | Boolean | Whether smoking is allowed | 
| accessible | Boolean | If the table accommodates accessibility needs | 
| location | ForeignKey | Linked to Location | 


**Reservation**
Captures each booking made by a user, including time, table, guest count, and preferences.
| Field | Type | Description | 
| table | ForeignKey | Reserved table (Table) | 
| location | ForeignKey | Optional—can mirror table.location or be filtered | 
| user | ForeignKey | The user placing the booking (User) | 
| booking_date | DateField | Date of the reservation | 
| booking_time | TimeField | Time of the reservation | 
| num_of_guests | PositiveSmallInteger | Guest count | 
| booking_status | ForeignKey | Reservation status (BookingStatus) | 
| special_requests | TextField | Freeform requests (Summernote-enabled) | 
| booked_on | DateTimeField | Auto-generated timestamp when reservation is made | 


**Ordering**: Reservations are sorted newest-first via Meta.ordering = ["-booked_on"].

### 🧑‍💻 Access Control
- Users can only view and manage their own reservations.
- Staff and admins can see and edit all bookings via the Django Admin panel.
- Each reservation is linked to a user and referentially aware of its table and seating area.

## 🗂️ Entity-Relationship Overview

![custom model](/static/images/screenshots/custom-model.jpg)

🧠 Legend
- PK: Primary Key
- →: Foreign Key reference
- Arrows (↑) show relationships (e.g., Reservation → Table → Location)

### Admin backen available for the restaurant owner

**Back-end user manager**
![Admin user manager](/static/images/screenshots/admin-back-end-user-manager.jpg)

**Back-end reservation list**
![Back-end reservation list](/static/images/screenshots/admin-back-end-reservations-list.jpg)

**Back-end reservation editor**
![Back-end reservation editor](/static/images/screenshots/admin-back-end-reservations-editor.jpg)

## 🛡️ Security Measures
- **Encrypted passwords** using Django’s authentication system.  
- **CSRF protection** for all forms.  
- **User roles and permissions** to restrict access to sensitive data.

## 🧪 Testing

### 🔄 Manual Testing
**Perform functional testing by following these steps:**
- User Authentication: Test login, logout, and registration flows.
- Booking Process: Make, update, and cancel a reservation.
- Admin Panel: Verify access control and reservation management.

### ✅ Steps to Validate Django Templates Using W3C Validator
- 1️⃣ Open your browser's Developer Tools (F12 → Elements tab).
- 2️⃣ Find the rendered HTML of the Django page.
- 3️⃣ Right-click → "View Page Source" or "Inspect" → Copy the full HTML.
- 4️⃣ Go to W3C Validator.
- 5️⃣ Choose "Validate by Direct Input" and paste the copied HTML.
- 6️⃣ Click "Check" and review the errors/warnings.
- 7️⃣ Fix any structural issues in your Django templates ( folder).
- ✔ Validates dynamic HTML instead of raw Django template tags.
- ✔ Helps detect missing closing tags, incorrect attributes, and accessibility issues.

**W3 validation results for the start page**
![w3validator start page](/static/images/screenshots/w3validator-start-page.jpg)

**W3 validation results for the booking page**
![w3validator booking page](/static/images/screenshots/w3validator-booking-page.jpg)

## 🔍 Code Quality & Linting

### 📝 PEP8 Validation with Code Institute Linter
**To ensure your Python code follows best practices:**
- 1️⃣ Go to [Code Institute Linter](https://pep8ci.herokuapp.com/).  
- 2️⃣ Paste your Python code into the input field.  
- 3️⃣ Click **"Check Code"** to identify formatting issues.  
- 4️⃣ Apply suggested fixes for improved readability and maintainability.

#### C.I. Linter validation results:

**C.I. validation results for the booking views**
![Booking app views.py](/static/images/screenshots/ci_linter_results_for_booking_views.jpg)

**C.I. validation results for the booking urls**
![Booking urls.py](/static/images/screenshots/ci_linter_results_for_booking_urls.jpg)

### 

### ✅ Additional Linting Tools
**For automated checks, use:**

```bash
pip install flake8
flake8 your_project/
```

### 🐛 Debugging & Error Handling
- Check logs: tail -f logs/error.log
- Use Django’s debug mode: DEBUG=True in settings.py
- Inspect database queries: python manage.py shell

## 🛠️ Installation
Follow these steps to set up the project locally:

### bash
- git clone https://github.com/your-repo.git
- cd your-repo
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py runserver

## 🎯 Usage
- Sign up/Login to access your booking dashboard.
- Create a reservation with your preferred date and time.
- Manage bookings via the member page.
- Admin users can oversee all reservations.

### 📌 Technologies Used
- Django (backend framework)
- SQLite/PostgreSQL (database)
- Bootstrap (frontend styling)
- Python (core programming language)
- CSS
- JavaScript
- HTML

### 🤝 Contributing
We welcome contributions! To contribute:
- Fork the repository.
- Create a new branch (git checkout -b feature-branch).
- Commit changes (git commit -m "Added new feature").
- Push to GitHub and create a pull request.

## Known Bugs
There are no known bugs.

### 📄 License
This project is licensed under the MIT License.

### 📢 Contact
For questions or support, reach out at kopchinskiy@gmail.com.
