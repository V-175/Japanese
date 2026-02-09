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

# Basic Font Registration Check
if os.path.exists(font_filename):
    try:
        pdfmetrics.registerFont(TTFont(jp_font_name, font_filename))
    except Exception as e:
        print(f"Font Error: {e}")
        jp_font_name = 'Helvetica'
else:
    print(f"Warning: {font_filename} not found. Japanese text will not display.")
    jp_font_name = 'Helvetica'

# --- STYLES ---
styles = getSampleStyleSheet()
title_style = ParagraphStyle('TitleJP', parent=styles['Heading1'], fontName=jp_font_name, fontSize=18, alignment=1, spaceAfter=12)
header_style = ParagraphStyle('HeaderJP', parent=styles['Heading2'], fontName=jp_font_name, fontSize=14, spaceBefore=12, spaceAfter=6, textColor=colors.darkblue)
normal_style = ParagraphStyle('NormalJP', parent=styles['Normal'], fontName=jp_font_name, fontSize=11, leading=16, spaceAfter=10)
answer_style = ParagraphStyle('AnswerJP', parent=normal_style, textColor=colors.red)

# --- HELPER FUNCTION ---
def create_pdf(filename, content_data):
    doc = SimpleDocTemplate(filename, pagesize=A4, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=72)
    story = []
    
    for item in content_data:
        if item['type'] == 'title':
            story.append(Paragraph(item['text'], title_style))
        elif item['type'] == 'header':
            story.append(Paragraph(item['text'], header_style))
        elif item['type'] == 'text':
            story.append(Paragraph(item['text'], normal_style))
        elif item['type'] == 'table':
            t = Table(item['data'], colWidths=item['widths'])
            t.setStyle(TableStyle([
                ('FONTNAME', (0,0), (-1,-1), jp_font_name),
                ('GRID', (0,0), (-1,-1), 1, colors.black),
                ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
                ('PADDING', (0,0), (-1,-1), 6),
                ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ]))
            story.append(t)
            story.append(Spacer(1, 12))
        elif item['type'] == 'break':
            story.append(PageBreak())
        elif item['type'] == 'spacer':
            story.append(Spacer(1, 15))

    doc.build(story)
    print(f"Generated: {filename}")

# --- CONTENT: WORKSHEET 2 (Respectful Advice & Gratitude) ---
ws2_content = [
    {'type': 'title', 'text': 'Genki II L19: Respectful Advice & Gratitude'},
    
    # Grammar 2: お + Verb Stem + ください
    {'type': 'header', 'text': 'I. Respectful Advice (お + Stem + ください)'},
    {'type': 'text', 'text': 'Imagine you are a store clerk or station attendant. Change the following polite requests into Respectful Advice.'},
    {'type': 'table', 'widths': [150, 200], 'data': [
        ['Standard Polite (てください)', 'Respectful Advice (お〜ください)'],
        ['入ってください (はいる)', '___________________________'],
        ['待ってください (まつ)', '___________________________'],
        ['切符を取ってください (とる)', '___________________________'],
        ['説明を読んでください (よむ)', '___________________________'],
        ['家に帰ってください (かえる)', '___________________________'],
    ]},
    
    # Grammar 3: ～てくれてありがとう
    {'type': 'header', 'text': 'II. Expressing Gratitude (～てくれてありがとう)'},
    {'type': 'text', 'text': 'You are talking to a friend. Express gratitude for the specific actions below.'},
    {'type': 'text', 'text': '<b>Example:</b> Friend helped you. <br/>&nbsp;&rightarrow; 手伝ってくれてありがとう。 (Tetsudatte kurete arigatou.)'},
    {'type': 'spacer'},
    
    {'type': 'text', 'text': '1. Your friend wrote a recommendation letter (すいせんじょう) for you.'},
    {'type': 'text', 'text': '&nbsp;&nbsp;&nbsp;_________________________________________________________'},
    
    {'type': 'text', 'text': '2. Your friend came to pick you up (むかえにくる) at the station.'},
    {'type': 'text', 'text': '&nbsp;&nbsp;&nbsp;_________________________________________________________'},
    
    {'type': 'text', 'text': '3. Your friend waited (まつ) for you for one hour.'},
    {'type': 'text', 'text': '&nbsp;&nbsp;&nbsp;_________________________________________________________'},
    
    {'type': 'text', 'text': '4. Your friend lent (かす) you money.'},
    {'type': 'text', 'text': '&nbsp;&nbsp;&nbsp;_________________________________________________________'},

    # Translation Challenge
    {'type': 'header', 'text': 'III. Dialogue Translation'},
    {'type': 'text', 'text': 'Translate the bracketed English into Japanese.'},
    {'type': 'text', 'text': '<b>A:</b> This bag is heavy...'},
    {'type': 'text', 'text': '<b>B:</b> I will carry it. (Use <i>Humble</i>: motsu -> o-mochi shimasu)'},
    {'type': 'text', 'text': '<b>A:</b> Really? [Thank you for carrying it.]'},
    
    
    # Answer Key Page
    {'type': 'break'},
    {'type': 'header', 'text': 'ANSWER KEY'},
    {'type': 'text', 'text': '<b>I. Respectful Advice</b><br/>1. お入りください (O-hairi kudasai)<br/>2. お待ちください (O-machi kudasai)<br/>3. お取りください (O-tori kudasai)<br/>4. お読みください (O-yomi kudasai)<br/>5. お帰りください (O-kaeri kudasai)'},
    {'type': 'text', 'text': '<b>II. Gratitude</b><br/>1. すいせんじょうを書いてくれてありがとう。<br/>2. (駅まで) むかえに来てくれてありがとう。<br/>3. 待ってくれてありがとう。<br/>4. (お金を) 貸してくれてありがとう。'},
    {'type': 'text', 'text': '<b>III. Translation</b><br/>持ってくれてありがとう (Motte kurete arigatou)'},
]

# --- CONTENT: WORKSHEET 3 (Gladness & Expectations) ---
ws3_content = [
    {'type': 'title', 'text': 'Genki II L19: Reflections & Expectations'},

    # Grammar 4: ～てよかったです
    {'type': 'header', 'text': 'I. I am glad that... (～てよかったです)'},
    {'type': 'text', 'text': 'Combine the situation with "yokatta desu". Pay attention to Positive (〜て) vs Negative (〜なくて).'},
    {'type': 'table', 'widths': [200, 200], 'data': [
        ['Situation', 'Result ("I am glad that...")'],
        ['I studied Japanese. (勉強する)', '___________________________'],
        ['I did not catch a cold. (風邪をひく)', '___________________________'],
        ['I went to the festival. (お祭りに行く)', '___________________________'],
        ['I did not give up. (あきらめる)', '___________________________'],
    ]},
    
    # Grammar 5: ～はずです
    {'type': 'header', 'text': 'II. Expectations (～はずです)'},
    {'type': 'text', 'text': 'Finish the sentences based on logical expectation. <br/>(Remember: Nouns take <b>no</b> / Na-adj take <b>na</b> before hazu)'},
    
    {'type': 'text', 'text': '1. Tanaka-san lived in America for 10 years.'},
    {'type': 'text', 'text': '&nbsp;&nbsp;&nbsp;He [should be able to speak English].'},
    {'type': 'text', 'text': '&nbsp;&nbsp;&nbsp;田中さんは ___________________________________ です。'},
    
    {'type': 'text', 'text': '2. Today is a national holiday (祝日).'},
    {'type': 'text', 'text': '&nbsp;&nbsp;&nbsp;The bank [should be closed (shimaru)].'},
    {'type': 'text', 'text': '&nbsp;&nbsp;&nbsp;銀行は _______________________________________ です。'},

    {'type': 'text', 'text': '3. Mary studied very hard.'},
    {'type': 'text', 'text': '&nbsp;&nbsp;&nbsp;The exam [should not be difficult].'},
    {'type': 'text', 'text': '&nbsp;&nbsp;&nbsp;試験は _______________________________________ です。'},
    
   

    # Answer Key Page
    {'type': 'break'},
    {'type': 'header', 'text': 'ANSWER KEY'},
    {'type': 'text', 'text': '<b>I. Glad that...</b><br/>1. 勉強してよかったです。<br/>2. 風邪をひかなくてよかったです。<br/>3. お祭りに行ってよかったです。<br/>4. あきらめなくてよかったです。'},
    {'type': 'text', 'text': '<b>II. Expectations</b><br/>1. 英語が話せるはずです (Eigo ga hanaseru hazu desu)<br/>2. 閉まっているはずです (Shimatteiru hazu desu)<br/>3. 難しくないはずです (Muzukashikunai hazu desu)'},
  
]

# --- GENERATE FILES ---
if __name__ == "__main__":
    create_pdf("Genki_L19_Worksheet_Interact.pdf", ws2_content)
    create_pdf("Genki_L19_Worksheet_Reflect.pdf", ws3_content)