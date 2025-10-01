# Coders Sushi bar website

![Website responsiveness mock up](/static/images/sushi-bar-mockup.png) 

Coders Sushi Bar is a full-stack Django web application that simulates a modern sushi restaurant experience, combining user-friendly booking functionality, secure authentication, and dynamic content delivery. Built around three modular apps—booking, pages, and users—the system offers a clean, responsive interface powered by Bootstrap, with centralized templates and rich text editing via Summernote. It’s designed for deployment on Heroku, supports cloud development with Gitpod, and integrates optional Google Sheets functionality for data export. Whether you're managing reservations or customizing your profile, Coders Sushi Bar delivers a polished, production-ready platform with a playful touch.

---

## Table of Contents

* [Overview](#overview)
* [Agile Methodology](#agile-methodology)
* [User Experience (UX)](#user-experience-ux)
  * [Strategy / Site Goals](#-strategy--site-goals)
  * [Scope / User Stories](#-scope--user-stories)
  * [Structure / Design Choices](#-structure--design-choices)
  * [Skeleton / Wireframes](#-skeleton--wireframes)
  * [Surface](#-surface)
* [Features](#features)
  * [Existing Features](#-existing-features)
  * [Future Features](#-future-enhancements)
* [Business Model](#-business-model)
* [Screenshots](#screenshots)
* [Database design](#️-database-design)
* [Django Apps](#-django-apps-overview)
* [Authentication & Authorization](#-authentication--authorization)
* [Technologies Used](#-technologies-used)
* [Testing](#-manual-testing)
* [Bugs & Limitations](#known-bugs-and-limitations)
* [Deployment](#-deployment)
* [Credits](#-credits)
* [Acknowledgements](#-acknowledgements)
* [License](#-license)
* [Contact](#-contact)

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

- Kanban board:

![Kanband: Kanban board](/static/images/github-user-stories-kanban-broject.PNG)

- User Stories and epic board

![Kanband: User Stories and epic board](/static/images/github-user-stories-list.png)

- Milestones:

![Kanband: Milestones](/static/images/github-milestones.jpg)

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

### 🎯 MoSCoW Prioritization

To ensure delivery of a minimum viable product (MVP) while allowing room for enhancement, features were prioritized using the **MoSCoW method**:

- **Must-Have**: User authentication, booking system, dashboard access, email confirmations, secure deployment
- **Should-Have**: Menu management, role-based access control, customer feedback, automated testing
- **Could-Have**: Blog interface, analytics dashboard, Google Sheets integration, monitoring tools
- **Won’t-Have (for now)**: Real-time availability updates, multi-language support, payment integration

This Agile framework enabled Coders Sushi Bar to evolve from concept to cloud-deployed reality with clarity, velocity, and resilience. Each sprint delivered tangible value, and every epic was aligned with user stories that reflected real-world needs — from hungry customers to busy restaurant owners to meticulous developers.

[Back To Top](#table-of-contents)

---

## User Experience (UX)

Coders Sushi Bar was designed with a user-first mindset, balancing intuitive navigation, responsive design, and functional clarity. The UX strategy was informed by Agile planning, detailed user stories, and a modular architecture that supports both customer-facing and administrative workflows.

---

### 🎯 Strategy / Site Goals

The primary goal was to create a seamless digital experience for a fictional sushi restaurant, enabling users to:
- Browse the restaurant’s offerings without logging in
- Book tables with real-time availability and receive confirmation
- Manage their accounts and reservations
- Provide restaurant owners with a dashboard to oversee bookings, menus, and customer feedback

Secondary goals included:
- Ensuring mobile responsiveness across all devices
- Supporting secure authentication and role-based access
- Delivering a polished, production-ready deployment with clear documentation

---

### 📋 Scope / User Stories

User stories were categorized by persona and prioritized using the MoSCoW method:

#### Must-Have
- Customers can sign up, log in, and book tables
- Restaurant owners can view, modify, and cancel reservations
- Email confirmations for bookings
- Secure authentication and role-based access control

#### Should-Have
- Menu management for restaurant owners
- Customer feedback system
- Responsive design and mobile-friendly navigation
- Automated testing and performance optimization

#### Could-Have
- Blog interface for restaurant updates
- Google Sheets integration for analytics
- Monitoring and logging tools

User stories were grouped into strategic **epics**:
- **Booking System**
- **User Authentication & Role-Based Access**
- **Dashboard**
- **Front-End**
- **Deployment & Security**
- **Testing & Validation**
- **Version Control & Documentation**
- **Monitoring**
- **Database Optimization**
- **User Feedback & Assistance**
- **Blog**
- **Back-End**

---

### 🧱 Structure / Design Choices

The site architecture reflects a clean separation of concerns:
- Three core Django apps: `booking`, `pages`, and `users`
- Centralized template directory with modular subfolders
- A shared `base.html` layout with dynamic navigation and content blocks
- Responsive design powered by Bootstrap 5 and custom CSS
- Summernote integration for rich text editing in admin views

Navigation adapts based on authentication state, offering personalized greetings and member-only access. Dropdown menus are hover-enabled for desktop users and toggle-friendly on mobile.

---

### 📐 Skeleton / Wireframes

Initial wireframes were sketched to define:
- Homepage layout with hero image and call-to-action
- Booking form with calendar and time slots
- Member dashboard with reservation overview
- Profile page with editable user details
- Admin dashboard for restaurant owners

These wireframes informed the HTML structure and guided the CSS layout grid, ensuring consistency across breakpoints.

---

### 🎨 Surface

The visual layer emphasizes clarity, warmth, and brand identity:
- Background image: a giant sushi set with overlay, fixed and center-aligned
- Color palette: deep gray, vibrant green accents, and soft whites
- Typography: Roboto for modern readability
- Interactive elements: hover effects, transitions, and dropdowns
- Mobile-first adjustments: stacked tables, scrollable containers, and adaptive navbar

The result is a polished, intuitive interface that feels welcoming to customers and empowering to restaurant owners — all while maintaining technical elegance and deployment resilience.

*🎨 Main Color Palette*

| Purpose                        | Color Code     | Description                          |
|-------------------------------|----------------|--------------------------------------|
| Background overlay (fallback) | `#F9FAFC`      | Soft off-white for clean contrast    |
| Primary background override   | `darkgray`     | Neutral fallback tone                |
| Navbar background             | `#343a40`      | Dark slate for header/nav            |
| Navbar text & links           | `#ffffff`      | White for high contrast              |
| Navbar hover & accent         | `#08e02c`      | Vibrant green for interactive cues   |
| Footer background             | `#445261`      | Deep blue-gray for footer & dropdown |
| Image background (cards)      | `#188181`      | Teal accent for image containers     |
| Dropdown hover (optional)     | `blueviolet`   | Highlight color for menu items       |

This palette balances clarity, contrast, and brand personality — with vibrant green accents and deep neutrals supporting a sushi-inspired aesthetic. Let me know if you'd like a visual swatch or accessibility contrast check.

[Back To Top](#table-of-contents)

---

## Features

Coders Sushi Bar offers a full-stack, production-ready experience for both customers and restaurant owners. The platform is designed to be intuitive, secure, and scalable, with modular functionality and responsive design at its core. Below is the list of currently implemented features followed by the list of potential future improvements & enchantments.

### ✅ Existing Features

| Feature | Description |
|--------|-------------|
| **User Authentication** | Secure sign-up, login, logout, and password reset flows using Django’s built-in auth system. |
| **Role-Based Access Control (RBAC)** | Differentiated access for customers and restaurant owners, enabling tailored dashboards and permissions. |
| **Table Booking System** | Customers can select date and time, view availability, and receive email confirmations for reservations. |
| **Booking Management Dashboard** | Restaurant owners can view, modify, or cancel bookings from a centralized interface. |
| **Menu Display & Editing** | Customers can browse the restaurant’s menu; owners can update offerings via a rich text editor (Summernote). |
| **Responsive Design** | Mobile-first layout with adaptive navigation, scrollable tables, and optimized typography across devices. |
| **Email Notifications** | Automated confirmation emails for bookings and welcome messages for new users. |
| **Secure Deployment** | Environment variables, debug mode disabled, and static file handling via WhiteNoise for Heroku deployment. |
| **Centralized Templates** | All HTML templates organized under `/templates`, with modular subfolders and a shared `base.html`. |
| **Custom Styling** | Clean, sushi-inspired aesthetic using Bootstrap 5 and custom CSS with media queries for all screen sizes. |
| **User Feedback System** | Customers can leave reviews and comments (optional feature, integrated via dashboard). |
| **Developer Documentation** | README, milestone tracking, and GitHub Wiki support for setup, contribution, and testing. |

### 🚀 Future Enhancements

| Planned Feature | Purpose |
|----------------|---------|
| **Restaurant Blog Interface** | Allow owners to post updates, specials, and stories to engage customers. |
| **Reservation Analytics Dashboard** | Visualize booking trends, peak hours, and customer behavior. |
| **Google Sheets Integration** | Export bookings and feedback to Google Sheets for external analysis. |
| **Real-Time Availability Updates** | Dynamic table availability without page reloads (AJAX or WebSockets). |
| **Multi-Language Support** | Enable localization for broader accessibility. |
| **Payment Integration** | Allow customers to pre-pay or hold reservations with deposits. |
| **Monitoring & Logging Tools** | Add system health tracking and error reporting for long-term stability. |
| **Accessibility Enhancements** | Improve ARIA roles, keyboard navigation, and screen reader support. |
| **Restaurant Profile Customization** | Let owners personalize branding, images, and contact info. |
| **Customer Loyalty Features** | Track repeat visits, offer discounts, and gamify engagement. |

This feature set reflects a balance between MVP delivery and long-term scalability. Every existing feature was built with modularity and user value in mind, while future enhancements aim to deepen engagement, improve performance, and expand functionality across user roles.

[Back To Top](#table-of-contents)

---

## 💼 Business Model

Coders Sushi Bar simulates a digital-first restaurant experience, designed to streamline operations, enhance customer engagement, and support scalable growth. While built as a portfolio project, the platform reflects real-world business logic and could be adapted for commercial deployment.

### 🧩 Core Value Proposition

- **For Customers**: A seamless, mobile-friendly interface to browse menus, book tables, and manage reservations — with instant feedback and email confirmations.
- **For Restaurant Owners**: A centralized dashboard to oversee bookings, update menus, and analyze reservation trends — reducing manual overhead and improving service efficiency.

### 🧮 Revenue Streams (Hypothetical)

| Stream | Description |
|--------|-------------|
| **Subscription Model** | Monthly fee for restaurant owners to access dashboard, analytics, and customization tools. |
| **Premium Features** | Add-ons like SMS notifications, branded email templates, or advanced analytics. |
| **Booking Fees** | Small service fee per confirmed reservation (optional, customer-side or owner-side). |
| **Advertising & Promotions** | Featured placement for restaurants or seasonal menu highlights. |
| **Data Insights** | Aggregated, anonymized analytics for industry benchmarking (opt-in only). |

### 🛠 Operational Model

| Role | Capabilities |
|------|--------------|
| **Customer** | Browse, book, modify/cancel reservations, manage account, leave feedback. |
| **Restaurant Owner** | View and manage bookings, edit menus, access dashboard analytics, customize restaurant profile. |
| **Administrator** | Oversee platform health, manage user roles, moderate content, and maintain security. |

### 📈 Scalability Potential

The platform is designed with modular Django apps, centralized templates, and cloud deployment via Heroku — making it easy to onboard multiple restaurants, expand to new regions, or integrate third-party services (e.g., payment gateways, delivery APIs).

### 🧪 MVP vs. Commercial Expansion

| Tier | Features |
|------|----------|
| **MVP (Portfolio)** | Authentication, booking system, dashboard, menu editing, email confirmations. |
| **Commercial** | Multi-restaurant support, payment integration, loyalty programs, real-time availability, mobile app. |

Coders Sushi Bar demonstrates how thoughtful UX, robust architecture, and Agile development can support a viable business model — whether for a single restaurant or a scalable SaaS platform serving the hospitality industry.

[Back To Top](#table-of-contents)

---

## Screenshots

<details>
<summary>Below are screenshots of the main pages of the project. For each page a mobile screenshot is given as well.</summary>

### Homepage — Hero image, navigation, call-to-action

- Start page

![Startpage screenshot](/static/images/screenshots/screenshot-booking-page.jpg)

- Start page mobile

![Startpage mobile screenshot](/static/images/screenshots/screenshot-start-page-mobile.jpg)

### Booking Page — Date/time selector, form layout

- Booking page

![Booking page screenshot](/static/images/screenshots/screenshot-booking-page.jpg)

- Booking page mobile

![Booking page mobile screenshot](/static/images/screenshots/screenshot-booking-page-mobile.jpg)

### Menu Page — Menu items, styling, responsiveness

- Menu page

![Menu page screenshot](/static/images/screenshots/screenshot-menu-page.jpg)

- Menu page mobile

![Menu page mobile screenshot](/static/images/screenshots/screenshot-menu-page-mobile.jpg)

### Login/Signup — Auth flow and feedback messages

- Login page

![Login page screenshot](/static/images/screenshots/screenshot-login-page.jpg)

- Login page mobile

![Login page mobile screenshot](/static/images/screenshots/screenshot-login-page-mobile.jpg)

- Logout page

![Log out page screenshot](/static/images/screenshots/screenshot-logout-page.jpg)

- Logout page mobile

![Log out page mobile screenshot](/static/images/screenshots/screenshot-logout-page-mobile.jpg)

- Sign up page

![Sign up page screenshot](/static/images/screenshots/screenshot-sign-up-page.jpg)

- Sign up page mobile

![Sign up page mobile screenshot](/static/images/screenshots/screenshot-sign-up-page-mobile.jpg)

### Member Dashboard — Reservation overview, profile links

- Member page

![Member page screenshot](/static/images/screenshots/screenshot-member-page.jpg)

- Member page mobile

![Member page mobile screenshot](/static/images/screenshots/screenshot-member-page-mobile.jpg)

### Restaurant Owner Dashboard — Booking management, menu editing

As Restaurant Owner by definition has admin to Django admin, his admin board is looking like this:

- Admin backend available for the restaurant owner

![Restaurant Owner Django admin interface](/static/images/screenshots/screenshot-owner-django-admin.jpg)

- Back-end user manager

![Admin user manager](/static/images/screenshots/admin-back-end-user-manager.jpg)

- Back-end reservation list

![Back-end reservation list](/static/images/screenshots/admin-back-end-reservations-list.jpg)

- Back-end reservation editor

![Back-end reservation editor](/static/images/screenshots/admin-back-end-reservations-editor.jpg)

</details>

[Back To Top](#table-of-contents)

---

## 🗄️ Database Design

**Coders Sushi Bar** uses a relational database powered by Django’s ORM, structured to reflect real-world restaurant operations. The schema is modular, normalized, and designed for scalability, with clear relationships between users, tables, locations, and reservations.

### 🧩 Core Models & Relationships

| Model            | Description                                                                 | Relationships |
|------------------|-----------------------------------------------------------------------------|---------------|
| **User**         | Built-in Django user model for authentication and role-based access         | One-to-many with `Reservation` |
| **Table**        | Represents individual tables with attributes like size, smoking, accessible | ForeignKey to `Location`; One-to-many with 
| **Reservation**  | Captures booking details: user, table, date/time, status, and special requests | ForeignKey to `User`, `Table`, `Location`, and `BookingStatus` |
| **BookingStatus**| Represents the status of a reservation (e.g., Pending, Confirmed, Cancelled)| One-to-many with `Reservation` |
| **Location**     | Defines seating zones (e.g., Patio, Main Hall, VIP Room)                    | One-to-many with `Table` and `Reservation` |

![ER diagram of the DB login](./static/images/screenshots/database-relations.jpg)

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

### 🔗 Relationship Diagram (Textual)

- **User ↔ Reservation**: A user can make multiple reservations; each reservation belongs to one user.
- **Table ↔ Reservation**: Each reservation is linked to a specific table to prevent double-booking.
- **Location ↔ Table**: Tables are grouped by seating area (e.g., Main Hall, Terrace etc.).
- **Location ↔ Reservation**: Reservations optionally reference a location for analytics or filtering.
- **BookingStatus ↔ Reservation**: Each reservation has a status (Pending, Confirmed, Cancelled), allowing for workflow control.

---

### 🧠 Design Considerations

- **Normalization**: Reusable entities like `Location` and `BookingStatus` prevent duplication and support filtering.
- **Extensibility**: Easily supports future features like multi-restaurant support, analytics, or dynamic availability.
- **Performance**: Indexed fields like `booking_date`, `booking_time`, and `booked_on` support fast queries and sorting.
- **Security**: Reservations are tied to authenticated users; access control is enforced via Django views and templates.
- **Business Logic Alignment**: Reflects how real restaurants manage seating zones, table attributes, and booking workflows.

---

### 📈 Real-World Mapping

This schema mirrors operational needs:
- Customers book specific tables in defined locations.
- Restaurant owners can filter bookings by status, date, or seating area.
- Special requests and guest count are stored for service preparation.
- Booking status enables confirmation workflows and cancellation tracking.

[Back To Top](#table-of-contents)

---

## 🧩 Django Apps Overview

Coders Sushi Bar is structured as a modular Django project, composed of three dedicated apps: `booking`, `pages`, and `users`. This separation of concerns ensures maintainability, scalability, and clarity across both front-end and back-end development.

### 🗓️ `booking` App

Handles all reservation-related functionality, including table management, booking workflows, and seating logic.

**Key Features:**
- Models for `Reservation`, `Table`, `Location`, and `BookingStatus`
- Prevents double bookings via table/date/time constraints
- Supports seating zones (e.g., patio, indoor) and table attributes (smoking, accessible)
- Includes special requests, guest count, and booking status tracking
- Reservation ordering by creation timestamp (`booked_on`)
- Admin-friendly model string representations for clarity

**User Roles:**
- **Customers**: Can create, view, and cancel their reservations
- **Restaurant Owners**: Can view, modify, and manage all bookings

### 📄 `pages` App

Manages static and semi-static content that defines the public-facing identity of the restaurant.

**Key Features:**
- Homepage, About, and Menu views
- Centralized templates with shared `base.html` layout
- Summernote integration for rich text editing (e.g., menu descriptions)
- Responsive design powered by Bootstrap and custom CSS
- Optional blog interface for restaurant updates (future enhancement)

**User Roles:**
- **All Visitors**: Can browse content without logging in
- **Restaurant Owners**: Can edit menu content and manage blog posts

### 👤 `users` App

Handles authentication, profile management, and role-based access control. This app is built on Django’s robust built-in `User` model, extended with custom logic to differentiate between customer and restaurant owner roles.

**Key Features:**
- Secure sign-up, login, logout, and password reset flows
- Role differentiation using Django’s built-in user groups or flags
- Profile editing and account management
- Personalized dashboard access based on user type
- Welcome email and login feedback messages
- Seamless integration with Django’s authentication system

**User Roles:**
- **Customers**: Can manage their account and bookings
- **Restaurant Owners**: Gain access to admin tools and dashboards

This modular app architecture ensures that each domain—content, booking, and authentication—is cleanly separated, making the codebase easier to navigate, test, and extend.


[Back To Top](#table-of-contents)

---

## 🔐 Authentication & Authorization

This project includes foundational authentication and authorization mechanisms, with room for future enhancements as user roles and access control evolve.

### ✅ Authentication

- **User Login & Logout**: Handled via Django’s built-in auth system (`django.contrib.auth`)
  - Login view supports credential validation and session management
  - Logout securely clears session data
- **Session-Based Auth**: Users are authenticated via secure session cookies
- **Password Handling**: Passwords are hashed using Django’s default PBKDF2 algorithm
- **Login Form**: Customizable form with validation and error messaging
- **Throttling**: Not yet implemented — rate-limiting for login attempts is planned for production hardening

### 🔒 Authorization

- **Authenticated Access**: Views and forms are protected using `@login_required` decorators or `LoginRequiredMixin`
- **Role-Based Access**: Not yet implemented — all authenticated users currently share the same access level
- **Admin Panel**: Django admin is enabled for superusers with full model control
- **Future Plans**:
  - Introduce user roles (e.g. staff, manager, customer)
  - Restrict access to booking, editing, and reporting features based on role
  - Add granular permissions via `django.contrib.auth.models.Permission` or custom logic

### 🛡️ Security Notes

- **CSRF Protection**: Middleware is present but not enforced across all forms. CSRF tokens will be added once form flows are finalized.
- **Environment Isolation**: Authentication logic is tested in local and staging environments before production rollout

[Back To Top](#table-of-contents)

---

## 🧪 Manual Testing

Due to simplicity of the project and the limited time available, the manual testing was preferred over automated testing. With this in mind the Coders Sushi Bar underwent extensive manual scrutiny to ensure usability, reliability, and role-based functionality across all major features. Testing was performed iteratively throughout development, with each milestone followed by targeted validation of newly implemented components.

### 👥 User Role Testing

#### 🔐 Authentication & Access Control

- ✅ Verified sign-up, login, logout flows for both customers and restaurant owners
- ✅ Confirmed password reset email delivery and form validation
- ✅ Ensured role-based access: restaurant owners see dashboard tools; customers do not
- ❌ Attempted unauthorized access to owner-only views (correctly redirected or denied)

<details>
    <summary>See corresponding snapshots</summary>

- validation feedback on the sign-up page

![Sign-up form validation](/static/images/screenshots/screenshot-signup-form-validation.jpg)

- validation feedback on the login page

![Login validation](/static/images/screenshots/screenshot-login-form-validation.jpg)

- logout feedback

![Logout feedback snapshot](/static/images/screenshots/screenshot-logout-page.jpg)

- password reset feedback

![Password reset confirmation](/static/images/screenshots/screenshot-password-reset-confirmation.jpg)

- admin page denied access

![](/static/images/screenshots/screenshot-admin-page-dinied-access.jpg)

</details>

#### 👤 Profile & Account Management
- ✅ Tested profile editing and feedback messages
- ✅ Checked personalized greetings and conditional navbar rendering
- ✅ Verified session persistence and logout behavior

<details>
    <summary>See corresponding snapshots</summary>

- validation user profile editor

![validation user profile editor](/static/images/screenshots/screenshot-update-user-profile-form-check.jpg)

- feedback after user profile update

![feedback after user profile update](/static/images/screenshots/screenshot-feedback-after-user-profile-updated.JPG)

- Redirect after unauthorized attempt to access member page

![Redirect after unauthorized attempt to access member page](/static/images/screenshots/screenshot-redirect-after-attempt-to-access-member-page.jpg)

</details>

### 📅 Booking System Testing

#### 🧾 Reservation Creation
- ✅ Created bookings with valid date/time and guest count
- ✅ Submitted special requests and verified database storage
- ✅ Displayed confirmation page with correct details

<details>
    <summary>See corresponding snapshots</summary>

- Booking confirmation

![Booking confirmation](/static/images/screenshots/screenshot-booking-confirmation-mobile.jpg)

- Special request in the admin area

![Special request](/static/images/screenshots/screenshot-admin-special-requests.jpg)

</details>

#### 🚫 Double Booking Prevention
- ✅ Attempted to book same table at same time — correctly blocked by filtering out tables that are already booked within a ±1 hour window of the requested time
- ✅ Booked different tables at overlapping times — allowed

<details>
    <summary>See corresponding snapshots</summary>

- Already booked table removed from the booking list

![Table is safely removed](/static/images/screenshots/screenshot-ommited-table-in-the-list.jpg)

</details>

#### 🗑️ Booking Modification & Cancellation
- ✅ List of existing booking available for review
- ✅ Option to cancel booking

<details>
    <summary>See corresponding snapshots</summary>

- Booking cancellation routine

![Table is safely removed](/static/images/screenshots/screenshot-booking-cencellation-path.jpg)

- Update booking

![Update booking with confirmation](/static/images/screenshots/screenshot-update-bokking-with-confirmation.jpg)

</details>

### 🧭 Navigation & UX Testing

#### 📱 Responsive Design
- ✅ Tested layout on desktop, tablet, and mobile (Chrome DevTools)
- ✅ Verified navbar toggler behavior and dropdown hover activation
- ✅ Confirmed scrollable tables and mobile-friendly booking form

<details>
    <summary>See corresponding snapshots</summary>

- Mobile start page:

![Mobile start page](/static/images/screenshots/screenshot-start-page-mobile.jpg)

- Mobile member page:

![Mobile member page](/static/images/screenshots/screenshot-member-page-mobile.jpg)

- Mobile booking page:

![Mobile booking page](/static/images/screenshots/screenshot-booking-page-mobile.jpg)

- Mobile profile editor page:

![Mobile profile editor](/static/images/screenshots/screenshot-update-user-profile-mobile.jpg)

</details>


#### 🖼️ Content Pages
- ✅ Viewed homepage, about, and menu pages without login
- ✅ Checked Summernote rendering for rich text content
- ✅ Verified static file loading and background image display

<details>
    <summary>See corresponding snapshots</summary>

- Summernote rich text content in the Booking editor:

![Summernote rich text content in the Booking editor](/static/images/screenshots/screenshot-checked-summernote-rendering-for-richtext-content.jpg)

- Static files loading

![Static files loading](/static/images/screenshots/screenshot-verified-static-file-loading-and-background-imagedisplay.jpg)

</details>


### 🧰 Admin & Dashboard Testing

#### 🧑‍🍳 Restaurant Owner Dashboard (Django Admin)
- ✅ Viewed all reservations with status and guest info

<details>
    <summary>See corresponding snapshots</summary>

- Django Admin: list of active reservation

![Django Admin: list of active reservation](/static/images/screenshots/screenshot-django-admin-reservation-list.JPG)

</details>

### 🔐 Security & Deployment Checks

- ✅ Disabled Django debug mode in production
- ✅ Verified environment variable usage for secret keys

<details>
    <summary>See corresponding snapshots</summary>

- Debug set to False

![Debug -> false](/static/images/screenshots/screenshot-debug-false.jpg)

- Secrets are accessed securely

![secrets isolated](/static/images/screenshots/screenshot-secret-key-isolated.jpg)

- .gitignore

![.gitignore](/static/images/screenshots/screenshot-gitignore.jpg)


</details>

### ✅ Steps taken to Validate Django Templates Using W3C Validator
- Right-click on the page → "View Page Source" or "Inspect" → Copy the full HTML.
- Go to W3C Validator (https://validator.w3.org/).
- Choose "Validate by Direct Input" and paste the copied HTML.
- Click "Check" and review the errors/warnings.
- Fix any structural issues in your Django templates ( folder).
- ✔ Validates dynamic HTML instead of raw Django template tags.
- ✔ Helps detect missing closing tags, incorrect attributes, and accessibility issues.

<details>
    <summary>See corresponding snapshots</summary>

- W3 validation results for the start page
![w3validator start page](/static/images/screenshots/w3validator-start-page.jpg)

- W3 validation for member page

![Member page w3 validation](/static/images/screenshots/screenshot-w3-validation-member-page.jpg)

- W3 validation results for the booking page
![w3validator booking page](/static/images/screenshots/w3validator-booking-page.jpg)

</details>

### Validating with JSHint

**No errors found by JSHint:**
![JSHint report](/static/images/screenshots/validation-jshint.jpg)

### 🔍 Code Quality & Linting

#### 📝 PEP8 Validation with Code Institute Linter
**To ensure your Python code follows best practices:**
- 1️⃣ Go to [Code Institute Linter](https://pep8ci.herokuapp.com/).  
- 2️⃣ Paste your Python code into the input field.  
- 3️⃣ Click **"Check Code"** to identify formatting issues.  
- 4️⃣ Apply suggested fixes for improved readability and maintainability.

#### C.I. Linter validation results:

**C.I. validation results for the user app**

<details>
    <summary>See corresponding snapshots</summary>

- User app views

![User app views](/static/images/screenshots/ci-python-linter-user-views.jpg)

- User app urls

![User app urls](/static/images/screenshots/ci-python-linter-user-urls.jpg)

- User app forms

![User app forms](/static/images/screenshots/ci-python-linter-user-forms.jpg)

</details>    

**C.I. validation results for the pages urls**

<details>
    <summary>See corresponding snapshots</summary>

- Pages app views

![Pages app views](/static/images/screenshots/ci-python-linter-pages-views.jpg)

- Pages app urls

![Pages app urls](/static/images/screenshots/ci-python-linter-pages-urls.jpg)

</details>    

**C.I. validation results for the booking urls**

<details>
    <summary>See corresponding snapshots</summary>

- booking app views

![booking app views](/static/images/screenshots/ci-python-linter-booking-views.jpg)

- booking app urls

![booking app urls](/static/images/screenshots/ci-python-linter-booking-urls.jpg)

- booking app forms

![booking app forms](/static/images/screenshots/ci-python-linter-booking-forms.jpg)

- booking app models

![booking app forms](/static/images/screenshots/ci-python-linter-booking-models.jpg)

</details> 

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


[Back To Top](#table-of-contents)

---


## 🚀 Deployment

This project is ready for both local development and remote deployment on Heroku. Below are the setup steps and security considerations.

---

### 🖥️ Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/your-project.git
   cd your-project
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create `.env` file for local secrets**
   ```ini
   DJANGO_SECRET_KEY=your-local-secret-key
   DEBUG=True
   DATABASE_URL=sqlite:///db.sqlite3
   ```

5. **Apply migrations and run the server**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

6. **Collect static files (optional for local testing)**
   ```bash
   python manage.py collectstatic --noinput
   ```

---

### ☁️ Heroku Deployment

1. **Create a Heroku app**
   ```bash
   heroku create your-app-name
   ```

2. **Set environment variables**
   ```bash
   heroku config:set DJANGO_SECRET_KEY=your-production-secret-key
   heroku config:set DEBUG=False
   heroku config:set DATABASE_URL=your-production-db-url
   ```

3. **Push to Heroku**
   ```bash
   git push heroku main
   ```

4. **Run migrations**
   ```bash
   heroku run python manage.py migrate
   ```

5. **Collect static files**
   ```bash
   heroku run python manage.py collectstatic --noinput
   ```

6. **Verify deployment**
   - Visit `https://your-app-name.herokuapp.com`
   - Confirm static assets load correctly
   - Test login, booking, and form functionality

---

### 🔐 Security Notes

- **Environment Variables**: All secrets (e.g. `SECRET_KEY`, DB credentials) are injected via environment variables. No sensitive data is committed.
- **CSRF Protection**: Middleware is present but not actively used in forms. CSRF tokens are not enforced unless explicitly added.
- **Login Throttling**: Not currently implemented. Consider adding rate-limiting via `django-ratelimit` or DRF throttling for brute-force protection.

---

### 📁 Repo Hygiene

- `.env`, `.venv`, `__pycache__`, and platform-specific files are excluded via `.gitignore`
- Static files are versioned and served via `/static/`
- Deployment artifacts (e.g. `cloudinary_python.txt`, `blog/fixtures/`) are managed separately

### ✅ Visual Deployment Checklist

| Feature                          | Verified | Screenshot / Evidence |
|----------------------------------|----------|------------------------|
| **Environment Variables Used**   | ✅        | `settings.py` shows `os.environ.get()` usage |
| **`.env` Excluded from Git**     | ✅        | `.gitignore` includes `.env` |
| **Static Files Loaded Correctly**| ✅        | DevTools shows full `script.js`, no truncation |
| **Login Functionality**          | ✅        | Screenshot of successful login |
| **Booking Form Loads Tables**    | ✅        | Screenshot of table dropdown populated |
| **CSRF Token Present (if used)** | ⚠️        | Not enforced in forms (middleware present) |
| **Heroku Environment Configured**| ✅        | `heroku config` output with `DJANGO_SECRET_KEY` |
| **Local Setup Verified**         | ✅        | `runserver` output and working localhost |
| **Database Migrations Applied**  | ✅        | `python manage.py migrate` output |
| **No Secrets in Repo**           | ✅        | GitHub search for `SECRET_KEY` returns nothing |

[Back To Top](#table-of-contents)

---

## 🧰 Technologies Used

### 🖥️ Core Stack

- **Python 3.11+** — Primary language for backend logic
- **Django** — Web framework powering models, views, forms, and admin
- **SQLite / PostgreSQL** — Local development with SQLite; Heroku-ready for PostgreSQL
- **HTML5 / CSS3 / JavaScript (ES6+)** — Frontend templating and interactivity
- **Jinja-like Django Templates** — Dynamic rendering with block inheritance and context-aware logic

### 🧪 Development Tools

- **VS Code** — Customized for multi-file debugging and persistent tab workflow
- **JSHint** — Linting for JavaScript with ES11 support
- **Git & GitHub** — Version control and collaboration
- **Postman** — API testing and form submission simulation
- **Browser DevTools** — Visual validation of static assets, form behavior, and network responses

### ☁️ Deployment & Environment

- **Heroku** — Remote hosting with environment variable injection and CLI management
- **Gunicorn** — WSGI server for production deployment
- **WhiteNoise** — Static file serving in production
- **Environment Variables** — Secure injection of secrets (`SECRET_KEY`, DB credentials)
- **`.env` + `.gitignore`** — Local secrets excluded from version control

### 🛡️ Security & Validation

- **CSRF Middleware (Django)** — Present but not enforced in forms (see limitations)
- **Login Throttling** — Planned via `django-ratelimit` or DRF throttling
- **Session Management** — Explicit configuration for cookie age and browser behavior

[Back To Top](#table-of-contents)

---

## Known Bugs and Limitations

**Note on Password Reset Functionality**

Coders Sushi Bar uses Django’s built-in authentication system, which includes a password reset feature accessible via the login page and admin interface. While the form correctly prompts users to enter their email address to receive reset instructions, email delivery is currently disabled in this project. As this is a first Django-oriented application, the absence of mail server configuration is intentional and acceptable within the scope of the project. The feature remains visible to demonstrate standard Django capabilities, and can be fully activated by configuring SMTP settings in a production environment.

** ❌ CSRF Protection Not Fully Implemented**

While Django’s CSRF middleware is enabled by default, full CSRF protection is not currently enforced across all forms. This is a deliberate decision during development to streamline testing and avoid token-related interruptions in early-stage workflows.

- Forms do not yet include {% csrf_token %}, and POST requests may bypass CSRF validation.
- This setup simplifies local testing and integration with external tools (e.g. Postman, JS fetch).
- CSRF enforcement will be reintroduced once form flows are finalized and user authentication is hardened.

Security Note: This is acceptable in controlled environments but should be addressed before production deployment. Reviewers are encouraged to flag any form that handles sensitive data without CSRF protection.

[Back To Top](#table-of-contents)

---

## 🙌 Credits

This project was developed and maintained by **Alexey Kopchinskiy**, with a focus on secure deployment, reviewer empathy, and scalable backend architecture.

### 🧠 Core Contributions

- Code Institute Tutors / Stuff
- Django backend development and form validation
- JavaScript logic for booking flow and dynamic filtering
- Deployment troubleshooting and static asset integrity
- Repo hygiene, environment variable security, and documentation clarity

### 🛠 Tools & Libraries

- [Django](https://www.djangoproject.com/) — Web framework
- [JSHint](https://jshint.com/) — JavaScript linting
- [Heroku](https://www.heroku.com/) — Cloud deployment
- [VS Code](https://code.visualstudio.com/) — Development environment
- [CI Python Linter](https://pep8ci.herokuapp.com/) - CI Python Linter

### 💡 Inspiration & Support

- Code Institute Course of lectures
- Code Institute support at Discord
- Django documentation and community examples
- Stack Overflow for edge-case debugging
- GitHub issues and open-source best practices

[Back To Top](#table-of-contents)

---

## 🙏 Acknowledgements

This project was built with the support, insight, and inspiration of many individuals and resources.

### 👨‍🏫 Code Institute

Special thanks to the Code Institute tutors and support team for their guidance, technical feedback, and encouragement throughout the development process. Their expertise helped shape both the backend architecture and deployment strategy.

### 🧠 Community & Resources

- Django Documentation — For clear, practical guidance on models, forms, and deployment
- Stack Overflow — For solving edge-case bugs and implementation quirks
- GitHub Community — For repo hygiene inspiration and open-source best practices
- Heroku Docs — For environment variable setup and static file handling
- VS Code Extensions — For optimizing multi-file debugging and linting workflows

### 🙌 General Support

Thanks to friends, peers, and reviewers who provided feedback, challenged assumptions, and helped refine the user experience. Your input made the project stronger, more secure, and more user-friendly.

[Back To Top](#table-of-contents)

--

## 📄 License

This project is licensed under the [MIT License](LICENSE).  
You are free to use, modify, and distribute this software with proper attribution.  
See the `LICENSE` file for full terms.

[Back To Top](#table-of-contents)

--

## 📢 Contact

For questions or support, reach out at kopchinskiy@gmail.com.
