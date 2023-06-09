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

# 문장 단위로 명사만 추출해 학습 입력 데이터로 만듦
print('2) 형태소에서 명사만 추출 시작')
komoran = Komoran()
docs = [komoran.nouns(sentence[1]) for sentence in review_data]
print('2) 형태소에서 명사만 추출 완료 :', time.time()-start)

# Word2Vec 모델 학습
print('3) Word2Vec 모델 학습 시작')
model = Word2Vec(sentences=docs, vector_size=200, window=4, hs=1, min_count=2, sg=1)
# model = Word2Vec(sentences=docs, vector_size=200, window=8, hs=1, min_count=2, sg=1)
# model = Word2Vec(sentences=docs, vector_size=200, window=16, hs=1, min_count=2, sg=1)
print('3) Word2Vec 모델 학습 완료 :', time.time()-start)

# 모델 저장
print('4) 학습된 모델 저장 시작')
model.save('nvmc.model')
print('4) 학습된 모델 저장 완료 :', time.time()-start)

# 학습된 말뭉치 수, 코퍼스 내 전체 단어 수 
print('corpus_count :', model.corpus_count)
print('corpus_total_words :', model.corpus_total_words)