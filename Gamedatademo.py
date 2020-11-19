import openpyxl
import openpyxl.utils


def get_good_linux_games(worksheet):
    recomentation_cutoff = 10000
    game_count = 0
    for row in worksheet.rows:
        linux_column_number = openpyxl.utils.cell.column_index_from_string("AB")-1
        runs_on_linux = row[linux_column_number].value
        if runs_on_linux != "True":
            continue
        metacritic_col_num = openpyxl.utils.cell.column_index_from_string('J')-1
        recc_col_num = openpyxl.utils.cell.column_index_from_string('M')-1
        metacritic_score = row[metacritic_col_num].value
        num_of_reccs = row[recc_col_num].value
        if num_of_reccs > recomentation_cutoff and (metacritic_score > 90 or metacritic_score == 0):
            game_count += 1
            game_name = row[3].value
            print(f"You might be interested in {game_name}, it has {num_of_reccs} recommendations and a metacritic score of {metacritic_score} ")
    print(f"there are {game_count} games that run on linux and are recommended")

def main():
    game_xcel_file = openpyxl.load_workbook("games-features.xlsx")
    game_sheet = game_xcel_file.active
    get_good_linux_games(game_sheet)


main()