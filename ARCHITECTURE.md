 # AI-Powered Student Performance Prediction System - Architecture

## 1. Context Diagram
This diagram shows the system's high-level interaction with students, teachers, and databases.

```mermaid
graph LR
    A[Student] -->|Submits Assignments, Tests, Attendance| B[Performance Prediction System]
    B -->|Generates Reports| C[Teacher]
    B -->|Provides Learning Recommendations| A
    B -->|Fetches Data| D[School Database]

