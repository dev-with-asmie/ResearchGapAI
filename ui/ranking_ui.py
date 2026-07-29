import streamlit as st


def show_ranking(ranking):

    st.header("🏆 AI Project Ranking")

    st.caption("AI Evaluation")

    # -----------------------------
    # Ranking returned as dictionary
    # -----------------------------
    if isinstance(ranking, dict):

        if "ranking" in ranking:

            for project in ranking["ranking"]:

                st.markdown("---")

                col1, col2 = st.columns([1, 5])

                with col1:
                    st.metric(
                        "Rank",
                        project["rank"]
                    )

                with col2:

                    st.subheader(project["title"])

                    st.progress(project["score"] / 100)

                    st.write(
                        f"**Overall Score:** {project['score']}/100"
                    )

                st.markdown("### ✅ Strengths")

                for s in project["strengths"]:
                    st.success(s)

                st.markdown("### ❌ Weaknesses")

                for w in project["weaknesses"]:
                    st.error(w)

            st.markdown("---")

            st.success("🥇 BEST PROJECT")

            st.markdown(
                f"## {ranking['best_project']['title']}"
            )

            st.info(
                ranking["best_project"]["reason"]
            )

            return

        elif "ranking_text" in ranking:

            st.write(ranking["ranking_text"])

            return

    # -----------------------------
    # Gemini returned plain text
    # -----------------------------
    st.write(ranking) 