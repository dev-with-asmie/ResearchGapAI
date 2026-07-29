import streamlit as st


def show_papers(papers, analysis_agent):

    st.header("📚 Research Papers")

    all_analysis = ""

    for i, paper in enumerate(papers[:3]):

        with st.expander(
            f"📄 {paper['title']}",
            expanded=(i == 0)
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

            st.markdown("### 📖 Abstract")

            st.write(
                paper["summary"]
            )

            with st.spinner(
                "🤖 AI is analyzing this paper..."
            ):

                analysis = analysis_agent.analyze(
                    paper["summary"]
                )

            st.markdown("### 🧠 AI Analysis")

            st.json(analysis)

            all_analysis += f"""

TITLE:
{paper['title']}

{analysis}

"""

    return all_analysis 