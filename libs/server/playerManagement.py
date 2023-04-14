import socket
import threading
import libs.server.player as Player
import pickle
import copy

class PlayerManagement():
    """The player management class is used to manage the players"""

    def __init__(self) -> None:
        """
            The player management class is used to manage the players
        """
        self.players: dict[Player.Player] = {}
        self.pendingPlayers: dict[Player.Player] = {}
        self.playersSanitized: dict[Player.Player] = {}
        self.__nextId = -1

    @property
    def nextId(self) -> int:
        """Produces unique ids for the players"""

        self.__nextId -= 1
        return self.__nextId

    def addConnection(self, player: Player.Player):
        """
            Adds a player to the player management
        """
        # self.players[str(id)] = player
        self.pendingPlayers[player.id] = player

        print(self.players.keys())

    def refresh(self):
        """
            Refreshes the player management and saves the players
            to a file
        """
        # copy the pending players
        curPP = self.pendingPlayers.copy()

        # Move pendingPending to the players
        # Loads player info that connected from before
        for key, player in curPP.items():
            # If the player is not pending
            if not player.pending:
                oldId = player.id

                # If the player is already in the players dict
                if self.players.get(player.username) != None:
                    player.reload(self.players[player.username].id, self.players[player.username].currentCoor)
                    
                self.players[player.username] = curPP[oldId]

                # TODO potentially remove the old player from the players dict
                # could be a memeory leak

        # Saving to a file process
        pmPackage = {
            'players': {},
            'id': self.__nextId,
        }
        for id, player in self.players.items():
            # Get the sanitized player info
            pmPackage['players'][player.username] = player.export()

        # Save the players to a file
        with open('save.pickle', 'wb') as f:
            pickle.dump(pmPackage, f)
