import os
import requests
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def get_japanese_font():
    """
    Downloads KleeOne-Regular.ttf (a handwritten-style Japanese font) 
    from the official Fontworks GitHub repo.
    """
    font_filename = "KleeOne-Regular.ttf"
    
    # Stable URL for Klee One Regular (Static TTF)
    url = "https://github.com/fontworks-fonts/Klee/raw/master/fonts/ttf/KleeOne-Regular.ttf"

    if not os.path.exists(font_filename):
        print(f"Downloading font: {font_filename}...")
        print("This may take a moment (approx 4MB)...")
        try:
            response = requests.get(url, allow_redirects=True)
            response.raise_for_status()
            
            # Sanity check: verify it's not a text file error page
            if b"<!DOCTYPE html>" in response.content[:100]:
                raise Exception("Download failed (got HTML instead of TTF).")
                
            with open(font_filename, "wb") as f:
                f.write(response.content)
            print("Font downloaded successfully.")
        except Exception as e:
            print(f"Error downloading font: {e}")
            print(f"Please manually download {font_filename} and place it in this folder.")
            return None
    
    return font_filename

def create_worksheet():
    # 1. Setup the Font
    font_path = get_japanese_font()
    
    if font_path:
        try:
            # Register the downloaded TrueType Font
            pdfmetrics.registerFont(TTFont('JapaneseFont', font_path))
            jp_font_name = 'JapaneseFont'
        except Exception as e:
            print(f"Font Error: {e}")
            print("Try deleting the .ttf file and running this script again.")
            return
    else:
        print("Warning: Could not load Japanese font. Text will not display.")
        jp_font_name = 'Helvetica'

    # 2. Setup the Document
    pdf_filename = "Genki_Honorifics_Worksheet.pdf"
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
        alignment=1 # Center
    )
    
    header_style = ParagraphStyle(
        'HeaderJP',
        parent=styles['Heading2'],
        fontName=jp_font_name,
        fontSize=14,
        spaceBefore=12,
        spaceAfter=6
    )
    
    normal_style = ParagraphStyle(
        'NormalJP',
        parent=styles['Normal'],
        fontName=jp_font_name,
        fontSize=11,
        leading=16, 
        spaceAfter=10
    )

    story = []

    # --- Content ---

    story.append(Paragraph("Genki II - Chapter 19: Honorifics (Keigo)", title_style))
    story.append(Paragraph("Name: __________________________   Date: ____________", normal_style))
    story.append(Spacer(1, 12))

    # Section 1
    story.append(Paragraph("I. Special Honorific Verbs (尊敬語)", header_style))
    story.append(Paragraph("Fill in the correct Special Honorific dictionary form.", normal_style))
    
    data1 = [
        ['Standard (辞書形)', 'Meaning', 'Honorific (尊敬語)'],
        ['いく / くる / いる', 'to go/come/be', '__________________'],
        ['たべる / のむ', 'to eat/drink', '__________________'],
        ['する', 'to do', '__________________'],
        ['いう', 'to say', '__________________'],
        ['みる', 'to see', '__________________'],
        ['寝る (ねる)', 'to sleep', '__________________'],
    ]
    
    t1 = Table(data1, colWidths=[150, 100, 180])
    t1.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), jp_font_name),
        ('GRID', (0,0), (-1,-1), 1, colors.black),
        ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
        ('PADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t1)
    story.append(Spacer(1, 20))

    # Section 2
    story.append(Paragraph("II. Dialogue: Teacher and Student", header_style))
    story.append(Paragraph("Fill in the blanks using the appropriate Honorific form.", normal_style))
    
    dialogue_text = """
    <b>Context:</b> A student sees their teacher at the station.<br/><br/>
    <b>Student:</b> 先生、こんにちは。どちらに (1) ________________________ か。<br/>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(iku: honorific)<br/><br/>
    <b>Teacher:</b> ああ、田中さん。ちょっとデパートに (2) ________________________。<br/>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(iku: polite)<br/><br/>
    <b>Student:</b> そうですか。先生、もうお昼ご飯を (3) ________________________ か。<br/>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(taberu: honorific)<br/><br/>
    <b>Teacher:</b> いいえ、まだ (4) ________________________。忙しかったですから。<br/>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(taberu: polite negative)<br/>
    """
    story.append(Paragraph(dialogue_text, normal_style))
    story.append(Spacer(1, 10))

    # Section 3
    story.append(Paragraph("III. Choose the Correct Sentence", header_style))
    story.append(Paragraph("Circle the correct Honorific sentence for the <b>Teacher's</b> actions.", normal_style))

    q1 = """
    1. The teacher reads a book.<br/>
    &nbsp;&nbsp;a) 先生は本を読みます。<br/>
    &nbsp;&nbsp;b) 先生は本をお読みになります。<br/>
    &nbsp;&nbsp;c) 先生は本をお読みします。<br/>
    """
    story.append(Paragraph(q1, normal_style))

    
    
    # Section 4
    story.append(Paragraph("IV. Honorific Nouns & Adjectives", header_style))
    story.append(Paragraph("Add 'お (o)' or 'ご (go)' to the words below.", normal_style))

    data4 = [
        ['Word', 'Polite Form'],
        ['名前 (Name)', '__________________'],
        ['忙しい (Busy)', '__________________'],
        ['家族 (Family)', '__________________'],
        ['電話 (Phone)', '__________________'],
    ]
    t4 = Table(data4, colWidths=[150, 180])
    t4.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), jp_font_name),
        ('GRID', (0,0), (-1,-1), 1, colors.black),
        ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
        ('PADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t4)

    # Build
    doc.build(story)
    print(f"PDF generated successfully: {pdf_filename}")

if __name__ == "__main__":
    create_worksheet()