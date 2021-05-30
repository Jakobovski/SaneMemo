import random
import datetime

# The number of times needed for the user to get the card correct(EASY) consecutively before removing the card from
# the current sub_deck.
CONSECUTIVE_CORRECT_TO_REMOVE_FROM_SUBDECK_WHEN_KNOWN = 2
CONSECUTIVE_CORRECT_TO_REMOVE_FROM_SUBDECK_WHEN_WILL_FORGET = 3

# The number of cards in the sub-deck
SUBDECK_SIZE = 15
REMINDER_RATE = 1.6

class Deck(object):

    def __init__(self):
        self.cards = []

        # Used to make sure we don't display the same card twice
        self.last_card = None

    def add_card(self, card):
        self.cards.append(card)

    def get_next_card(self):
        self.cards = sorted(self.cards)  # Sorted by next_practice_time
        sub_deck = self.cards[0:min(SUBDECK_SIZE, len(self.cards))]
        card = random.choice(sub_deck)

        # In case card == last card lets select again. We don't want to show the same card two times in a row.
        while card == self.last_card:
            card = random.choice(sub_deck)

        self.last_card = card
        return card


class Card(object):

    def __init__(self, front, back):
        self.front = front
        self.back = back

        self.next_practice_time = datetime.utc.now()
        self.consecutive_correct_answer = 0
        self.last_time_easy = datetime.utc.now()

    def update(self, performance_str):
        """ Updates the card after the user has seen it and answered how difficult it was. The user can provide one of
        three options: [KNOW_IT, KNOW_BUT_WILL_FORGET, DONT_KNOW].
        """

        if performance_str == "KNOW_IT":
            self.consecutive_correct_answer += 1

            if self.consecutive_correct_answer >= CONSECUTIVE_CORRECT_TO_REMOVE_FROM_SUBDECK_WHEN_KNOWN:
                days_since_last_easy = (datetime.utc.now() - self.last_time_easy).days
                days_to_next_review = (days_since_last_easy + 2) * REMINDER_RATE
                self.next_practice_time = datetime.utc.now() + datetime.time(days=days_to_next_review)
                self.last_time_easy = datetime.utc.now()
            else:
                self.next_practice_time = datetime.utc.now()

        elif performance_str == "KNOW_BUT_WILL_FORGET":
            self.consecutive_correct_answer += 1

            if self.consecutive_correct_answer >= CONSECUTIVE_CORRECT_TO_REMOVE_FROM_SUBDECK_WHEN_WILL_FORGET:
                self.next_practice_time = datetime.utc.now() + datetime.time(days=1)
            else:
                self.next_practice_time = datetime.utc.now()

        elif performance_str == "DONT_KNOW":
            self.consecutive_correct_answer = 0
            self.next_practice_time = datetime.utc.now()

    def __cmp__(self, other):
        """Comparator or sorting cards by next_practice_time"""
        if hasattr(other, 'next_practice_time'):
            return self.number.__cmp__(other.next_practice_time)
