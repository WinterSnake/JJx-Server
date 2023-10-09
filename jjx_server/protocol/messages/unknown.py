#!/usr/bin/python
##-------------------------------##
## Junk Jack X: Protocol         ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Message: World Data           ##
##-------------------------------##

## Imports
from __future__ import annotations
import struct
from typing import cast

from .base import Message
from ...world import (
    Gamemode, InitSize, Planet, Season, TileMap, Time, World
)


## Classes
class Unknown1Message(Message):
    """
    JJx Message: Unknown 1
        - Is compressed
    """

    # -Constructor
    def __init__(self, data: bytes) -> None:
        self.unknown_data: bytes = data

    def __len__(self) -> int:
        return len(self.to_bytes())

    def __str__(self) -> str:
        return "WorldUnknown1"

    # -Instance Methods
    def to_args(self) -> tuple[bytes]:
        return (self.unknown_data,)


    def to_bytes(self) -> bytes:
        return self.unknown_data

    # -Class Methods
    @classmethod
    def from_bytes(cls, data: bytes) -> Unknown1Message:
        return cls(data)

    # -Class Properties
    opcode = 0x034C
