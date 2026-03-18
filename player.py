from stats import Stats

class Player:
    """
    Represents an individual athlete, tracking their personal profile and statistics.

    Parameters
    ----------
    name : str
        The full name of the player.
    cap : int or str
        The unique identification number (cap number) assigned to the player.
    position : str
        The designated playing position of the player.

    Attributes
    ----------
    name : str
        The player's name.
    cap : int or str
        The player's unique cap number.
    status : {'ready', 'in', 'excluded', 'bench'}
        The current game status of the player. Defaults to "ready".
    eligible : bool
        Indicates if the player is currently allowed to participate in the game.
    position : str
        The player's position.
    stats : Stats
        An instance of the Stats class containing the player's performance metrics.
    """

    def __init__(self, name, cap, position):
        self.name = name
        self.cap = cap
        self.status = "ready"
        self.eligible = True
        self.position = position
        self.stats = Stats()

    def set_status(self, status):
        """
        Updates the player's game status after validating it against allowed values.

        Parameters
        ----------
        status : str
            The new status to assign. Must be one of: 'in', 'excluded', 
            'bench', or 'ready'.

        Returns
        -------
        None
        """
        valid_status = ["in", "excluded", "bench", "ready"]
        if status not in valid_status:
            print(f'{status} not in {valid_status}')
            return

        self.status = status

    def print_stats(self):
        """
        Displays the player's profile information and any non-zero statistics.

        Returns
        -------
        None
        """
        print(f'Name: {self.name}')
        print(f'Cap: {self.cap}')
        print(f'Position: {self.position}')
        print(f'Status: {self.status}')
        print(f'Eligible: {self.eligible}')

        # Only print stats if there is a value other than 0
        stats_line = []
        for key, value in self.stats.stat.items():
            if value > 0:
                stats_line.append(f'{key}: {value}')
        print(stats_line)