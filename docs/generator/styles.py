from reportlab.lib.units import cm
from reportlab.lib.styles import (ParagraphStyle, getSampleStyleSheet)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, TableStyle
from .colors import *
defaultPageSize = 'A4'


styles = getSampleStyleSheet()
PAGE_HEIGHT = defaultPageSize[1]
PAGE_WIDTH = defaultPageSize[0]

pdfmetrics.registerFont(TTFont('FreeSans', 'FreeSans.ttf'))
pdfmetrics.registerFont(TTFont('FreeSansBold', 'FreeSansBold.ttf'))

text_table = TableStyle([('TEXTCOLOR', (0, 0), (-1, 0), col_pil_main_1),
                         ('FONT', (0, 0), (-1, 0), 'FreeSansBold'),
                         ('FONT', (0, 0), (0, -1), 'FreeSansBold'),
                         ('FONT', (1, 1), (-1, -1), 'FreeSans'),
                         ('FONTSIZE', (0, 0), (-1, -1), 8),
                         ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                         ('LINEBELOW', (0, 0), (-1, 0), 1.5, colors.black),
                         ('ALIGN', (1, 0), (-1, 0), 'LEFT'),
                         ('ALIGN', (1, 1), (-1, -1), 'LEFT'),
                         ('VALIGN', (0, 0), (-1, -1), 'TOP')
                         ])

details_table = TableStyle([('TEXTCOLOR', (0, 0), (-1, 0), col_pil_main_1),
                            ('FONT', (0, 0), (-1, 0), 'FreeSansBold'),
                            ('FONT', (0, 1), (0, -1), 'FreeSans'),
                            ('FONT', (1, 1), (-1, -1), 'FreeSans'),
                            ('FONTSIZE', (0, 0), (-1, -1), 8),
                            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                            ('LINEBELOW', (0, 0), (-1, 0), 1.5, colors.black),
                            ('ALIGN', (1, 0), (-1, 0), 'CENTER'),
                            ('ALIGN', (1, 1), (-1, -1), 'LEFT'),
                            ('VALIGN', (0, 0), (-1, -1), 'TOP')
                            ])

t1_style = ParagraphStyle(name='t1', fontName="FreeSansBold",
                          fontSize=12, leftIndent=2 * cm, rightIndent=2 * cm, alignment=1,
                          spaceBefore=2 * cm, spaceAfter=1.2 * cm)
pt1_style = ParagraphStyle(name='pt1', fontName="FreeSans",
                           fontSize=10, leftIndent=0, rightIndent=-1 * cm, alignment=4,
                           spaceBefore=0.3 * cm, spaceAfter=0.3 * cm, firstLineIndent=1 * cm)
intable_style = ParagraphStyle(name='intable', fontName="FreeSans",
                               fontSize=8, leftIndent=0, rightIndent=0, alignment=4,
                               spaceBefore=0.2 * cm, spaceAfter=0.2 * cm)
intable2_style = ParagraphStyle(name='intable', fontName="FreeSans",
                                fontSize=8, leftIndent=0, rightIndent=0, alignment=0,
                                spaceBefore=0.2 * cm, spaceAfter=0.2 * cm)
bl_style = ParagraphStyle(name='bl', fontName="FreeSans",
                          fontSize=10, leftIndent=1 * cm, rightIndent=-1 * cm, alignment=0,
                          spaceBefore=0 * cm, spaceAfter=0 * cm, bulletIndent=0 * cm)
t2_style = ParagraphStyle(name='t2', fontName="FreeSansBold",
                          fontSize=10, leftIndent=1 * cm, rightIndent=0, alignment=0,
                          spaceBefore=1 * cm, spaceAfter=0.6 * cm, textColor=col_pil_main_1,
                          bulletIndent=1 * cm, bulletFontName='FreeSansBold')
dn1_style = ParagraphStyle(name='dn1', fontName="FreeSansBold",
                           fontSize=10, leftIndent=100, alignment=0, textColor=col_pil_main_1)
pd1_style = ParagraphStyle(name='pd1', fontName="FreeSansBold",
                           fontSize=10, leftIndent=100, alignment=0, textColor=col_rep_white)
ft1_style = ParagraphStyle(name='ft1', fontName="FreeSans",
                           fontSize=8, leftIndent=100, alignment=0, textColor=col_pil_main_1)


def t2(t2_text):
    global num_seq
    t2_output = Paragraph(t2_text, t2_style, bulletText=str(num_seq) + '.')
    num_seq += 1
    return t2_output


def pt(pt_text):
    pt1_output = Paragraph(pt_text, pt1_style)
    return pt1_output


def bl(bl_text):
    bl_output = Paragraph(bl_text, bl_style, bulletText='-')
    return bl_output
