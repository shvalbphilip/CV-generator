from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable

# Data for CV with updated projects section
cv_data = {
    "name": "Philip Shvalb",
    "contact": {
        "phone": "054-477-3512",
        "email": "shvalb.philip@gmail.com",
        "linkedin": "https://www.linkedin.com/in/philip-shvalb/"
    },
    "profile": ("A dedicated software developer with an insatiable passion for coding, "
                "combined with a solid foundation in technical systems and a commitment to continuous growth. "
                "Explore my coding projects on GitHub."),
    "education": [
        {
            "degree": "Associate Degree in Electronics and Computer Engineering",
            "institution": "The Air Force Technological College, Mekif Alef Ashdod",
            "dates": "2018 - 2020",
            "details": [
                "Relevant Courses: Electronics and Electrical Theory, Communication and Control Systems, Computer Systems.",
                "Final Project: Developed a 'Smart Parking System' integrating advanced technologies for efficient management."
            ]
        },
        {
            "degree": "Full Stack Development Program",
            "institution": "IITC College, Israel",
            "dates": "March 2024 - November 2024",
            "details": [
                "Practical Training: 700 hours of hands-on coding experience, developing various projects.",
                "Key Projects: Developed a ToDo app, personal blog, and mobile application.",
                "Acquired Technologies: HTML, CSS, JavaScript, React, Node.js, and a comprehensive stack for Full Stack development."
            ]
        }
    ],
    "experience": [
        {
            "title": "Communication Technician & Systems Maintenance",
            "company": "Air Force Comm. Unit",
            "dates": "2020 - 2023",
            "responsibilities": [
                "Maintained analog (AM/FM) communication systems, radar systems, and ground-based navigation systems.",
                "Conducted maintenance and troubleshooting in high-security and classified environments.",
                "Installation and maintenance of security systems, including cameras, fences, and alarms.",
                "Extensive knowledge in computing, telephony, high-voltage systems, and advanced testing equipment."
            ]
        }
    ],
    "skills": [
        ("Languages", "JavaScript, C, Assembly"),
        ("Front-End Development", "HTML, CSS, React"),
        ("Back-End Development", "Node.js"),
        ("Hardware & Systems", "Arduino, Analog Modulation")
    ],
    "projects": [
        {
            "name": "Hotel Booking Clone",
            "description": "A hotel search and booking interface that shows hotel options, prices, and availability."
        },
        {
            "name": "Web Games Hub",
            "description": "An interactive website featuring a collection of random online games for browsing and playing.",
            "github": "https://github.com/shvalbphilip/Gamify"
        },
        {
            "name": "Spotify Clone",
            "description": "A music streaming web app interface inspired by Spotify, allowing users to browse, search, and play songs.",
            "github": "https://github.com/shvalbphilip/Spotify-clone"
        }
    ]
}


def generate_cv():
    # Create PDF
    doc = SimpleDocTemplate("Philip.pdf", pagesize=A4, rightMargin=40, leftMargin=40, topMargin=40,
                            bottomMargin=40)
    styles = getSampleStyleSheet()
    elements = []

    # Custom Styles
    title_style = ParagraphStyle(name="TitleStyle", fontSize=22, leading=24, spaceAfter=14,
                                 textColor=colors.HexColor("#333333"), alignment=1)
    section_title_style = ParagraphStyle(name="SectionTitleStyle", fontSize=14, leading=18, spaceAfter=10,
                                         textColor=colors.HexColor("#007acc"), spaceBefore=16)
    subsection_title_style = ParagraphStyle(name="SubsectionTitleStyle", fontSize=12, leading=14, spaceAfter=6,
                                            textColor=colors.HexColor("#005b9f"))
    normal_text_style = ParagraphStyle(name="NormalTextStyle", fontSize=10, leading=12, spaceAfter=4)
    tiny_text_style = ParagraphStyle(name="TinyTextStyle", fontSize=6, leading=8, textColor=colors.grey)

    # Header
    elements.append(Paragraph(cv_data["name"], title_style))

    # Contact Information with bold labels
    contact_info = (
        f"<b>Phone:</b> {cv_data['contact']['phone']} | "
        f"<b>Email:</b> {cv_data['contact']['email']} | "
        f"<b>GitHub:</b> <u>{cv_data['contact']['linkedin']}</u>"
    )
    elements.append(Paragraph(contact_info, normal_text_style))
    elements.append(HRFlowable(color=colors.grey, thickness=1, spaceBefore=12, spaceAfter=12))

    # Profile Section
    elements.append(Paragraph("Personal Profile", section_title_style))
    elements.append(Paragraph(cv_data["profile"], normal_text_style))

    # Education Section
    elements.append(Paragraph("Education", section_title_style))
    for edu in cv_data["education"]:
        elements.append(Paragraph(f"{edu['degree']}, {edu['institution']} ({edu['dates']})", subsection_title_style))
        for detail in edu["details"]:
            elements.append(Paragraph(f"• {detail}", normal_text_style))
        elements.append(Spacer(1, 6))

    # Experience Section
    elements.append(Paragraph("Professional Experience", section_title_style))
    for exp in cv_data["experience"]:
        elements.append(Paragraph(f"{exp['title']} - {exp['company']} ({exp['dates']})", subsection_title_style))
        for res in exp["responsibilities"]:
            elements.append(Paragraph(f"• {res}", normal_text_style))
        elements.append(Spacer(1, 6))

    # Skills Section
    elements.append(Paragraph("Technical Skills", section_title_style))
    skills_data = [[Paragraph(f"<b>{cat}</b>", normal_text_style), Paragraph(details, normal_text_style)] for
                   cat, details in cv_data["skills"]]
    skills_table = Table(skills_data, colWidths=[150, 300])
    skills_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey)
    ]))
    elements.append(skills_table)

    # Projects Section with updated content
    elements.append(Paragraph("Selected Personal Projects", section_title_style))
    for proj in cv_data["projects"]:
        # Only include GitHub link if available
        if "github" in proj:
            project_text = f"• <b>{proj['name']}</b>: {proj['description']} [GitHub]({proj['github']})"
        else:
            project_text = f"• <b>{proj['name']}</b>: {proj['description']}"
        elements.append(Paragraph(project_text, normal_text_style))
        elements.append(Spacer(1, 6))

    # Footer with a witty message
    footer_message = (
        "P.S. This CV was generated with Python code. Just in case you were wondering how deep my tech obsession goes! "
        "<a href='https://github.com/shvalbphilip' color='blue' target='_blank'>Check out my GitHub!</a>"
    )
    elements.append(Spacer(1, 5))
    elements.append(Paragraph(footer_message, tiny_text_style))

    # Build PDF
    doc.build(elements)


generate_cv()