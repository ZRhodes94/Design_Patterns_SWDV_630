from __future__ import annotations
from abc import ABC, abstractmethod


class Room_Status:

    _state = None

    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State):
        self._state = state
        self._state.context = self

    def change_status(self):
        self._state.handle1()

    def check_status(self):
        self._state.handle2()


class State(ABC):

    @property
    def context(self) -> Room_Status:
        return self._context

    @context.setter
    def context(self, context: Room_Status) -> None:
        self._context = context

    @abstractmethod
    def handle1(self) -> None:
        pass

    @abstractmethod
    def handle2(self) -> None:
        pass


class Clean_Room(State):
    def handle1(self) -> None:
        print("Guest has checked out. Room needs cleaning.")
        self.context.transition_to(Dirty_Room())

    def handle2(self) -> None:
        print("Room is clean and ready for booking.")


class Dirty_Room(State):
    def handle1(self) -> None:
        print("Custodial staff has cleaned the room.")
        print("Room is ready for booking.")
        self.context.transition_to(Clean_Room())

    def handle2(self) -> None:
        print("Room needs cleaning.")
        
def main():
    room = Room_Status(Clean_Room())
    room.check_status()
    room.change_status()
    room.check_status()
    room.change_status()
    
main()
