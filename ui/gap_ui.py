import streamlit as st


def show_research_gaps(
    all_analysis,
    gap_agent,
    local_gap_agent
):
    """
    Generates and displays research gaps.
    Returns:
        gaps (str)
    """

    st.header("🔍 Research Gaps")

    st.caption(
        "AI combines all paper analyses and automatically "
        "identifies recurring limitations, missing evaluations "
        "and unexplored research opportunities."
    )

    with st.spinner("🔍 Finding research gaps..."):

        gaps = gap_agent.find_gaps(all_analysis)

        if (
            "resource_exhausted" in gaps.lower()
            or "unavailable" in gaps.lower()
            or "gemini unavailable" in gaps.lower()
        ):

            st.warning(
                "Gemini unavailable. Using Local Gap Generator..."
            )

            gaps = local_gap_agent.generate(
                all_analysis
            )

    st.success("Research gaps generated successfully!")

    st.markdown("---")

    st.markdown(gaps)

    return gaps 