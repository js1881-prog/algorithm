# def solution(cards1, cards2, goal):
#     answer = ''
#     for i in range(len(goal)):
#         if cards1 != [] and (goal[0] in cards1[0]):
#             goal.pop(0)
#             cards1.pop(0)
#         if cards2 != [] and (goal[0] in cards2[0]):
#             goal.pop(0)
#             cards2.pop(0)
#     if len(goal) == 0:
#         answer = 'YES'
#     else:
#         answer = 'NO'
#     print(answer)
#     return answer


# cards1 = ["i", "drink", "water"]
# cards2 = ["want", "to"]
# goal = ["i", "want", "to", "drink", "water"]

# solution(cards1, cards2, goal)