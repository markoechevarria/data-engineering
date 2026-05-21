from dataclasses import InitVar, dataclass, field

@dataclass
class ClubMember:
    name: str
    guests: list[str] = field(default_factory=list)
    athlete: bool = field(default=False, repr=False)

### Post-init Processing

class HackerClubMember(ClubMember):
    all_handles = set()
    # all_handles: ClassVar[set[str]] = set()
    handle: str = ''

    def __post_init__(self):

        cls = self.__class__

        if self.handle == '':
            self.handle = self.name.split()[0]

        if self.handle in cls.all_handles:
            msg = f'handle {self.handle!r} already exists.'
            raise ValueError(msg)

        cls.all_handles.add(self.handle)
            

@dataclass
class C:
    i: int
    j: int = None
    database: InitVar[DatabaseType] = None

    def __post_init__(self, database):
        if self.j is None and database is not None:
            self.j = database.lookup('j')

c = C(10, database=my_database)




