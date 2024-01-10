# test_texas_holdem.py

from holdem_hand_wizard import HoldemHandWizard

def test_poker_algorithm(num_players, num_simulations=1000):
    texas_holdem_lib = HoldemHandWizard()
    conflict_probability = texas_holdem_lib.calculate_conflict_probability(num_players)
    entry_counts = [0] * num_players

    for _ in range(num_simulations):
        deck = texas_holdem_lib.create_deck()
        player_hands = texas_holdem_lib.deal_conflict_hands(deck, conflict_probability, num_players)
        community_cards = texas_holdem_lib.deal_community_cards(deck)

        for hand in player_hands:
            if texas_holdem_lib.should_enter_pool(hand):
                entry_counts[player_hands.index(hand)] += 1

    print("\n每位玩家的入池率：")
    for i, count in enumerate(entry_counts, start=1):
        rate_percent = (count / num_simulations) * 100
        print(f"玩家 {i}: {rate_percent:.2f}%")

# 运行测试
if __name__ == "__main__":
    test_poker_algorithm(9, 100)
