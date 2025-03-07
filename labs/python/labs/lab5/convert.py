import re
import json

with open('row.txt', 'r', encoding='utf-8') as txt:
    txt = txt.read()


def convert(text):
    json_data = {
        "branch": "",
        "bin": "",
        "nds_series": "",
        "kassa": "",
        "smena": "",
        "sequence_number": "",
        "check_number": "",
        "kassir": "",
        "items": [],
        "bank_card": "",
        "all": "",
        "nds": "",
        "fiskal": "",
        "date": "",
        "operator": "",
        "ink_ofd": "",
        "rnm": "",
        "znm": "",
    }
    br = re.search(r'Филиал (.+)', text) #object none 
    if br:
        json_data["branch"]=br.group(1)
    
    bin = re.search(r'БИН (\d{12})', text)
    if bin:
        json_data["bin"]=bin.group(1)
    
    nds_s = re.search(r'НДС Серия (\d+)', text)
    if nds_s:
        json_data["nds_series"]=nds_s.group(1)

    kassa = re.search(r'Касса (\d{3}-\d{3})', text)
    if kassa:
        json_data["kassa"]=kassa.group(1)

    smena = re.search(r'Смена (\d+)', text)
    if smena:
        json_data["smena"]=smena.group(1)
    
    sequence = re.search(r'Порядковый номер чека (№\d+)', text)
    if sequence:
        json_data["sequence_number"]=sequence.group(1)

    check = re.search(r'Чек (№\d+)', text)
    if check:
        json_data["check_number"]=check.group(1)

    kassir = re.search(r'Кассир (.+)', text)
    if kassir:
        json_data["kassir"]=kassir.group(1)

    bank_card = re.search(r'Банковская карта:\n(\d{1,3}(?: \d{3})*,\d{2})', text, re.DOTALL)
    if bank_card:
        json_data["bank_card"]=bank_card.group(1)

    alll = re.search(r'ИТОГО:\n(\d{1,3}(?: \d{3})*,\d{2})', text, re.DOTALL)
    if alll:
        json_data["all"]=alll.group(1)
    
    nds = re.search(r'в т.ч. НДС 12%:\n(\d{1,3}(?: \d{3})*,\d{2})', text, re.DOTALL)
    if nds:
        json_data["nds"]=nds.group(1)

    fiskal = re.search(r'Фискальный признак:\n(\d{10})', text, re.DOTALL)
    if fiskal:
        json_data["fiskal"]=fiskal.group(1)

    date = re.search(r'Время: (\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2})', text)
    if date:
        json_data["date"]=date.group(1)
    
    operator = re.search(r'Оператор фискальных данных: (.+)', text)
    if operator:
        json_data["operator"]=operator.group(1)

    ink_ofd = re.search(r'ИНК ОФД: (\d{6})', text)
    if ink_ofd:
        json_data["ink_ofd"]=ink_ofd.group(1)

    rnm = re.search(r'Код ККМ КГД \(РНМ\): (\d{12})', text)
    if rnm:
        json_data["rnm"]=rnm.group(1)

    znm = re.search(r'ЗНМ: (.+)', text)
    if znm:
        json_data["znm"]=znm.group(1)

    items_pattern = re.findall(r'(\d+)\.\n(.+?)\n(\d{1,3}(?: \d{3})*,\d+) x (\d{1,3}(?: \d{3})*,\d+)\n(\d{1,3}(?: \d{3})*,\d+)', text, re.DOTALL)
    for item in items_pattern:
        json_data["items"].append({
            "id": item[0],
            "name": item[1],
            "price": item[2],
            "quantity": item[3],
            "sum": item[4]
        })

    #return json.dumps(json_data, indent=4, ensure_ascii=False)
    return json_data



json_output = convert(txt)
with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(json_output, file, indent=4, ensure_ascii=False)

#print(json_output)


