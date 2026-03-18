The goal of this project is to run a functioning score board for a water
polo game, as well as some player statistics.

It is event driven

The user can interact by using either the given events in this file or
add their own events.

A general outline of the rules of water polo to help understanding of
the code:

* there is a limit of 7 players in the pool at all times (per team)
* this includes 1 goalie and 6 field players per team
* goals are 1 point each, and each quarter starts with a sprint to
determine who starts with possession of the ball
* players can be temporarily taken out of the game (like a penalty
box in hockey) for violating rules. This is called an exclusion
* Players are perminantly taken out of the game once they have 3
exclusions, on their third they must be subbed out of play.


Structure
code is arranged in classes using a modular approach

Stats (stats.py)

Player (player.py)

Team (team.py)

Game (game.py)


Players have Stats and player information

Teams are composed of Players and have Stats

Games are composed of Teams

Games have Events that happen to Players on Teams

Events are formatted as a tuple (team, player, event)
E.G
('home', 5, 'goal'),

Events are added to Games
