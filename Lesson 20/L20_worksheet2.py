import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

# --- FONT SETUP ---
font_filename = "KleeOne-Regular.ttf"
jp_font_name = 'JapaneseFont'

if os.path.exists(font_filename):
    try:
        pdfmetrics.registerFont(TTFont(jp_font_name, font_filename))
    except Exception as e:
        print(f"Font Error: {e}")
        jp_font_name = 'Helvetica'
else:
    print(f"Warning: {font_filename} not found. Japanese text will not display correctly.")
    jp_font_name = 'Helvetica'

# --- STYLES ---
styles = getSampleStyleSheet()
title_style = ParagraphStyle('TitleJP', parent=styles['Heading1'], fontName=jp_font_name, fontSize=16, alignment=1, spaceAfter=6)
header_style = ParagraphStyle('HeaderJP', parent=styles['Heading2'], fontName=jp_font_name, fontSize=12, spaceBefore=10, spaceAfter=4, textColor=colors.darkblue)
normal_style = ParagraphStyle('NormalJP', parent=styles['Normal'], fontName=jp_font_name, fontSize=10.5, leading=14, spaceAfter=2)
table_text_style = ParagraphStyle('TableText', parent=normal_style, alignment=1, leading=12)

def create_worksheet():
    filename = "Genki_L19_20_Review_Worksheet.pdf"
    doc = SimpleDocTemplate(filename, pagesize=A4, rightMargin=50, leftMargin=50, topMargin=50, bottomMargin=50)
    story = []

    # --- TITLE ---
    story.append(Paragraph("Genki II - Lesson 19 & 20 Review", title_style))
    story.append(Paragraph("Name: __________________________   Date: ____________", normal_style))
    story.append(Spacer(1, 10))

    # --- SECTION 1: VERB REVIEW TABLE ---
    story.append(Paragraph("I. Honorific vs. Extra-Modest Verbs", header_style))
    story.append(Paragraph("Fill in the correct Special Verbs. Pay attention to the subject!", normal_style))
    story.append(Spacer(1, 5))

    # Data for the table
    # Columns: Standard | Honorific (Respect for Others) | Extra-Modest (Lowering Self)
    data1 = [
        [
            'Standard', 
            'Honorific\n<font size=8 color=grey>Subject: Teacher/Guest</font>', 
            'Extra-Modest\n<font size=8 color=grey>Subject: Me/My Company</font>'
        ],
        ['行く / 来る\n<font size=8>(いく / くる)</font>', '__________________', '__________________'],
        ['言う\n<font size=8>(いう)</font>', '__________________', '__________________'],
        ['する', '__________________', '__________________'],
        ['食べる / 飲む\n<font size=8>(たべる / のむ)</font>', '__________________', '__________________'],
        ['いる', '__________________', '__________________'],
    ]

    # Process table data into Paragraphs
    table_data = []
    for row in data1:
        processed_row = [Paragraph(cell, table_text_style) for cell in row]
        table_data.append(processed_row)

    t1 = Table(table_data, colWidths=[120, 160, 160])
    t1.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 1, colors.black),
        ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
        ('PADDING', (0,0), (-1,-1), 6),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(t1)
    
    # --- SECTION 2: LESSON 19 GRAMMAR REVIEW ---
    story.append(Paragraph("II. Lesson 19 Grammar Review", header_style))
    
    # Q1: Respectful Advice (お + Stem + ください)
    story.append(Paragraph("<b>1. Respectful Advice (お〜ください):</b> You work at a station.", normal_style))
    story.append(Paragraph("Please take a ticket (切符 (きっぷ) を取 (と) る).", normal_style))
    story.append(Paragraph("&rarr; __________________________________________________________________", normal_style))
    story.append(Spacer(1, 8))

    # Q2: Gratitude (〜てくれてありがとう) & Gladness (〜てよかったです)
    story.append(Paragraph("<b>2. Gratitude & Gladness:</b> You are talking with a friend. Translate the following.", normal_style))
    story.append(Paragraph("Thank you for helping (手伝 (てつだ) う). I am glad I did not give up (あきらめる).", normal_style))
    story.append(Paragraph("&rarr; __________________________________________________________________", normal_style))
    story.append(Spacer(1, 8))

    # Q3: Expectations (〜はずです)
    story.append(Paragraph("<b>3. Expectations (〜はずです):</b>", normal_style))
    story.append(Paragraph("Today is Sunday, so the banks should be closed (閉 (し) まっている).", normal_style))
    story.append(Paragraph("&rarr; 今日は日曜日ですから、______________________________________________", normal_style))

    # --- SECTION 3: LESSON 20 HUMBLE EXPRESSIONS ---
    story.append(Paragraph("III. Lesson 20 Humble Expressions (謙譲語 I)", header_style))
    story.append(Paragraph("Change the verbs to Humble Form: <font color=darkblue>お + Stem + する</font>", normal_style))
    story.append(Spacer(1, 5))

    # Q1
    story.append(Paragraph("<b>1. I (humbly) borrowed a book from the professor.</b>", normal_style))
    story.append(Paragraph("&rarr; 先生に本を (借 (か) りる) ______________________________ ました。", normal_style))
    story.append(Spacer(1, 8))

    # Q2
    story.append(Paragraph("<b>2. I (humbly) met the professor yesterday.</b>", normal_style))
    story.append(Paragraph("&rarr; 昨日、先生に (会 (あ) う) ______________________________ ました。", normal_style))
    story.append(Spacer(1, 8))

    # --- ANSWER KEY PAGE ---
    story.append(PageBreak())
    story.append(Paragraph("ANSWER KEY: Genki II L19-20 Review", title_style))
    
    story.append(Paragraph("<b>I. Verb Review Table</b>", header_style))
    ans_table_style = ParagraphStyle('AnsTable', parent=normal_style, alignment=1)
    
    ans_data = [
        ['Verb', 'Honorific (Respect)', 'Extra-Modest (Humble/Polite)'],
        ['行く/来る', 'いらっしゃいます', '<b>参 (まい) ります</b>'],
        ['言う', 'おっしゃいます', '<b>申 (もう) します</b>'],
        ['する', 'なさいます', '<b>いたします</b>'],
        ['食べる/飲む', '召 (め) し上 (あ) がります', '<b>いただきます</b>'],
        ['いる', 'いらっしゃいます', '<b>おります</b>'],
    ]
    
    # Format Answer Table
    ans_table_rows = []
    for row in ans_data:
        ans_table_rows.append([Paragraph(cell, ans_table_style) for cell in row])

    t2 = Table(ans_table_rows, colWidths=[120, 160, 160])
    t2.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 1, colors.black),
        ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
        ('PADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t2)

    story.append(Paragraph("<b>II. Lesson 19 Review</b>", header_style))
    story.append(Paragraph("1. 切符をお取りください (きっぷをおとりください)", normal_style))
    story.append(Paragraph("2. 手伝ってくれてありがとう。あきらめなくてよかったです。", normal_style))
    story.append(Paragraph("3. 銀行は閉まっているはずです (ぎんこうはしまっているはずです)", normal_style))

    story.append(Paragraph("<b>III. Lesson 20 Humble Expressions</b>", header_style))
    story.append(Paragraph("1. お借りしました (おかりしました)", normal_style))
    story.append(Paragraph("2. お会いしました (おあいしました)", normal_style))

    # Build PDF
    doc.build(story)
    print(f"Generated successfully: {filename}")

if __name__ == "__main__":
    create_worksheet()