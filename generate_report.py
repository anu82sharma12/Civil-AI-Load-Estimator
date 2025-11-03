from fpdf import FPDF
from datetime import datetime

def export_pdf(results_df):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, "Civil-AI Load Report", ln=1, align="C")
    pdf.set_font("Helvetica", size=10)
    pdf.cell(0, 10, f"Generated: {datetime.now():%Y-%m-%d %H:%M}", ln=1)
    pdf.ln(5)
    for _, row in results_df.iterrows():
        pdf.set_font("Helvetica", "B", 10)
        pdf.cell(0, 8, f"Bridge: {row.get('name', 'Span')} {row['span_m']}m", ln=1)
        pdf.set_font("Helvetica", size=10)
        pdf.multi_cell(0, 6, f"""
Bending: {row['Max Bending (kN·m)']:,} kN·m
Shear:   {row['Max Shear (kN)']:,} kN
Deflection: {row['Deflection (mm)']} mm
Safety Factor: {row['Safety Factor']:.2f} → {'SAFE' if row['Safety Factor']>1.05 else 'REVIEW'}
        """.strip())
        pdf.ln(4)
    output = pdf.output(dest='S').encode('latin-1')
    return output
