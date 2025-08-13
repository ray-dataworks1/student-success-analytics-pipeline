# student-success-analytics-pipeline

## Project Purpose
This mini-project demonstrates how I would approach Analytics Engineering at an EdTech firm as the first AE hire.
My goal: build a strategic, scalable data foundation that empowers everyone—product, marketing, and founders—to answer “what happened” and “why” in real time.

###What’s Included
This MVP covers two core needs:

Learning Outcomes & ND Cohorts

Track and compare student progress (quiz scores, retention, engagement) by cohort, with special attention to neurodivergent (ND) learners.

Showcase how analytics can power inclusivity, not just “average” metrics.

Business Metrics as Defined in JD

Sample “active user” metric definition and model.

Foundation for future business-critical metrics: retention, ARPU, quiz accuracy, and more.

### Tech Stack
dbt (Core)

PostgreSQL (simulated warehouse)

Python/CSV for mock data generation

(Optional): Notion/Metabase/Lightdash for dashboards


### Data Models
Example Models:
stg_users – User table with ND status flag, sign-up and activity dates

fct_quiz_events – Simulated quiz/flashcard usage

int_learning_outcomes – Aggregated progress, improvement, and retention by cohort (including ND)

int_active_users – “Active user” conformed metric as per Gizmo’s JD

(Optional: Add retention, NPS, or sentiment marts if time)

### Why This Approach?
Creativity: I’m passionate about understanding how people learn, not just what they click. Tracking ND outcomes is both a personal and strategic differentiator for Gizmo.

Aanalytics Engineering Alignment: I included core business metric definitions (like “active user”) to show I can balance product creativity with concrete business needs.

Foundation for Scale: This stack and model design scales—future A/B tests, feature usage, revenue analytics, or more complex experimentation can all build on top.

###  Demo/Results
Sample queries/charts: average score improvement, ND vs non-ND retention, weekly active users, etc.

For demo purposes, mock data is used to simulate production insights.

### Next Steps 
Expand to cover full revenue and subscription analytics (integrate with RevenueCat).

Add pipeline orchestration (Argo, Airbyte) and event tracking (Posthog).

Instrument real-time user feedback and close the loop with AI-powered BI.

Collaborate cross-functionally to deliver self-serve dashboards and iterate on metrics with all teams.

📝 README Summary
This repo is a living proof-of-concept of how I’d build an actionable, inclusive, and business-aligned analytics platform for Gizmo.
I’m excited by your mission and would love to take this further as your first Analytics Engineer!
