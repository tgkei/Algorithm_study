def solution(encrypted_text, key, rotation):
    ALPHA = "abcdefghijklmnopqrstuvwxyz"

    tmp = dict()
    tmp2 = dict()
    idx = 1

    for alpha in ALPHA:
        tmp[alpha] = idx
        tmp2[idx] = alpha
        idx += 1

    answer = ""

    rotation %= len(encrypted_text)
    if rotation > 0:
        encrypted_text = encrypted_text[rotation:] + encrypted_text[:rotation]
    elif rotation < 0:
        encrypted_text = encrypted_text[rotation:] + \
            encrypted_text[:rotation]

    for text, k in zip(encrypted_text, key):
        text_idx = tmp[text]
        key_idx = tmp[k]
        text_idx = text_idx - key_idx
        print(text_idx)
        if text_idx <= 0:
            text_idx += 26
        tmp_text = tmp2[text_idx]
        answer += tmp_text

    return answer


if __name__ == "__main__":
    enc = "ptvfbqyyigo"
    key = "abcdefghijk"
    rotation = -3
    print(solution(enc, key, rotation))
