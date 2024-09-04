# 📧 Cold Email Generator for Service Companies

Effortlessly craft personalized cold emails for service companies using cutting-edge technologies like **Groq**, **LangChain**, and **Streamlit**.

## How It Works:
Simply provide the URL of a company's careers page, and our tool automatically extracts relevant job listings. Based on these listings, it generates customized cold emails tailored to specific job descriptions. To make the outreach even more impactful, the tool includes relevant portfolio links sourced intelligently from a vector database. 

### Imagine This Scenario:

Nike is looking for a Principal Software Engineer and investing heavily in the hiring process—recruiting, onboarding, training, and more. 

Atliq, a software development company, has the perfect solution. Mohan, a business development executive from Atliq, can offer Nike a dedicated software engineer without the overhead of hiring. To make this offer stand out, he sends a personalized cold email crafted by this tool, highlighting Atliq's relevant portfolio and expertise—all tailored to Nike’s needs.

### Key Features:
- **Automated Job Listing Extraction**: Easily pull job details from a careers page.
- **Tailored Cold Emails**: Generate unique, targeted emails based on job descriptions.
- **Portfolio Integration**: Automatically link relevant work samples from your portfolio database.

## Architecture Diagram
<img width="100%" alt="Screenshot 2024-09-04 212946" src="https://github.com/user-attachments/assets/1449a36f-faae-4f46-9437-6b358a676ee0">


## Setup Instructions:

1. **Get an API Key**: First, obtain an API key from [Groq](https://console.groq.com/keys). 
2. **Configure**: In the `app/.env` file, update the `GROQ_API_KEY` with your API key.
3. **Install Dependencies**: Run the following to install required packages:
   ```bash
   pip install -r requirements.txt
4.**Run the App**: Launch the app by running:
   ```bash
   streamlit run app/main.py
