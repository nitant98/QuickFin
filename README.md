# QuickFin: An Innovative Financial Document Analysis Chatbot

## Overview

QuickFin is a powerful, AI-driven financial document analysis tool that leverages Retrieval-Augmented Generation (RAG) to extract and summarize key information from complex financial reports such as 10-K and 10-Q filings. By integrating document retrieval with advanced language models, QuickFin provides users with concise and accurate responses to financial queries.

## Features

- **Document Retrieval:** Efficiently fetches and processes financial documents from the SEC EDGAR database.
- **Text Processing:** Cleans and splits large documents into manageable chunks for efficient analysis.
- **Embeddings and Vector Store:** Converts text chunks into embeddings and stores them in a vector database for quick retrieval.
- **RAG System:** Combines document retrieval with generative AI to provide contextually relevant answers.
- **User Interface:** Intuitive Streamlit interface for easy interaction with the chatbot.

## Architecture

The architecture of QuickFin is designed to efficiently handle large volumes of financial data, ensuring that users receive accurate and relevant information with minimal effort. The system's components include:

1. **Data Ingestion and Processing**
2. **Text Chunking and Embedding**
3. **Vector Store for Efficient Retrieval**
4. **Query Handling via a QA Chain**
5. **Response Generation with GPT-3.5-turbo**

For a detailed explanation of the architecture, refer to the `QuickFin_Final_Report.pdf`.

## How to Run

#### 1. Clone the Repository:
```bash
clone https://github.com/nitant98/QuickFin
```

#### 2. Install Dependencies:
```bash
pip install -r requirements.txt
```

#### 3. Run the Streamlit App:
```bash
streamlit run app.py
```

#### 4. Access the Streamlit Dashboard: Open a web browser and navigate to http://localhost:8501 to interact with the financial data analysis dashboard.

#### 5. Run Evaluation
```bash
python eval.py
```
![Pdf1](https://github.com/user-attachments/assets/3982f870-ec3b-4da6-bb57-1b2ed9feb608)

![pdf2](https://github.com/user-attachments/assets/81a68209-5260-4312-b1b3-a002f1fee49f)


## Insights
1. **Revenue Growth Trends:** Understand the revenue growth trajectory of the analyzed company over the specified period.
2. **Net Income Fluctuations:** Analyze the fluctuations in net income to gauge profitability trends.
3. **Total Assets and Liabilities:** Visualize changes in total assets and liabilities to assess financial stability.

## Summary
The architecture of QuickFin is designed to optimize the process of analyzing and extracting relevant information from large financial documents. By integrating document retrieval with advanced generative AI, the system provides users with reliable, contextually accurate answers, 
making it a powerful tool for financial analysis. 

## Contact Us
Github - https://github.com/nitant98
LinkedIn - https://www.linkedin.com/in/nitantjatale/
