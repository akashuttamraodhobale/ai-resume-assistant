# Interactive AI Resume Assistant (RAG Chatbot)

A live-deployed, responsive web application that turns a professional executive resume into an intelligent, interactive conversational assistant powered by Google Gemini API and Streamlit.

---

## 🎯 Key Features

* **🤖 RAG-Grounded Assistant:** Grounded strictly in professional candidate experience data (12+ years in enterprise cybersecurity, banking transformations, HA/DR design, and GRC compliance) to eliminate AI hallucinations.
* **⚡ Interactive Recruiter Chat:** Enables hiring managers, recruiters, and technical interviewers to converse directly with the candidate's professional profile in real time.
* **🛡️ Built-in Security & Fallbacks:** Includes API key verification, error handling, and pre-prompt guardrails.
* **📱 Responsive Streamlit UI:** Clean, modern interface designed for mobile and desktop browsing.

---

## 📁 Repository Structure

```directory
.
├── streamlit_resume_app.py  # Core Streamlit web application & Gemini API logic
├── requirements.txt         # Python package dependencies
└── README.md                # Project documentation
```

---

## 🚀 Installation & Rapid Deployment

### 1. Clone the Repository
```bash
git clone https://github.com/akashuttamraodhobale/ai-resume-assistant.git
cd ai-resume-assistant
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Your Gemini API Key
Obtain a free API key from [Google AI Studio](https://aistudio.google.com/) and set it as an environment variable or inside Streamlit Secrets:

```bash
export GEMINI_API_KEY="your-gemini-api-key-here"
```

### 4. Run the Web Application
```bash
streamlit run streamlit_resume_app.py
```

---

## ⚙️ Deployment Options

### Deploying on Streamlit Community Cloud (Free)
1. Push this repository to your GitHub account.
2. Sign in to [share.streamlit.io](https://share.streamlit.io/).
3. Click **New app**, select `ai-resume-assistant` repository, and set main file path to `streamlit_resume_app.py`.
4. In **Advanced Settings** -> **Secrets**, add your API key:
   ```toml
   GEMINI_API_KEY = "your-api-key-here"
   ```
5. Click **Deploy**!
