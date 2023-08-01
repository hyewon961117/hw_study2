from chatbot.Preprocess1 import Preprocess1

sent = '내일 오전 10시에 짜장면 주문하고 싶어'

# 객체 생성 (클래스가 메모리에 올라감)
p = Preprocess1(userdic='C:/workspace/hw_study3/FoodShop/chatbot/data/user_dic.tsv')

pos = p.pos(sent)
keywords = p.get_keywords(pos, without_tag=False)

print(keywords)