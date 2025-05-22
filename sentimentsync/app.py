#Libraries
import streamlit as st
import pandas as pd
from sklearn.metrics import confusion_matrix, jaccard_score
from scipy.stats import pearsonr, spearmanr, kendalltau
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
import time

from modules import gemini_sentiment, textblob_sentiment, vader_sentiment

# Streamlit UI
st.set_page_config(page_title="SentimentSync", layout="wide")
st.title("SentimentSync: Compare Sentiment Analysis Methods")

# Brief Description
st.markdown("""
**SentimentSync** is a powerful benchmarking tool that lets you compare the performance and agreement of popular sentiment analysis methods—**VADER**, **TextBlob**, and **Gemini** —on your own text inputs.  
Analyze sentence-level sentiments, visualize intensity scores, explore pairwise correlations and agreement rates, and dive deep into confusion matrices and benchmarking metrics.  
Ideal for data scientists, NLP practitioners, and anyone evaluating sentiment AI!
""")

# Input Section
texts = []


text_input = st.text_area("Enter text (one sentence per line)", height=200)
texts = [line.strip() for line in text_input.strip().split('\n') if line.strip()]

methods = st.sidebar.multiselect("Select methods to compare", ["VADER", "TextBlob", "Gemini"])
# Gemini API Key and Model Selection
if "Gemini" in methods:
    gemini_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

    gemini_models = ["gemini-1.5-flash", "gemini-pro", "gemini-1.5-pro-latest", "gemini-vision", "Other"]
    selected_gemini_model = st.sidebar.selectbox("Select Gemini Model", gemini_models)

    if selected_gemini_model == "Other":
        custom_model = st.sidebar.text_input("Enter custom Gemini model name")
        gemini_model = custom_model
    else:
        gemini_model = selected_gemini_model
else:
    gemini_key = None
    gemini_model = None

# Analyze Button
if st.sidebar.button("Analyze"):
    if not texts:
        st.error("Please enter or upload at least one sentence.")
    elif not methods:
        st.error("Please select at least one method.")
    else:
        results = []
        timings = {"Method": [], "Sentence #": [], "Execution Time (s)": []}
        batch_start = time.perf_counter()

        # Validate Gemini once before main analysis
        gemini_valid = True
        if "Gemini" in methods:
            try:
                # A test call with dummy text to validate API key & model
                gemini_sentiment.get_gemini_sentiment("test validation text", gemini_key, gemini_model)
            except Exception as e:
                st.error(f"Gemini setup error: {e}")
                gemini_valid = False
                # Remove Gemini from methods to skip it entirely in later processing
                methods.remove("Gemini")

        for idx, text in enumerate(texts):
            row = {"Text": text}

            if "VADER" in methods:
                start = time.perf_counter()
                s, i = vader_sentiment.get_vader_sentiment(text)
                elapsed = time.perf_counter() - start
                row.update({"VADER_Sentiment": s, "VADER_Intensity": i})
                timings["Method"].append("VADER")
                timings["Sentence #"].append(idx + 1)
                timings["Execution Time (s)"].append(elapsed)


            if "TextBlob" in methods:
                start = time.perf_counter()
                s, i = textblob_sentiment.get_textblob_sentiment(text)
                elapsed = time.perf_counter() - start
                row.update({"TextBlob_Sentiment": s, "TextBlob_Intensity": i})
                timings["Method"].append("TextBlob")
                timings["Sentence #"].append(idx + 1)
                timings["Execution Time (s)"].append(elapsed)

            if "Gemini" in methods and gemini_valid:
                try:
                    start = time.perf_counter()
                    s, i = gemini_sentiment.get_gemini_sentiment(text, gemini_key, gemini_model)
                    elapsed = time.perf_counter() - start
                    row.update({"Gemini_Sentiment": s, "Gemini_Intensity": i})
                    timings["Method"].append("Gemini")
                    timings["Sentence #"].append(idx + 1)
                    timings["Execution Time (s)"].append(elapsed)
                except Exception as e:
                    st.error(f"Error during Gemini analysis on sentence #{idx+1}: {e}")
                    row.update({"Gemini_Sentiment": "ERROR", "Gemini_Intensity": 0.0})


            results.append(row)

        batch_end = time.perf_counter()

        if results:
            df = pd.DataFrame(results)
            st.subheader("Analysis Result")
            st.dataframe(df, use_container_width=True)

            sentiment_cols = [col for col in df.columns if "Sentiment" in col and col != "Text"]
            intensity_cols = [col for col in df.columns if "Intensity" in col]

            # Benchmark Results
            timing_df = pd.DataFrame(timings)
            st.subheader("Performance Benchmarking")
            col1, col2 = st.columns(2)
            col1.metric("Batch Processing Time (s)", f"{batch_end - batch_start:.3f}")
            col2.metric("Average Time per Sentence", f"{timing_df['Execution Time (s)'].mean():.3f}")
            st.dataframe(timing_df, use_container_width=True)

            if len(methods) > 1:
                df["Agreement"] = df[sentiment_cols].nunique(axis=1) == 1
                agreement_percent = df["Agreement"].mean() * 100
                st.metric("Agreement Percentage", f"{agreement_percent:.2f}%")

                # Pairwise Agreement Percentage
                st.subheader("Pairwise Agreement Percentage (Sentiment Labels)")
                agreement_data = []

                for i in range(len(sentiment_cols)):
                    for j in range(i + 1, len(sentiment_cols)):
                        col1, col2 = sentiment_cols[i], sentiment_cols[j]
                        total = len(df)
                        matches = (df[col1] == df[col2]).sum()
                        percent = round((matches / total) * 100, 2)
                        agreement_data.append((col1, col2, f"{percent}%"))

                st.dataframe(pd.DataFrame(agreement_data, columns=["Method 1", "Method 2", "Agreement %"]), use_container_width=True)


                # Correlation Section
                st.subheader("Pairwise Correlations (Intensity)")
                corr_types = ["Pearson", "Spearman", "Kendall"]
                corr_df_all = []

                for corr_type in corr_types:
                    for i in range(len(intensity_cols)):
                        for j in range(i + 1, len(intensity_cols)):
                            col1, col2 = intensity_cols[i], intensity_cols[j]
                            try:
                                if corr_type == "Pearson":
                                    corr, _ = pearsonr(df[col1], df[col2])
                                elif corr_type == "Spearman":
                                    corr, _ = spearmanr(df[col1], df[col2])
                                else:
                                    corr, _ = kendalltau(df[col1], df[col2])
                                corr_df_all.append((corr_type, col1, col2, round(corr, 3)))
                            except:
                                corr_df_all.append((corr_type, col1, col2, "N/A"))

                st.dataframe(pd.DataFrame(corr_df_all, columns=["Type", "Method 1", "Method 2", "Correlation"]), use_container_width=True)

                # Jaccard Index
                st.subheader("Jaccard Index (Sentiment Labels)")
                jaccard_results = []
                for i in range(len(sentiment_cols)):
                    for j in range(i + 1, len(sentiment_cols)):
                        a = df[sentiment_cols[i]]
                        b = df[sentiment_cols[j]]
                        score = jaccard_score(a, b, average="macro", labels=["POSITIVE", "NEGATIVE", "NEUTRAL"])
                        jaccard_results.append((sentiment_cols[i], sentiment_cols[j], round(score, 3)))

                st.dataframe(pd.DataFrame(jaccard_results, columns=["Method 1", "Method 2", "Jaccard Index"]), use_container_width=True)

                # Intensity Bar Plot
                st.subheader("Bar Plot of Mean Intensities")
                bar_df = df[intensity_cols].mean().reset_index()
                bar_df.columns = ["Method", "Mean Intensity"]
                fig_bar = go.Figure([go.Bar(x=bar_df["Method"], y=bar_df["Mean Intensity"])])
                st.plotly_chart(fig_bar, use_container_width=True)

                # Radar Chart
                st.subheader("Radar Chart - Intensity Distribution")
                radar_fig = go.Figure()
                for i, row in df.iterrows():
                    radar_fig.add_trace(go.Scatterpolar(
                        r=[row[col] for col in intensity_cols],
                        theta=intensity_cols,
                        fill='toself',
                        name=f"Text {i+1}"
                    ))
                radar_fig.update_layout(polar=dict(radialaxis=dict(visible=True)), showlegend=True)
                st.plotly_chart(radar_fig, use_container_width=True)

                # Confusion Matrices
                st.subheader("Confusion Matrix (Pairwise)")
                labels = ["POSITIVE", "NEUTRAL", "NEGATIVE"]
                for i in range(len(sentiment_cols)):
                    for j in range(i + 1, len(sentiment_cols)):
                        y_true = df[sentiment_cols[i]]
                        y_pred = df[sentiment_cols[j]]
                        cm = confusion_matrix(y_true, y_pred, labels=labels)
                        fig_cm, ax = plt.subplots()
                        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=labels, yticklabels=labels, ax=ax)
                        ax.set_xlabel('Predicted')
                        ax.set_ylabel('Actual')
                        ax.set_title(f"{sentiment_cols[i]} vs {sentiment_cols[j]}")
                        st.pyplot(fig_cm)

            else:
                st.info("Only one method selected. Comparison not applicable.")
