import pandas as pd
import matplotlib.pyplot as plt

full_data = pd.read_csv('./Dataset/all_seasons.csv')

filtered_data = full_data[['player_name','team_abbreviation','pts','reb','ast','ts_pct','season']]


def input_error_handle_team():
    team_choose = input('Please add your team abbreviation: ').upper()
    while team_choose not in filtered_data['team_abbreviation'].unique():
        print("Invalid team abbreviation. Please try again.")
        team_choose = input('Please add your team abbreviation: ').upper()
    return team_choose

choosable_stats = {
    'pts' : ['pts','points','pt','point'],
    'reb' : ['reb','rebounds','rebs'],
    'ast' : ['ast','assists','assist'],
    'ts_pct' : ['ts pct','true shooting','ts percentage','ts']
}

def input_error_handle_stats():
    stat = input('Please choose stats(pts,ast,reb,ts pct): ').lower()
    while not any(stat in aliases for aliases in choosable_stats.values()):
        print("Invalid stat request!Please try again!")
        stat = input('Please choose stats(pts,ast,reb,ts pct): ').lower()
    for key, aliases in choosable_stats.items():
        if stat in aliases:
            return key

        

choosable_number = [1,3,5,10]

def input_error_player_number():
    while True:
        try:
            player_number = int(input('Please choose how many players want to request in order(1,3,5,10): '))
            if player_number in choosable_number:
                return player_number
            else:
                print("Invalid number! Please choose a valid number!")
        except:
            print("Invalid input!Please try again with number!")
            
while True:   
    team = input_error_handle_team()       
    stats = input_error_handle_stats()
    players = input_error_player_number()

    print(stats)

    team_sorted_data = filtered_data[filtered_data['team_abbreviation'] == team]


    def stat_search():
            column = stats
            top = team_sorted_data.sort_values(by=column,ascending=False)
            result = top.head(players)[['player_name',column,'season']]
            print(result)


            def limits_on_graph():
                max_value = team_sorted_data[column].max()
                return max_value * 1.2
            

            ax = result.plot(x='player_name', y=column, kind='bar', legend=False,color='skyblue')
            plt.title(f"Top {players} Players for {stats.upper()} in Team {team}")
            plt.ylabel(stats)
            plt.ylim(0,limits_on_graph())
            plt.xlabel("Player(s) Name")
            plt.xticks(rotation = 45)
            for i,value in enumerate(result[column]):
                ax.text(i, value + (limits_on_graph() * 0.03), round(value, 2), ha='center', va='bottom')
            plt.show()


    stat_search()


    restart = input("Would you like to make an other search? (yes/no)")

    if restart != 'yes':
        print("Thank you for using the program!")
        break












