from stats import Stats

class Team:
    """
    Represents a sports team and manages player rosters and statistics.

    Parameters
    ----------
    name : str
        The name of the team.

    Attributes
    ----------
    name : str
        The team's name.
    players_by_cap : dict
        A dictionary mapping player cap numbers to Player objects.
    stats : Stats
        The aggregated statistics for the entire team.
    """
    def __init__(self, name):
        self.name = name
        self.players_by_cap = {}
        self.stats = Stats()

    def add_player(self, player):
        """
        Adds a player to the team's roster.

        Parameters
        ----------
        player : Player
            The player object to be added to the team.

        Returns
        -------
        None
        """
        self.players_by_cap[player.cap] = player

    def validate_team(self):
        """
        Validates the team's current lineup based on eligibility and player count.

        Checks that no ineligible players are in the game and that the total 
        number of active players does not exceed 7.

        Returns
        -------
        bool
            True if the team lineup is valid, False otherwise.
        """
        # Check that there are only 7 players with status "in"
        in_players = 0
        for cap, player in self.players_by_cap.items():
          if player.status == 'in':

            if player.eligible == False:
              print('substituted ineligible player')
              return False

            in_players += 1

        if in_players > 7:
          print('too many players (must be 7)')
          return False

        # All players are valid
        return True

    def check_stats(self, stat_key):
        """
        Verifies the integrity of team-wide statistics against individual player data.

        Parameters
        ----------
        stat_key : str
            The specific statistic category to verify (e.g., 'goal', 'exclusion').

        Returns
        -------
        bool
            True if the team stat matches the sum of player stats, False otherwise.
        """
        player_stat = 0

        for i, player in self.players_by_cap.items():
          player_stat += player.stats.stat[stat_key]

        if self.stats.stat[stat_key] == player_stat:
          return True
        else:
          return False

    def print_stats(self):
        """
        Prints the individual statistics for every player on the team.

        Returns
        -------
        None
        """
        for key, player in self.players_by_cap.items():
          print()
          player.print_stats()
