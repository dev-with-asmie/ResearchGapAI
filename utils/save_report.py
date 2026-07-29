from fpdf import FPDF


def save_report(text):

    # Save Markdown Report
    with open("report/report.md", "w", encoding="utf-8") as f:
        f.write(text)

    # Save PDF Report
    pdf = FPDF()
    pdf.add_page()

    pdf.add_font(
        "DejaVu",
        "",
        "DejaVuSans.ttf"
    )

    pdf.set_font(
        "DejaVu",
        size=10
    )

    pdf.set_auto_page_break(
        auto=True,
        margin=15
    )

    pdf.multi_cell(
        0,
        6,
        text
    )

    pdf.output(
        "report/report.pdf"
    )

    print("PDF saved successfully!")
    print("Markdown saved successfully!") 