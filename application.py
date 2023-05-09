virtualimport streamlit as st
import pandas as pd
from content_similarity import sentence_similarity
import time




def main():
    st.set_page_config(page_title="FAQ Similarity Checker", layout="wide", page_icon="🧊")
    # Create a menu to select the option
    st.title("Semantic Search and Sentence Similarity")
    menu = ["Retrieve from DB", "Check Similarity"]
    choice = st.sidebar.selectbox("Select an option", menu)

    if choice == "Retrieve from DB":
        st.title("FAQ Similarity Checker")

        data = None
        uploaded_file = st.file_uploader("Upload FAQ data (CSV or excel file)", type=("xlsx", "csv"))
        if uploaded_file is not None:
            data = pd.read_excel(uploaded_file)

        # Get user input and show results
        if data is not None:
            with st.spinner('Loading data...'):
                time.sleep(3)
                st.subheader("FAQ Data")
            # st.write(data)

            st.subheader("Ask your Query")
            input_question = st.text_input("Enter your question")
            if input_question:
                similarity_scores = []
                for question in data["questions"]:
                    score = sentence_similarity(input_question, question)
                    similarity_scores.append(score)
                max_score = max(similarity_scores)
                print("The max score is:", max_score)
                if max_score >= 50:
                    index = similarity_scores.index(max_score)
                    matching_question = data.iloc[index]["questions"]
                    matching_answer = data.iloc[index]["answers"]
                    st.write("Matching question:", matching_question)
                    st.write("Matching answer:", matching_answer)
                else:
                    st.write("No matching question found")

    else:
        st.title("Sentence Similarity Checker")
        input1 = st.text_input("Enter sentence 1")
        input2 = st.text_input("Enter sentence 2")
        if input1 and input2:
            similarity_score = sentence_similarity(input1, input2)
            st.write("Similarity between two sentences is:", str(similarity_score) + " %")
        else:
            st.write("Please enter two sentences to check their similarity.")

if __name__ == "__main__":
    main()
