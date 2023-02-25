from random import randint
from time import strftime, gmtime
import pandas as pd
import os

from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

from docs.generator.corp_unipage import corp_unipage
from docs.generator.styles import intable2_style, styles, t1_style, pt1_style
from docs.models import StandardTesContract

# For python shell: from docs.generator.temps.stc import generate_stc_pdf

# Reading contract contents

settings_dir = os.path.dirname(__file__)
GENERATOR_ROOT = os.path.abspath(os.path.dirname(settings_dir))
content = pd.read_excel(GENERATOR_ROOT + '/contents/stc.xls')

def generate_stc_pdf(pk):

    # Defining current contract as a DB object

    stc = StandardTesContract.objects.get(pk=pk)

    # Defining contract number

    if stc.contract_number == '-':
        stc_id = f'{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}'
    else:
        stc_id = stc.contract_number

    # Defining contract date

    if stc.contract_date == '-':
        stc_date = strftime('%d.%m.%Y', gmtime())
    else:
        stc_date = '.'.join([
            stc.contract_date.split('-')[2], stc.contract_date.split('-')[1], stc.contract_date.split('-')[0]
        ])

    # Defining city of signing

    if stc.contract_city == '-':
        stc_city = 'г. Санкт-Петербург'
    else:
        stc_city = stc.contract_city

    # Defining customer company name

    if stc.customer == '-':
        stc_cust = 'НЕ УКАЗАНО'
    else:
        if stc.customer.company_type == 'ИП':
            stc_cust = stc.customer.company_type + ' ' + stc.customer.person_nom
        elif stc.customer.company_type == 'Физлицо':
            stc_cust = stc.customer.person_nom
        else:
            stc_cust = stc.customer.company_type + ' "' + stc.customer.company_name + '"'

    # Defining agent's company name

    if stc.agent == '-':
        stc_agent = 'НЕ УКАЗАНО'
    else:
        if stc.agent.company_type == 'ИП':
            stc_agent = stc.agent.company_type + ' ' + stc.agent.person_nom
        elif stc.agent.company_type == 'Физлицо':
            stc_agent = stc.agent.person_nom
        else:
            stc_agent = stc.agent.company_type + ' "' + stc.agent.company_name + '"'

    # Defining customers position and person in accusative

    if stc.customer.pos_per_acc == '-':
        stc_cust_ppa = 'НЕ УКАЗАНО'
    else:
        stc_cust_ppa = stc.customer.pos_per_acc

    # Defining agent's position and person in accusative

    if stc.agent.pos_per_acc == '-':
        stc_agent_ppa = 'НЕ УКАЗАНО'
    else:
        stc_agent_ppa = stc.agent.pos_per_acc

    # Defining customers representative's position in nominative

    if stc.customer.position_nom == '-':
        stc_cust_pos = 'НЕ УКАЗАНО'
    else:
        stc_cust_pos = stc.customer.position_nom

    # Defining agent's representative's position in nominative

    if stc.agent.position_nom == '-':
        stc_agent_pos = 'НЕ УКАЗАНО'
    else:
        stc_agent_pos = stc.agent.position_nom

    # Defining customer's representative's name in nominative

    if stc.customer.person_nom == '-':
        stc_cust_per = 'НЕ УКАЗАНО'
    else:
        stc_cust_per = stc.customer.person_nom

    # Defining agent's representative's name in nominative

    if stc.agent.person_nom == '-':
        stc_agent_per = 'НЕ УКАЗАНО'
    else:
        stc_agent_per = stc.agent.person_nom

    # Defining customer's authority (on the basis of ...) in accusative

    if stc.customer.acting_on == '-':
        stc_cust_act = 'Устава'
    else:
        stc_cust_act = stc.customer.acting_on

    # Defining customer's authority (on the basis of ...) in accusative

    if stc.agent.acting_on == '-':
        stc_agent_act = 'Устава'
    else:
        stc_agent_act = stc.agent.acting_on

    # Defining date of validity of the contract

    if stc.valid_until == '-':
        stc_val = strftime(f'31.12.%Y', gmtime())
    else:
        stc_val = stc.valid_until

    # Defining legal address of the customer

    if stc.customer.legal_addr == '-':
        stc_cust_leg = 'НЕ УКАЗАНО'
    else:
        stc_cust_leg = stc.customer.legal_addr

    # Defining legal address of the agent

    if stc.agent.legal_addr == '-':
        stc_agent_leg = 'НЕ УКАЗАНО'
    else:
        stc_agent_leg = stc.agent.legal_addr

    # Defining registration address of the customer

    if stc.customer.registration_addr == '-':
        stc_cust_reg = 'НЕ УКАЗАНО'
    else:
        stc_cust_reg = stc.customer.registration_addr

    # Defining registration address of the agent

    if stc.agent.registration_addr == '-':
        stc_agent_reg = 'НЕ УКАЗАНО'
    else:
        stc_agent_reg = stc.agent.registration_addr

    # Defining postal address of the customer

    if stc.customer.postal_addr == '-':
        if stc.customer.company_type == 'ИП' or stc.customer.company_type == 'Физлицо':
            stc_cust_post = stc_cust_reg
        else:
            stc_cust_post = stc_cust_leg
    else:
        stc_cust_post = stc.customer.postal_addr

    # Defining postal address of the agent

    if stc.agent.postal_addr == '-':
        if stc.agent.company_type == 'ИП' or stc.agent.company_type == 'Физлицо':
            stc_agent_post = stc_agent_reg
        else:
            stc_agent_post = stc_cust_leg
    else:
        stc_agent_post = stc.agent.postal_addr

    # Defining contact telephone of the customer

    if stc.customer.tel == '-':
        stc_cust_tel = 'НЕ УКАЗАНО'
    else:
        stc_cust_tel = stc.customer.tel

    # Defining contact telephone of the agent

    if stc.agent.tel == '-':
        stc_agent_tel = 'НЕ УКАЗАНО'
    else:
        stc_agent_tel = stc.agent.tel

    # Defining customer's email address

    if stc.customer.email == '-':
        stc_cust_email = 'НЕ УКАЗАНО'
    else:
        stc_cust_email = stc.customer.email

    # Defining agent's email address

    if stc.agent.email == '-':
        stc_agent_email = 'НЕ УКАЗАНО'
    else:
        stc_agent_email = stc.agent.email

    # Defining customer's bank name

    if stc.customer.bank_name == '-':
        stc_cust_bank = 'НЕ УКАЗАНО'
    else:
        stc_cust_bank = stc.customer.bank_name

    # Defining agent's bank name

    if stc.agent.bank_name == '-':
        stc_agent_bank = 'НЕ УКАЗАНО'
    else:
        stc_agent_bank = stc.agent.bank_name

    # Defining customer's BIC

    if stc.customer.bic == '-':
        stc_cust_bic = 'НЕ УКАЗАНО'
    else:
        stc_cust_bic = stc.customer.bic

    # Defining agent's BIC

    if stc.agent.bic == '-':
        stc_agent_bic = 'НЕ УКАЗАНО'
    else:
        stc_agent_bic = stc.agent.bic

    # Defining customer's current account

    if stc.customer.curr_acc == '-':
        stc_cust_curr = 'НЕ УКАЗАНО'
    else:
        stc_cust_curr = stc.customer.curr_acc

    # Defining agent's current account

    if stc.agent.curr_acc == '-':
        stc_agent_curr = 'НЕ УКАЗАНО'
    else:
        stc_agent_curr = stc.agent.curr_acc

    # Defining customer's correspondent account

    if stc.customer.corr_acc == '-':
        stc_cust_corr = 'НЕ УКАЗАНО'
    else:
        stc_cust_corr = stc.customer.corr_acc

    # Defining agent's correspondent account

    if stc.agent.corr_acc == '-':
        stc_agent_corr = 'НЕ УКАЗАНО'
    else:
        stc_agent_corr = stc.agent.corr_acc

    # Defining customer's INN

    if stc.customer.inn == '-':
        stc_cust_inn = 'НЕ УКАЗАНО'
    else:
        stc_cust_inn = stc.customer.inn

    # Defining agent's INN

    if stc.agent.inn == '-':
        stc_agent_inn = 'НЕ УКАЗАНО'
    else:
        stc_agent_inn = stc.agent.inn

    # Defining customer's KPP

    if stc.customer.kpp == '-':
        stc_cust_kpp = 'НЕ УКАЗАНО'
    else:
        stc_cust_kpp = stc.customer.kpp

    # Defining agent's KPP

    if stc.agent.kpp == '-':
        stc_agent_kpp = 'НЕ УКАЗАНО'
    else:
        stc_agent_kpp = stc.agent.kpp

    # Defining customer's OGRN

    if stc.customer.ogrn == '-':
        stc_cust_ogrn = 'НЕ УКАЗАНО'
    else:
        stc_cust_ogrn = stc.customer.ogrn

    # Defining agent's OGRN

    if stc.agent.ogrn == '-':
        stc_agent_ogrn = 'НЕ УКАЗАНО'
    else:
        stc_agent_ogrn = stc.agent.ogrn

    # Defining customer's OKPO

    if stc.customer.okpo == '-':
        stc_cust_okpo = 'НЕ УКАЗАНО'
    else:
        stc_cust_okpo = stc.customer.okpo

    # Defining agent's OKPO

    if stc.agent.okpo == '-':
        stc_agent_okpo = 'НЕ УКАЗАНО'
    else:
        stc_agent_okpo = stc.agent.okpo

    # Defining if stamp is needed

    if stc.stamp == '-':
        stc_stamp = False
    else:
        stc_stamp = stc.stamp

    # Defining if blank is needed

    if stc.blank == '-':
        stc_blank = False
    else:
        stc_blank = stc.blank

    # Defining customer's passport series

    if stc.customer.passport_series == '-':
        stc_cust_ps = 'НЕ УКАЗАНО'
    else:
        stc_cust_ps = stc.customer.passport_series

    # Defining agent's passport series

    if stc.agent.passport_series == '-':
        stc_agent_ps = 'НЕ УКАЗАНО'
    else:
        stc_agent_ps = stc.agent.passport_series

    # Defining customer's passport number

    if stc.customer.passport_number == '-':
        stc_cust_pn = 'НЕ УКАЗАНО'
    else:
        stc_cust_pn = stc.customer.passport_number

    # Defining agent's passport number

    if stc.agent.passport_number == '-':
        stc_agent_pn = 'НЕ УКАЗАНО'
    else:
        stc_agent_pn = stc.agent.passport_number

    # Defining customer's passport issued by whom

    if stc.customer.pass_issued_by == '-':
        stc_cust_pissby = 'НЕ УКАЗАНО'
    else:
        stc_cust_pissby = stc.customer.pass_issued_by

    # Defining agent's passport issued by whom

    if stc.agent.pass_issued_by == '-':
        stc_agent_pissby = 'НЕ УКАЗАНО'
    else:
        stc_agent_pissby = stc.agent.pass_issued_by

    # Defining customer's passport issue date

    if stc.customer.pass_issued_date == '-':
        stc_cust_pissdt = 'НЕ УКАЗАНО'
    else:
        stc_cust_pissdt = stc.customer.pass_issued_date

    # Defining agent's passport issue date

    if stc.agent.pass_issued_date == '-':
        stc_agent_pissdt = 'НЕ УКАЗАНО'
    else:
        stc_agent_pissdt = stc.agent.pass_issued_date

    # Defining customer's passport issue code

    if stc.customer.pass_issued_code == '-':
        stc_cust_pisscd = 'НЕ УКАЗАНО'
    else:
        stc_cust_pisscd = stc.customer.pass_issued_code

    # Defining agent's passport issue code

    if stc.agent.pass_issued_code == '-':
        stc_agent_pisscd = 'НЕ УКАЗАНО'
    else:
        stc_agent_pisscd = stc.agent.pass_issued_code

    # Creating details for contract

    if stc.agent.company_type == 'ИП':
        stc_agent_det = f'<font face="FreeSansBold">{stc_agent}</font face="FreeSansBold"><br/><br/>\
        <font face="FreeSansBold">Адрес прописки:</font face="FreeSansBold"> {stc_agent_reg}<br/>\
        <font face="FreeSansBold">Почтовый адрес:</font face="FreeSansBold"> {stc_agent_post}<br/>\
        <font face="FreeSansBold">Телефон:</font face="FreeSansBold"> {stc_agent_tel}<br/>\
        <font face="FreeSansBold">E-mail:</font face="FreeSansBold"> {stc_agent_email}<br/>\
        <font face="FreeSansBold">Банковские реквизиты</font face="FreeSansBold"><br/>\
        <font face="FreeSansBold">Банк:</font face="FreeSansBold"> {stc_agent_bank}<br/>\
        <font face="FreeSansBold">БИК:</font face="FreeSansBold"> {stc_agent_bic}<br/>\
        <font face="FreeSansBold">Р/с:</font face="FreeSansBold"> {stc_agent_curr}<br/>\
        <font face="FreeSansBold">Корр/с:</font face="FreeSansBold"> {stc_agent_corr}<br/>\
        <font face="FreeSansBold">ИНН:</font face="FreeSansBold"> {stc_agent_inn}<br/>\
        <font face="FreeSansBold">ОКПО:</font face="FreeSansBold"> {stc_agent_okpo}<br/>\
        <font face="FreeSansBold">ОГРНИП:</font face="FreeSansBold"> {stc_agent_ogrn}<br/><br/>\
        {stc.agent.company_type}<br/><br/><br/>______________________ {stc_agent_per}'
    elif stc.agent.company_type == 'Физлицо':
        stc_agent_det = f'<font face="FreeSansBold">{stc_agent}</font face="FreeSansBold"><br/><br/>\
        <font face="FreeSansBold">Паспорт:</font face="FreeSansBold"> {stc_agent_ps} {stc_agent_pn}<br/>\
        <font face="FreeSansBold">Выдан:</font face="FreeSansBold"> {stc_agent_pissby}<br/>\
        <font face="FreeSansBold">Дата выдачи:</font face="FreeSansBold"> {stc_agent_pissdt}<br/>\
        <font face="FreeSansBold">Код подразделения:</font face="FreeSansBold"> {stc_agent_pisscd}<br/><br/>\
        <font face="FreeSansBold">Адрес прописки:</font face="FreeSansBold"> {stc_agent_reg}<br/>\
        <font face="FreeSansBold">Почтовый адрес:</font face="FreeSansBold"> {stc_agent_post}<br/>\
        <font face="FreeSansBold">Телефон:</font face="FreeSansBold"> {stc_agent_tel}<br/>\
        <font face="FreeSansBold">E-mail:</font face="FreeSansBold"> {stc_agent_email}<br/>\
        <font face="FreeSansBold">Банковские реквизиты</font face="FreeSansBold"><br/>\
        <font face="FreeSansBold">Банк:</font face="FreeSansBold"> {stc_agent_bank}<br/>\
        <font face="FreeSansBold">БИК:</font face="FreeSansBold"> {stc_agent_bic}<br/>\
        <font face="FreeSansBold">Р/с:</font face="FreeSansBold"> {stc_agent_curr}<br/>\
        <font face="FreeSansBold">Корр/с:</font face="FreeSansBold"> {stc_agent_corr}<br/>\
        <font face="FreeSansBold">ИНН:</font face="FreeSansBold"> {stc_agent_inn}<br/><br/>\
        {stc.agent.company_type}<br/><br/><br/>______________________ {stc_agent_per}'
    else:
        stc_agent_det = f'<font face="FreeSansBold">{stc_agent}</font face="FreeSansBold"><br/><br/>\
        <font face="FreeSansBold">Юр. адрес:</font face="FreeSansBold"> {stc_agent_leg}<br/>\
        <font face="FreeSansBold">Почтовый адрес:</font face="FreeSansBold"> {stc_agent_post}<br/>\
        <font face="FreeSansBold">Телефон:</font face="FreeSansBold"> {stc_agent_tel}<br/>\
        <font face="FreeSansBold">E-mail:</font face="FreeSansBold"> {stc_agent_email}<br/>\
        <font face="FreeSansBold">Банковские реквизиты</font face="FreeSansBold"><br/>\
        <font face="FreeSansBold">Банк:</font face="FreeSansBold"> {stc_agent_bank}<br/>\
        <font face="FreeSansBold">БИК:</font face="FreeSansBold"> {stc_agent_bic}<br/>\
        <font face="FreeSansBold">Р/с:</font face="FreeSansBold"> {stc_agent_curr}<br/>\
        <font face="FreeSansBold">Корр/с:</font face="FreeSansBold"> {stc_agent_corr}<br/>\
        <font face="FreeSansBold">ИНН/КПП:</font face="FreeSansBold"> {stc_agent_inn}/{stc_agent_kpp}<br/>\
        <font face="FreeSansBold">ОГРН:</font face="FreeSansBold"> {stc_agent_ogrn}<br/><br/>\
        {stc_agent_pos}<br/><br/><br/>______________________ {stc_agent_per}'

    if stc.customer.company_type == 'ИП':
        stc_cust_det = f'<font face="FreeSansBold">{stc_cust}</font face="FreeSansBold"><br/><br/>\
        <font face="FreeSansBold">Адрес прописки:</font face="FreeSansBold"> {stc_cust_reg}<br/>\
        <font face="FreeSansBold">Почтовый адрес:</font face="FreeSansBold"> {stc_cust_post}<br/>\
        <font face="FreeSansBold">Телефон:</font face="FreeSansBold"> {stc_cust_tel}<br/>\
        <font face="FreeSansBold">E-mail:</font face="FreeSansBold"> {stc_cust_email}<br/>\
        <font face="FreeSansBold">Банковские реквизиты</font face="FreeSansBold"><br/>\
        <font face="FreeSansBold">Банк:</font face="FreeSansBold"> {stc_cust_bank}<br/>\
        <font face="FreeSansBold">БИК:</font face="FreeSansBold"> {stc_cust_bic}<br/>\
        <font face="FreeSansBold">Р/с:</font face="FreeSansBold"> {stc_cust_curr}<br/>\
        <font face="FreeSansBold">Корр/с:</font face="FreeSansBold"> {stc_cust_corr}<br/>\
        <font face="FreeSansBold">ИНН:</font face="FreeSansBold"> {stc_cust_inn}<br/>\
        <font face="FreeSansBold">ОКПО:</font face="FreeSansBold"> {stc_cust_okpo}<br/>\
        <font face="FreeSansBold">ОГРНИП:</font face="FreeSansBold"> {stc_cust_ogrn}<br/><br/>\
        {stc.customer.company_type}<br/><br/><br/>______________________ {stc_cust_per}'
    elif stc.customer.company_type == 'Физлицо':
        stc_cust_det = f'<font face="FreeSansBold">{stc_cust}</font face="FreeSansBold"><br/><br/>\
        <font face="FreeSansBold">Паспорт:</font face="FreeSansBold"> {stc_cust_ps} {stc_cust_pn}<br/>\
        <font face="FreeSansBold">Выдан:</font face="FreeSansBold"> {stc_cust_pissby}<br/>\
        <font face="FreeSansBold">Дата выдачи:</font face="FreeSansBold"> {stc_cust_pissdt}<br/>\
        <font face="FreeSansBold">Код подразделения:</font face="FreeSansBold"> {stc_cust_pisscd}<br/><br/>\
        <font face="FreeSansBold">Адрес прописки:</font face="FreeSansBold"> {stc_cust_reg}<br/>\
        <font face="FreeSansBold">Почтовый адрес:</font face="FreeSansBold"> {stc_cust_post}<br/>\
        <font face="FreeSansBold">Телефон:</font face="FreeSansBold"> {stc_cust_tel}<br/>\
        <font face="FreeSansBold">E-mail:</font face="FreeSansBold"> {stc_cust_email}<br/>\
        <font face="FreeSansBold">Банковские реквизиты</font face="FreeSansBold"><br/>\
        <font face="FreeSansBold">Банк:</font face="FreeSansBold"> {stc_cust_bank}<br/>\
        <font face="FreeSansBold">БИК:</font face="FreeSansBold"> {stc_cust_bic}<br/>\
        <font face="FreeSansBold">Р/с:</font face="FreeSansBold"> {stc_cust_curr}<br/>\
        <font face="FreeSansBold">Корр/с:</font face="FreeSansBold"> {stc_cust_corr}<br/>\
        <font face="FreeSansBold">ИНН:</font face="FreeSansBold"> {stc_cust_inn}<br/><br/>\
        {stc.customer.company_type}<br/><br/><br/>______________________ {stc_cust_per}'
    else:
        stc_cust_det = f'<font face="FreeSansBold">{stc_cust}</font face="FreeSansBold"><br/><br/>\
        <font face="FreeSansBold">Юр. адрес:</font face="FreeSansBold"> {stc_cust_leg}<br/>\
        <font face="FreeSansBold">Почтовый адрес:</font face="FreeSansBold"> {stc_cust_post}<br/>\
        <font face="FreeSansBold">Телефон:</font face="FreeSansBold"> {stc_cust_tel}<br/>\
        <font face="FreeSansBold">E-mail:</font face="FreeSansBold"> {stc_cust_email}<br/>\
        <font face="FreeSansBold">Банковские реквизиты</font face="FreeSansBold"><br/>\
        <font face="FreeSansBold">Банк:</font face="FreeSansBold"> {stc_cust_bank}<br/>\
        <font face="FreeSansBold">БИК:</font face="FreeSansBold"> {stc_cust_bic}<br/>\
        <font face="FreeSansBold">Р/с:</font face="FreeSansBold"> {stc_cust_curr}<br/>\
        <font face="FreeSansBold">Корр/с:</font face="FreeSansBold"> {stc_cust_corr}<br/>\
        <font face="FreeSansBold">ИНН/КПП:</font face="FreeSansBold"> {stc_cust_inn}/{stc_cust_kpp}<br/>\
        <font face="FreeSansBold">ОГРН:</font face="FreeSansBold"> {stc_cust_ogrn}<br/><br/>\
        {stc_cust_pos}<br/><br/><br/>______________________ {stc_cust_per}'

    details_columns = ['Экспедитор', 'Клиент']
    details_content = [
        [Paragraph(stc_agent_det, intable2_style),
         Paragraph(stc_cust_det, intable2_style)],
    ]
    details_content.insert(0, details_columns)

    # Creating contract

    num_seq = 1

    def main_tes_contract():

        global num_seq

        doc = SimpleDocTemplate(f'Договор {stc_id} {stc_agent} - {stc_cust} от {stc_date}.pdf')
        doc.leftMargin, doc.bottomMargin, doc.rightMargin, doc.topMargin = 2.5 * cm, 3 * cm, 3 * cm, 4 * cm

        Story = [Spacer(0, -1 * cm)]
        style = styles["Normal"]

        t1_text = f'Договор № {stc_id} <br/> на транспортно-экспедиционное обслуживание'
        t1 = Paragraph(t1_text, t1_style)
        Story.append(t1)

        if stc.agent.company_type == 'ИП':
            preamble_1st = f'<font face="FreeSansBold">{stc_agent}</font face="FreeSansBold"> \
            именуемый в дальнейшем "Экспедитор", с одной стороны, и '
        elif stc.agent.company_type == 'Физлицо':
            preamble_1st = f'<font face="FreeSansBold">{stc_agent}</font face="FreeSansBold">, \
            паспорт серия {stc_agent_ps}, номер {stc_agent_pn}, выдан {stc_agent_pissby}, дата выдачи \
            {stc_agent_pissdt}, код подразделения {stc_agent_pisscd}, именуемый(ая) в дальнейшем "Экспедитор", \
            с одной стороны, и '
        else:
            preamble_1st = f'<font face="FreeSansBold">{stc_agent}</font face="FreeSansBold"> \
            в лице {stc_agent_ppa}, действующего(ей) на основании {stc_agent_act}, именуемое в дальнейшем "Экспедитор", \
            с одной стороны, и '

        if stc.customer.company_type == 'ИП':
            preamble_2nd = f'<font face="FreeSansBold">{stc_cust}</font face="FreeSansBold">, именуемый в дальнейшем "Клиент" \
            с другой стороны, далее совместно именуемые "Стороны", заключили настоящий Договор о нижеследующем:'
        elif stc.customer.company_type == 'Физлицо':
            preamble_2nd = f'<font face="FreeSansBold">{stc_cust}</font face="FreeSansBold">, \
            паспорт серия {stc_cust_ps}, номер {stc_cust_pn}, выдан {stc_cust_pissby}, дата выдачи \
            {stc_cust_pissdt}, код подразделения {stc_cust_pisscd}, именуемый(ая) в дальнейшем "Клиент", \
            с другой стороны, далее совместно именуемые "Стороны", заключили настоящий Договор о нижеследующем:'
        else:
            preamble_2nd = f'<font face="FreeSansBold">{stc_cust}</font face="FreeSansBold"> \
            в лице {stc_cust_ppa}, действующего(ей) на основании {stc_cust_act}, именуемое в дальнейшем "Клиент", \
            с другой стороны, далее совместно именуемые "Стороны", заключили настоящий Договор о нижеследующем:'

        pt1_text = preamble_1st + preamble_2nd
        pt1 = Paragraph(pt1_text, pt1_style)
        Story.append(pt1)

        for i in content.index:
            if len(content['point'][i].split('.')) > 2:
                pt_text = f'<font face="FreeSansBold">{content["point"][i]}\
                </font face="FreeSansBold"> {content["basic_ver"][i]}'
            else:
                pt_text = f'<font face="FreeSansBold">{content["point"][i]}\
                {content["basic_ver"][i]}</font face="FreeSansBold">'
            pt2 = Paragraph(pt_text, pt1_style)
            Story.append(pt2)

        # Start adding blocks

        doc.build(Story, onFirstPage=corp_unipage, onLaterPages=corp_unipage)

    if __name__ == "__main__":
        main_tes_contract()  # Printing the pdf







    print(stc_cust_per)

    return stc

