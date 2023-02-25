import pandas as pd
import os

settings_dir = os.path.dirname(__file__)
GENERATOR_ROOT = os.path.abspath(os.path.dirname(settings_dir))

content = pd.read_excel(GENERATOR_ROOT + '/contents/stc.xls')

print(content)