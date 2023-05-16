import csv, openpyxl as excel

in_file = './input/name_addr.csv'
template_file = './input/card-template.xlsx'
save_file = './output/csv_card.xlsx'

def read_csv(fname):
    with open(fname, encoding='ansi') as f:
        reader = csv.reader(f)
        next(reader)
        return [v for v in reader]

book = excel.load_workbook(template_file)

sheet_tpl = book['Sheet']

for i, person in enumerate(read_csv(in_file)):
    name, zipnum, addr = person
    idx = i % 10
    if idx == 0:
        sheet = book.copy_worksheet(sheet_tpl)
        sheet.title = 'Page'+str(i//10)
    row = 4 * (idx % 5) + 2
    col = 2 * (idx // 5) + 2
    print(person)
    print('idx % 5:{}, row:{}, idx // 5:{}, col:{}'.format(idx % 5, row, idx // 5, col))
    
    sheet.cell(row=row+0, column=col, value=name)
    sheet.cell(row=row+1, column=col, value=zipnum)
    sheet.cell(row=row+2, column=col, value=addr)

book.remove(sheet_tpl)
book.save(save_file)
