from stats import Stats
from player import Player
from team import Team
from game import Game

def test_game():
    """
    Simulates a full game scenario to validate the logic of all integrated classes.

    This test function performs the following:
    1. Initializes two teams (Home and Away) with specific rosters.
    2. Validates team composition rules (e.g., maximum 7 active players).
    3. Simulates a series of game events including goals, exclusions, and substitutions.
    4. Asserts that the final scores and team states are correct according to game logic.

    Returns
    -------
    None

    Raises
    ------
    AssertionError
        If team validation fails or if the final scores do not match expected values.
    """
    # set up starting teams (starters) for home
    player1 = Player('B', 1, 'goalie')
    player1.status = 'in'
    player2 = Player('evie', 2, 'utility')
    player2.status = 'in'
    player3 = Player('Em', 3, 'attacker')
    player3.status = 'in'
    player4 = Player('Oli', 4, 'guard')
    player4.status = 'in'
    player5 = Player('Holly', 5, 'utility')
    player5.status = 'in'
    player6 = Player('Ken', 6, 'attacker')
    player6.status = 'in'
    player7 = Player('Lex', 7, 'guard')
    player7.status = 'in'
    player8 = Player('Kyla', 8, 'attacker')
    player8.status = 'bench'

    # set up starting team (starters) for away
    player14 = Player('Mary', 13 , 'goalie')
    player14.status = 'in'
    player15 = Player('Lisa', 15 , 'set')
    player15.status = 'in'
    player16 = Player('Linsey', 16, 'attacker')
    player16.status = 'in'
    player17 = Player('Mel', 17, 'guard')
    player17.status = 'in'
    player18 = Player('Hannah', 18, 'attacker')
    player18.status = 'in'
    player19 = Player('Shirley', 19, 'set')
    player19.status = 'in'
    player20 = Player('Dianna', 20, 'utility')
    player20.status = 'in'

    players_home = [player1, player2, player3, player4, player5, player6, player7,
                    player8]
    players_away = [player14, player15, player16, player17, player18, player19,
                    player20]

    # create and validate home team
    home_team = Team('home')
    for player in players_home:
        home_team.add_player(player)

    assert(home_team.validate_team() == True)

    # create and validate away team
    away_team = Team('away')
    for player in players_away:
        away_team.add_player(player)
    assert(away_team.validate_team() == True)

    # Create game and add events
    game = Game(home_team, away_team)
    events = [
        ('home', 2, 'exclusion'),
        ('away', 18, 'exclusion'),
        ('home', 1, 'block'),
        ('home', 2, 'goal'),
        ('home', 5, 'goal'),
        ('away', 15, 'goal'),
        ('home', 2, 'exclusion'),
        ('away', 13, 'block'),
        ('home', 5, 'goal'),
        ('away', 20, 'exclusion'),
        ('away', 20, 'exclusion'),
        ('away', 20, 'sub out'),
        ('away', 20, 'sub in'),
        ('home', 6, 'goal'),
        ('home', 7, 'block'),
        ('away', 15, 'goal'),
        ('away', 13, 'block')
    ]

    for event in events:
        team_name = event[0]
        player_cap = event[1]
        event_info = event[2]
        game.add_event(team_name, player_cap, event_info)

    # after events, ensure we have a valid team
    assert(home_team.validate_team() == True)
    assert(away_team.validate_team() == True)

    # Check score is 4 v 2
    assert(home_team.stats.stat['goal'] == 4)
    assert(away_team.stats.stat['goal'] == 2)
