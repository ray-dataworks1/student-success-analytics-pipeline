@startuml
```plantuml
entity "dim_student" as student {
  * student_id : UUID <<PK>>
  age : int
  gender : string
  nd_flag : boolean
  enrollment_date : date
  subscription_id : int
}

entity "dim_subscription" as subscription {
  * subscription_id : int <<PK>>
  plan : string
  status : string
  churn_date : date
}

entity "dim_content" as content {
  * quiz_id : int <<PK>>
  subject : string
  topic : string
  difficulty : string
  ai_generated : boolean
  source : string
}

entity "dim_device" as device {
  * device_id : int <<PK>>
  device_type : string
  os : string
  app_version : string
}

entity "dim_time" as time {
  * date_id : int <<PK>>
  date : date
  week : int
  month : int
  year : int
}

entity "dim_feedback_type" as feedback_type {
  * feedback_type_id : int <<PK>>
  feedback_type : string
  category : string
}

entity "fct_quiz_sessions" as quiz_sessions {
  * quiz_session_id : int <<PK>>
  student_id : int <<FK>>
  quiz_id : int <<FK>>
  device_id : int <<FK>>
  quiz_session_date : date
  quiz_score : int
  time_spent_minutes : int
  flashcards_used : boolean
  pass_or_fail : string
}

entity "fct_flashcard_reviews" as flashcard_reviews {
  * flashcard_review_id : int <<PK>>
  student_id : int <<FK>>
  quiz_session_id : int <<FK>>
  quiz_id : int <<FK>>
  flashcard_accuracy : int
  review_timestamp : datetime
}

entity "fct_customer_reviews" as customer_reviews {
  * review_id : int <<PK>>
  student_id : int <<FK>>
  feedback_type_id : int <<FK>>
  review_date : date
  satisfaction_rating : int
  comments : string
  sentiment_score : int
}

student ||--o{ quiz_sessions : ""
quiz_sessions }o--|| content : ""
quiz_sessions }o--|| device : ""
quiz_sessions }o--|| time : ""
student ||--o{ flashcard_reviews : ""
flashcard_reviews }o--|| quiz_sessions : ""
flashcard_reviews }o--|| content : ""
flashcard_reviews }o--|| time : ""
student ||--o{ customer_reviews : ""
customer_reviews }o--|| feedback_type : ""
customer_reviews }o--|| time : ""
student }|--|| subscription : ""
quiz_sessions }o--|| time : ""

@enduml
