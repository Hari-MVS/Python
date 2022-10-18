def calculate_league_points(wins, draws, losses):
    return (wins*4)+(draws*2)-losses
    


statistics = input().split(",")
wins = int(statistics[0])
draws = int(statistics[1])
losses = int(statistics[2])
print(calculate_league_points(wins,draws,losses))
