# High card => Nothing matches
# Pair => Two cards have the same rank
# Two pair => Two different pair of cards have the same rank
# Three of a kind => Three cards have the same rank
# Straight => Five consecutive rows
# Flush => All cards have same suit
# Full house => A pair + Three of a same suit
# Four of a kind => Four card have the same ranks
# Straight flush => Straight + flush simultaneously

from random import choice

class Counter:

    def __init__(self):

        self.counter = {}

    def __str__(self):

        return f"{self.counter}"

    def __setitem__(self, key, value):

        if not isinstance(value, int):
            raise ValueError("Only integers allowed")

        self.counter[key] = value

    def __getitem__(self, key):

        return self.counter.get(key, 0)

    def __len__(self):

        return len( self.counter )

    def search_ocurrence(self, number, times = None):

        if times is not None:
            matched = list( filter( lambda x: x == number , list( self.counter.values() ) ) )
            return len( matched ) == times 

        return number in self.counter.values()

class PokerHandEvaluator:

    SUITS = 'spades hearts diamonds clubs'.split()
    RANKS = list( map( str, range(2, 11) ) ) + list('JQKA')
    RANKS_VALUES = dict( zip( RANKS, range(2, 15) ) )

    def __init__(self):

        self.generate_hand()
        self.ranks = [ self.RANKS_VALUES[rank] for rank, _ in self.hand]
        self.suits = [ suit for _, suit in self.hand]

    def generate_hand(self, size = 5):

        hand_generator = ( ( choice(self.RANKS), choice(self.SUITS) ) for _ in range(size) )
        self.hand = list( hand_generator )
        print('Hand generated: ', self.hand)

    def evaluate(self):
        
        self.rank_counter = Counter()
        self.suit_counter = Counter()

        for rank in self.ranks:
            self.rank_counter[rank] += 1

        for suit in self.suits:
            self.suit_counter[suit] += 1

        is_straight = list( range( min(self.ranks), max(self.ranks) + 1 ) ) == sorted(self.ranks)
        is_flush = len(self.suit_counter) == 1
        is_high_card = len(self.rank_counter) == 5

        if is_straight and is_flush: return 'Straight Flush'
        if self.rank_counter.search_ocurrence(4): return 'Four of a kind'
        if self.rank_counter.search_ocurrence(2) and self.rank_counter.search_ocurrence(3): return 'Full house'
        if is_flush: return 'Flush'
        if is_straight: return 'Straight'
        if self.rank_counter.search_ocurrence(3): return 'Three of a kind'
        if self.rank_counter.search_ocurrence(2, 2): return 'Two Pair'
        if self.rank_counter.search_ocurrence(2): return 'Pair'
        if is_high_card: return 'High Card'
        return 'Nothing' 

if __name__ == "__main__":

    evaluator = PokerHandEvaluator()
    result = evaluator.evaluate()
    print(result)


