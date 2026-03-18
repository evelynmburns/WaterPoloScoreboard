class Game:
    """
    Manages the state and event logging for a sports match between two teams.

    Parameters
    ----------
    home : Team
        The object representing the home team.
    away : Team
        The object representing the away team.

    Attributes
    ----------
    home : Team
        The home team instance.
    away : Team
        The away team instance.
    events : list of str
        A chronological log of valid event messages occurring during the game.
    """
    def __init__(self, home, away):
        self.home = home
        self.away = away
        self.events = []


    def add_event(self, team_name, player_cap, event):
        """
        Records a specific game event for a player and updates statistics.

        Processes substitutions, increments event counters, and manages player 
        eligibility based on exclusion rules.

        Parameters
        ----------
        team_name : {'home', 'away'}
            The identifier for which team the player belongs to.
        player_cap : int or str
            The unique identifier (cap number) for the player.
        event : str
            The type of event to record (e.g., 'goal', 'exclusion', 'sub in').

        Returns
        -------
        None
        """
        # Check if team is "home" or "away"
        # Look for player_cap number in team's players_by_cap{} dict

        # Validate team name
        if team_name == "home":
          team = self.home
        elif team_name == "away":
          team = self.away
        else:
          print("Team must be 'home' or 'away'.")
          return

        # check team is valid class
        if not team.validate_team():
          print("Invalid team")
          return

        # check if event is valid
        if event not in team.stats.stat:
          print(f'bad event: {event}')
          return

        player = team.players_by_cap[player_cap]
        event_message = f'Number: {player_cap}, {player.name} \
          for {team.name} -> {event}'


        # Handle Events
        # For substitution out, change status and leave, no counts needed
        if event == 'sub out':
          player.status = 'bench'
          self.events.append(event_message)
          return

        # For substitution in, check if the player is eligible, and return,
        # no counts needed
        if event == 'sub in':
          if player.eligible == False:
            print(f'{player.cap}, {player.name} is not eligible')
            return
          player.status = 'in'
          return


        # Increment stats for event
        player.stats.stat[event] +=1
        team.stats.stat[event] +=1

        # Check if event is exclusion if player is still eligible to play (<3)
        if event == 'exclusion' and player.stats.stat[event] == 3:
          print(f'{player.cap}, {player.name}, has 3 exclusions and is ineligible')
          player.eligible = False


        # Append events
        self.events.append(event_message)

    def print_events(self):
        """
        Prints all recorded event messages in chronological order.

        Returns
        -------
        None
        """
        print(f'Number of events: {len(self.events)}')

        for event in self.events:
          print(event)

    def print_score(self):
        """
        Displays the current score summary. 
        
        Returns
        -------
        None
        """
        print(f'HOME {self.home.name} vs AWAY {self.away.name}')
        home_score = self.home.stats.stat['goal']
        away_score = self.away.stats.stat['goal']
        print(f'Score: {home_score} vs {away_score}')
