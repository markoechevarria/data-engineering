from dataclasses import dataclass, field
from datetime import datetime

@dataclass(frozen=True)
class Event:
    timestamps: datetime
    user_id: int

@dataclass(frozen=True)
class UserRegistered(Event):
    name: str

@dataclass(frozen=True)
class UserLoggedIn(Event):
    location: str

@dataclass(frozen=True)
class PasswordChanged(Event):
    location: str

@dataclass(frozen=True)
class PurchaseCompleted(Event):
    amount: float

@dataclass
class EventStore:

    events: list = field(default_factory=list)

    def __init__(self):
        pass

    def append_events(self, event):
        
        if not issubclass(type(event), Event):
            raise NotImplemented

        match event:

            case UserRegistered(timestamp=tm, user_id=id, name=name):
                self.events.append({ 'timestamp': tm ,'user_id': id, 'name': name})

            case _:
                print(f'Event not registered')

    def show_events(self):
        
        return self.events

eventStore = EventStore()

new_event = UserRegistered( datetime.now(), 1, 'marko' )
eventStore.append_events( new_event )

eventStore.show_events()
