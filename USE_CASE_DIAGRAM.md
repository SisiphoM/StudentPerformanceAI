# Use Case Diagram

## Overview
The diagram below represents interactions between actors (Students, Teachers, Parent, Amin and Database.) and the system.

https://www.mermaidchart.com/app/projects/8e46d07a-e802-4efa-971b-48f52adfb76f/diagrams/435c2f83-2296-421d-9009-79025061cc94/version/v0.1/edit

```mermaid
graph TD
    A[Student] -->|View Performance Report| B[AI-Powered System]
    A -->|Receive Learning Recommendations| B
    C[Teacher] -->|Monitor Student Progress| B
    C -->|Generate Reports| B
    D[Parent] -->|Access Student Reports| B
    E[Admin] -->|Manage User Accounts| B
    B -->|Fetch Data from School Database| F[Database]
