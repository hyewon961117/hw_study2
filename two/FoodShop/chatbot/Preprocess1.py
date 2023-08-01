from konlpy.tag import Komoran
import jpype

class Preprocess1:
    def __init__(self, word2index_dic='', userdic=None):
        # init 초기화 함수 - 객체 생성, 자동 호출

        self.word_index = None

        # 형태소 분석기 초기화
        self.komoran = Komoran(userdic=userdic) # 사용자 사전

        # 제외할 품사
        # 참조 : https://docs.komoran.kr/firststep/postypes.html
        # 관계언, 기호, 어미, 접미사 제거
        self.exclusion_tags = [
            'JKS', 'JKC', 'JKG', 'JKO', 'JKB', 'JKV', 'JKQ', 'JX', 'JC',
            'SF', 'SP', 'SS', 'SE', 'SO',
            'EP', 'EF', 'EC', 'ETN', 'ETM',
            'XSN', 'XSV', 'XSA'
        ]

    # 형태소 분석기
    def pos(self, sentence):
        jpype.attachThreadToJVM() # komoran에서 자바로 연결해주는 코드
        return self.komoran.pos(sentence)

    # 불용어 제거 후, 필요한 품사 정보만 가져오기
    def get_keywords(self, pos, without_tag=False):
        f = lambda x : x in self.exclusion_tags
        word_list = []
        for p in pos :
            if f(p[1]) is False:
                # 불용어가 아니면 추가
                word_list.append(p if without_tag is False else p[0])
        return word_list