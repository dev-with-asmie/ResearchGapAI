from fpdf import FPDF

pdf = FPDF()

pdf.add_page()

pdf.add_font(
    "DejaVu",
    "",
    "DejaVuSans.ttf"
)

pdf.set_font("DejaVu", size=12)

pdf.multi_cell(
    0,
    10,
    "Testing Unicode — AI Research ✓"
)

pdf.output("test.pdf")

print("Success") 