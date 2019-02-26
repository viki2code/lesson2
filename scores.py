import numpy as np

def mean_score(score_lists):
    cnt_classes = len(score_lists)
    sum_mean_score = 0
    for i in score_lists:
        mean_score = np.mean(i['scores'])
        sum_mean_score += mean_score
        print('Средняя оценка по классу {}: {}'.format(i['school_class'],mean_score))
    return sum_mean_score/cnt_classes

score_lists = [{'school_class': '4a', 'scores': [3,4,4,5,2]}, 
                {'school_class': '4b', 'scores': [3,4,5,5,2]},
                {'school_class': '4c', 'scores': [4,4,4,4,4]},
                {'school_class': '4d', 'scores': [3,3,3,2]},
                {'school_class': '4e', 'scores': [5,5,5,5]}]
common_mean_score = mean_score(score_lists)
print('Средняя оценка по всем классам: {}'.format(common_mean_score))