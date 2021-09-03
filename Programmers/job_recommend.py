def solution(table, languages, preference):
    answer = ''
    k = 1
    new_table = sorted([list(t.split()) for t in table], key=lambda x : x[0])
    job = {n: new_table[n][0] for n in range(len(new_table))}
    print(new_table)
    scoreList = list()
    for i in range(len(new_table)):
        score_value = 0
        for j in range(len(languages)):
            score = 0
            for k in range(len(new_table[i])):
                if new_table[i][k] == languages[j]:
                    score += (len(new_table[i]) - k) * preference[j]
            score_value += score
        scoreList.append(score_value)
    print(scoreList)
    return answer


print(solution(	["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["PYTHON", "C++", "SQL"], [7, 5, 5]))