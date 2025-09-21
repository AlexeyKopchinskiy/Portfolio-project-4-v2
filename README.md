# Coders Sushi bar website

![Website responsiveness mock up](./static/images/sushi-bar-mockup.png) 

Coders Sushi Bar is a full-stack Django web application that simulates a modern sushi restaurant experience, combining user-friendly booking functionality, secure authentication, and dynamic content delivery. Built around three modular apps—booking, pages, and users—the system offers a clean, responsive interface powered by Bootstrap, with centralized templates and rich text editing via Summernote. It’s designed for deployment on Heroku, supports cloud development with Gitpod, and integrates optional Google Sheets functionality for data export. Whether you're managing reservations or customizing your profile, Coders Sushi Bar delivers a polished, production-ready platform with a playful touch.

---

## Table of Contents

* [Overview](#overview)
* [Agile Methodology](#agile-methodology)
- User Experience (UX)
  - Strategy / Site Goals
  - Scope / User Stories
  - Structure / Design Choices
  - Skeleton / Wireframes
  - Surface
- Features
  - Existing Features
  - Future Features
- Business Model
- Database design
- Django Apps
- Authentication & Authorization
- Product Management
- Cart & Checkout Flow
- Payment Integration
- Order Management
- Media & File Storage
- Session & Security Features
- Technologies Used
- Testing
- Bugs
- Deployment
- Credits
- Acknowledgements

---

## Overview

**Coders Sushi Bar** is a full-stack Django web application built as part of the Code Institute Portfolio Project 4. It simulates a modern sushi restaurant platform, offering users a seamless experience to explore the menu, book tables, and manage their profiles — all within a clean, responsive interface.

The project is structured around three core Django apps:

- **`booking`**: Handles table reservations, including form submissions, availability logic, and user-specific booking views.
- **`pages`**: Manages static and semi-static content such as the homepage, about page, and menu, providing the public-facing identity of the restaurant.
- **`users`**: Manages user authentication, registration, profile editing, and personalized member areas.

The application is designed with modularity and maintainability in mind. All templates are centralized under a shared `/templates` directory, with subfolders for each app and a unified `base.html` layout that includes navigation, footer, and content blocks. The interface is styled using Bootstrap 5 and enhanced with custom CSS and JavaScript, while rich text editing is supported via Summernote.

Coders Sushi Bar is deployed on Heroku and configured for cloud development via Gitpod. It uses environment variables for secure settings, integrates Google Sheets via `gspread` for optional data export, and supports full password reset flows out of the box.

Whether you're a hungry coder or a curious diner, this project serves up a polished, production-ready experience — with no errors, just sushi.

[Back To Top](#table-of-contents)

---

## Agile Methodology

Coders Sushi Bar was developed using a structured Agile approach, emphasizing iterative delivery, stakeholder alignment, and continuous improvement. The project was divided into five weekly milestones, each functioning as a sprint with clearly defined deliverables and review checkpoints. Development was guided by a comprehensive set of user stories and grouped into strategic **epics**, ensuring that every feature served a real user need and contributed to the overall system architecture.

<details>
<summary>Screenshots of Kanban Board, Milestones and project board view</summary>

![Kanband: Kanban board](./static/images/github-user-stories-kanban-broject.PNG)

![Kanband: User Stories and epic board](./static/images/github-user-stories-list.png)

![Kanband: Milestones](./static/images/github-milestones.JPG)

</details>

### 📆 Milestone Breakdown

**Milestone 1: Project Setup & Authentication (Week 1)**
- Initialize Git repository and configure GitHub
- Set up Django project and database structure
- Implement user authentication (sign-up, login, logout)
- Apply role-based access control for customers & restaurant owners
- Deploy basic version for testing

**Milestone 2: Booking System Development (Week 2)**
- Design models for restaurant, tables, reservations
- Implement booking functionality with date/time selection
- Prevent double bookings
- Create email notifications for confirmed bookings
- Develop user-friendly booking interface

**Milestone 3: Dashboard & Menu Management (Week 3)**
- Build restaurant owner dashboard to manage reservations
- Display menu details with update functionality
- Allow restaurant owners to cancel/modify bookings
- Implement feedback system for customer reviews
- Optimize UI for easy navigation

**Milestone 4: Testing & Optimization (Week 4)**
- Write automated Python and JavaScript tests for major features
- Perform manual UX testing
- Optimize performance (database indexing, caching)
- Secure app (hiding secret keys, disabling debug mode)
- Final debugging before deployment

**Milestone 5: Deployment & Documentation (Week 5)**
- Deploy final version & test in cloud environment
- Complete final README documentation
- Ensure repo cleanliness (no secrets, structured commits)
- Submit project 🎉

---

### 🧩 Epic Overview

| Epic | Focus |
|------|-------|
| **Back-End** | Django architecture, models, views, and database logic |
| **Blog** | Optional restaurant blog interface and content management |
| **Booking System** | Reservation flow, availability checks, and email confirmations |
| **Version Control & Documentation** | GitHub setup, commit hygiene, README and Wiki |
| **User Authentication & Role-Based** | Secure login, sign-up, and access control |
| **User Feedback & Assistance** | Reviews, help guides, and onboarding flows |
| **Database Optimization** | Query tuning, indexing, and performance improvements |
| **Deployment & Security** | Heroku deployment, environment variables, and HTTPS |
| **Testing & Validation** | Unit tests, integration tests, and manual UX reviews |
| **Dashboard** | Admin interface for managing bookings and menus |
| **Front-End** | Responsive design, navigation, and user experience |
| **Monitoring** | Logging, error tracking, and system stability tools |

---

### 🎯 MoSCoW Prioritization

To ensure delivery of a minimum viable product (MVP) while allowing room for enhancement, features were prioritized using the **MoSCoW method**:

- **Must-Have**: User authentication, booking system, dashboard access, email confirmations, secure deployment
- **Should-Have**: Menu management, role-based access control, customer feedback, automated testing
- **Could-Have**: Blog interface, analytics dashboard, Google Sheets integration, monitoring tools
- **Won’t-Have (for now)**: Real-time availability updates, multi-language support, payment integration

---

This Agile framework enabled Coders Sushi Bar to evolve from concept to cloud-deployed reality with clarity, velocity, and resilience. Each sprint delivered tangible value, and every epic was aligned with user stories that reflected real-world needs — from hungry customers to busy restaurant owners to meticulous developers.



























--------------------------------------------------------------------------------
OLD STUFF
--------------------------------------------------------------------------------

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

### Validating with JSHint

**No erros found by JSHint:**
![JSHint report](/static/images/screenshots/jshint-report.jpg)

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
