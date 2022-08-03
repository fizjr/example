lines = 0
fp = open('passwords.csv', 'r')
for l in fp:
    lines += 1
    if lines == 1: continue # skip header
    u, p = l.split(',')
    assert(len(u) >= 3)
    # must have at sign in email
    assert('@' in u)
    # password must be non-empty
    assert(len(p) >= 1)
    lhs, rhs = u.split('@')
    # left part of email must be non-empty
    assert(len(lhs) >= 1)
    # right part of email must have a period
    assert('.' in rhs)
    # ... and at least something else
    assert(len(rhs) >= 2)
