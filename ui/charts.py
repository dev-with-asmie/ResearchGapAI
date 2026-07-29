import streamlit as st
import plotly.express as px
import pandas as pd


def show_research_trends(papers):
    """
    Displays publication trend chart.
    """

    if not papers:
        return

    years = []

    for paper in papers:
        year = paper.get("year")

        if year not in [None, "", "-", "Unknown"]:
            try:
                years.append(int(year))
            except:
                pass

    if len(years) == 0:
        return

    df = pd.DataFrame(years, columns=["Year"])

    trend = (
        df.groupby("Year")
        .size()
        .reset_index(name="Papers")
    )

    fig = px.bar(
        trend,
        x="Year",
        y="Papers",
        title="📈 Research Publication Trend",
        text_auto=True,
        color="Papers"
    )

    fig.update_layout(
        height=420,
        template="plotly_dark"
    )

    st.plotly_chart(
    fig,
    use_container_width=True,
    key="research_trend_chart"
) 