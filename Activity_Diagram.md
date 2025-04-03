## 2. Activity Workflow Modeling with Activity Diagrams 

### **2.1 Student Registration Workflow**
```mermaid
graph TD
    A[Start] --> B[User enters details]
    B --> C[Validate input]
    C -- Invalid --> D[Show error message]
    C -- Valid --> E[Create account]
    E --> F[Send confirmation email]
    F --> G[End]
```
**Explanation:**
- Users enter registration details.
- If invalid, an error message is shown.
- If valid, the account is created, and an email is sent.

---

### **2.2 Submit Assignment Workflow**
```mermaid
graph TD
    A[Start] --> B[Student selects assignment]
    B --> C[Upload file]
    C --> D[Validate format]
    D -- Invalid --> E[Show error message]
    D -- Valid --> F[Mark as submitted]
    F --> G[End]
```
**Explanation:**
- A student selects and uploads an assignment.
- If the format is invalid, an error is shown.
- If valid, the assignment is **Submitted**.
