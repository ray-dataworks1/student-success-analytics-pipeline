@startuml
entity "Learners" as learners {
  +Student_ID : UUID
  Age : INT
  Gender : VARCHAR
  Learning_Disabilities : VARCHAR
  Enrollment_Date : DATE
  Subscription_Type : VARCHAR
}

entity "Activities" as activities {
  +Activity_ID : UUID
  Student_ID : UUID
  Quiz_Session_Date : DATE
  Quiz_ID : VARCHAR
  Quiz_Topic : VARCHAR
  Quiz_Score : INT
  Time_Spent_on_Quiz : INT
  Flashcards_Used : VARCHAR
  Flashcard_Accuracy : INT
  Total_Active_Sessions_weekly : INT
  Session_Duration : INT
  Device_Used : VARCHAR
}

entity "Outcomes" as outcomes {
  +Outcome_ID : UUID
  Student_ID : UUID
  Cumulative_Learning_Progress : FLOAT
  Retention_Rate_weekly : FLOAT
  Retention_Rate_monthly : FLOAT
  Time_to_Master_Key_Concepts : INT
  Math_Accuracy : FLOAT
  Science_Accuracy : FLOAT
  History_Accuracy : FLOAT
  English_Accuracy : FLOAT
  Geography_Accuracy : FLOAT
}

entity "Feedback" as feedback {
  +Feedback_ID : UUID
  Student_ID : UUID
  Satisfaction_Rating : INT
  Feedback_Type : VARCHAR
  Date_of_Feedback : DATE
  Comments_Sentiment : VARCHAR
}

' Relationships
learners ||--o{ activities : has
learners ||--o{ outcomes : has
learners ||--o{ feedback : gives

@enduml
