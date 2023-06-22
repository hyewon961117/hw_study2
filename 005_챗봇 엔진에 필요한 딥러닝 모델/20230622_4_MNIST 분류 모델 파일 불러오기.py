from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt

# MNIST 데이터셋 가져오기
_, (X_test, y_test) = mnist.load_data()
X_test = X_test/255.0 # 데이터 정규화

# 모델 불러오기
model = load_model('mnist_model.h5')
model.summary()
model.evaluate(X_test, y_test, verbose=2)

# 테스트셋에서 20번째 이미지 출력
plt.imshow(X_test[20], cmap='gray')
plt.show()

# 테스트셋의 20번째 이미지 클래스 분류
picks = [20]
predict = model.predict_classes(X_test[picks])
print('손글씨 이미지 예측값 : ', predict)