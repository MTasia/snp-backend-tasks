class WrongNumberOfPlayersError(Exception):
    def __init__(self, msg):
        self.msg = msg


class NoSuchStrategyError(Exception):
    def __init__(self, msg):
        self.msg = msg


def rps_game_winner(players):
    try:
        if len(players) != 2:
            raise WrongNumberOfPlayersError("Wrong number of players")
        win = {"P": "R", "R": "S", "S": "P"}
        player1 = players[0]
        player2 = players[1]
        if player1[1] not in win or player2[1] not in win:
            raise NoSuchStrategyError("Wrong strategy")
        for elem in win:
            if player1[1] == elem:
                if player2[1] == win[elem] or player2[1] == elem:
                    return player1[0] + " " + player1[1]
                else:
                    return player2[0] + " " + player2[1]
    except WrongNumberOfPlayersError as wn:
        print(wn.msg)
    except NoSuchStrategyError as nss:
        print(nss.msg)


def main():
    players = [['player1', 'P'], ['player2', 'P']]
    win_player = rps_game_winner(players)
    print(win_player)


if __name__ == '__main__':
    main()