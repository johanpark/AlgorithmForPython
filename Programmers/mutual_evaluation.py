def solution(scores):
    answer = ''
    for i in range(len(scores)):
        list = []
        for j in range(len(scores[i])):
            list.append(scores[j][i])
        maxScore = max(list)
        minScore = min(list)
        selfScore = list[i]
        if maxScore == selfScore or minScore == selfScore:
            if list.count(selfScore) == 1:
                list.remove(selfScore)
        average = sum(list) / len(list)
        if average >= 90:
            grade = 'A'
        elif average >= 80:
            grade = 'B'
        elif average >= 70:
            grade = 'C'
        elif average >= 50:
            grade = 'D'
        else:
            grade = 'F'
        answer = answer + grade
    return answer






# print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))
# print(solution([[50,90],[50,87]]))
print(solution([[70,49,90],[68,50,38],[73,31,100]]))