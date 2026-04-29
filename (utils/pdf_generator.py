from fpdf import FPDF

def generate_pdf(data, filename):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="YT Insight Pro Report", ln=True)

    pdf.cell(200, 10, txt=f"Title: {data['title']}", ln=True)
    pdf.cell(200, 10, txt=f"Channel: {data['channel']}", ln=True)
    pdf.cell(200, 10, txt=f"Views: {data['views']}", ln=True)

    pdf.multi_cell(0, 10, txt=data["summary"])

    pdf.output(filename)
