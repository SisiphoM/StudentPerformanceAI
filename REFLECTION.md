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
