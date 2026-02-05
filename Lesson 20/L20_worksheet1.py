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
    print(f"Warning: {font_filename} not found. Please ensure the font file is in the folder.")
    jp_font_name = 'Helvetica'

# --- STYLES ---
styles = getSampleStyleSheet()
title_style = ParagraphStyle('TitleJP', parent=styles['Heading1'], fontName=jp_font_name, fontSize=18, alignment=1, spaceAfter=12)
header_style = ParagraphStyle('HeaderJP', parent=styles['Heading2'], fontName=jp_font_name, fontSize=14, spaceBefore=12, spaceAfter=6, textColor=colors.darkblue)


# Normal text (sentences)
normal_style = ParagraphStyle('NormalJP', parent=styles['Normal'], fontName=jp_font_name, fontSize=11, leading=18, spaceAfter=10)

# Table text (Centered, usually for drill columns)
table_text_style = ParagraphStyle('TableText', parent=normal_style, alignment=1, leading=14)

def create_worksheet():
    filename = "Genki_L20_ExtraModest_Furigana.pdf"
    doc = SimpleDocTemplate(filename, pagesize=A4, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=72)
    story = []

    # --- TITLE ---
    story.append(Paragraph("Genki II - Lesson 20: Extra-modest Expressions", title_style))
    story.append(Paragraph("Name: __________________________   Date: ____________", normal_style))
    story.append(Spacer(1, 12))

    # --- SECTION 1: CONVERSION TABLE ---
    story.append(Paragraph("I. Verbs to Extra-modest Expressions (謙譲語・丁重語)", header_style))
    story.append(Paragraph("Convert the verbs into their Extra-modest 'masu' forms.", normal_style))

    # Note: We use <br/> to put the reading on the next line (Below the Kanji)
    data1 = [
        ['Standard Verb\n(辞書形)', 'Extra-modest\n(〜ます)', 'Meaning'],
        ['いる', '__________________', '(to be)'],
        ['行く / 来る\n', '__________________', '(to go/come)'],
        ['言う\n', '__________________', '(to say)'],
        ['する', '__________________', '(to do)'],
        ['食べる / 飲む\n', '__________________', '(to eat/drink)'],
        ['ある', '__________________', '(to exist)',],
        ['〜ている', '__________________', '(is doing...)'],
        ['〜です', '__________________', '(is...)'],
    ]

    # Convert text strings to Paragraphs for formatting
    table_data = []
    for row in data1:
        processed_row = [Paragraph(cell, table_text_style) for cell in row]
        table_data.append(processed_row)

    t1 = Table(table_data, colWidths=[150, 180, 100])
    t1.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 1, colors.black),
        ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
        ('PADDING', (0,0), (-1,-1), 8),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(t1)
    story.append(Spacer(1, 20))

    # --- SECTION 2: Q&A TRANSFORMATION ---
    story.append(Paragraph("II. Q&A: Honorific vs. Extra-modest", header_style))
    story.append(Paragraph("Read the Question (Honorific). Fill in the Answer using the <b>Extra-modest</b> form.", normal_style))
    story.append(Spacer(1, 6))

    # Q1
    story.append(Paragraph("<b>Q1:</b> お名前は何とおっしゃいますか。", normal_style))
    story.append(Paragraph("<b>A:</b> 田中と _____________________________ 。(say)", normal_style))
    story.append(Spacer(1, 8))

    # Q2
    story.append(Paragraph("<b>Q2:</b> どちらにいらっしゃいますか。", normal_style))
    story.append(Paragraph("<b>A:</b> 駅 (えき) に _____________________________ 。(go)", normal_style))
    story.append(Spacer(1, 8))

    # Q3
    story.append(Paragraph("<b>Q3:</b> トイレはどちらにありますか。", normal_style))
    story.append(Paragraph("<b>A:</b> あちらに _____________________________ 。(exist)", normal_style))
    story.append(Spacer(1, 8))

    # Q4
    story.append(Paragraph("<b>Q4:</b> 学生さんでいらっしゃいますか。", normal_style))
    story.append(Paragraph("<b>A:</b> はい、学生_____________________________ 。(is)", normal_style))
    story.append(Spacer(1, 20))

    # --- SECTION 3: BUSINESS DIALOGUE ---
    story.append(Paragraph("III. Business Dialogue: Honorific or Modest?", header_style))
    story.append(Paragraph("Circle the correct verb. Remember: Raise the customer up (Honorific), lower yourself down (Modest).", normal_style))
    story.append(Spacer(1, 6))

    dialogue = """
    <b>Situation:</b> Mr. Miller (Customer) visits a Japanese company.<br/><br/>
    <b>Receptionist:</b> いらっしゃいませ。<br/><br/>
    <b>Miller:</b> あの、私はミラーと ( a. おっしゃいます / b. 申 (もう) します )。<br/>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2時に山下先生に会うやくそくが<br/>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;( a. ございます / b. あります )。<br/><br/>
    <b>Receptionist:</b> ああ、ミラー様( a. でございます / b. でいらっしゃいます ) ね。<br/>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;お待ちして ( a. いました / b.おりました )。<br/><br/>
    <b>Miller:</b> よろしく ( a. お願 (ねが) いいたします / b. お願 (ねが) いなさいます )。<br/><br/>
    <b>Receptionist:</b> どうぞ、こちらへ。<br/>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ごあんない ( a. いたします / b. なさいます )。
    """
    story.append(Paragraph(dialogue, normal_style))

    # --- ANSWER KEY PAGE ---
    story.append(PageBreak())
    story.append(Paragraph("ANSWER KEY: Lesson 20 Extra-modest", title_style))
    
    story.append(Paragraph("<b>I. Table</b>", header_style))
    ans_table = """
    いる &rarr; <b>おります</b><br/>
    行く / 来る &rarr; <b>参 (まい) ります</b><br/>
    言う &rarr; <b>申 (もう) します</b><br/>
    する &rarr; <b>いたします</b><br/>
    食べる / 飲む &rarr; <b>いただきます</b><br/>
    ある &rarr; <b>ございます</b><br/>
    〜ている &rarr; <b>〜ております</b><br/>
    〜です &rarr; <b>〜でございます</b>
    """
    story.append(Paragraph(ans_table, normal_style))

    story.append(Paragraph("<b>II. Q&A</b>", header_style))
    ans_qa = """
    1. 田中と<b>申 (もう) します</b>。<br/>
    2. 駅へ<b>参 (まい) ります</b>。<br/>
    3. あちらに<b>ございます</b>。<br/>
    4. はい、学生<b>でございます</b>。
    """
    story.append(Paragraph(ans_qa, normal_style))

    story.append(Paragraph("<b>III. Dialogue</b>", header_style))
    ans_dialogue = """
    1. <b>(b) 申します</b><br/>
    2. <b>(a) ございます</b><br/>
    3. <b>(b) でいらっしゃいます</b><br/>
    4. <b>(b) おりました</b><br/>
    5. <b>(a) お願いいたします</b><br/>
    6. <b>(a) いたします</b>
    """
    story.append(Paragraph(ans_dialogue, normal_style))

    # Build PDF
    doc.build(story)
    print(f"Generated successfully: {filename}")

if __name__ == "__main__":
    create_worksheet()