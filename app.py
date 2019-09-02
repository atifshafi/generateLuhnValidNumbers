import random

def generate_valid_card():
    """Valid card generated using Luhn algorithm. The code is only valid for python 2.7"""

    card_number = map(int, "47" +
                      ''.join([str(random.randint(1, 9)) for x in range(14)]))

    tmp_card = list(card_number)

    # Step1
    for i in range(14, -1, -2):
        if int(tmp_card[i]) * 2 > 9:
            tmp_card[i] = int(list(str(tmp_card[i] * 2))[0]) + \
                          int(list(str(tmp_card[i] * 2))[1])
        else:
            tmp_card[i] = tmp_card[i] * 2

    # Step2
    if sum(tmp_card) % 10 != 0:
        tmp_card = tmp_card[:15]
        card_number[15] = (10 - (sum(tmp_card) % 10))

    return ''.join(map(str, card_number))

