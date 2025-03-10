# Use Case Diagram

## Overview
The diagram below represents interactions between actors (Students, Teachers, etc.) and the system.

```mermaid
graph TD
    A[Student] -->|View Performance Report| B[AI-Powered System]
    A -->|Receive Learning Recommendations| B
    C[Teacher] -->|Monitor Student Progress| B
    C -->|Generate Reports| B
    D[Parent] -->|Access Student Reports| B
    E[Admin] -->|Manage User Accounts| B
    B -->|Fetch Data from School Database| F[Database]

## 1. View Performance Report
**Actor:** Student  
**Preconditions:** Student must be logged in.  
**Postconditions:** Student sees a report of academic performance.  
**Basic Flow:**  
1. Student logs into the system.  
2. Selects "View Performance Report."  
3. System fetches data from the database.  
4. Report is displayed on the dashboard.  
**Alternative Flow:**  
- If no data is available, the system shows "No records found."

## 2. Generate Student Reports
**Actor:** Teacher  
**Preconditions:** Teacher must be authenticated.  
**Postconditions:** Reports are generated and stored.  
**Basic Flow:**  
1. Teacher logs in.  
2. Selects a student.  
3. Clicks "Generate Report."  
4. System processes and displays the report.  
**Alternative Flow:**  
- If the student has missing data, a warning appears.

## 3. Receive Learning Recommendations
**Actor:** Student  
**Preconditions:** AI model must be trained.  
**Postconditions:** Student receives study suggestions.  
**Basic Flow:**  
1. Student accesses learning recommendations.  
2. System analyzes past performance.  
3. AI suggests study resources.  
**Alternative Flow:**  
- If AI model fails, a generic suggestion appears.