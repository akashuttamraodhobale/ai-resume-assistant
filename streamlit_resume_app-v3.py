import os
import google.generativeai as genai
import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Akash Dhobale - AI Resume Assistant",
    page_icon="🛡️",
    layout="centered"
)

# Hardcoded, grounded resume data to ensure the AI doesn't hallucinate
AKASH_RESUME_DATA = """
Candidate Name: Akash Dhobale
Current Target Roles: Technical Program Manager (TPM), Head of Security Assurance, Cybersecurity Director, GRC Lead
Location: India (Open to Remote B2B EMEA / Europe Contracts)
Contact: akashuttamraodhobale@gmail.com | linkedin.com/in/akash-dhobale-cybersecurity

PROFESSIONAL SUMMARY:
Results-driven Enterprise Cybersecurity Leader and Technical Program Manager with 12+ years of progressive success directing complex, large-scale technology transformations and infrastructure programs in the highly regulated banking sector. Designed and deployed a ₹9 Crore ($1.1M+) enterprise security transformation protecting 80,000+ endpoints across 9,000+ branch locations within 15 days with zero business disruption. Highly skilled in Active-Active HA/DR system designs, GRC (NIST CSF, RBI compliance), vendor procurement (RFP, SOW, SLA), multi-million dollar commercial contract negotiations (~60% cost optimization), and high-priority technical escalation triage.

CORE WORK EXPERIENCE:
1. Senior Manager & Branch Head | Canara Bank (July 2026 - Present)
   - Lead overall branch operations, corporate/retail portfolios, and P&L accountability.
   - Enforce robust risk mitigation, audit controls, and regulatory compliance (RBI guidelines).
   - Mentor cross-functional branch teams to elevate service standards.

2. IT Manager - Enterprise Cybersecurity & IT Assets Section Head | Canara Bank (HO, Bengaluru) (April 2020 - July 2026)
   - Spearheaded a ₹9 Crore enterprise cybersecurity rollout protecting 80,000+ endpoints across 9,000+ branches.
   - Executed the complete nationwide security rollout in a record 15 days with zero downtime using rigorous dependency mapping.
   - Engineered and deployed an Active-Active high-availability (HA/DR) architecture bridging Primary DC and DR sites, achieving an RTO of <15 minutes.
   - Authored technical RFPs, Statement of Works (SOWs), and SLA agreements for multi-million dollar vendor selections.
   - Negotiated commercial contracts, achieving ~60% licensing cost optimization without compromising security or operational parameters.
   - Served as the core escalation checkpoint for high-priority technical security incidents, coordinating cross-functional zonal triage.
   - Built automated analytical pipelines and custom VBA reporting engines, reducing weekly administrative data tracking workloads by ~80%.
   - Led asset database compliance audits to ensure absolute data integrity across corporate assets.

3. Officer - Branch Operations & Administration | Canara Bank (July 2014 - March 2020)
   - Managed retail/commercial operations, credit audits, risk assessments, and regulatory reporting.
   - Rotated through administrative portfolios including Human Resources (HRM) and regional procurement.

PUBLICATIONS & THOUGHT LEADERSHIP:
- Industry Article (IFSEC India, August 2026): "The Most Expensive Mistake in Cybersecurity Isn't a Data Breach" - Advocated for people-centric governance, first-principles security, and tight alignment between IT and corporate objectives rather than over-procuring fragmented tools.
- Peer-Reviewed Case Study (IJSCI Journal, July 2026): "Leading Enterprise Cybersecurity Transformation at Scale: A Case Study on Programme Leadership, Enterprise Architecture and Governance."

GLOBAL CERTIFICATIONS:
- Cybersecurity: CISSP Specialization (InfoSec Inst.), CISA Specialization (Coursera), Certified Ethical Hacker (CEH) Specialization (Pearson), ISC2 CC, IIBF Certificate in IT Security.
- Program Management & AI: Google Project Management Professional, Google Cybersecurity Professional & Advanced Risk Management, Google Cloud Generative AI Leader.
- Banking: CAIIB, JAIIB, Certified Customer Service Professional (CCSP).

EDUCATION:
- MBA in IT Management (NMIMS CDOE, 2026 - 2028 Expected)
- B.Tech in Petroleum & Petrochemical Engineering (Laxminarayan Institute of Technology, 2009 - 2013)
"""

# App Header Styling
st.title("🛡️ Akash Dhobale")
st.subheader("AI Executive Resume Assistant")
st.write(
    "Welcome! This interactive assistant is powered by the Google Gemini API "
    "and trained directly on my professional background. Feel free to interview me!"
)

# Sidebar with Credentials Quick View
st.sidebar.markdown("### 🏅 Verified Credentials")
st.sidebar.markdown("**Globally Recognized Certifications:**")
st.sidebar.markdown("- **CISSP** (Specialization)")
st.sidebar.markdown("- **CISA** (Specialization)")
st.sidebar.markdown("- **CEH** (Specialization)")
st.sidebar.markdown("- **Google PM Professional**")
st.sidebar.markdown("- **Google Cybersecurity Professional**")
st.sidebar.markdown("- **Google GenAI Leader (GCP)**")

st.sidebar.markdown("---")
st.sidebar.markdown("### 📰 Recent Thought Leadership")
st.sidebar.markdown(
    "[Read on IFSEC India: 'The Most Expensive Mistake in Cybersecurity Isn't a Data Breach'](https://ifsecindia.com/the-most-expensive-mistake-in-cybersecurity-isnt-a-data-breach)"
)

# Handle API Key Safely
api_key = os.environ.get("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY", "")

if not api_key:
    st.info("💡 To chat, please provide a Google Gemini API Key. (You can get a free key from Google AI Studio).", icon="🔑")
    user_key = st.text_input("Enter your Gemini API Key:", type="password")
    if user_key:
        api_key = user_key

if api_key:
    genai.configure(api_key=api_key)
    
    # Custom system prompt to guide the AI persona
    system_instruction = (
        "You are 'Akash Dhobale\\'s AI Executive Assistant'. Your purpose is to represent Akash professionally "
        "to recruiters, hiring managers, and prospective business partners. Your responses must be entirely "
        "grounded in his provided resume and background. Never make up facts, certifications, or projects. "
        "Adopt a professional, executive, confident, yet humble tone. Always cite metrics when applicable "
        "(e.g., ₹9 Crore budget, 80,000+ endpoints, 15-day deployment, ~60% cost savings, <15 min RTO). "
        "Highlight his thought leadership published on IFSEC India and his strategic balance of GRC with technical execution.\\n\\n"
        f"Here is Akash\\'s official career history and metadata:\\n{AKASH_RESUME_DATA}"
    )

    # Initialize Chat Session
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
        
    # Display previous chat messages
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if user_query := st.chat_input("Ask about my experience, certifications, or project impact..."):
        # Display user message
        with st.chat_message("user"):
            st.markdown(user_query)
        st.session_state.chat_history.append({"role": "user", "content": user_query})

        # Generate Response using Gemini 3.8 Flash (Latest 2026 Model)
        try:
            model = genai.GenerativeModel(
                model_name="gemini-3.8-flash",
                system_instruction=system_instruction
            )
            
            response = model.generate_content(user_query)
            response_text = response.text

            # Display assistant response
            with st.chat_message("assistant"):
                st.markdown(response_text)
            st.session_state.chat_history.append({"role": "assistant", "content": response_text})

        except Exception as e:
            st.error(f"Error generating response: {e}")
else:
    st.warning("Please enter your Gemini API Key to enable the chat interface.")
