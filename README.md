# Student_Performance_Prediction_System
This project is part of my Data Science & Machine Learning Internship at DSPL Technologies. The goal is to predict student performance based on various features such as attendance, study hours, previous grades, and more, using supervised machine learning techniques.

📌 Problem Statement
Educational institutions are constantly striving to identify students who need support early. By predicting student performance using machine learning, we can assist teachers and administrators in making data-driven interventions to improve academic outcomes.

📁 Dataset
Source: Kaggle – Student Performance Predictions
Features:
StudentID
Name
Gender
AttendanceRate
StudyHoursPerWeek
PreviousGrade
ExtracurricularActivities
ParentalSupport
FinalGrade (used to derive Performance class: High, Medium)
🔍 Exploratory Data Analysis (EDA)
Checked for missing values, data types, and distributions
Visualized distributions of grades, attendance, and study hours
Correlation analysis to find key influencing features
🧪 Preprocessing
Dropped irrelevant columns (Name, StudentID)
Encoded categorical variables (Gender, ExtracurricularActivities, ParentalSupport)
Mapped final grades to performance categories:
High: FinalGrade ≥ 75
Medium: 50 ≤ FinalGrade < 75
Low: FinalGrade < 50 (not present in this dataset)
🤖 Machine Learning Models
Two classification models were trained and evaluated:

Model	Accuracy
Logistic Regression	100%
Random Forest	100%
📌 Note: Due to small and imbalanced dataset, accuracy appears perfect. Real-world results may vary with larger datasets.

🧠 Feature Importance (Random Forest)
Top features influencing performance:

PreviousGrade
StudyHoursPerWeek
AttendanceRate
💾 Model Deployment
Best model saved using joblib:
joblib.dump(model, 'student_performance_model.pkl')
📂 Project Structure kotlin Copy Edit student-performance-prediction/ ├── data/ │ └── Student_Performance.csv ├── model/ │ └── student_performance_model.pkl ├── notebook/ │ └── student_performance_analysis.ipynb ├── README.md └── Task2_Presentation.pptx 🙋‍♂️ Author Ragini Kushwaha 📧 raginikushwaha1804@gmail.com 🔗 LinkedIn | GitHub

🚀 Future Work Handle class imbalance for better generalization

Deploy as a web app using Streamlit

Incorporate more data (e.g., behavior, class participation)
