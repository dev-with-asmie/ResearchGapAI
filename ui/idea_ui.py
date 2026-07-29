import streamlit as st


def show_ideas(projects):

    st.header("💡 AI Generated Project Ideas")

    st.markdown(
        """
Based on the discovered research gaps, the AI proposes innovative research projects.
"""
    )

    if not projects:
        st.info("No project ideas generated.")
        return

    for i, project in enumerate(projects, start=1):

        st.markdown("---")

        st.subheader(f"🚀 Project {i}")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Difficulty",
                project.get("difficulty", "-")
            )

        with col2:
            st.metric(
                "Resume Impact",
                project.get("resume_impact_score", "-")
            )

        with col3:
            st.metric(
                "Research Potential",
                project.get("research_potential_score", "-")
            )

        st.markdown("### 🎯 Problem Solved")
        st.write(project.get("problem_solved", "-"))

        st.markdown("### ✨ Novelty")
        st.write(project.get("novelty", "-"))

        st.markdown("### 📂 Suggested Dataset")
        st.write(project.get("suggested_dataset", "-"))

        st.markdown("### ⚙ Tech Stack")
        st.write(project.get("tech_stack", "-")) 