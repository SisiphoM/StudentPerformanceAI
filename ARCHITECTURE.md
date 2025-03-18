 # AI-Powered Student Performance Prediction System - Architecture

## 1. Context Diagram

This diagram shows the system's high-level interaction with students, teachers, admin and databases. Click link for Mermaid diagram https://www.mermaidchart.com/app/projects/8e46d07a-e802-4efa-971b-48f52adfb76f/diagrams/b5557db4-f768-488b-b8c7-953e707371d5/version/v0.1/edit

graph LR
    A[Student] -->|Submits Assignments, Tests, Attendance| B[Performance Prediction System]
    B -->|Generates Reports| C[Teacher]
    B -->|Provides Learning Recommendations| A
    B -->|Fetches Data| D[School Database]

## 2. Container Diagram
This system consists of three main parts: Frontend, Backend, and Database. https://www.mermaidchart.com/app/projects/8e46d07a-e802-4efa-971b-48f52adfb76f/diagrams/36e12fa6-0a2c-49b5-b2dd-e82c4ff78783/version/v0.1/edit

graph LR
    subgraph "Frontend (User Interface)"
        A[Web Dashboard]
    end

    subgraph "Backend (API & AI Model)"
        B[Prediction API]
        C[Machine Learning Model]
    end

    subgraph "Database"
        D[Student Performance Database]
    end

    A --> B
    B --> C
    B --> D
    C --> D


## 3. Use case diagram.
The diagram below represents interactions between actors (Students, Teachers, admin and database) and the system. https://www.mermaidchart.com/app/projects/8e46d07a-e802-4efa-971b-48f52adfb76f/diagrams/435c2f83-2296-421d-9009-79025061cc94/version/v0.1/edit

graph TD
    A[Student] -->|View Performance Report| B[AI-Powered System]
    A -->|Receive Learning Recommendations| B
    C[Teacher] -->|Monitor Student Progress| B
    C -->|Generate Reports| B
    D[Parent] -->|Access Student Reports| B
    E[Admin] -->|Manage User Accounts| B
    B -->|Fetch Data from School Database| F[Database]


## 4. High-level architecture.
This is High-level architecture diagram. https://www.mermaidchart.com/app/projects/954ba711-e390-447d-bc86-64fd8cbd3c14/diagrams/90d2154f-58d2-4186-b0e0-d5ba6dde873c/version/v0.1/edit

graph TD
    A[Student] -->|Requests Report| B[AI-Powered System]
    B -->|Processes Data| C[Machine Learning Model]
    B -->|Fetches Records| D[School Database]
    C -->|Sends Insights| A

AI Model: Analyzes student performance trends.
Database: Stores student records, grades, and attendance.
Frontend: Web dashboard for students, teachers, and parents.
Backend: Handles API requests and runs AI predictions.

## 5. Data Flow Diagram
This is the data flow diagram. https://www.mermaidchart.com/app/projects/954ba711-e390-447d-bc86-64fd8cbd3c14/diagrams/35215afb-e241-41ff-a97b-fcb373a47137/version/v0.1/edit

graph TD
    A[Student] -->|Requests Report| B[Backend API]
    B -->|Fetch Data| C[Database]
    B -->|Runs Analysis| D[Machine Learning Model]
    D -->|Returns Insights| B
    B -->|Displays Report| A

## 6. Sequence diagram
The diagram below shows how different components interact when a student requests a performance report. https://www.mermaidchart.com/app/projects/954ba711-e390-447d-bc86-64fd8cbd3c14/diagrams/b23efe95-b5c5-4a9d-9e55-233e7db55501/version/v0.1/edit

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