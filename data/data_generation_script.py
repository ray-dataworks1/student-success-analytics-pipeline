import pandas as pd
import numpy as np
from faker import Faker

# Initialize Faker instance for generating synthetic data
fake = Faker()

# Define constants for dataset
n_learners = 500
n_quizzes = 20
n_days = 90  # 3 months worth of days
quiz_topics = ['Math', 'Science', 'History', 'English', 'Geography']
devices = ['Mobile', 'Desktop']
subscription_types = ['Free', 'Premium']
feedback_types = ['Bug', 'Feature Request', 'Suggestion']
sentiment = ['Positive', 'Neutral', 'Negative']
genders = ['Male', 'Female', 'Non-binary']
learning_disabilities = ['ND', 'Non-ND']

# Helper function to create randomized data
def create_learner_data(n):
    learner_data = []
    for _ in range(n):
        learner = {
            'Student ID': fake.uuid4(),
            'Age': np.random.randint(18, 40),
            'Gender': np.random.choice(genders),
            'Learning Disabilities': np.random.choice(learning_disabilities),
            'Enrollment Date': fake.date_this_decade(),
            'Subscription Type': np.random.choice(subscription_types),
        }
        learner_data.append(learner)
    return pd.DataFrame(learner_data)

def create_activity_data(learners, n_days):
    activity_data = []
    for student_id in learners['Student ID']:
        total_sessions = np.random.randint(10, 30)  # Simulate sessions per learner
        for _ in range(total_sessions):
            quiz_session = {
                'Student ID': student_id,
                'Quiz Session Date': fake.date_this_year(),
                'Quiz ID': np.random.choice([f"Q{str(i)}" for i in range(1, n_quizzes+1)]),
                'Quiz Topic/Subject': np.random.choice(quiz_topics),
                'Quiz Score': np.random.randint(50, 100),
                'Time Spent on Quiz': np.random.randint(5, 25),
                'Flashcards Used': np.random.choice(['Yes', 'No']),
                'Flashcard Accuracy': np.random.randint(60, 100) if np.random.choice(['Yes', 'No']) == 'Yes' else None,
                'Total Active Sessions (weekly)': np.random.randint(2, 5),
                'Session Duration': np.random.randint(30, 180),
                'Device Used': np.random.choice(devices),
            }
            activity_data.append(quiz_session)
    return pd.DataFrame(activity_data)

def create_outcomes_data(learners):
    outcomes_data = []
    for student_id in learners['Student ID']:
        cumulative_progress = np.random.uniform(40, 85)
        topic_accuracy = {topic: np.random.uniform(50, 90) for topic in quiz_topics}
        outcomes_data.append({
            'Student ID': student_id,
            'Cumulative Learning Progress (%)': cumulative_progress,
            'Retention Rate (weekly)': np.random.uniform(0.5, 0.9),
            'Retention Rate (monthly)': np.random.uniform(0.4, 0.8),
            'Time to Master Key Concepts': np.random.randint(10, 40),
            **topic_accuracy
        })
    return pd.DataFrame(outcomes_data)

def create_feedback_data(learners, n_days):
    feedback_data = []
    for student_id in learners['Student ID']:
        total_feedbacks = np.random.randint(0, 3)  # Each learner could leave multiple feedbacks
        for _ in range(total_feedbacks):
            feedback = {
                'Student ID': student_id,
                'Satisfaction Rating': np.random.randint(1, 6),
                'Feedback Type': np.random.choice(feedback_types),
                'Date of Feedback': fake.date_this_year(),
                'Comments/Sentiment': np.random.choice(sentiment),
            }
            feedback_data.append(feedback)
    return pd.DataFrame(feedback_data)

# Generate learner demographic data
learners = create_learner_data(n_learners)

# Generate activity, outcomes, and feedback data
activity = create_activity_data(learners, n_days)
outcomes = create_outcomes_data(learners)
feedback = create_feedback_data(learners, n_days)

# Combine all dataframes into a single synthetic dataset
learner_data = pd.merge(learners, outcomes, on='Student ID', how='left')
learner_data = pd.merge(learner_data, activity, on='Student ID', how='left')
learner_data = pd.merge(learner_data, feedback, on='Student ID', how='left')

learner_data.to_csv('synthetic_edtech_data.csv', index=False)
print(learner_data.head()) 