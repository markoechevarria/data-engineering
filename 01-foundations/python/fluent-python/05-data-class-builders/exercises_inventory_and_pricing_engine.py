from dataclasses import dataclass, field

@dataclass(order=True, slots=True)
class Product:

    sort_index: tuple = field(init=False, repr=False)

    name: str
    sku: str
    price: float
    quantity: int
    tags: list[str]
    discount: float = 0.0

    def __post_init__(self):

        if self.price <= 0:
            raise ValueError('Price should be more than 0')

        if self.quantity < 0:
            raise ValueError('Quantity should be at least 0')

        if not (0 <= self.discount <= 1):
            raise ValueError('Discount should be between 0 and 1')

        self.sort_index = (-self.total, self.name)

    @property
    def total(self) -> float:
        return self.price * self.quantity * (1 - self.discount)

@dataclass(order=True, frozen=True, slots=True)
class FrozenProduct:

    sort_index: tuple = field(init=False, repr=False)

    name: str
    sku: str
    price: float
    quantity: int
    tags: tuple[str, ...]
    discount: float = 0.0

    def __post_init__(self):

        if self.price <= 0:
            raise ValueError('Price should be more than 0')

        if self.quantity < 0:
            raise ValueError('Quantity should be at least 0')

        if not (0 <= self.discount <= 1):
            raise ValueError('Discount should be between 0 and 1')

        object.__setattr__( self, 'sort_index', (-self.total, self.name) )

    @property
    def total(self) -> float:
        return self.price * self.quantity * (1 - self.discount)
