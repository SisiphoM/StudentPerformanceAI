# Use Case Specifications

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

## 4. Parent Access Student Progress
**Actor:** Parent  
**Preconditions:** Parent must have an account linked to the student's profile.  
**Postconditions:** Parent views their child's academic performance.  
**Basic Flow:**  
1. Parent logs into the system.  
2. Selects "View Child's Progress."  
3. System retrieves and displays the child's report.  
**Alternative Flow:**  
- If the parent account is not linked, an error message is displayed.

## 5. AI Model Training
**Actor:** System (Automated process)  
**Preconditions:** New student data must be available.  
**Postconditions:** AI model is updated with the latest student performance trends.  
**Basic Flow:**  
1. System collects student performance data.  
2. AI model processes and learns from the data.  
3. New performance predictions are generated.  
**Alternative Flow:**  
- If training fails, an error log is recorded, and previous predictions remain active.

## 6. Manage User Accounts
**Actor:** Admin  
**Preconditions:** Admin must be logged in with valid credentials.  
**Postconditions:** New accounts are created or updated.  
**Basic Flow:**  
1. Admin logs into the system.  
2. Selects "Manage Users."  
3. Adds, updates, or removes user accounts.  
4. System saves changes and notifies users.  
**Alternative Flow:**  
- If the email is already in use, an error message is displayed.

## 7. System Sends Alerts for At-Risk Students
**Actor:** System  
**Preconditions:** AI model must detect a significant drop in student performance.  
**Postconditions:** Teachers and parents receive alerts.  
**Basic Flow:**  
1. AI model identifies an at-risk student.  
2. System generates an alert.  
3. Alert is sent via email/SMS to the teacher and parent.  
**Alternative Flow:**  
- If no contact information is available, the alert is logged in the system.

## 8. Data Synchronization with School Database
**Actor:** System  
**Preconditions:** System must have API access to the school's database.  
**Postconditions:** Student records are updated daily.  
**Basic Flow:**  
1. System connects to the school database.  
2. Fetches the latest student performance data.  
3. Updates local records.  
**Alternative Flow:**  
- If the connection fails, the system retries after 30 minutes.
