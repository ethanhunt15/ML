import streamlit as st
from rag_pipeline import ingest_document, query_rag
import tempfile
from pdf_parser import extract_text_from_pdf
from summariser import summarise_regulation
from insights import generate_business_insights

st.title("FinAI Analyst: Regulatory Compliance & Business Insights")

uploaded_file = st.file_uploader("Upload a regulatory PDF", type="pdf")

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        pdf_text = extract_text_from_pdf(tmp_file.name)
    
    st.subheader("Extracted Text")
    with st.expander("Show extracted text"):
        st.write(pdf_text[:3000])  # show first 3000 chars

    if st.button("Generate Summary"):
        with st.spinner("Generating summary..."):
            summary = summarise_regulation(pdf_text)
        st.subheader("Regulation Summary")
        st.write(summary)

        with st.spinner("Generating business insights..."):
            insights = generate_business_insights(summary)
        st.subheader("Business Impact & Operational Insights")
        st.write(insights)

st.subheader("RAG Pipeline")

if uploaded_file:
    # if st.button("Ingest into Knowledge Base"):
    #     with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
    #         tmp_file.write(uploaded_file.read())
    #         pdf_text = extract_text_from_pdf(tmp_file.name)
        
        with st.spinner("Ingesting document..."):
            result = ingest_document(pdf_text, metadata={"filename": uploaded_file.name})
        st.success(result)

query = st.text_input("Ask a question from ingested regulations:")
if st.button("Query KB"):
    with st.spinner("Generating answer..."):
        answer = query_rag(query)
    st.subheader("Answer")
    st.write(answer)
