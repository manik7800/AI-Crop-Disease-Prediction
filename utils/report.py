from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO


def generate_report(disease, confidence, info):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>AI Crop Disease Prediction Report</b>", styles["Title"]))

    story.append(Paragraph(f"<b>Disease:</b> {disease}", styles["Normal"]))

    story.append(Paragraph(f"<b>Confidence:</b> {confidence:.2f}%", styles["Normal"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    if info:

        story.append(Paragraph("<b>Symptoms</b>", styles["Heading2"]))

        for item in info["symptoms"]:
            story.append(Paragraph("• " + item, styles["Normal"]))

        story.append(Paragraph("<b>Treatment</b>", styles["Heading2"]))

        for item in info["treatment"]:
            story.append(Paragraph("• " + item, styles["Normal"]))

        story.append(Paragraph("<b>Prevention</b>", styles["Heading2"]))

        for item in info["prevention"]:
            story.append(Paragraph("• " + item, styles["Normal"]))

    doc.build(story)

    pdf = buffer.getvalue()

    buffer.close()

    return pdf