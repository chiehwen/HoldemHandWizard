# HoldemHandWizard

## Introduction
HoldemHandWizard is a library designed for controlling the probability of hand conflicts in Texas Hold'em poker. It aims to provide Texas Hold'em game developers with an easy way to simulate and manage hand conflicts, creating a more challenging and strategic gaming experience.

## Features
- Calculate and manage the probability of hand conflicts for different numbers of players.
- Support for multiple common Texas Hold'em hand conflict types.
- Flexible hand scoring system supporting various hand types.

## Installation
Instructions on how to install your library. For example:
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
Detail the main functions and classes offered by your library. For example:
- `create_deck()`: Generates a new deck of poker cards.
- `deal_conflict_hands(deck, num_players)`: Deals hands to players based on the number of players.

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
