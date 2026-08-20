import io, re, zipfile, requests
import pandas as pd
from io import StringIO

BASE_URL = "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/"

factors_list = ["size","value","momentum","profitability","cashflow","investment"]

filename_dict = {
	"size" : "Portfolios_Formed_on_ME",
	"value" : "Portfolios_Formed_on_BE-ME",
	"momentum" : "10_Portfolios_Prior_12_2",
	"profitability" : "Portfolios_Formed_on_OP",
	"cashflow" : "Portfolios_Formed_on_CF-P",
	"investment" : "Portfolios_Formed_on_INV"
}

section_key_dict_monthly = {
	"size" : 'Average Value Weight Returns -- Monthly',
	"value" : 'Value Weight Returns -- Monthly',
	"momentum" : 'Value Weight Returns -- Monthly',
	"profitability" : 'Average Value Weight Returns -- Monthly',
	"cashflow" : 'Value Weight Returns -- Monthly',
	"investment" : 'Average Value Weight Returns -- Monthly'
}

section_key_dict_annual = {
	"size" : 'Value Weight Returns -- Annual from January to December',
	"value" : 'Value Weight Returns -- Annual from January to December',
	"momentum" : 'Average Value Weighted Returns -- Annual',
	"profitability" : 'Value Weight Returns -- Annual from January to December',
	"cashflow" : 'Value Weight Returns -- Annual from January to December',
	"investment" : 'Value Weight Returns -- Annual from January to December'
}

column_names_dict = {
	"size" : {
            'Negative' : '<= 0',
            'lo30' : 'Lo 30',
            'med40' : 'Med 40',
            'hi30' : 'Hi 30',
            'q1' : 'Lo 20',
            'q2' : 'Qnt 2',
            'q3' : 'Qnt 3',
            'q4' : 'Qnt 4',
            'q5' : 'Hi 20',
            'd1' : 'Lo 10',
            'd2' : '2-Dec',
            'd3' : '3-Dec',
            'd4' : '4-Dec',
            'd5' : '5-Dec',
            'd6' : '6-Dec',
            'd7' : '7-Dec',
            'd8' : '8-Dec',
            'd9' : '9-Dec',
            'd10' : 'Hi 10'
        },
	"value" : {
            'Negative' : '<= 0',
            'lo30' : 'Lo 30',
            'med40' : 'Med 40',
            'hi30' : 'Hi 30',
            'q1' : 'Lo 20',
            'q2' : 'Qnt 2',
            'q3' : 'Qnt 3',
            'q4' : 'Qnt 4',
            'q5' : 'Hi 20',
            'd1' : 'Lo 10',
            'd2' : '2-Dec',
            'd3' : '3-Dec',
            'd4' : '4-Dec',
            'd5' : '5-Dec',
            'd6' : '6-Dec',
            'd7' : '7-Dec',
            'd8' : '8-Dec',
            'd9' : '9-Dec',
            'd10' : 'Hi 10'
	},
	"momentum" : {
           'd1' : 'Lo PRIOR',
           'd2' : 'PRIOR 2',
           'd3' : 'PRIOR 3',
           'd4' : 'PRIOR 4',
           'd5' : 'PRIOR 5',
           'd6' : 'PRIOR 6',
           'd7' : 'PRIOR 7',
           'd8' : 'PRIOR 8',
           'd9' : 'PRIOR 9',
           'd10' : 'Hi PRIOR'
        },
	"profitability" : {
            'lo30' : 'Lo 30',
            'med40' : 'Med 40',
            'hi30' : 'Hi 30',
            'q1' : 'Lo 20',
            'q2' : 'Qnt 2',
            'q3' : 'Qnt 3',
            'q4' : 'Qnt 4',
            'q5' : 'Hi 20',
            'd1' : 'Lo 10',
            'd2' : '2-Dec',
            'd3' : '3-Dec',
            'd4' : '4-Dec',
            'd5' : '5-Dec',
            'd6' : '6-Dec',
            'd7' : '7-Dec',
            'd8' : '8-Dec',
            'd9' : '9-Dec',
            'd10' : 'Hi 10'
	},
	"cashflow" : {
            'Negative' : '<= 0',
            'lo30' : 'Lo 30',
            'med40' : 'Med 40',
            'hi30' : 'Hi 30',
            'q1' : 'Lo 20',
            'q2' : 'Qnt 2',
            'q3' : 'Qnt 3',
            'q4' : 'Qnt 4',
            'q5' : 'Hi 20',
            'd1' : 'Lo 10',
            'd2' : '2-Dec',
            'd3' : '3-Dec',
            'd4' : '4-Dec',
            'd5' : '5-Dec',
            'd6' : '6-Dec',
            'd7' : '7-Dec',
            'd8' : '8-Dec',
            'd9' : '9-Dec',
            'd10' : 'Hi 10'
	},
	"investment" : {
            'lo30' : 'Lo 30',
            'med40' : 'Med 40',
            'hi30' : 'Hi 30',
            'q1' : 'Lo 20',
            'q2' : 'Qnt 2',
            'q3' : 'Qnt 3',
            'q4' : 'Qnt 4',
            'q5' : 'Hi 20',
            'd1' : 'Lo 10',
            'd2' : '2-Dec',
            'd3' : '3-Dec',
            'd4' : '4-Dec',
            'd5' : '5-Dec',
            'd6' : '6-Dec',
            'd7' : '7-Dec',
            'd8' : '8-Dec',
            'd9' : '9-Dec',
            'd10' : 'Hi 10'
	}
}

def read_French_portfolios(filename, session=None, timeout=30):
    zip_filename = filename + '_CSV.zip'
    csv_filename = filename + '.csv'
    
    url = BASE_URL + zip_filename

    sess = session or requests.Session()
    r = sess.get(url,timeout=timeout)
    r.raise_for_status()

    z = zipfile.ZipFile(io.BytesIO(r.content))

    raw = z.read(csv_filename)
    text = raw.decode("latin-1", errors="replace").strip()

    sections = re.split(r"(?:\r?\n){2,}", text)
    sections_dict = {}    
    
    for section in sections:
        lines = section.strip().splitlines()
        if len(lines) < 2: continue
        title = lines[0].strip()
        csv_text = '\n'.join(lines[1:])
        df = pd.read_csv(StringIO(csv_text), index_col=0)
        sections_dict[title] = df

    return sections_dict

def get_French_portfolios_monthly(style, session=None):
    style = style.lower()
    if style not in factors_list: raise ValueError(f"Invalid style {style}, must be one of " + ", ".join(factors_list) + ".")
    filename = filename_dict[style]
    section_key = section_key_dict_monthly[style]
    old_column_names = column_names_dict[style]

    sections_dict = read_French_portfolios(filename,session=session)

    portfolios = sections_dict[section_key]

    portfolios.rename(columns={old_name: new_name for new_name, old_name in old_column_names.items()},inplace=True)

    portfolios.index = pd.to_datetime(portfolios.index,format="%Y%m",exact=True).to_period('M')

    for column_name in old_column_names.keys():
        portfolios[column_name] = portfolios[column_name] / 100

    return portfolios

def get_French_portfolios_annual(style,session=None):
    style = style.lower()
    if style not in factors_list: raise ValueError(f"Invalid style {style}, must be one of " + ", ".join(factors_list) + ".")
    filename = filename_dict[style]
    section_key = section_key_dict_annual[style]
    old_column_names = column_names_dict[style]

    sections_dict = read_French_portfolios(filename,session=session)

    portfolios = sections_dict[section_key]

    portfolios.rename(columns={old_name: new_name for new_name, old_name in old_column_names.items()},inplace=True)

    portfolios.index = pd.to_datetime(portfolios.index,format="%Y",exact=True).to_period('Y')

    for column_name in old_column_names.keys():
        portfolios[column_name] = portfolios[column_name] / 100

    return portfolios
