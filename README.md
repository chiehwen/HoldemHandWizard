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

## Quick Start
Provide a simple example to demonstrate how to use your library. For instance:
```python
from holdemhandwizard import TexasHoldemLibrary

# Create an instance of the library
poker_lib = TexasHoldemLibrary()

# Generate a deck of cards
deck = poker_lib.create_deck()

# Simulate a round of the game
player_hands = poker_lib.deal_conflict_hands(deck, 5)
for hand in player_hands:
    print(hand, poker_lib.classify_hand(hand))
```

## API Reference
Detail the main functions and classes offered by your library. For example:
- `create_deck()`: Generates a new deck of poker cards.
- `deal_conflict_hands(deck, num_players)`: Deals hands to players based on the number of players.

## Contribution
Encourage other developers to contribute to your project and explain how to do so.

## License
Specify the license for your project. For example, if you're using the MIT License:
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
