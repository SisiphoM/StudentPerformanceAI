 # 📘 README.md

## 🎓 Student Performance Prediction System

This system predicts students' academic performance using AI and supports educators with smart insights. This version includes full object-oriented class models and implementations of six creational design patterns, backed by unit tests.

An AI-driven system designed to predict academic performance and assist educators with early intervention strategies. This project combines full object-oriented modeling, creational design patterns, repository persistence, Agile GitHub project management, and comprehensive documentation.

---

## 📚 Table of Contents
- [System Overview](#system-overview)
- [Setup Instructions](#setup-instructions)
- [Folder Structure](#folder-structure)
- [Assignments Breakdown](#assignments-breakdown)
- [Implemented Creational Patterns](#implemented-creational-patterns)
- [Repository Layer and Persistence](#repository-layer-and-persistence)
- [Running the Project](#running-the-project)
- [Challenges Faced](#challenges-faced)
- [Features](#features)
- [Author](#author)

---

## 📖 System Overview
The system predicts student performance based on their academic records, stores student profiles, and generates reports. Built using Python, following SOLID principles and Agile methodology.

---

## 🛠 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/StudentPerformanceAI.git
cd StudentPerformanceAI
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate # On Mac/Linux
```

### 3. Install Dependencies
```bash
pip install pytest pytest-cov
```

### 4. (Important) Fix Import Errors
Set your `PYTHONPATH` before running tests:
```bash
set PYTHONPATH=.
```

To automate, create a `.env` file containing:
```
PYTHONPATH=.
```

---

## 📁 Folder Structure
```
StudentPerformanceAI/
├── src/models/                      # Domain Models
├── creational_patterns/             # Design Pattern Implementations
├── repositories/                    # Persistence Layer
│   ├── inmemory/                    # In-Memory Storage
│   ├── database/                    # Future-proof Database Storage
├── factories/                       # Repository Factory
├── tests/                           # Unit Tests
├── run_example.py                   # Manual execution script
├── README.md
├── CHANGELOG.md
├── .env
├── .vscode/settings.json
```

---

## 📚 Assignments Breakdown

| Assignment | Contribution |
|------------|--------------|
| **Assignment 3** | Defined the problem domain and objectives. |
| **Assignment 4** | Identified stakeholders and functional requirements. |
| **Assignment 5** | Created Use Case Diagram and actors. |
| **Assignment 6** | Developed full Use Case Specifications. |
| **Assignment 7** | Set up GitHub Agile Project Board with Issues and Milestones. |
| **Assignment 8** | Modeled State and Activity Diagrams. |
| **Assignment 9** | Created Domain Model Table and UML Class Diagram. |
| **Assignment 10** | Implemented source code, applied creational design patterns, and wrote unit tests. |
| **Assignment 11** | Designed Repository Persistence Layer and completed full system integration. |

---

## 🧠 Implemented Creational Patterns
| Pattern | Summary |
|---------|---------|
| **Simple Factory** | `PredictionFactory` creates AI models. |
| **Factory Method** | Exporters (PDF/CSV) for reports. |
| **Abstract Factory** | `UIFactory` generates platform-specific UI components. |
| **Builder** | Step-by-step construction of `StudentProfile`. |
| **Prototype** | Cloning `AIModel` instances. |
| **Singleton** | Single instance of `DatabaseConnection` ensured. |

---

## 🗄️ Repository Layer and Persistence
- **Base Repository Interface:** Generic CRUD methods.
- **In-Memory Repository:** Quick storage for testing.
- **Repository Factory:** Selects between Memory or (future) Database implementation.
- **Database Repository (Stub):** Placeholder ready for SQL backend integration.

```python
from factories.repository_factory import RepositoryFactory
student_repo = RepositoryFactory.get_student_repository("MEMORY")
```

---

## ▶️ Running the Project

### Manual Run
```bash
set PYTHONPATH=.
python run_example.py
```

### Run Unit Tests
```bash
set PYTHONPATH=.
pytest
```

> ⚠️ **Important:** Tests currently **failing** due to path import issues under `pytest`. Manual running works fine.


---

## 🛠 Challenges Faced
- **ModuleNotFoundError:** Python could not find `repositories/` because VS Code didn’t automatically set PYTHONPATH.
- **pytest Import Error:** Had to manually set `PYTHONPATH=.` before running.
- **Test Failures:** Despite correct manual running, pytest could not resolve imports without deep configuration.
- **Environment Configuration:** Required setting `.env` and `.vscode/settings.json`.

✅ Manual running (`run_example.py`) works perfectly.
❌ Full `pytest` automation pending due to time constraints.

---

## ✨ Features
- Predicts student performance with AI logic
- Generates academic performance reports
- Saves student data in an in-memory store
- Future-proof repository ready for SQL database
- Follows SOLID principles and Agile Methodology

---

## 👩‍💻 Author
**Sisipho Mdaka**  
Postgraduate Diploma in ICT: Application Development  
Cape Peninsula University of Technology  

---

# 📝 CHANGELOG.md

## [v1.0.0] - 2025-04-16
### 🎉 Milestone Completion
- Implemented full class diagram in code.
- Applied six major creational design patterns.
- Added Repository Persistence Layer.
- Integrated manual test cases.
- Detailed README.md and project documentation.
