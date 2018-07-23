





def search_games(games):
	search_term = input(" >>> ")
	found_games = []
	for game in games:
		if search_term in game["VG_NAME"]:
			found_games.append(game)
	return found_games
  
