from gensim.models import Word2Vec
from konlpy.tag import Komoran
import time

# 네이버 영화 리뷰 데이터 읽어옴
def read_review_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        data = data[1:] # 헤더 제거
    return data

# 학습 시간 측정 시작
start = time.time()

# 리뷰 파일 읽어오기
print('1) 말뭉치 데이터 읽기 시작')
review_data = read_review_data('./data/ratings.txt')
print(len(review_data))
print('1) 말뭉치 데이터 읽기 완료 :', time.time()-start)

print('2) 형태소에서 명사만 추출 시작')
komoran = Komoran()
docs = [komoran.nouns(sentence[1]) for sentence in review_data]
print('2) 형태소에서 명사만 추출 완료 :', time.time()-start)

print(docs)