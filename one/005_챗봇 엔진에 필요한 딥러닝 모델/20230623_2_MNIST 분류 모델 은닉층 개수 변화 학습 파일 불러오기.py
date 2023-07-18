from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd

# MNIST 데이터셋 가져오기
_, (X_test, y_test) = mnist.load_data()
X_test = X_test/255.0 # 데이터 정규화

# 모델 불러오기
model = load_model('mnist_model_adam_add30.h5')
# model.summary()
# model.evaluate(X_test, y_test, verbose=2)

# random.seed(2023)
# lst = random.sample(range(1,10000),100)

# cnt=0
# lst1=[]

# for i in lst:
#     cnt+=1
#     predict = np.argmax(model.predict(X_test[[i]]), axis=1)
    
#     if predict!=y_test[i]:
#         print(cnt, predict, y_test[i])
#         lst1.append(cnt)
        
# print(lst1)

predict_lst = np.argmax(model.predict(X_test), axis=1)
predict_S = pd.Series(predict_lst)
y_test_S = pd.Series(y_test)
pred = pd.concat([predict_S, y_test_S], axis=1)
pred['test'] = pred[0]==pred[1]
print(pred['test'].value_counts())