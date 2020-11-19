import openpyxl
import numbers

def examine_income_data(exel_file_name):
    workbook_file = openpyxl.load_workbook(exel_file_name)
    worksheet = workbook_file.active
    for current_row in worksheet.rows:
        state_cell = current_row[0]
        state_name = state_cell.value
        median_income2018 = current_row[1].value
        if not isinstance(median_income2018, numbers.Number):
            continue
        #print(f"{state_name}\t: {median_income2018}")
        median_income2016col_num = openpyxl.utils.cell.column_index_from_string('H')-1
        median_income2016_income = current_row[median_income2016col_num].value
        change_in_income = median_income2018 - median_income2016_income
        if change_in_income < 0:
            print(f"{state_name}\t: {change_in_income}")

def main():
    examine_income_data("CensuseMedianIncome.xlsx")

main()