import streamlit as st
from main import analyze_data, generate_recommendations, visualize_insights
import pandas as pd

def main():
    st.title("Students Performance Analysis")
    st.write("Upload a CSV file to analyze students' performance in exams.")

    # File uploader for CSV
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

    if uploaded_file is not None:
        try:
            # Load the dataset
            current_quiz = pd.read_csv(uploaded_file)

            # Analyze data
            insights = analyze_data(current_quiz)

            # Generate recommendations
            recommendations = generate_recommendations(insights)

            # Display insights
            st.subheader("Insights")
            st.json(insights)

            # Display recommendations
            st.subheader("Recommendations")
            for rec in recommendations:
                st.write(f"- {rec}")

            # Visualize insights
            st.subheader("Visualizations")
            visualize_insights(current_quiz)  # Directly call the updated function
            
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
