# Test Cases

| Test Case ID | Requirement ID | Description | Steps | Expected Result | Actual Result | Status |
|-------------|---------------|-------------|-------|-----------------|---------------|--------|
| TC-001 | FR-003 | Student views performance report | 1. Log in 2. Click "View Report" | Report is displayed | - | - |
| TC-002 | FR-005 | Teacher generates a report | 1. Log in 2. Select student 3. Click "Generate Report" | Report is saved | - | - |
| TC-003 | FR-007 | Parent accesses student progress | 1. Log in 2. Select child 3. View progress | Data is displayed | - | - |
| TC-004 | FR-009 | AI suggests learning resources | 1. Log in 2. Click "Recommendations" | Resources are shown | - | - |

## Non-Functional Tests
### Performance Test
**Requirement:** "System must handle 1000 concurrent users."  
**Test:** Simulate 1000 users accessing reports simultaneously.  

### Security Test
**Requirement:** "All user data must be encrypted."  
**Test:** Try accessing data without authorization. Expect access denial.
