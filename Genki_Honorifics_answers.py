import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def create_answer_key():
    # 1. Setup the Font (Checks for the file you already downloaded)
    font_filename = "KleeOne-Regular.ttf"
    
    if os.path.exists(font_filename):
        try:
            pdfmetrics.registerFont(TTFont('JapaneseFont', font_filename))
            jp_font_name = 'JapaneseFont'
        except Exception as e:
            print(f"Font Error: {e}")
            return
    else:
        print(f"Error: {font_filename} not found. Please run the worksheet script first to download it.")
        return

    # 2. Setup the Document
    pdf_filename = "Genki_Honorifics_AnswerKey.pdf"
    doc = SimpleDocTemplate(
        pdf_filename, 
        pagesize=A4, 
        rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=72
    )
    
    styles = getSampleStyleSheet()
    
    # Custom Styles
    title_style = ParagraphStyle(
        'TitleJP',
        parent=styles['Heading1'],
        fontName=jp_font_name,
        fontSize=18,
        spaceAfter=12,
        alignment=1, # Center
        textColor=colors.darkblue
    )
    
    header_style = ParagraphStyle(
        'HeaderJP',
        parent=styles['Heading2'],
        fontName=jp_font_name,
        fontSize=14,
        spaceBefore=12,
        spaceAfter=6,
        textColor=colors.black
    )
    
    normal_style = ParagraphStyle(
        'NormalJP',
        parent=styles['Normal'],
        fontName=jp_font_name,
        fontSize=11,
        leading=16, 
        spaceAfter=10
    )

    answer_style = ParagraphStyle(
        'Answer',
        parent=normal_style,
        textColor=colors.red  # Answers in Red
    )

    story = []

    # --- Content ---

    story.append(Paragraph("ANSWER KEY: Genki II - Chapter 19", title_style))
    story.append(Spacer(1, 12))

    # Section 1
    story.append(Paragraph("I. Special Honorific Verbs (尊敬語)", header_style))
    
    data1 = [
        ['Standard (辞書形)', 'Meaning', 'Honorific (Answer)'],
        ['いく / くる / いる', 'to go/come/be', 'いらっしゃる'],
        ['たべる / のむ', 'to eat/drink', '召し上がる (めしあがる)'],
        ['する', 'to do', 'なさる'],
        ['いう', 'to say', 'おっしゃる'],
        ['みる', 'to see', 'ご覧になる (ごらんになる)'],
        ['寝る (ねる)', 'to sleep', 'お休みになる (おやすみになる)'],
    ]
    
    # Create table with Red text for answers
    table_data = []
    for row in data1:
        if row[2] == 'Honorific (Answer)':
            table_data.append([row[0], row[1], row[2]])
        else:
            # Format the answer column in red
            table_data.append([row[0], row[1], Paragraph(f"<font color='red'>{row[2]}</font>", normal_style)])

    t1 = Table(table_data, colWidths=[150, 100, 180])
    t1.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), jp_font_name),
        ('GRID', (0,0), (-1,-1), 1, colors.black),
        ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
        ('PADDING', (0,0), (-1,-1), 6),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(t1)
    story.append(Spacer(1, 20))

    # Section 2
    story.append(Paragraph("II. Dialogue: Teacher and Student", header_style))
    
    dialogue_answers = """
    1. <b>いらっしゃいます</b> (or いらっしゃいました)<br/>
    &nbsp;&nbsp;&nbsp;<font size=9 color=grey>Subject is Teacher (Honorific)</font><br/><br/>
    2. <b>参ります (まいります)</b> or <b>行きます</b><br/>
    &nbsp;&nbsp;&nbsp;<font size=9 color=grey>Subject is Teacher talking about himself (Humble/Polite)</font><br/><br/>
    3. <b>召し上がりました (めしあがりました)</b><br/>
    &nbsp;&nbsp;&nbsp;<font size=9 color=grey>Subject is Teacher (Honorific)</font><br/><br/>
    4. <b>食べていません</b> or <b>まだなんです</b><br/>
    &nbsp;&nbsp;&nbsp;<font size=9 color=grey>Subject is Teacher talking about himself (Polite/Humble)</font>
    """
    story.append(Paragraph(dialogue_answers, answer_style))
    story.append(Spacer(1, 10))

    # Section 3
    story.append(Paragraph("III. Choose the Correct Sentence", header_style))

    q1_ans = "1. <b>(b) 先生は本をお読みになります。</b>"
    
    story.append(Paragraph(q1_ans, answer_style))
    story.append(Spacer(1, 10))

    # Section 4
    story.append(Paragraph("IV. Honorific Nouns & Adjectives", header_style))

    data4 = [
        ['Word', 'Polite Form'],
        ['名前 (Name)', 'お名前'],
        ['忙しい (Busy)', 'お忙しい'],
        ['家族 (Family)', 'ご家族'],
        ['電話 (Phone)', 'お電話'],
    ]
    
    table4_data = []
    for row in data4:
        if row[1] == 'Polite Form':
            table4_data.append(row)
        else:
            table4_data.append([row[0], Paragraph(f"<font color='red'>{row[1]}</font>", normal_style)])

    t4 = Table(table4_data, colWidths=[150, 180])
    t4.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), jp_font_name),
        ('GRID', (0,0), (-1,-1), 1, colors.black),
        ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
        ('PADDING', (0,0), (-1,-1), 6),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(t4)

    # Build
    doc.build(story)
    print(f"Answer Key generated successfully: {pdf_filename}")

if __name__ == "__main__":
    create_answer_key()