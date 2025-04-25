# 🐾 PawPal – Pet Supplies & Services E-Commerce Platform

PawPal is a cloud-based web application that brings together **pet care products** and **local pet services** like vet appointments, grooming, dog walking, and foster care—all in one unified platform.

Deployed on [Render](https://render.com) using Docker and GitHub integration, PawPal offers pet owners a simple, user-friendly, and scalable solution to manage their furry friends’ needs with ease.

---

## 📦 Features

- 🛍️ **Pet Product Store** – Food, toys, and health products
- 🐶 **Service Booking** – Vet appointments, dog walking, grooming
- 📦 **Subscription Boxes** – Auto-replenishment for food & essentials
- 📍 **Local Integration** – Connects users with nearby service providers
- 📑 **Admin Panel** – Manage listings, orders, and user data
- 🌐 **Deployed using Docker + Render** – For consistent performance and easy scaling

---

## 🧰 Tech Stack

| Component      | Tool/Tech Used       |
|----------------|----------------------|
| Frontend       | HTML, CSS, JavaScript, Jinja2 |
| Backend        | Python (Flask)       |
| Database       | PostgreSQL (via SQLAlchemy) |
| Cloud Hosting  | Render               |
| Containerization | Docker             |
| Version Control | Git & GitHub        |

---

## 🚀 Deployment Overview

This project is deployed using Render’s cloud platform. The deployment is automated through:

- **`Dockerfile`** – Defines how the app is built and run inside a container
- **`render.yaml`** – Configuration file for Render to manage build/start processes
- **GitHub Integration** – Every push triggers a new build and deployment

---

## 🛠️ How to Run Locally

```bash
# Clone the repository
git clone https://github.com/your-username/pawpal.git
cd pawpal

# Build and run using Docker
docker build -t pawpal .
docker run -p 5000:5000 pawpal
