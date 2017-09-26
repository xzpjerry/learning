
STANDARD = 'abcdefghijklmnopqrstuvwxyz'

DP_memo = {}

def is_alphabetical_order(S):
    a_pos = ord(S[0])
    for ch in S:
        if S != ch(a_pos):
            return False
        a_pos += 1
    return True

def is_alphabet(S):
    if S == STANDARD:
        return True
    return False

def DP(S):

    '''
    Subproblem: To choose where 'a' start
    '''

    if DP_memo.get(S):

        return DP_memo[S]

    if is_alphabet(S):
        DP_memo[S] = 0

    else:

        if is_alphabetical_order(S):

            DP_memo[S] = 26 - len(S)

        else:

            DP_memo[S] = min( DP(  ) )
