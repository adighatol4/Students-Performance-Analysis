import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st  # Import Streamlit

# Analyze Data
def analyze_data(current_quiz):
    """Analyze performance and generate insights."""
    insights = {}

    # Analyze based on gender and parental education
    gender_perf = current_quiz.groupby('gender')[['math score', 'reading score', 'writing score']].mean()
    insights['Gender Performance'] = gender_perf.to_dict()

    parental_edu_perf = current_quiz.groupby('parental level of education')[['math score', 'reading score', 'writing score']].mean()
    insights['Parental Education Performance'] = parental_edu_perf.to_dict()

    return insights

# Generate Recommendations
def generate_recommendations(insights):
    """Create actionable steps based on insights."""
    recommendations = []

    # Recommendations based on gender performance
    gender_perf = insights['Gender Performance']
    for gender, scores in gender_perf.items():
        low_score_subject = min(scores, key=scores.get)
        recommendations.append(f"Students identifying as {gender} may benefit from focusing on improving {low_score_subject} scores.")

    # Recommendations based on parental education
    parental_edu_perf = insights['Parental Education Performance']
    for level, scores in parental_edu_perf.items():
        low_score_subject = min(scores, key=scores.get)
        recommendations.append(f"Students whose parents have a {level} education level may benefit from extra resources in {low_score_subject}.")

    return recommendations

# Visualize Insights
def visualize_insights(current_quiz):
    """Create visualizations for insights."""
    # Gender-based performance
    gender_perf = current_quiz.groupby('gender')[['math score', 'reading score', 'writing score']].mean()
    fig, ax = plt.subplots()
    gender_perf.plot(kind='bar', title='Performance by Gender', ax=ax)
    st.pyplot(fig)  # Pass the figure object to Streamlit

    # Parental education level performance
    parental_edu_perf = current_quiz.groupby('parental level of education')[['math score', 'reading score', 'writing score']].mean()
    fig, ax = plt.subplots()
    parental_edu_perf.plot(kind='bar', title='Performance by Parental Education Level', ax=ax)
    ax.set_xlabel('Parental Education Level')
    ax.set_ylabel('Average Scores')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(fig)  # Pass the figure object to Streamlit
