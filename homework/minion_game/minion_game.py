def minion_game(s: str) -> str:
    maganhangzok = 'AEIOU'
    kevin_score = 0
    stuart_score = 0
    length = len(s)
    for i in range(length):
        if s[i] in maganhangzok:
            kevin_score += length - i
        else:
            stuart_score += length - i
    if kevin_score > stuart_score:
        return f"Kevin {kevin_score}"
    elif stuart_score > kevin_score:
        return f"Stuart {stuart_score}"
    else:
        return "Draw"
