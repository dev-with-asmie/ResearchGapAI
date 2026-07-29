#  ResearchGapAI

An AI-powered Multi-Agent Research Discovery Platform that automates research paper discovery, analysis, research gap detection, project idea generation, project ranking, and report generation.

---

##  Features

-  Search research papers from arXiv
-  Search papers from Semantic Scholar
-  AI-powered paper analysis using Google Gemini
-  Automatic research gap detection
-  AI-generated research project ideas
-  Project ranking based on feasibility and impact
-  Research publication trend visualization
-  Export reports as PDF, Markdown, and JSON
-  Interactive Streamlit dashboard

---

##  Tech Stack

- Python
- Streamlit
- Google Gemini API
- arXiv API
- Semantic Scholar API
- FPDF
- JSON
- REST APIs

---

##  Project Structure

```text
ResearchGapAI/
│
├── agents/
├── services/
├── ui/
├── utils/
├── parsers/
├── report/
├── streamlit_app.py
├── requirements.txt
└── README.md
```

---

##  Installation

Clone the repository

```bash
git clone <repository-url>
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application

```bash
streamlit run streamlit_app.py
```

---


##  Future Enhancements

- User authentication
- Research history
- Save previous searches 
- Paper bookmarking
- Citation graph visualization
- Multi-LLM support
- Cloud deployment

---

## Author

**Asmita Chakraborty** 