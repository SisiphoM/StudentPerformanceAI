classDiagram
    class Student {
        -studentId: String
        -name: String
        -email: String
        -attendanceRecord: Float
        -GPA: Float
        +viewPerformance()
        +updateProfile()
    }

    class Course {
        -courseId: String
        -title: String
        -credits: Int
        +addStudent()
        +removeStudent()
    }

    class Instructor {
        -instructorId: String
        -name: String
        -email: String
        -department: String
        +createAssignment()
        +reviewPerformance()
    }

    class Assignment {
        -assignmentId: String
        -title: String
        -dueDate: Date
        -maxScore: Float
        +submit()
        +gradeAssignment()
    }

    class PerformanceRecord {
        -recordId: String
        -studentId: String
        -courseId: String
        -grade: Float
        +calculateAverage()
    }

    class PredictionModel {
        -modelId: String
        -version: String
        -accuracy: Float
        -modelType: String
        +trainModel()
        +predictPerformance()
    }

    class Feedback {
        -feedbackId: String
        -content: String
        -date: Date
        -relatedTo: String
        +generateFeedback()
        +editFeedback()
    }

    Student "1" -- "*" PerformanceRecord : has
    Course "1" -- "*" PerformanceRecord : contains
    Student "1" -- "*" Assignment : completes
    Instructor "1" -- "*" Course : teaches
    Course "1" -- "*" Assignment : contains
    Assignment "1" -- "1" Feedback : has
    PredictionModel "1" -- "*" Student : predictsFor