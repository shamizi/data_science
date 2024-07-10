# exactitude = VRAI positif + vrai negatif / (vp + vn +fp +fn)
# precision = VP / (VP + FP)
#recall ou sensibilite = VP / (VP + FN)
#score f1 = 2 x (precision x rappel / precision + rappel)
#specificité = VN / VN + FP
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def matrice(prediction_path, truth_path):
    with open(prediction_path, 'r') as file:
        prediction = [line.strip() for line in file.readlines()]
    with open(truth_path, 'r') as file:
        truth = [line.strip() for line in file.readlines()]
    vp = 0
    fp = 0
    vn = 0
    fn = 0
    jedi_nb = 0
    sith_nb = 0
    #need to calculate : precision recall f1 score and totall
    for a, b in zip(prediction, truth):
        if a == 'Jedi' and b == 'Jedi':
            vp += 1
            jedi_nb +=1
        if a == 'Jedi' and b == 'Sith':
            fp += 1
            sith_nb += 1
        if a == 'Sith' and b == 'Jedi':
            jedi_nb +=1
            fn += 1
        if a == 'Sith' and b == 'Sith':
            sith_nb +=1
            vn += 1
    #print(vn, vp, fn, fp)
    # precision = VP / (VP + FP)
    precision = round(vp / (vp + fp), 2)
    precision2 = round(vn / (vn + fn), 2)
    #recall ou sensibilite = VP / (VP + FN)
    recall = round(vp / (vp + fn),2)
    recall2 = round(vn / (vn + fp),2)
    #score f1 = 2 x (precision x rappel / precision + rappel)
    f1 = round(2 * ((precision * recall) / (precision + recall)),2)
    f2 = round(2 * ((precision2 * recall2) / (precision2 + recall2)),2)
    #print(precision, recall, f1, jedi_nb)
   # print(precision2, recall2, f2, sith_nb)

    data = {
        'precision': [precision, precision2, '',''],
        'recall': [recall, recall2,'',''],
        'f1_score': [f1, f2,'',(f1 + f2) / 2],
        'total': [jedi_nb, sith_nb,'',sith_nb + jedi_nb]
    }
    index = ['Jedi', 'Sith', '','accuracy']
    res = pd.DataFrame(data, index=index)
    res2 = np.array([[vp,fn],[fp,vn]])
    print(res)
    print(res2)
    plt.matshow(res2)
    for (i, j), val in np.ndenumerate(res2):
        plt.text(j, i, f'{val}', ha='center', va='center', color='black')
    plt.show()
matrice("C:/Users/said/Desktop/data_science/day05/prediction.txt", "C:/Users/said/Desktop/data_science/day05/truth.txt")