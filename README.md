# HoldemHandWizard

## Introduction
HoldemHandWizard is a library designed for controlling the probability of hand conflicts in Texas Hold'em poker. It aims to provide Texas Hold'em game developers with an easy way to simulate and manage hand conflicts, creating a more challenging and strategic gaming experience.

## Features
- Calculate and manage the probability of hand conflicts for different numbers of players.
- Support for multiple common Texas Hold'em hand conflict types.
- Flexible hand scoring system supporting various hand types.

## Installation
```bash
pip install holdemhandwizard
```

## Quick Start Example

Below is an example script demonstrating how to use the HoldemHandWizard library to simulate a Texas Hold'em poker game and calculate the hand entry rates for players.

```python
# Import the HoldemHandWizard library
from holdem_hand_wizard import HoldemHandWizard

def test_poker_algorithm(num_players, num_simulations=1000):
    # Create an instance of the library
    texas_holdem_lib = HoldemHandWizard()

    # Calculate the conflict probability based on the number of players
    conflict_probability = texas_holdem_lib.calculate_conflict_probability(num_players)

    # Initialize a list to count the number of times each player enters the pool
    entry_counts = [0] * num_players

    # Simulate the specified number of poker games
    for _ in range(num_simulations):
        # Generate a new deck of cards
        deck = texas_holdem_lib.create_deck()

        # Deal hands to players considering potential conflicts
        player_hands = texas_holdem_lib.deal_conflict_hands(deck, conflict_probability, num_players)

        # Deal community cards
        community_cards = texas_holdem_lib.deal_community_cards(deck)

        # Determine whether each hand should enter the pool
        for hand in player_hands:
            if texas_holdem_lib.should_enter_pool(hand):
                # Increment the entry count for the player
                entry_counts[player_hands.index(hand)] += 1

    # Print the entry rates for each player
    print("\nEntry rates for each player:")
    for i, count in enumerate(entry_counts, start=1):
        rate_percent = (count / num_simulations) * 100
        print(f"Player {i}: {rate_percent:.2f}%")

# Run the test with 9 players and 100 simulations
if __name__ == "__main__":
    test_poker_algorithm(9, 100)
```

## API Reference

This section provides detailed information about the key functionalities available in the HoldemHandWizard library.

### HoldemHandWizard

A class that encapsulates all the functionalities of the Texas Hold'em hand conflict management.

#### `__init__(self)`

Constructor for the HoldemHandWizard class. Initializes the deck and sets default values for various parameters.

#### `create_deck(self)`

Generates and returns a new deck of standard Texas Hold'em playing cards.

- **Returns**: A list of tuples, each representing a card. For example, `('A', 'Hearts')`.

#### `rank_to_value(self, rank)`

Converts a card rank to its corresponding numerical value.

- **Parameters**:
  - `rank` (str): The rank of the card (e.g., 'A', 'K', 'Q', '2', ...).
- **Returns**: Integer value corresponding to the given rank.

#### `is_straight(self, ranks)`

Determines whether a given set of card ranks forms a straight.

- **Parameters**:
  - `ranks` (list): A list of card ranks.
- **Returns**: `True` if the ranks form a straight, `False` otherwise.

#### `is_flush(self, suits)`

Determines whether a given set of card suits forms a flush.

- **Parameters**:
  - `suits` (list): A list of card suits.
- **Returns**: `True` if the suits form a flush, `False` otherwise.

#### `classify_hand(self, hand)`

Classifies a given poker hand and assigns it a rank based on Texas Hold'em rules.

- **Parameters**:
  - `hand` (list): A list of tuples representing a poker hand.
- **Returns**: A tuple containing the name of the hand type and its rank.

#### `calculate_conflict_probability(self, num_players)`

Calculates the probability of a conflict occurring based on the number of players.

- **Parameters**:
  - `num_players` (int): The number of players in the game.
- **Returns**: A float representing the conflict probability.

#### `select_conflict_type(self)`

Randomly selects a type of hand conflict.

- **Returns**: A string representing the selected conflict type.

#### `deal_conflict_hand(self, deck, conflict_type, ranks, suits)`

Deals a hand of cards based on the specified conflict type.

- **Parameters**:
  - `deck` (list): The deck of cards.
  - `conflict_type` (str): The type of conflict to simulate.
  - `ranks` (list): The list of card ranks.
  - `suits` (list): The list of card suits.
- **Returns**: A list of tuples representing the dealt hand.

#### `deal_conflict_hands(self, deck, conflict_probability, num_players)`

Deals hands to each player, considering potential conflicts.

- **Parameters**:
  - `deck` (list): The deck of cards.
  - `conflict_probability` (float): The probability of a conflict occurring.
  - `num_players` (int): The number of players.
- **Returns**: A list of hands, each hand is a list of card tuples.

#### `deal_community_cards(self, deck)`

Deals and returns community cards for the round.

- **Parameters**:
  - `deck` (list): The deck of cards.
- **Returns**: A list of tuples representing the community cards.

#### `should_enter_pool(self, hand)`

Determines if a given hand should enter the betting pool based on its strength.

- **Parameters**:
  - `hand` (list): A list of tuples representing a poker hand.
- **Returns**: `True` if the hand should enter the pool, `False` otherwise.

## License
```plaintext
Copyright (c) 2024 CHIEH-WEN YANG

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
...
```
