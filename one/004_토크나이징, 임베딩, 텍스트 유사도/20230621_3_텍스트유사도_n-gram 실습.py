from konlpy.tag import Komoran

# 어절 단위 n-gram
def word_ngram(bow, num_gram):
    text = tuple(bow)
    ngrams = [text[x:x + num_gram] for x in range(0,len(text)-num_gram+1)]
    return tuple(ngrams)

# 유사도 계산
def similarity(doc1, doc2):
    cnt = 0
    for token in doc1:
        if token in doc2:
            cnt = cnt+1
    return cnt/len(doc1)

def n_gram_similarity():
    sentence1 = input("문장 1: ")
    sentence2 = input("문장 2: ")
    num_gram = int(input("n-gram의 n값: "))
    
    komoran = Komoran()
    bow1 = komoran.nouns(sentence1)
    bow2 = komoran.nouns(sentence2)
    
    doc1 = word_ngram(bow1, num_gram)
    doc2 = word_ngram(bow2, num_gram)
        
    print(doc1)
    print(doc2)
    
    r1 = similarity(doc1, doc2)
    print(r1)
    print("-"*50)
    
n_gram_similarity()


