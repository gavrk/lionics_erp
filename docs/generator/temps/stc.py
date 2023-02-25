from random import randint
from time import strftime, gmtime

import pandas as pd
import os
from docs.models import StandardTesContract

# For python shell: from docs.generator.temps.stc import generate_stc_pdf

# Reading contract contents

settings_dir = os.path.dirname(__file__)
GENERATOR_ROOT = os.path.abspath(os.path.dirname(settings_dir))
content = pd.read_excel(GENERATOR_ROOT + '/contents/stc.xls')

def generate_stc_pdf(pk):

    # Defining current contract as a DB object

    cstc = StandardTesContract.objects.get(pk=pk)

    # Defining contract number

    if cstc.contract_number == '-':
        contract_id = f'{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}'
    else:
        contract_id = cstc.contract_number

    # Defining contract date

    if cstc.contract_date == '-':
        contract_date = strftime('%d.%m.%Y', gmtime())
    else:
        contract_date = cstc.contract_date

    print(contract_date)

    return cstc

