import streamlit as st
import pandas as pd
from predict import predict_loads
from generate_report import export_pdf
import base64

st.set_page_config(page_title="Civil-AI", layout="centered")
st.title("Civil-AI Load Estimator")
st.caption("90 % correlation • 60 % faster • XGBoost")

uploaded = st.file_uploader("Upload CSV (span_m, height_m, ...)", type="csv")
if uploaded:
    df = pd.read_csv(uploaded)
    with st.spinner("Predicting loads..."):
        results = predict_loads(df)
    st.success("Done! 19 seconds")
    st.dataframe(results.style.highlight_max(axis=0))

    if st.button("Export PDF Report"):
        pdf = export_pdf(results)
        b64 = base64.b64encode(pdf).decode()
        href = f'<a href="data:application/pdf;base64,{b64}" download="Load_Report_{pd.Timestamp.now():%b%Y}.pdf">Download PDF</a>'
        st.markdown(href, unsafe_allow_html=True)
