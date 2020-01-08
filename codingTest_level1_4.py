import collections

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
answer = ''

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
