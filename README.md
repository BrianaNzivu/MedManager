# MedManager - Health Information Management System

[Presentation slides](https://docs.google.com/presentation/d/1Hl-UzBE2Jj3ZO563htZEmDNViQzNgsMdB1oaLXZT-k8/edit?usp=sharing)

**MedManager** is a clean, responsive Flask web app for managing health programs and client enrollments. It’s backed by Firebase Firestore and Firebase Authentication, offering a simple and secure way to manage healthcare programs, clients, and their enrollments.

## Features
- **Health Programs Management**  
  - Add, edit, and delete health programs (e.g., TB, Malaria, HIV).
  - Programs are color-tagged with statuses (Active, Critical, Inactive).

![image](https://github.com/user-attachments/assets/732ac3b3-85e2-487f-a4a4-dbe0bae6db7d)


- **Clients Management**  
  - Register new clients (with name, age, gender).
  - Enroll clients in one or more health programs.
  - Full client profile (view/edit).
  - Searchable client list with filtering by program.

![image](https://github.com/user-attachments/assets/873f74d0-5c2b-4eca-8436-340a1814dda4)

- **Dashboard**  
  - Displays total clients, total programs, and the number of enrolled clients.
  - Bar charts and pie charts displaying the program enrollment statistics using **Chart.js**.

![image](https://github.com/user-attachments/assets/b48926c9-c477-4063-9595-5a2664a55a4d)
![image](https://github.com/user-attachments/assets/8c9a5bf9-dabe-49d9-a8b2-05afba1c468f)
![image](https://github.com/user-attachments/assets/44ad358b-13d1-435d-9476-e2a22ee63dd2)

- **Program Detail**  
  - Lists enrolled clients for each health program.
  - Option to download the client list as a CSV file.

![image](https://github.com/user-attachments/assets/dade970f-84e9-4c75-bafa-14d50d4d873d)

- **Client Profile API**  
  - Access individual client data in JSON format via the `/api/client/<id>` endpoint.

![image](https://github.com/user-attachments/assets/ce763ddd-8bcd-4d05-9bf1-89c4b4dff43d)

- **UI Enhancements**  
  - Light/Dark Mode toggle, saved in **localStorage**.
  - Responsive design using **Bootstrap 5** for a clean, modern look.
  - Client-side search and filtering for easy data management.

![image](https://github.com/user-attachments/assets/bd5158d6-7324-40ef-be2c-022586ab9810)
![image](https://github.com/user-attachments/assets/dae2798c-e4e8-4611-a73b-d980fe6cc88f)

---

## Tech Stack
- **Backend:** Python with Flask  
- **Database:** Firebase Firestore (via firebase-admin)  
- **Frontend:** HTML, Bootstrap 5, Animate.css, Chart.js, Vanilla JavaScript  

