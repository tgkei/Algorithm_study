def compare(player, dealer):
    p = sum(player)
    d = sum(dealer)

    if 1 in player and p + 10 <= 21:
        p += 10
    if 1 in dealer and d + 10 <= 21:
        d += 10

    if p > d:
        return 2
    if p < d:
        return -2
    if p == d:
        return 0


def is_done(player, v):
    if sum(player) >= v:
        return True
    if 1 in player:
        return sum(player) + 10 >= v


def solution(cards):
    answer = 0

    th = 0
    player = []
    opened = None
    closed = None
    dealer = []
    for card in cards:
        if card > 10:
            card = 10
        if closed == None:
            if th == 0:
                player.append(card)
                th += 1
                continue
            if th == 1:
                opened = card
                th += 1
                continue
            if th == 2:
                player.append(card)
                th += 1
                continue
            closed = card
            th = 0
            dealer = [opened, closed]
            if sum(player) == 21 or (1 in player and sum(player) + 10 == 21):
                if (sum(dealer) != 21) or ((opened == 1 or closed == 1) and (opened+closed+10 != 21)):
                    answer += 3
                player = []
                dealer = []
                closed = None
            continue

        if opened == 1 or opened >= 7:
            if not is_done(player, 17):
                player.append(card)
                if sum(player) > 21:
                    answer -= 2
                    closed = None
                    player = []
                    dealer = []
                continue

        if opened in [2, 3]:
            if not is_done(player, 12):
                player.append(card)
                if sum(player) > 21:
                    answer -= 2
                    closed = None
                    player = []
                    dealer = []
                continue

        if not is_done(dealer, 17):
            dealer.append(card)

            if sum(dealer) > 21:
                answer += 2
                closed = None
                player = []
                dealer = []
            continue

        answer += compare(player, dealer)

        closed = None
        player = []
        dealer = []

    if closed:
        if is_done(dealer, 17):
            answer += compare(player, dealer)
    return answer


if __name__ == "__main__":
    cards = [10, 13, 10, 1, 2, 3, 4, 5, 6, 2]
    print(solution(cards))
