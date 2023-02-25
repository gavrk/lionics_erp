from PIL import ImageColor
from reportlab.lib import colors

col_pil_main_1 = ImageColor.getrgb("#590059")
col_pil_main_2 = ImageColor.getrgb('#7F007F')
col_pil_light = ImageColor.getrgb('#ffd700')
col_pil_add_1 = ImageColor.getrgb('#42aaff')
col_pil_add_2 = ImageColor.getrgb('#b3b3b3')

col_rep_main_1 = colors.Color(red=(89.25/255), green=(0/255), blue=(89.25/255))
col_rep_white = colors.Color(red=(255/255), green=(255/255), blue=(255/255))