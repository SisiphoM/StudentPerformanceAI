 # AI-Powered Student Performance Prediction System

## Project Description
This system predicts student academic performance using AI. It analyzes past grades, attendance records, and study habits to provide early intervention and personalized learning support. The **AI-Powered Student Performance Prediction System** helps educators and students by analyzing academic data to predict performance trends.  
It provides **real-time reports, learning recommendations, and early alerts** for students at risk of failing.  

## Installation setup
On terminal :
git clone https://github.com/yourusername/StudentPerformanceAI.git
cd StudentPerformanceAI
## Documentation
- [System Specification](SPECIFICATION.md)
- [Architecture Documentation](ARCHITECTURE.md)


## Key Features  
**Student Reports** – View detailed academic performance reports.  
**AI-Based Learning Suggestions** – Personalized study plans for students.  
**Teacher Dashboard** – Monitor student progress and generate reports.  
**Parent Portal** – Allows parents to track student performance.  
**Secure User Access** – Role-based authentication for students, teachers, and admins.  
**Data Integration** – Connects with school databases to keep records updated.  

---

AI Model: Analyzes student performance trends.
Database: Stores student records, grades, and attendance.
Frontend: Web dashboard for students, teachers, and parents.
Backend: Handles API requests and runs AI predictions.

---

## Usage Instructions
1️⃣ Log in as a Student, Teacher, or Admin.
2️⃣ View Reports to analyze academic performance.
3️⃣ Generate Reports (Teachers only).
4️⃣ Get Study Recommendations based on AI analysis.

---

## 🔐 Security & Access Control
Student Access: Can view reports and receive recommendations.
Teacher Access: Can view, analyze, and generate reports.
Admin Access: Manages users and controls system settings.

---

## Data Flow diagram 
Step 1: Student requests a performance report.
Step 2: Backend retrieves data from the database.
Step 3: AI model analyzes past trends.
Step 4: The final report is displayed to the student.

---

## Deployment & Setup
Frontend: React, hosted on Vercel or Netlify.
Backend: Flask, deployed on AWS EC2 or Heroku.
Database: PostgreSQL, hosted on AWS RDS.

---

## System Interaction Flow
The diagram below shows how different components interact when a student requests a performance report.

```mermaid
sequenceDiagram
    participant Student
    participant WebApp
    participant Backend
    participant Database
    Student->>WebApp: Request Performance Report
    WebApp->>Backend: Fetch Student Data
    Backend->>Database: Retrieve Performance Data
    Database-->>Backend: Data Retrieved
    Backend-->>WebApp: Process & Return Report
    WebApp-->>Student: Display Report


