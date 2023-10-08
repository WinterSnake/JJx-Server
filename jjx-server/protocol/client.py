#!/usr/bin/python
##-------------------------------##
## Junk Jack X: Protocol         ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Client                        ##
##-------------------------------##

## Imports
import logging

from enet import Address, Host, Peer  # type: ignore

from .connection import CHANNELS, Connection
from ..version import Version

## Constants
LOGGER = logging.getLogger(__name__)


## Classes
class Client(Connection):
    """
    JJx: Client Connection
    """

    # -Constructor
    def __init__(
        self, name: str, version: Version = Version.Latest
    ) -> None:
        super().__init__(Host(None, 1, CHANNELS))
        self.name: str = name
        self.version: Version = version

    # -Instance Methods
    def close(self) -> None:
        pass

    def run(self, ip: str, port: int) -> None:
        '''Connect to server and run enet loop for handling server messages'''
        self._peer = self.host.connect(Address(ip.encode('utf-8'), port), CHANNELS)
        super().run(ip, port)

    def _on_connected(self, peer: Peer) -> None:
        '''Log server peer info'''
        LOGGER.info(f"Client connected to {peer.address}")
        self.on_connected()

    def _on_disconnected(self, peer: Peer) -> None:
        '''Log server peer info'''
        LOGGER.info(f"Client disconnected from {peer.address}")
        self.on_disconnected()
        self.close()

    # -Instance Methods: API
    def disconnect(self) -> None:
        '''Disconnect peer from server'''
        self.connection.disconnect()

    def on_connected(self) -> None: ...
    def on_disconnected(self) -> None: ...

    # -Properties
    @property
    def connection(self) -> Peer:
        '''Returns server peer'''
        return self._host.peers
