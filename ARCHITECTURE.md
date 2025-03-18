 # AI-Powered Student Performance Prediction System - Architecture

## 1. Context Diagram
This diagram shows the system's high-level interaction with students, teachers, admin and databases. Click link for Mermaid diagram https://www.mermaidchart.com/app/projects/8e46d07a-e802-4efa-971b-48f52adfb76f/diagrams/b5557db4-f768-488b-b8c7-953e707371d5/version/v0.1/edit

## 2. Container Diagram
This diagram breaks down the system into its primary containers: the client side (mobile and web), server side (API Gateway, Application Server, Real-Time Processing Engine), and data storage (Cloud Database). https://www.mermaidchart.com/app/projects/954ba711-e390-447d-bc86-64fd8cbd3c14/diagrams/35215afb-e241-41ff-a97b-fcb373a47137/version/v0.1/edit

## 3. Link to mermaid for Use case diagram.
The diagram below represents interactions between actors (Students, Teachers, admin and database) and the system. https://www.mermaidchart.com/app/projects/8e46d07a-e802-4efa-971b-48f52adfb76f/diagrams/435c2f83-2296-421d-9009-79025061cc94/version/v0.1/edit

## 3. High-level architecture.
https://www.mermaidchart.com/app/projects/8e46d07a-e802-4efa-971b-48f52adfb76f/diagrams/36e12fa6-0a2c-49b5-b2dd-e82c4ff78783/version/v0.1/edit
https://www.mermaidchart.com/app/projects/954ba711-e390-447d-bc86-64fd8cbd3c14/diagrams/35215afb-e241-41ff-a97b-fcb373a47137/version/v0.1/edit

AI Model: Analyzes student performance trends.
Database: Stores student records, grades, and attendance.
Frontend: Web dashboard for students, teachers, and parents.
Backend: Handles API requests and runs AI predictions.

## 4. Data Flow Diagram
This is the data flow diagram. https://www.mermaidchart.com/app/projects/954ba711-e390-447d-bc86-64fd8cbd3c14/diagrams/90d2154f-58d2-4186-b0e0-d5ba6dde873c/version/v0.1/edit

graph TD
    A[Student] -->|Requests Report| B[Backend API]
    B -->|Fetch Data| C[Database]
    B -->|Runs Analysis| D[Machine Learning Model]
    D -->|Returns Insights| B
    B -->|Displays Report| A