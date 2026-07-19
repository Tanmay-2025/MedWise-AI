from io import BytesIO
from datetime import datetime

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)


def generate_pdf(result, recommendations):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "MedWise AI - Assessment Report",
            styles["Title"],
        )
    )

    story.append(Spacer(1, 12))

    story.append(
        Paragraph(
            f"Date: {datetime.now().strftime('%d-%m-%Y %H:%M')}",
            styles["BodyText"],
        )
    )

    story.append(
        Paragraph(
            f"Risk Level: {result['level']}",
            styles["BodyText"],
        )
    )

    story.append(
        Paragraph(
            f"Risk Score: {result['score']}",
            styles["BodyText"],
        )
    )

    story.append(Spacer(1, 15))

    story.append(
        Paragraph(
            "<b>Unsafe Habits</b>",
            styles["Heading2"],
        )
    )

    if result["flags"]:

        for flag in result["flags"]:

            story.append(
                Paragraph(f"• {flag}", styles["BodyText"])
            )

    else:

        story.append(
            Paragraph(
                "No unsafe habits identified.",
                styles["BodyText"],
            )
        )

    story.append(Spacer(1, 15))

    story.append(
        Paragraph(
            "<b>Recommendations</b>",
            styles["Heading2"],
        )
    )

    for rec in recommendations:

        story.append(
            Paragraph(f"• {rec}", styles["BodyText"])
        )

    story.append(Spacer(1, 15))

    story.append(
        Paragraph(
            "<b>Disclaimer</b>",
            styles["Heading2"],
        )
    )

    story.append(
        Paragraph(
            "This report is intended for educational purposes only. It is not a medical diagnosis and should not replace professional medical advice.",
            styles["BodyText"],
        )
    )

    doc.build(story)

    pdf = buffer.getvalue()

    buffer.close()

    return pdf