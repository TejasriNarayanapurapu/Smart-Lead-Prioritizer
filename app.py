import streamlit as st
import pandas as pd

# Set up the Streamlit app
st.set_page_config(page_title="Smart Lead Prioritizer", layout="wide")
st.title("🚀 Smart Lead Prioritizer")
st.markdown("Upload your B2B leads CSV and get instant prioritization insights.")

# Upload CSV
uploaded_file = st.file_uploader("Upload Lead CSV", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Preprocess: Fill NA for safety
    df.fillna("", inplace=True)

    # Define scoring logic
    def score_lead(row):
        score = 0
        if "@" in row["email"]: score += 2
        if "linkedin.com" in row["linkedin"]: score += 2
        if any(kw in row["company"].lower() for kw in ["ai", "ml", "saas"]): score += 2
        if row["website"]: score += 1
        if row["linkedin"]: score += 1
        return score

    # Apply scoring
    df["score"] = df.apply(score_lead, axis=1)

    # Sort and show
    df_sorted = df.sort_values(by="score", ascending=False)
    st.success(f"Top {len(df_sorted)} leads prioritized by score.")
    st.dataframe(df_sorted)

    # Download option
    csv = df_sorted.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download Scored Leads CSV",
        data=csv,
        file_name="prioritized_leads.csv",
        mime="text/csv",
    )
else:
    st.info("👆 Upload a CSV with columns like: `email`, `linkedin`, `company`, `website`.")

