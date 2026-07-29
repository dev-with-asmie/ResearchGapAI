import os
import streamlit as st


def show_export_section():

    st.header("📥 Export Report")

    st.success("Everything has been generated successfully!")

    st.markdown("### Generated Files")

    pdf_path = "report/report.pdf"
    md_path = "report/report.md"
    json_path = "report/report.json"

    col1, col2, col3 = st.columns(3)

    # ---------------- PDF ----------------

    with col1:

        if os.path.exists(pdf_path):

            with open(pdf_path, "rb") as file:

                st.download_button(
                    label="⬇ Download PDF",
                    data=file,
                    file_name="ResearchGapAI_Report.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )

    # ---------------- Markdown ----------------

    with col2:

        if os.path.exists(md_path):

            with open(md_path, "rb") as file:

                st.download_button(
                    label="⬇ Download Markdown",
                    data=file,
                    file_name="ResearchGapAI_Report.md",
                    mime="text/markdown",
                    use_container_width=True
                )

    # ---------------- JSON ----------------

    with col3:

        if os.path.exists(json_path):

            with open(json_path, "rb") as file:

                st.download_button(
                    label="⬇ Download JSON",
                    data=file,
                    file_name="ResearchGapAI_Report.json",
                    mime="application/json",
                    use_container_width=True
                )

    st.divider()

    st.info("Reports are also saved automatically inside the **report/** folder.") 