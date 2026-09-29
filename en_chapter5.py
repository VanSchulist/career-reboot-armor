# -*- coding: utf-8 -*-
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx_helpers import set_cell_background, set_cell_margins
from make_english_book import add_heading_1, add_heading_2, add_callout

def build_en_chapter_5(doc):
    add_heading_1(doc, "Chapter 5: The 30-Second Pivot — Defensive Interview Scripts & Privacy Firewalls")
    
    add_heading_2(doc, "1. The Problem: The Ambush in the Interview Room")
    doc.add_paragraph(
        "The most psychologically harrowing moment in a returner's job search occurs 15 minutes into a screening call or video interview. "
        "The recruiter pauses, glances at their notes, and asks the inevitable question: "
        "'I see you left your last full-time role in late 2022, and while you have some consulting listed, there's a multi-year gap here. "
        "Can you walk me through what was happening during that time?'"
    )
    doc.add_paragraph(
        "For candidates who have endured hospice care, parental dementia, or personal medical recovery, this question triggers acute vulnerability. "
        "Unprepared candidates stammer, apologize, or launch into an emotional, unprompted narrative detailing hospital shifts, diagnoses, "
        "and grief. The recruiter listens with polite sympathy—and subsequently eliminates the candidate for 'concerns regarding readiness and resilience.'"
    )

    add_heading_2(doc, "2. Why It Happens: The Employer's True Fear is Recurrence & Distraction")
    doc.add_paragraph(
        "Candidates fail this interaction because they misinterpret the recruiter's motive. They assume the interviewer is evaluating their "
        "moral character or inquiring about their personal grief.\n"
        "In reality, **corporate recruitment is an exercise in risk mitigation**. The interviewer has only one commercial concern:\n"
        "**'Is this family crisis truly over, or will this candidate be distracted, call in sick every Tuesday, and quit three months in?'**"
    )
    doc.add_paragraph(
        "When a candidate shares intimate medical details or displays emotional distress, they unintentionally broadcast three severe risk signals:\n"
        "1. Active Trauma: The emotional wound is still raw, suggesting fragile executive bandwidth;\n"
        "2. Lack of Professional Boundaries: Oversharing personal domestic matters in a commercial business negotiation;\n"
        "3. Recurrence Risk: If a caregiving situation sounds unresolved, the employer assumes family obligations will constantly override business priorities."
    )

    add_heading_2(doc, "3. Common Mistakes: Trauma-Dumping, Apologizing, and Fictitious Startups")
    doc.add_paragraph("Returners consistently sabotage themselves with three defensive errors:")
    doc.add_paragraph("• Trauma-Dumping: Describing surgeries, palliative care schedules, and family disputes. This makes interviewers deeply uncomfortable and creates an atmosphere of pity rather than professional respect.")
    doc.add_paragraph("• The Submissive Apology: Beginning with 'I'm sorry, I know it looks terrible on paper, but I had no choice.' Apologizing for fulfilling an honorable family duty hands the employer total psychological dominance and invites severe salary low-balling.")
    doc.add_paragraph("• The Phantom E-Commerce Business: Claiming 'I took time off to build a direct-to-consumer drop-shipping business.' When the interviewer asks for customer acquisition costs, churn rates, and balance sheets, the candidate is exposed as dishonest.")

    add_heading_2(doc, "4. The Correct Approach: The 30-Second Pivot (The 3-Act Structure)")
    doc.add_paragraph(
        "The definitive solution is the **30-Second Defensive Pivot**.\n"
        "This framework executes three disciplined psychological moves in exactly 30 to 45 seconds:\n"
        "**[Act 1: Factual Boundary (10 sec)] → [Act 2: Permanent Resolution (10 sec)] → [Act 3: Value Pivot (10 sec)]**.\n"
        "It frames your break as a responsible, planned family duty, slams the door shut on privacy inquiries, and instantly bounces the ball back to the employer's business challenges."
    )

    add_callout(
        doc,
        "THE PRIVACY FIREWALL & TITLE VII / ADA PROTECTIONS:\n"
        "Under US Equal Employment Opportunity Commission (EEOC) guidelines and the Americans with Disabilities Act (ADA), "
        "interviewers are legally prohibited from asking about your personal medical history or the medical conditions of family members.\n"
        "You owe no one a medical narrative. You owe them only one reassurance: that your availability and focus are 100% unrestricted.",
        title="LEGAL SHIELD PRINCIPLE"
    )

    add_heading_2(doc, "5. Step-by-Step Implementation: The Anatomy of the 30-Second Script")
    doc.add_paragraph("Commit this three-act structure to memory:")

    doc.add_paragraph("Act 1: The Factual Boundary (0:00 – 0:10)\n"
                  "- The Script: 'In late 2022, I chose to take a planned career sabbatical to personally manage an acute family health matter...'\n"
                  "- Psychological Impact: You frame the hiatus as an active, deliberate leadership choice—not an involuntary firing or passive drift. You maintain immediate dignity.")

    doc.add_paragraph("Act 2: The Permanent Resolution (0:10 – 0:20)\n"
                  "- The Script: '...That family matter has now reached a complete and permanent resolution [or: has been fully transitioned to permanent professional care], and my time and availability are 100% unencumbered...'\n"
                  "- Psychological Impact: You obliterate the employer's core fear of recurrence. Words like 'permanently resolved' leave zero room for follow-up probes.")

    doc.add_paragraph("Act 3: The Value Pivot (0:20 – 0:35)\n"
                  "- The Script: '...Over the past several months, I've channeled that energy into independent advisory work and refreshing my digital toolchain. What drew me so strongly to this role is your current initiative in [Target Problem from Job Description], which aligns directly with my core background in [Your Specialty].'\n"
                  "- Psychological Impact: The narrative spotlight shifts immediately from your past personal life to the company's future revenue and efficiency.")

    add_heading_2(doc, "6. Concrete Example: Three Word-for-Word Real-World Scripts")
    
    # Scripts Table
    table = doc.add_table(rows=4, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    headers = ["Life Scenario", "Word-for-Word 30-Second Script (Ready to Deliver)"]
    col_widths = [1.8, 4.4]
    
    for i, title in enumerate(headers):
        cell = table.cell(0, i)
        cell.width = Inches(col_widths[i])
        set_cell_background(cell, "EDF2F7")
        set_cell_margins(cell, 80, 80, 100, 100)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(title)
        run.font.bold = True
        run.font.size = Pt(9.5)
        run.font.color.rgb = RGBColor(0x2D, 0x37, 0x48)
        
    script_data = [
        ("Scenario A: Parent / Spouse Illness (Deceased)", 
         "\"In late 2022, I made the conscious decision to step back from full-time corporate work to manage end-of-life care for a terminally ill family member. It was an intense, essential responsibility that I saw through to the end. That chapter is now closed and fully resolved, and my professional availability is completely unencumbered. Over the past several months, I've been staying sharp through project consulting, and I'm energized to channel my full operational bandwidth back into high-growth environments—specifically around your regional expansion goals.\""),
         
        ("Scenario B: Family Chronic Illness (Now in Care)", 
         "\"A few years ago, I took a planned career sabbatical to stabilize a complex family medical situation and establish a long-term care infrastructure. That framework is now fully operational, managed entirely by specialized professional healthcare providers, and my caregiving responsibilities have concluded. My schedule is entirely unrestricted. I've spent recent months executing targeted advisory projects in supply chain automation, and I'm thrilled to discuss how my fulfillment turnaround experience can solve your current delivery bottlenecks.\""),
         
        ("Scenario C: Personal Medical Recovery (Fully Cleared)", 
         "\"In 2023, I took a medical leave to undergo a necessary planned surgical intervention and complete full rehabilitation. I am fortunate to report that my medical team has given me a clean bill of health with zero physical restrictions, and I am operating with higher vitality than ever before. I've used my recovery window to modernize my tech stack in data analytics, and I'm eager to bring that focused problem-solving capability to your core finance team.\"")
    ]
    
    for row_idx, data in enumerate(script_data, start=1):
        for col_idx, text in enumerate(data):
            cell = table.cell(row_idx, col_idx)
            cell.width = Inches(col_widths[col_idx])
            set_cell_margins(cell, 80, 80, 100, 100)
            set_cell_background(cell, "FFFFFF" if row_idx % 2 == 1 else "F7FAFC")
            p = cell.paragraphs[0]
            run = p.add_run(text)
            run.font.size = Pt(9)
            if col_idx == 0:
                run.font.bold = True
                run.font.color.rgb = RGBColor(0x1A, 0x36, 0x5D)
            else:
                run.font.color.rgb = RGBColor(0x2D, 0x37, 0x48)

    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    add_heading_2(doc, "7. Practical Checklist: The 7 Interview Verbal Firewalls")
    doc.add_paragraph("Before entering any interview, verify you uphold all 7 defensive rules:")
    doc.add_paragraph("[1] Zero tears, wavering voice, or visible emotional distress during delivery.")
    doc.add_paragraph("[2] Zero clinical, surgical, pharmacological, or hospital operational details.")
    doc.add_paragraph("[3] Zero victim language ('It was unfair,' 'I was forced,' 'I was in a bad spot').")
    doc.add_paragraph("[4] Explicitly include words meaning 'permanently resolved' or 'fully transitioned.'")
    doc.add_paragraph("[5] Total delivery time is strictly between 30 and 45 seconds.")
    doc.add_paragraph("[6] The answer concludes with a direct, business-oriented question or statement about the company's needs.")
    doc.add_paragraph("[7] If an interviewer inappropriately presses on medical details, politely hold the boundary: 'I appreciate your interest, but the health matter is fully resolved. What matters today is my capacity to deliver results for this role.'")

    add_heading_2(doc, "8. Immediate Actionable Step")
    doc.add_paragraph(
        "IMMEDIATE ACTION TODAY: Open the voice memo app on your smartphone. Select the script above that matches your reality. "
        "Record yourself delivering it 3 times without looking at the text. Listen back to your cadence. "
        "Tune your voice until it sounds as calm, composed, and steady as an executive giving a quarterly financial briefing."
    )
    
    doc.add_page_break()

print("EN Chapter 5 ready.")
