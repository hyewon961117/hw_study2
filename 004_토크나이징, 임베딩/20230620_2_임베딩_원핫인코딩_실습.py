from konlpy.tag import Komoran
import numpy as np

komoran = Komoran()
# text = '선생님과 학생들이 학원에서 수업한다.'
# text = '학원 수업은 컴퓨터 수업이다.'
text = '선생님과 학생들이 학원에서 수업한다. 수업 내용은 컴퓨터 수업이다.'

# 명사만 추출
nouns = komoran.nouns(text)
print(nouns)

# 단어 사전 구축 및 단어별 인덱스 부여
dics = {}
for word in nouns:
    if word not in dics.keys():
        dics[word] = len(dics)
print(dics)

# 원-핫 인코딩
nb_classes = len(dics)
targets = list(dics.values())
one_hot_targets = np.eye(nb_classes)[targets]
print(one_hot_targets)
# print(np.eye(nb_classes)[[0,2]])