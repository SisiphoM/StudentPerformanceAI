# Reflection: Balancing Stakeholder Needs

### Challenges Faced:
1. **Conflicting Priorities:**  
   - Students want **instant feedback**, but AI models require **time to process** accurate predictions.  
2. **Data Privacy Concerns:**  
   - Parents want **full access** to their child’s data, but **privacy laws limit** what can be shared.  
3. **Scalability vs. Cost:**  
   - Schools want **AI predictions in real-time**, but **processing power is expensive**.  
4. **Technical Complexity:**  
   - IT staff need **a secure, scalable system**, but **maintaining AI models requires expertise**.  

### Solutions:
- **Compromises:** AI predictions update **every 24 hours** instead of instantly.  
- **Data Governance:** Parents can see **performance trends**, but not **raw student data**.  
- **Optimized Costs:** AI runs on **cloud-based GPUs** during peak times only.  

# Reflection: Challenges in Use Case Modeling & Testing

### **Challenges Faced**
1. **Translating Requirements into Use Cases**  
   - Some stakeholder concerns were broad, requiring careful breakdown into clear use cases.
2. **Handling Alternative Flows**  
   - Predicting edge cases (e.g., missing data) was tricky.
3. **Designing Meaningful Test Cases**  
   - Ensuring test cases matched requirements was challenging.

### **Lessons Learned**
- Clearly defining **preconditions and postconditions** helps structure use cases.  
- Test cases should be designed **alongside requirements** to ensure full coverage.  
- **Stakeholder collaboration** ensures all needs are addressed properly.

# Reflection: Challenges in Agile Planning  

### **1. Prioritization Challenges**  
- Some user stories felt equally important, making MoSCoW prioritization difficult.  
- Solution: Focused on **core functionalities first** (performance reports, user management).  

### **2. Effort Estimation Issues**  
- Assigning **story points** was tricky without exact workload details.  
- Solution: Used the **Fibonacci sequence** for rough estimation.  

### **3. Aligning Agile with Stakeholder Needs**  
- Balancing **technical complexity vs. user needs** was tough.  
- Solution: Ensured that **must-have** stories addressed key stakeholder concerns.  

### **4. Planning Dependencies**  
- Some tasks required system integration before they could be tested.  
- Solution: Scheduled **integration tasks** early in the sprint.  

### **Lessons Learned**  
- **Break down large tasks** into smaller, testable increments.  
- **Use backlog prioritization** to ensure MVP is functional ASAP.  
- **Plan for dependencies early** to avoid blockers.  


# Reflection on Using GitHub Projects

## **Challenges Faced**

### **1. Choosing the Right Template**
Selecting the most suitable Kanban template was a challenge.  
- Some templates lacked **automation**, requiring **manual updates**.  
- Others, like **Bug Triage**, were too focused on issue tracking rather than Agile workflows.  
- **Solution:** We selected the **Automated Kanban** template for its ability to **automate issue progression**, reducing manual effort.

### **2. Customizing the Board**
Finding the right balance between **simplicity and detail** was tricky.  
- Too many columns made the board **complicated**, while too few lacked **workflow clarity**.  
- **Solution:** We added only necessary columns, such as **"Testing"** for QA and **"Blocked"** for dependencies.

### **3. Task Assignment & Traceability**
Ensuring each issue had a **clear owner and priority** was time-consuming.  
- Some issues were **misassigned**, leading to confusion.  
- **Solution:** Used `@mentions` to **assign tasks**, linked **GitHub Issues to the board**, and added **labels for priority tracking**.

---

## **Comparison with Other Tools**

### **GitHub Projects vs. Trello**
| Feature | GitHub Projects | Trello |
|---------|----------------|--------|
| **Integration** | Directly integrates with GitHub Issues | Requires manual linking of issues |
| **Automation** | Supports **issue tracking automation** | No built-in automation for GitHub Issues |
| **Best For** | Developers using GitHub | General project tracking |

📌 **Conclusion:** *GitHub Projects is better for developer-focused workflows, while Trello is more flexible for general teams.*

### **GitHub Projects vs. Jira**
| Feature | GitHub Projects | Jira |
|---------|----------------|------|
| **Complexity** | Lightweight and easy to set up | More complex with detailed reporting |
| **Reporting & Insights** | Basic tracking and automation | Advanced sprint reports, velocity charts |
| **Best For** | Small to medium teams using GitHub | Large organizations needing **detailed Agile metrics** |

📌 **Conclusion:** *Jira provides more powerful reporting for large teams, but GitHub Projects is simpler and more developer-friendly.*

---

## **Final Thoughts**
Using **GitHub Projects** significantly improved our workflow by:
- **Automating task tracking** and reducing manual updates.
- **Enhancing team collaboration** through clear issue assignments.
- **Providing an easy-to-use Agile tool** without additional overhead.

Overall, **GitHub Projects** proved to be a **lightweight, developer-friendly alternative** to more complex tools like Jira. 🚀

# Reflection on Using domain model 
## Challenges Faced
One of the main challenges I faced during this assignment was understanding how to accurately translate the system's domain logic into a structured domain model. It required a solid grasp of the relationships between the various entities in the Student Performance Prediction System and how those entities interact. Designing the table to include relevant attributes and methods for each class also took time and thoughtful consideration.

Another challenge was learning and applying the Mermaid syntax to create the class diagram. While it is a powerful tool, making sure the diagram accurately reflected the model without syntax errors involved trial and error.

## What I Learned
This assignment helped me understand the importance of domain modeling in software engineering. I learned how crucial it is to define clear entities, their properties, and behaviors, which serve as a blueprint for system design. I also improved my skills in using Mermaid to visually represent models, which is an effective way to communicate system structure to stakeholders and developers.

I gained practical experience in balancing abstraction and detail—making sure the model was not too complex but still captured the essential parts of the system.

## Application to My Project
By completing this domain model, I now have a clear overview of the key components of the Student Performance Prediction System. This will serve as a foundational reference when implementing the backend logic, database schema, and even the AI prediction flow. It also ensures better collaboration with teammates, as everyone can refer to the same structured view of the system.

---
# Reflection on Service Layer and REST API
## Module Import Errors:

ModuleNotFoundError: No module named 'repositories.inmemory'
✅ Solution: Ensure directory structure matches import paths exactly.

## Test Discovery Issues:

Caused by misplaced or improperly named test files.

## VS Code Python Path Issues:

Fixed by setting Python interpreter manually via Ctrl+Shift+P → Python: Select Interpreter.

## Missing .vscode/settings.json:

Resolved by manually configuring interpreter.

## Tests Not Passing:

Not all dependencies/modules were fully integrated. Known and being worked on.


## 📚 Learning Journey by Assignment

### Assignment 3 – UML Class Diagram
- Designed core domain models such as `Student`, `Course`, `Lecturer`, `PerformanceReport`.
- Learned how to translate real-world educational concepts into class-based object-oriented structures.

### Assignment 4 – Creational Design Patterns
- Implemented six creational patterns: Simple Factory, Factory Method, Abstract Factory, Builder, Prototype, Singleton.
- Gained a deeper understanding of design pattern purposes and real-world application in Python.
- Learned how to separate creation logic from usage for scalability.

### Assignment 5 – Unit Testing and Coverage
- Used `pytest` and `pytest-cov` to test creational patterns and class models.
- Ensured all features were testable and measurable.
- Learned how to structure tests per module and pattern.

### Assignment 6 – Prediction Service Logic
- Integrated dummy logic for student performance prediction.
- Understood how to separate AI logic from structural models using service classes.

### Assignment 7 – CSV/PDF Export Logic
- Created export interfaces and used Factory Method to choose between formats.
- Learned how to work with external data formats programmatically.

### Assignment 8 – Prototype Cloning
- Implemented `.clone()` methods using deep/shallow copy logic.
- Gained insight into object replication needs in AI/ML workflows.

### Assignment 9 – Singleton Database Connection
- Designed a `DatabaseConnection` Singleton to control database access.
- Understood the importance of avoiding multiple DB connections.

### Assignment 10 – Integration and Demo File
- Created a `run_example.py` script to showcase system flow from profile building to prediction.
- Refactored and connected various modules.

### Assignment 11 – Repository Layer
- Built `IRepository`, `IStudentRepository`, and in-memory implementations using HashMap.
- Introduced `RepositoryFactory` to abstract implementation details.
- Faced errors related to missing packages and folder structure, such as:
  - `ModuleNotFoundError: No module named 'repositories.inmemory'`
- Learned how to organize Python packages and fix import paths.

### Assignment 12 – Service Layer and REST API
- Added service layer between logic and repository for better separation of concerns.
- Built RESTful API using FastAPI and tested Swagger documentation.
- Gained practical experience with API development and documentation tools.

---

## ⚠️ Challenges Encountered

- **Import errors** due to incorrect folder structure or missing `__init__.py` files.
- **Test failures** from unresolved module paths and structure inconsistencies.
- **Tooling issues** such as missing `.vscode/settings.json` or lack of clear instructions for running the project.
- **Python version inconsistencies** (e.g., using Python 3.13 caused some unexpected import issues).

---

## 🧠 Key Learnings

- Mastered Python OOP fundamentals, especially design patterns and modular design.
- Learned to test and measure code quality early using `pytest` and coverage tools.
- Understood how to abstract infrastructure using repositories and services.
- Built confidence with FastAPI and documenting APIs with Swagger.
- Developed strong troubleshooting skills by debugging path and import issues.

---

## ✅ Current Status

- Project structure is complete through Assignment 12.
- Core logic and patterns are implemented.
- Unit tests exist but are currently **not passing** due to unresolved path issues (see `README.md`).
- Ready for final debugging and polish phase.

---