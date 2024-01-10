# HoldemHandWizard.py - A library for controlling the probability of hand conflicts in Texas Hold'em poker.
import random

class HoldemHandWizard:
    def __init__(self):
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']  # 四種花色
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']  # 十三種等級
        self.deck = self.create_deck()  # 生成一副完整的牌
        self.hand_ranks = {
            'Royal Flush': 10, 'Straight Flush': 9, 'Four of a Kind': 8, 'Full House': 7,
            'Flush': 6, 'Straight': 5, 'Three of a Kind': 4, 'Two Pair': 3, 'One Pair': 2, 'High Card': 1
        }
        self.value_dict = {str(i): i for i in range(2, 11)}
        self.value_dict.update({'J': 11, 'Q': 12, 'K': 13, 'A': 14})

    def create_deck(self):
        """生成一副牌"""
        return [(rank, suit) for suit in self.suits for rank in self.ranks]

    def rank_to_value(self, rank):
        """將牌面轉換為數值，便於比較大小"""
        return self.value_dict[rank]

    def is_straight(self, ranks):
        """判斷是否為順子"""
        values = [self.rank_to_value(rank) for rank in ranks]
        values_set = set(values)
        if len(values_set) < 5:
            return False
        min_value = min(values_set)
        return all(value in values_set for value in range(min_value, min_value + 5)) or \
               (14 in values_set and all(value in values_set for value in [2, 3, 4, 5]))

    def is_flush(self, suits):
        """判斷是否為同花"""
        return len(set(suits)) == 1

    def classify_hand(self, hand):
        """分類和評分牌型"""
        ranks = [card[0] for card in hand]
        suits = [card[1] for card in hand]
        rank_count = {rank: ranks.count(rank) for rank in set(ranks)}

        if self.is_flush(suits):
            if self.is_straight(ranks):
                if set(['10', 'J', 'Q', 'K', 'A']).issubset(set(ranks)):
                    return 'Royal Flush', self.hand_ranks['Royal Flush']
                return 'Straight Flush', self.hand_ranks['Straight Flush']
            return 'Flush', self.hand_ranks['Flush']

        if self.is_straight(ranks):
            return 'Straight', self.hand_ranks['Straight']

        if 4 in rank_count.values():
            return 'Four of a Kind', self.hand_ranks['Four of a Kind']
        if 3 in rank_count.values() and 2 in rank_count.values():
            return 'Full House', self.hand_ranks['Full House']
        if 3 in rank_count.values():
            return 'Three of a Kind', self.hand_ranks['Three of a Kind']
        if list(rank_count.values()).count(2) == 2:
            return 'Two Pair', self.hand_ranks['Two Pair']
        if 2 in rank_count.values():
            return 'One Pair', self.hand_ranks['One Pair']

        return 'High Card', self.hand_ranks['High Card']

    def calculate_conflict_probability(self, num_players):
        """根據玩家數量計算衝突概率"""
        if num_players <= 2:
            return 0.004
        elif num_players <= 5:
            return 0.009
        else:
            return 0.015

    def select_conflict_type(self):
        """隨機選擇衝突類型"""
        conflict_types = ['High Pair', 'Two Pair', 'Three of a Kind', 'Straight', 'Flush', 'Full House', 'Four of a Kind', 'Straight Flush']
        return random.choice(conflict_types)

    def deal_conflict_hand(self, deck, conflict_type, ranks, suits):
        """根據衝突類型發放手牌"""

        def count_ranks_and_suits(deck):
            rank_count = {rank: 0 for rank in ranks}
            suit_count = {suit: [] for suit in suits}
            for card in deck:
                rank_count[card[0]] += 1
                suit_count[card[1]].append(card)
            return rank_count, suit_count

        def find_straight(cards, ranks):
            for i in range(len(ranks) - 4):
                straight_ranks = ranks[i:i + 5]
                if all(rank in [card[0] for card in cards] for rank in straight_ranks):
                    return [card for card in cards if card[0] in straight_ranks]
            return None

        rank_count, suit_count = count_ranks_and_suits(deck)

        # ...處理各種衝突類型...
        # 處理高對（High Pair）衝突
        if conflict_type == 'High Pair':
            for rank in ['A', 'K', 'Q', 'J']:
                if rank_count[rank] >= 2:
                    return random.sample([card for card in deck if card[0] == rank], 2) + random.sample(deck, 3)

        # 處理兩對（Two Pair）衝突
        elif conflict_type == 'Two Pair':
            pairs = []
            for rank in ranks:
                if rank_count[rank] >= 2:
                    pairs.append(rank)  # 尋找兩個符合條件的等級
                if len(pairs) == 2:
                    break
            if len(pairs) == 2:
                pair1 = random.sample([card for card in deck if card[0] == pairs[0]], 2)  # 隨機選擇第一對
                pair2 = random.sample([card for card in deck if card[0] == pairs[1]], 2)  # 隨機選擇第二對
                remaining_cards = [card for card in deck if card[0] not in pairs]  # 獲取剩餘的牌
                return pair1 + pair2 + random.sample(remaining_cards, 1)  # 返回兩對加一張隨機牌

        # 處理三條（Three of a Kind）衝突
        # 遍歷所有等級，尋找至少有三張的等級
        elif conflict_type == 'Three of a Kind':
            for rank in ranks:
                if rank_count[rank] >= 3:
                    # 如果找到，從牌組中隨機抽取三張該等級的牌
                    three_cards = random.sample([card for card in deck if card[0] == rank], 3)
                    # 從剩餘的牌中隨機抽取兩張牌，以形成完整的手牌
                    remaining_cards = [card for card in deck if card not in three_cards]
                    return three_cards + random.sample(remaining_cards, 2)

        # 處理順子（Straight）衝突
        # 遍歷所有可能的五張連續等級組合
        elif conflict_type == 'Straight':
            for i in range(len(ranks) - 4):
                straight_ranks = ranks[i:i + 5]
                # 檢查牌組中是否有這五個等級的牌
                if all(rank_count[rank] > 0 for rank in straight_ranks):
                    # 如果有，找出能形成順子的牌
                    straight_cards = find_straight(deck, straight_ranks)
                    if straight_cards:
                        # 隨機抽取這些牌中的五張
                        return random.sample(straight_cards, 5)
            # 如果找不到順子，則隨機發兩張牌
            return random.sample(deck, 2)

        # 處理同花（Flush）衝突
        # 遍歷所有花色，尋找至少有五張的花色
        elif conflict_type == 'Flush':
            for suit, cards in suit_count.items():
                if len(cards) >= 5:
                    # 如果找到，從這些牌中隨機抽取五張
                    return random.sample(cards, 5)

        # 處理葫蘆（Full House）衝突
        # 先尋找三條，再尋找一對
        elif conflict_type == 'Full House':
            three_kind_card = two_kind_card = None
            for rank in ranks:
                if rank_count[rank] >= 3:
                    three_kind_card = rank
                    break
            if three_kind_card:
                for rank in ranks:
                    if rank != three_kind_card and rank_count[rank] >= 2:
                        two_kind_card = rank
                        break
            if three_kind_card and two_kind_card:
                # 如果找到三條和一對，從牌組中抽取這些牌
                three_cards = random.sample([card for card in deck if card[0] == three_kind_card], 3)
                two_cards = random.sample([card for card in deck if card[0] == two_kind_card], 2)
                return three_cards + two_cards

        # 處理四條（Four of a Kind）衝突
        # 遍歷所有等級，尋找至少有四張的等級
        elif conflict_type == 'Four of a Kind':
            for rank in ranks:
                if rank_count[rank] >= 4:
                    # 如果找到，從牌組中隨機抽取四張該等級的牌
                    four_cards = random.sample([card for card in deck if card[0] == rank], 4)
                    # 從剩餘的牌中隨機抽取一張牌，以形成完整的手牌
                    remaining_cards = [card for card in deck if card not in four_cards]
                    return four_cards + random.sample(remaining_cards, 1)

        # 處理同花順（Straight Flush）衝突
        # 遍歷所有花色，尋找至少有五張的花色
        elif conflict_type == 'Straight Flush':
            for suit in suits:
                if len(suit_count[suit]) >= 5:
                    # 如果找到，檢查這些牌中是否能組成順子
                    straight_flush_cards = find_straight(suit_count[suit], ranks)
                    if straight_flush_cards:
                        # 如果能組成順子，隨機抽取五張牌
                        return random.sample(straight_flush_cards, 5)
            # 如果找不到同花順，則隨機發兩張牌
            return random.sample(deck, 2)

        # 如果不符合以上任何衝突類型，則默認隨機發兩張牌
        return random.sample(deck, 2)

    def deal_conflict_hands(self, deck, conflict_probability, num_players):
        """根據衝突概率和玩家數量發放手牌"""
        shuffled_deck = deck[:]
        random.shuffle(shuffled_deck)
        player_hands = []
        conflict_type = self.select_conflict_type() if random.random() < conflict_probability else None
        dealt_cards = set()

        for _ in range(num_players):
            hand = self.deal_conflict_hand(shuffled_deck, conflict_type, self.ranks, self.suits) if conflict_type else random.sample(shuffled_deck, 2)
            dealt_cards.update(hand)
            player_hands.append(hand)

        shuffled_deck = [card for card in shuffled_deck if card not in dealt_cards]
        return player_hands

    def deal_community_cards(self, deck):
        """發放公牌"""
        return random.sample(deck, 5)

    def should_enter_pool(self, hand):
        """根據手牌決定是否入池"""
        first_value, second_value = self.rank_to_value(hand[0][0]), self.rank_to_value(hand[1][0])
        first_suit, second_suit = hand[0][1], hand[1][1]

        if first_value == second_value:
            return True
        if abs(first_value - second_value) == 1 and (first_value >= 8 or second_value >= 8):
            return True
        if first_suit == second_suit:
            return True
        if abs(first_value - second_value) == 2:
            return True

        return False