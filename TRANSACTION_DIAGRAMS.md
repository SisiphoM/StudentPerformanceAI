Below are state transition diagrams for critical objects in the Student Performance Prediction System.

### **1.1 Student State Transition**
```mermaid
stateDiagram
    [*] --> Active
    Active --> Suspended : Violates academic policies
    Suspended --> Active : Reinstated
    Active --> Graduated : Completes requirements
    Suspended --> Dropped Out : Does not return
```
**Explanation:**
- A student starts in the **Active** state.
- If they violate academic policies, they get **Suspended**.
- Suspended students can either be **Reinstated** or **Drop Out**.
- If they complete their studies, they **Graduate**.

---

### **1.2 Assignment Submission State Transition**
```mermaid
stateDiagram
    [*] --> Pending
    Pending --> Submitted : Student uploads file
    Submitted --> Graded : Instructor assigns a grade
    Graded --> [*]
```
**Explanation:**
- A student starts with a **Pending** assignment.
- Once uploaded, it moves to **Submitted**.
- After grading, it reaches the final state **Graded**.

---

### **1.3 Performance Report State Transition**
```mermaid
stateDiagram
    [*] --> Generated
    Generated --> Under Review : Instructor checks report
    Under Review --> Approved : Report is validated
    Approved --> [*]
```
**Explanation:**
- The system **Generates** a report.
- The report goes **Under Review**.
- Once validated, it is **Approved**.

---


