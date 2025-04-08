# Domain Model Table

| **Entity**         | **Attributes**                                                                 | **Methods**                            | **Relationships**                                      | **Business Rules**                                                                 |
|--------------------|---------------------------------------------------------------------------------|----------------------------------------|--------------------------------------------------------|-------------------------------------------------------------------------------------|
| Student            | student_id, name, email, gender, age, attendance_rate, previous_scores         | calculatePerformance(), updateProfile()| Enrolled in Courses; Has Performance Prediction        | A student must be registered to generate a prediction                              |
| Course             | course_id, course_name, credits                                                 | assignStudent(), calculateAverage()    | Contains Modules; Taught by Lecturer                   | A course must have at least one module                                              |
| Module             | module_id, module_name, weight                                                  | getModuleDetails()                     | Belongs to Course                                      | Each module must belong to a course                                                |
| Lecturer           | lecturer_id, name, email, department                                            | assignMarks(), viewReport()            | Teaches Course                                         | Only assigned lecturers can submit student marks                                    |
| PerformanceReport  | report_id, student_id, prediction_score, risk_level, generated_on               | generateReport(), exportToPDF()        | Belongs to Student                                     | Reports must be generated after prediction is run                                   |
| AIModel            | model_id, version, accuracy, training_data_summary                             | trainModel(), predict(), evaluate()    | Used to Generate Performance Report                    | Model must be trained before prediction                                             |



classDiagram
    class Student {
        +int student_id
        +String name
        +String email
        +String gender
        +int age
        +float attendance_rate
        +List<float> previous_scores
        +calculatePerformance()
        +updateProfile()
    }

    class Course {
        +int course_id
        +String course_name
        +int credits
        +assignStudent()
        +calculateAverage()
    }

    class Module {
        +int module_id
        +String module_name
        +float weight
        +getModuleDetails()
    }

    class Lecturer {
        +int lecturer_id
        +String name
        +String email
        +String department
        +assignMarks()
        +viewReport()
    }

    class PerformanceReport {
        +int report_id
        +int student_id
        +float prediction_score
        +String risk_level
        +Date generated_on
        +generateReport()
        +exportToPDF()
    }

    class AIModel {
        +int model_id
        +String version
        +float accuracy
        +String training_data_summary
        +trainModel()
        +predict()
        +evaluate()
    }

    Student "1" --> "*" PerformanceReport : generates
    Student "1" --> "*" Course : enrolled_in
    Course "1" --> "*" Module : contains
    Lecturer "1" --> "*" Course : teaches
    PerformanceReport "1" --> "1" AIModel : uses
