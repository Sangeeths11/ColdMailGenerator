import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from chains import Chain
from portfolio import Portfolio
from utils import clean_text

def create_streamlit_app(llm, portfolio, clean_text):
    st.title("📧 Cold Email Generator")
    st.subheader("Generate personalized cold emails based on job listings")

    url_input = st.text_input(
        "Enter the Careers Page URL:", 
        value="https://jobs.nike.com/de/job/R-36827", 
        help="Paste the URL of the company's careers page to extract job listings."
    )

    tone = st.selectbox("Select Email Tone", ["Formal", "Casual", "Friendly"], index=0)

    if st.button("Generate Email"):
        with st.spinner('Extracting job listings and generating email...'):
            try:
                loader = WebBaseLoader([url_input])
                page_content = loader.load().pop().page_content
                cleaned_data = clean_text(page_content)

                portfolio.load_portfolio()
                jobs = llm.extract_jobs(cleaned_data)

                st.session_state.jobs = jobs

                if jobs:
                    st.success(f"Found {len(jobs)} job listings!")
                else:
                    st.warning("No job listings were found on the provided page.")
            
            except Exception as e:
                st.error(f"An error occurred while processing the URL: {e}")

    if 'jobs' in st.session_state:
        jobs = st.session_state.jobs

        job_titles = [job.get('role', 'Unknown Position') for job in jobs]

        selected_jobs_titles = st.multiselect(
            "Select the jobs you want to generate emails for:",
            options=job_titles,
            help="Select the jobs for which you'd like to generate cold emails."
        )

        if selected_jobs_titles:
            selected_jobs = [job for job in jobs if job.get('role', 'Unknown Position') in selected_jobs_titles]
            
            for i, job in enumerate(selected_jobs, 1):
                skills = job.get('skills', [])
                if not skills:
                    st.warning(f"No skills found for Job {i}: {job.get('role', 'Unknown Position')}. Email will not be generated.")
                    continue
                else:
                    portfolio_links = portfolio.query_links(skills)

                if not portfolio_links:
                    st.warning(f"No portfolio links available for Job {i}: {job.get('role', 'Unknown Position')}. Email will not be generated.")
                else:
                    email = llm.write_mail(job, portfolio_links, tone=tone)

                    st.markdown(f"### Suggested Email for Job {i}: {job.get('role', 'Unknown Position')}")
                    st.text_area(f"Edit and Copy Email for Job {i}", value=email, height=600)
        else:
            st.warning("No jobs selected for email generation.")

if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()

    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    create_streamlit_app(chain, portfolio, clean_text)
