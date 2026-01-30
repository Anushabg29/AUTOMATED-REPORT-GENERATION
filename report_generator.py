import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

# Read data
data = pd.read_csv("data.csv")

# Analyze data
avg = data["Marks"].mean()
high = data["Marks"].max()
low = data["Marks"].min()

# Create PDF
pdf = canvas.Canvas("Automated_Report.pdf", pagesize=A4)
width, height = A4

pdf.setFont("Helvetica-Bold", 16)
pdf.drawCentredString(width/2, height-2*cm, "Student Performance Report")

pdf.setFont("Helvetica", 12)
pdf.drawString(2*cm, height-3.5*cm, "Automated Report Generation Using Python")

pdf.setFont("Helvetica-Bold", 12)
pdf.drawString(2*cm, height-5*cm, "Student Marks:")

y = height - 6*cm
pdf.setFont("Helvetica", 11)
for _, row in data.iterrows():
    pdf.drawString(2*cm, y, f"{row['Name']} : {row['Marks']}")
    y -= 0.7*cm

pdf.setFont("Helvetica-Bold", 12)
pdf.drawString(2*cm, y-1*cm, "Analysis Summary")

pdf.setFont("Helvetica", 11)
pdf.drawString(2*cm, y-2*cm, f"Average Marks : {avg:.2f}")
pdf.drawString(2*cm, y-3*cm, f"Highest Marks : {high}")
pdf.drawString(2*cm, y-4*cm, f"Lowest Marks  : {low}")

pdf.save()
print("PDF Report Generated Successfully")
