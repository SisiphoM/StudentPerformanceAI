 # 📘 README.md

## 🎓 Student Performance Prediction System

This system predicts students' academic performance using AI and supports educators with smart insights. This version includes full object-oriented class models and implementations of six creational design patterns, backed by unit tests.

---

## 📁 Project Structure
```
StudentPerformanceAI/
├── src/models/                # UML class diagram implementations
├── creational_patterns/      # Creational design patterns
├── tests/                    # Unit tests for each pattern
├── README.md                 # Project overview and usage
└── CHANGELOG.md              # Feature tracking
```

---

## 🧠 Implemented Creational Patterns

| Pattern            | Summary                                                       |
|--------------------|---------------------------------------------------------------|
| **Simple Factory** | `PredictionFactory` creates either Linear or Neural AI models |
| **Factory Method** | Exporters (PDF/CSV) handle output format generation           |
| **Abstract Factory** | `UIFactory` creates OS-specific UI components               |
| **Builder**        | Builds a flexible StudentProfile step-by-step                 |
| **Prototype**      | Clones AIModel instances with `.clone()`                      |
| **Singleton**      | Ensures one database connection with `DatabaseConnection`     |

---

## 🧪 Running Tests
Install requirements:
```bash
pip install pytest pytest-cov
```
Run all tests with coverage:
```bash
python -m pytest --cov=creational_patterns
```

---

## 🏗 Class Diagram (Overview)
- Classes implemented: Student, Course, Lecturer, Assignment, Feedback, PerformanceReport, AIModel
- Encapsulates behavior and structure as per object-oriented principles

---

## ✨ Features
- Predict student performance using ML logic
- Generate and export reports
- Testable, reusable, and extendable architecture
- Built using SOLID and OOP principles

---

## 👤 Author
**Sisipho Mdaka**  
Postgraduate Diploma in ICT: Application Development  
Cape Peninsula University of Technology

