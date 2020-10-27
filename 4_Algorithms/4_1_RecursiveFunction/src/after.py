def solution(p):
    return correctParenthesis(p)


def isCorrect(s):
    balance = 0    
    for c in s:
        if c == '(':
            balance += 1
        else:
            balance -= 1

        if balance < 0:
            return False

    return balance == 0
    

def splitParenthesis(s):
    balance = 0
    
    for ind, c in enumerate(s):
        if c == '(':
            balance += 1 
        else:
            balance -= 1
        
        if ind > 0 and balance == 0:
            u = s[:ind + 1]
            v = s[ind + 1:]
            break
    
    return [u, v]


def correctParenthesis(s):
    if s == '' or isCorrect(s) is True:
        return s
    
    u, v = splitParenthesis(s)
    
    if isCorrect(u) is True:
        return u + correctParenthesis(v)
    
    else:
        v_ = '(' + correctParenthesis(v) + ')'
        u_ = u[1:-1]
        for c in u_:
            if c == '(':
                v_ += ')'
            else:
                v_ += '('
        return v_
    


print(solution('(()())()'))
print(solution(')('))
print(solution('()))((()'))
