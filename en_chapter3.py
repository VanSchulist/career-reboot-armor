# -*- coding: utf-8 -*-
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx_helpers import set_cell_background, set_cell_margins
from make_english_book import add_heading_1, add_heading_2, add_callout

def build_en_chapter_3(doc):
    add_heading_1(doc, "Chapter 3: Beating the Machine — Engineering an ATS-Proof Hybrid Chronological Resume")
    
    add_heading_2(doc, "1. The Problem: The Cold Portal Void")
    doc.add_paragraph(
        "Returning professionals who submit standard resumes through corporate job boards (Workday, Greenhouse, Lever, Taleo, iCIMS) "
        "consistently report a bewildering phenomenon: after sending out 200 applications, they receive nothing but automated rejections "
        "within 48 hours, or complete silence. The assumption is that recruiters are actively rejecting them because of their gap. "
        "The reality is far more mechanistic: **human eyes never saw the resume. The Applicant Tracking System's parsing engine "
        "disqualified the file before it ever reached a recruiter's dashboard.**"
    )

    add_heading_2(doc, "2. Why It Happens: Linear Date Calculations & Parser Collapse")
    doc.add_paragraph(
        "Enterprise ATS software does not 'read' resumes like a human; it executes regular-expression text scraping. "
        "When an applicant submits a resume with an unaddressed gap, two distinct failure modes occur:"
    )
    doc.add_paragraph(
        "1. The Unemployed Duration Filter: The ATS algorithm extracts the most recent `End Date`. If the end date is a past year (e.g., '10/2022'), "
        "the system computes `Current_Date - Last_Job_End_Date`. In many automated recruiting workflows, candidates with an unmitigated gap exceeding "
        "180 days are automatically assigned a low score or hidden in recruiter views under 'Archived / Unqualified' buckets."
    )
    doc.add_paragraph(
        "2. Structural Parsing Collapse: In an attempt to mask gaps or appear modern, job seekers frequently download graphic-heavy templates "
        "(from Canva, Etsy, or Word) with dual columns, text boxes, and skill graphs. When an ATS parses a two-column PDF, it often reads across the page "
        "horizontally, concatenating left-column job titles with right-column company names. The output becomes an unreadable scramble of broken text, "
        "triggering an instant automated rejection."
    )

    add_heading_2(doc, "3. Common Mistakes: Counterproductive Camouflage")
    doc.add_paragraph("Returners frequently employ resume formats that actively sabotage their chances:")
    doc.add_paragraph("• The Functional Resume: Stripping away all dates and organizing solely by skills ('Leadership,' 'Project Management'). Recruiters unanimously despise this format; they immediately recognize it as a desperate attempt to obscure a spotty work history and discard it within 5 seconds.")
    doc.add_paragraph("• Year-Only Date Masking: Writing '2019 – 2022' instead of '03/2019 – 11/2022.' ATS parsers frequently default year-only dates to January 1st of that year, inadvertently magnifying a gap or miscalculating total years of experience.")
    doc.add_paragraph("• Graphic Infographics & Skill Meters: Visual bars indicating 'Python: 90%' or 'Negotiation: 5 Stars.' ATS parsers cannot read images or CSS bars, resulting in missed keywords and empty candidate profiles.")

    add_heading_2(doc, "4. The Correct Approach: The Single-Column Hybrid Chronological Architecture")
    doc.add_paragraph(
        "The industry-proven solution is the **Single-Column Hybrid Chronological Resume (Combination Format)**.\n"
        "This architecture accomplishes two vital objectives simultaneously:\n"
        "1. Machine Compliant: A clean, top-to-bottom, single-column hierarchy with standardized `MM/YYYY – Present` dates, ensuring 100% data extraction by any ATS engine.\n"
        "2. Human Captivating: The top third of the first page (the critical 6-second eye-scan zone) is dominated by an authoritative Executive Summary, a Core Impact Matrix, and a Modern Toolchain block. By the time a human recruiter reads down to your past employment history, they have already framed you as an accomplished, high-caliber subject matter expert."
    )

    add_callout(
        doc,
        "THE ATS GOLDEN SPECIFICATION:\n"
        "• Single-column layout exclusively. No tables within tables, no headers/footers containing critical info, no floating text boxes.\n"
        "• Standard dates: Use 'MM/YYYY – MM/YYYY' or 'MM/YYYY – Present'. Never use season names (e.g., 'Spring 2022').\n"
        "• Standard fonts: Arial, Calibri, Times New Roman, or Georgia (10–11pt body text; 14–16pt section headers).\n"
        "• Standard export: Clean .docx or text-based .pdf directly generated from Microsoft Word.",
        title="PARSER PASSING PROTOCOL"
    )

    add_heading_2(doc, "5. Step-by-Step Implementation: Building Your 4-Tier Hybrid Resume")
    doc.add_paragraph("Construct your resume following this precise top-to-bottom blueprint:")

    doc.add_paragraph("Tier 1: The Contact & Professional Title Block\n"
                  "Full Name, Phone, Professional Email (clean, modern Gmail/custom domain), City/State, and LinkedIn URL. "
                  "Immediately underneath, insert a clear, target-specific Professional Headline (e.g., 'SENIOR OPERATIONS DIRECTOR | Lean Six Sigma Black Belt | Supply Chain Optimization').")

    doc.add_paragraph("Tier 2: Executive Summary & Core Impact Metrics\n"
                  "A 3-to-4 sentence narrative framing your career scope, followed by 4 bulleted career milestones featuring hard numbers:\n"
                  "• Directed multi-site operations managing annual operating budgets exceeding $25M across 4 regional distribution hubs.\n"
                  "• Spearheaded workflow re-engineering programs that cut order fulfillment cycle time by 32% while reducing inventory carrying costs by $1.8M.")

    doc.add_paragraph("Tier 3: The Active Bridge Experience (Current Role)\n"
                  "Position your Chapter 2 consulting engagement at the top of Professional Experience:\n"
                  "• Independent Project Consultant | Advisory Services               [MM/YYYY] – Present\n"
                  "• Detail 2–3 structured bullet points focused on client deliverables, efficiency gains, and modern tool application. This resets the ATS unemployment clock to ZERO.")

    doc.add_paragraph("Tier 4: Reverse Chronological Full-Time Career History\n"
                  "Present your pre-break corporate track record in reverse order: [Company Name], [City, State], [Official Title], [MM/YYYY – MM/YYYY]. "
                  "Use the PAR framework (Problem, Action, Result) for all bullet points, beginning with strong action verbs (Spearheaded, Restructured, Negotiated, Optimized).")

    add_heading_2(doc, "6. Concrete Example: Complete Structural Blueprint")
    
    # Resume Sample Box
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    cell = table.cell(0, 0)
    cell.width = Inches(6.2)
    set_cell_background(cell, "FAFAFA")
    set_cell_margins(cell, 120, 120, 140, 140)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(2)
    
    sample_resume = (
        "DAVID K. MILLER\n"
        "Philadelphia, PA | (215) 555-0192 | david.miller@email.com | linkedin.com/in/david-miller-ops\n"
        "================================================================================\n"
        "SENIOR OPERATIONS DIRECTOR\n"
        "Supply Chain Transformation | Cross-Functional Leadership | Lean Process Optimization\n\n"
        "EXECUTIVE SUMMARY\n"
        "Accomplished Operations Executive with 14+ years of experience steering logistics, warehouse distribution, and process automation "
        "across complex discrete manufacturing environments. Track record of revitalizing underperforming fulfillment hubs, eliminating "
        "operational redundancies, and institutionalizing KPI-driven performance cultures. Leverages modern digital toolchains (Notion, Airtable, AI analytics) "
        "to drive end-to-end operational visibility.\n\n"
        "CORE IMPACT & VALUE HIGHLIGHTS\n"
        "• Scaled fulfillment infrastructure from 120K to 450K sq. ft., managing $40M+ in capital improvement budgets.\n"
        "• Slashed freight-per-unit costs by 18% via nationwide carrier renegotiations and dynamic load-routing algorithms.\n"
        "• Implemented real-time telemetry tracking, cutting inventory variance from 4.8% to under 0.4% across 3 distribution hubs.\n\n"
        "PROFESSIONAL EXPERIENCE\n\n"
        "INDEPENDENT ADVISORY SERVICES | Philadelphia, PA                   08/2024 – Present\n"
        "Operations & Process Consultant\n"
        "Retained by growth-stage e-commerce and distribution businesses to resolve fulfillment bottlenecks and modernize inventory management.\n"
        "• Re-engineered warehouse intake and return-merchandise-authorization (RMA) workflows for a mid-market retailer, reducing turnaround from 7 days to 48 hours.\n"
        "• Built automated inventory tracking dashboards utilizing Airtable and webhook triggers, eliminating 15 hours of weekly manual reporting.\n\n"
        "ALLIANCE SUPPLY CORP | Allentown, PA                               04/2016 – 10/2022\n"
        "Director of Operations & Fulfillment\n"
        "Directed daily operations of a 300,000 sq. ft. central distribution center supporting $120M in regional B2B sales. Managed 8 direct reports and 85 non-exempt personnel.\n"
        "• Directed full lifecycle deployment of Manhattan Associates WMS, achieving on-time, under-budget go-live with zero customer shipment interruptions.\n"
        "• Instituted safety and ergonomics overhaul, driving a 62% reduction in OSHA recordable incidents over a 3-year period.\n"
        "• Established daily labor-planning models balancing inbound freight volumes with staffing, reducing overtime expenditures by $310K annually.\n\n"
        "EDUCATION & CERTIFICATIONS\n"
        "• B.S. in Supply Chain Management | Pennsylvania State University, University Park, PA\n"
        "• Certified Supply Chain Professional (CSCP) | APICS / ASCM\n"
        "• Lean Six Sigma Green Belt | Institute of Industrial and Systems Engineers"
    )
    run_s = p.add_run(sample_resume)
    run_s.font.name = 'Consolas'
    run_s.font.size = Pt(8.5)
    run_s.font.color.rgb = RGBColor(0x2D, 0x37, 0x48)

    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    add_heading_2(doc, "7. Practical Checklist: The 7-Point ATS Defense Audit")
    doc.add_paragraph("Before uploading your document to any online portal, verify:")
    doc.add_paragraph("[1] Layout is strictly single-column. No columns, sidebars, or floating text boxes.")
    doc.add_paragraph("[2] Dates are standardized as 'MM/YYYY – MM/YYYY' or 'MM/YYYY – Present'.")
    doc.add_paragraph("[3] The current bridge consulting role is anchored at the top of Professional Experience with 'Present'.")
    doc.add_paragraph("[4] Font is standard system typography (Calibri, Arial, Georgia) with no custom vector icons.")
    doc.add_paragraph("[5] File is exported as a clean .docx or text-based .pdf (selectable and copy-pasteable).")
    doc.add_paragraph("[6] Key hard skills matching the target Job Description are naturally woven into Tier 2 and Tier 3.")
    doc.add_paragraph("[7] All bullet points lead with strong, past-tense action verbs (except the current role, which uses present tense).")

    add_heading_2(doc, "8. Immediate Actionable Step")
    doc.add_paragraph(
        "IMMEDIATE ACTION TODAY: Copy the raw text of your current resume and paste it into a simple Notepad / text editor file (.txt). "
        "If you see broken characters, scrambled lines, or missing sections, your resume is currently failing ATS parsing. "
        "Port your history into the clean, single-column blueprint above."
    )
    
    doc.add_page_break()

print("EN Chapter 3 ready.")
