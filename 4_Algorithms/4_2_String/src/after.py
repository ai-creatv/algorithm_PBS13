def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        last_ind = -1
        flag = False
        is_valid = True
        
        for a in skill:
            curr_ind = skill_tree.find(a)
            
            if curr_ind == -1:
                flag = True
                continue
            
            if flag is True:
                is_valid = False
                break
            
            if curr_ind < last_ind:
                is_valid = False
                break
            last_ind = curr_ind
        if is_valid:
            answer += 1
    
    return answer


skill = 'CBD'
skill_trees = ['BACDE', 'CBADF', 'AECB', 'BDA']
print(solution(skill, skill_trees))