# SaneMemo
An open-source, well documented, spaced repetition algorithm.



#### Features
- Introduces sub-decks for efficiently learning large decks (Super useful!)
- Intuitive variable names and algorithm parameters.
- Fully open-source with human-readable examples.
- Easily configurable parameters to accommodate for different users' memorization abilities. 
- Computationally cheap to compute next card. No need to run a computation on every card in the deck. 

#### Terminology
- `card: an item to be memorized`
- `deck: a set of cards`
- `sub-deck: a subset of a deck. This is generated dynamically by the algorithm.`

#### What are sub-decks?
The use case of sub-decks is as follows. A user adds a large number of cards to 
their deck (Ex: 100+) and now attempts to study. In order to facilitate efficient learning it
is imperative to repeat the new cards with a frequency greater than 1/100. To solve this problem SaneMemo 
groups new cards into sub-decks of a configurable size `default sub_deck_size=20`. Cards in a sub-deck are repeated more frequently, once the user indicates that they know the card, it is removed from the sub-deck and replaced with a new card.


#### Core Ideas
Users is given three options to describe the difficulty of a card.
- "I KNOW IT"
- "I KNOW IT BUT WILL FORGET"
- "DON'T KNOW"

These are roughly equivalent to easy, medium and hard. But are more intuitive, 
and more accurately model the human learning process.


#### Algorithm
See code.py

        
#### Inspiration
- SuperMemo2
- http://www.blueraja.com/blog/477/a-better-spaced-repetition-learning-algorithm-sm2
    
    
