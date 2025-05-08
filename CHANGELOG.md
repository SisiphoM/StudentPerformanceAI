 # 📝 CHANGELOG.md

## [v1.0.0] - 2025-04-16
### 🎉 Initial Submission
- Implemented class diagram: Student, Course, Lecturer, etc.
- Created 6 creational patterns under `/creational_patterns`
- Added complete test suite in `/tests`
- Integrated coverage using `pytest-cov`
- Updated `README.md` and created project structure
## [v1.3.0] - 2025-04-28
### 🚀 CI/CD Pipeline Integration (Assignment 13)
- Created GitHub Actions CI workflow in `.github/workflows/ci.yml`
- Automatically runs tests on every push and pull request
- Builds and uploads release artifact on successful push to `main`
- Enabled branch protection on `main` to block failed PRs
- Added `PROTECTION.md` documentation for GitHub branch rules

---

## [v1.2.0] - 2025-04-27
### 🌐 REST API with FastAPI (Assignment 12)
- Created FastAPI routes and services for students, courses, performance
- Integrated Swagger/OpenAPI documentation at `/docs`
- Defined all routes and logic in `/api/` and `/services/`

## [v1.1.0] - 2025-04-25
### 🗃 Repository Layer (Assignment 11)
- Defined generic and specific repository interfaces
- Created in-memory implementation using dictionary
- Implemented factory pattern for storage injection
- Added stub for future database repository

## [v1.0.0] - 2025-04-16
### 🎉 Initial Submission
- Implemented class diagram: Student, Course, Lecturer, etc.
- Created 6 creational patterns under `/creational_patterns`
- Added complete test suite in `/tests`
- Integrated coverage using `pytest-cov`
- Updated `README.md` and created project structure