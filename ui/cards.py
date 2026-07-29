import streamlit as st


# ---------------------------------------------------------
# HERO SECTION
# ---------------------------------------------------------

def hero():

    st.markdown(
        """
<div class="hero">

<div class="hero-title">
🧠 ResearchGapAI
</div>

<div class="hero-sub">

Multi-Agent AI Platform for discovering
research gaps and generating publication-worthy
research ideas.

</div>

</div>
""",
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------
# TOP METRICS
# ---------------------------------------------------------

def metrics(papers, ideas):

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.markdown(
            """
<div class="metric-card">

<div class="metric-value">
3
</div>

<div class="metric-label">
Papers Analysed
</div>

</div>
""",
            unsafe_allow_html=True,
        )

    with c2:

        st.markdown(
            f"""
<div class="metric-card">

<div class="metric-value">
{len(ideas)}
</div>

<div class="metric-label">
Project Ideas
</div>

</div>
""",
            unsafe_allow_html=True,
        )

    with c3:

        st.markdown(
            """
<div class="metric-card">

<div class="metric-value">
5
</div>

<div class="metric-label">
Research Gaps
</div>

</div>
""",
            unsafe_allow_html=True,
        )

    with c4:

        st.markdown(
            """
<div class="metric-card">

<div class="metric-value">
AI
</div>

<div class="metric-label">
Powered
</div>

</div>
""",
            unsafe_allow_html=True,
        )


# ---------------------------------------------------------
# PAPER CARD
# ---------------------------------------------------------

def paper_card(paper):

    st.markdown(
        f"""
<div class="paper-card">

### 📄 {paper["title"]}

**Source:** {paper.get("source","Unknown")}

**Year:** {paper.get("year","-")}

**Citations:** {paper.get("citations",0)}

</div>
""",
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------
# GAP CARD
# ---------------------------------------------------------

def gap_card(title, text):

    st.markdown(
        f"""
<div class="gap-card">

### 🔍 {title}

{text}

</div>
""",
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------
# PROJECT CARD
# ---------------------------------------------------------

def project_card(project):

    st.markdown(
        f"""
<div class="project-card">

## 🚀 {project.get("title","Project")}

### 🎯 Problem

{project.get("problem_solved","")}

---

### ✨ Novelty

{project.get("novelty","")}

---

### 📂 Dataset

{project.get("suggested_dataset","")}

---

### ⚙ Tech Stack

{project.get("tech_stack","")}

</div>
""",
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Difficulty",
        project.get("difficulty", "-"),
    )

    c2.metric(
        "Resume Impact",
        project.get(
            "resume_impact_score",
            "-",
        ),
    )

    c3.metric(
        "Research Potential",
        project.get(
            "research_potential_score",
            "-",
        ), 
    )


# ---------------------------------------------------------
# RANK CARD
# ---------------------------------------------------------

def ranking_card(rank, score, title):

    st.markdown(
        f"""
<div class="rank-card">

## 🏆 Rank {rank}

### {title}

### ⭐ Score : {score}/100

</div>
""",
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------
# DOWNLOAD CARD
# ---------------------------------------------------------

def report_card():

    st.success("🎉 Everything generated successfully!")

    st.markdown(
        """
### 📥 Generated Files

✅ report.pdf

✅ report.md

✅ report.json

These files are saved inside the **report/** folder.
"""
    ) 