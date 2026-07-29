import time
import streamlit as st

from agents.paper_search_agent import PaperSearchAgent
from agents.paper_analysis_agent import PaperAnalysisAgent
from agents.research_gap_agent import ResearchGapAgent
from agents.local_gap_generator import LocalGapGenerator
from agents.idea_generator_agent import IdeaGeneratorAgent
from agents.project_ranking_agent import ProjectRankingAgent
from ui.charts import show_research_trends 

from parsers.idea_parser import IdeaParser

from utils.save_json import save_json
from utils.save_report import save_report

from ui.export_ui import show_export_section

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="ResearchGapAI",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

html, body, [class*="css"]{
    font-family:'Segoe UI',sans-serif;
}

.stApp{
    background:#0B1220;
}

/* Hide Streamlit */

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

/* Hero */

.hero{

padding:45px;

border-radius:25px;

background:linear-gradient(135deg,#101C36,#172B4D);

border:1px solid #263A5A;

box-shadow:0 10px 35px rgba(0,0,0,.35);

margin-bottom:30px;

}

.hero h1{

font-size:40px;

color:white;

font-weight:700;

margin-bottom:8px;

}

.hero p{

color:#C9D3E0;
font-size:16px;
line-height:1.6;

}

/* Metric Cards */

.metric{

background:#131F36;

padding:18px;

border-radius:18px;

text-align:center;

border:1px solid #223554;

transition:.3s;

}

.metric:hover{

transform:translateY(-5px);

}

.metric h2{

color:#00E6A7;

font-size:28px;

margin-bottom:5px;

}

.metric p{

color:#C4CCD8;

font-size:14px;

}

.stButton > button{

    background: linear-gradient(135deg,#6D28D9,#7C3AED);

    color:white;

    height:52px;
    width:100%;

    border:none;
    border-radius:14px;

    font-size:17px;
    font-weight:700;

    transition:all .35s ease;

    box-shadow:0 10px 25px rgba(109,40,217,.35);
}

.stButton > button:hover{

    background: linear-gradient(135deg,#7C3AED,#8B5CF6);

    transform:translateY(-4px);

    box-shadow:0 18px 35px rgba(109,40,217,.55);

    cursor:pointer;
}

.stButton > button:active{

    transform:scale(.97);
}

/* Download */

.stDownloadButton>button{

background:#2962FF;

color:white;

border-radius:12px;

height:50px;

width:100%;

}

/* Expander */

.streamlit-expanderHeader{

font-size:16px;

font-weight:700;

}

/* Tabs */

button[data-baseweb="tab"]{

font-size:14px;

font-weight:600;

}

/* Success */

.stSuccess{

border-radius:12px;

}

/* Info */

.stInfo{

border-radius:12px;

}

</style>

""", unsafe_allow_html=True)

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.title("ResearchGapAI")

    st.markdown("---")

    st.subheader("Workflow")

    st.success("Search Papers")

    st.success("Analyze Papers")

    st.success("Detect Research Gaps")

    st.success("Generate Ideas")

    st.success("Rank Projects")

    st.success("Export Report")

    st.markdown("---")

    st.subheader("AI Stack")

    st.write("arXiv")

    st.write("Semantic Scholar")

    st.write("Gemini")

    st.write("Python")

    st.markdown("---")

    st.info("""

Multi-Agent AI Platform

• Paper Search Agent

• Paper Analysis Agent

• Gap Detection Agent

• Idea Generation Agent

• Ranking Agent

""")

    st.markdown("---")

    st.caption("Built by Asmita Chakraborty")

# ==========================================================
# HERO
# ==========================================================

st.markdown("""

<div class="hero">

<h1>ResearchGapAI</h1>

<p>

Autonomous Multi-Agent Research Discovery Platform

</p>

<p>

Discover research gaps, generate innovative research ideas,

rank projects automatically and export beautiful reports.

</p>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# METRICS
# ==========================================================

m1,m2,m3,m4 = st.columns(4)

with m1:

    st.markdown("""

<div class="metric">

<h2>10+</h2>

<p>Papers</p>

</div>

""", unsafe_allow_html=True)

with m2:

    st.markdown("""

<div class="metric">

<h2>AI</h2>

<p>Analysis</p>

</div>

""", unsafe_allow_html=True)

with m3:

    st.markdown("""

<div class="metric">

<h2>5</h2>

<p>Research Ideas</p>

</div>

""", unsafe_allow_html=True)

with m4:

    st.markdown("""

<div class="metric">

<h2>PDF</h2>

<p>Export</p>

</div>

""", unsafe_allow_html=True)

st.write("")

# ==========================================================
# INPUT
# ==========================================================

topic = st.text_input(

    "🔍 Enter Research Topic",

    placeholder="Example: Quantum Intrusion Detection"

)

generate = st.button("Generate Research Report") 
if generate:

    # ==========================================================
    # VALIDATION
    # ==========================================================

    if topic.strip() == "":
        st.warning("⚠ Please enter a research topic.")
        st.stop()

    # ==========================================================
    # INITIALIZE AGENTS
    # ==========================================================

    search_agent = PaperSearchAgent()
    analysis_agent = PaperAnalysisAgent()
    gap_agent = ResearchGapAgent()
    local_gap_agent = LocalGapGenerator()
    idea_agent = IdeaGeneratorAgent()
    ranking_agent = ProjectRankingAgent()
    parser = IdeaParser()

    # ==========================================================
    # PROGRESS BAR
    # ==========================================================

    progress = st.progress(0)

    status = st.empty()

    # ==========================================================
# SEARCH PAPERS
# ==========================================================

    status.info("Searching research papers...")

    papers = search_agent.search(topic)

    progress.progress(10)

    if len(papers) == 0:
        st.error("No papers found.")
        st.stop()

    all_analysis = ""

# ==========================================================
# CREATE TABS
# ==========================================================

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        [
            "Papers",
            "Research Gaps",
            "Project Ideas",
            "Ranking",
            "Export"
        ]
    )

# ==========================================================
# TAB 1 : PAPERS
# ==========================================================

    with tab1:

        st.header("Top Research Papers")

        st.caption(
            "The AI searched multiple academic databases and selected the most relevant papers."
        )

        for index, paper in enumerate(papers[:3]):

            status.info(
                f" AI is analyzing paper {index+1}..."
            )

            progress.progress(
                20 + index * 15
            )

            with st.expander(
                f" {paper['title']}",
                expanded=(index == 0)
            ):

                col1, col2, col3 = st.columns(3)

                with col1:

                    st.metric(
                        "Source",
                        paper.get("source", "-")
                    )

                with col2:

                    st.metric(
                        "Year",
                        paper.get("year", "-")
                    )

                with col3:

                    st.metric(
                        "Citations",
                        paper.get("citations", 0)
                    )

                st.markdown("### Abstract")

                st.write(
                    paper.get("summary", "")
                )

                with st.spinner(
                    "Analyzing paper..."
                ):

                    analysis = analysis_agent.analyze(
                        paper.get("summary", "")
                    )

                st.markdown("### AI Analysis")

                if isinstance(analysis, dict):

                    st.success("Main Problem")

                    st.write(
                        analysis.get(
                            "main_problem",
                            "-"
                        )
                    )

                    st.info("Methodology")

                    st.write(
                        analysis.get(
                            "methodology",
                            "-"
                        )
                    )

                    st.success("Key Contribution")

                    st.write(
                        analysis.get(
                            "key_contribution",
                            "-"
                        )
                    )

                    st.warning("Limitations")

                    limitations = analysis.get(
                        "limitations",
                        []
                    )

                    if isinstance(
                        limitations,
                        list
                    ):

                        for item in limitations:

                            st.write("•", item)

                    else:

                        st.write(limitations)

                    st.info("Future Research")

                    future = analysis.get(
                        "future_research",
                        []
                    )

                    if isinstance(
                        future,
                        list
                    ):

                        for item in future:

                            st.write("•", item)

                    else:

                        st.write(future)

                else:

                    st.write(analysis)

                all_analysis += f"""

    TITLE:
    {paper['title']}

    {analysis}

    """

                st.divider()

        st.markdown("## Research Publication Trend")

        show_research_trends(papers)

        progress.progress(65)
    # ==========================================================
    # TAB 2 : RESEARCH GAPS
    # ==========================================================

    with tab2:

        status.info("Detecting research gaps...")

        with st.spinner("Analyzing all papers..."):

            gaps = gap_agent.find_gaps(all_analysis)

            if (
                "unavailable" in gaps.lower()
                or "resource_exhausted" in gaps.lower()
                or "gemini unavailable" in gaps.lower()
            ):

                gaps = local_gap_agent.generate(all_analysis)

        progress.progress(80)

        st.header("Research Gaps")

        st.caption(
            "AI combines all paper analyses and automatically identifies recurring limitations, unexplored areas and future research opportunities."
        )

        st.info(gaps)


    # ==========================================================
    # TAB 3 : PROJECT IDEAS
    # ==========================================================

    with tab3:

        status.info("Generating project ideas...")

        with st.spinner("Creating innovative research ideas..."):

            ideas = idea_agent.generate(gaps)

        progress.progress(90)

        st.header("AI Generated Project Ideas")

        st.caption(
            "Based on the discovered research gaps, the AI proposes innovative research projects."
        )

        parsed_projects = parser.parse(ideas)

        save_json(parsed_projects)

        if len(parsed_projects) == 0:

            st.warning("Could not parse structured project details.")

            st.write(ideas)

        else:

            for index, project in enumerate(parsed_projects):

                with st.container(border=True):

                    st.subheader(f"Project {index + 1}")

                    st.markdown(
                        f"## {project.get('title', 'Untitled Project')}"
                    )

                    c1, c2, c3 = st.columns(3)

                    with c1:

                        st.metric(
                            "Difficulty",
                            project.get("difficulty", "-")
                        )

                    with c2:

                        st.metric(
                            "Resume Impact",
                            project.get("resume_impact_score", "-")
                        )

                    with c3:

                        st.metric(
                            "Research Potential",
                            project.get("research_potential_score", "-")
                        )

                    st.markdown("### Problem Solved")

                    st.write(
                        project.get("problem_solved", "-")
                    )

                    st.markdown("### Novelty")

                    st.write(
                        project.get("novelty", "-")
                    )

                    st.markdown("### Suggested Dataset")

                    st.write(
                        project.get("suggested_dataset", "-")
                    )

                    st.markdown("### Recommended Tech Stack")

                    tech_stack = project.get("tech_stack", "-")

                    if isinstance(tech_stack, list):
                        for tech in tech_stack:
                            st.write("•", tech)
                    else:
                        st.write(tech_stack)

                    st.divider()
    # ==========================================================
    # TAB 4 : PROJECT RANKING
    # ==========================================================

    with tab4:

        status.info("Ranking AI generated projects...")

        with st.spinner("Evaluating projects..."):

            ranking = ranking_agent.rank(ideas)

        progress.progress(100)

        st.header("AI Project Ranking")

        st.caption(
            "Projects are ranked based on novelty, feasibility, resume impact and research potential."
        )

        if isinstance(ranking, dict):

            if "ranking" in ranking:

                for item in ranking["ranking"]:

                    with st.container(border=True):

                        left, right = st.columns([1, 5])

                        with left:

                            st.metric(
                                "Rank",
                                item.get("rank", "-")
                            )

                        with right:

                            st.subheader(
                                item.get("title", "Untitled Project")
                            )

                            score = item.get("score", 0)

                            st.progress(score / 100)

                            st.write(
                                f"⭐ Overall Score : **{score}/100**"
                            )

                        st.markdown("### Strengths")

                        for strength in item.get("strengths", []):

                            st.write("•", strength)

                        st.markdown("### Weaknesses")

                        for weakness in item.get("weaknesses", []):

                            st.write("•", weakness)

                        st.divider()

                st.success(" Recommended Project")

                best = ranking.get("best_project", {})

                st.subheader(
                    best.get("title", "-")
                )

                st.write(
                    best.get("reason", "-")
                )

            else:

                st.write(ranking)

        else:

            st.markdown("### AI Evaluation")

            st.write(ranking)


    # ==========================================================
    # SAVE REPORT
    # ==========================================================

    full_report = f"""
    RESEARCH TOPIC

    {topic}

    =====================================================

    PAPER ANALYSIS

    {all_analysis}

    =====================================================

    RESEARCH GAPS

    {gaps}

    =====================================================

    PROJECT IDEAS

    {ideas}

    =====================================================

    PROJECT RANKING

    {ranking}
    """

    save_report(full_report)

    status.success(" Research Report Generated Successfully!")
    st.markdown("""
<style>
.notification {
    position: fixed;
    top: 24px;
    right: 24px;
    width: 360px;
    background: rgba(5, 102, 60, 0.96);
    color: white;
    border-radius: 14px;
    padding: 16px 18px;
    box-shadow: 0 12px 30px rgba(0,0,0,.35);
    backdrop-filter: blur(12px);
    z-index: 99999;
    animation: slideIn 0.45s ease-out, fadeOut 0.5s ease-in 5s forwards;
    border-left: 5px solid #22c55e;
    font-family: "Segoe UI", sans-serif;
}

.notification-title{
    font-size:18px;
    font-weight:700;
    margin-bottom:6px;
}

.notification-text{
    font-size:14px;
    color:#f3f4f6;
    line-height:1.5;
}

@keyframes slideIn{
    from{
        opacity:0;
        transform:translateX(120%);
    }
    to{
        opacity:1;
        transform:translateX(0);
    }
}

@keyframes fadeOut{
    to{
        opacity:0;
        transform:translateX(120%);
        visibility:hidden;
    }
}
</style>

<div class="notification">
    <div class="notification-title">
         Analysis Completed
    </div>
    <div class="notification-text">
        Your research report has been generated successfully.
        All papers, research gaps, project ideas and rankings are ready for review.
    </div>
</div>
""", unsafe_allow_html=True)

    # ==========================================================
    # TAB 5 : EXPORT
    # ==========================================================

    with tab5:

        st.header("Export Report")

        show_export_section()

        st.divider()

        st.subheader("Generated Files")

        st.write("PDF Report")

        st.write("Markdown Report")

        st.write("JSON File")



    st.divider()


    status.empty() 