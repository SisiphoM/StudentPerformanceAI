 # AI-Powered Student Performance Prediction System - Architecture

## 1. Context Diagram
This diagram shows the system's high-level interaction with students, teachers, and databases. Click link for Mermaid diagram https://www.mermaidchart.com/app/projects/8e46d07a-e802-4efa-971b-48f52adfb76f/diagrams/b5557db4-f768-488b-b8c7-953e707371d5/version/v0.1/edit

```mermaid
graph LR
    A[Student] -->|Submits Assignments, Tests, Attendance| B[Performance Prediction System]
    B -->|Generates Reports| C[Teacher]
    B -->|Provides Learning Recommendations| A
    B -->|Fetches Data| D[School Database]

## 2. Link to mermaid for Use case diagram https://www.mermaidchart.com/app/projects/8e46d07a-e802-4efa-971b-48f52adfb76f/diagrams/435c2f83-2296-421d-9009-79025061cc94/version/v0.1/edit