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


# 직접 그린 이미지
mask = np.array(Image.open('./8.png'))/255
mask = tf.image.rgb_to_grayscale(mask)
mask = np.mean(mask, axis=2)
mask = mask.reshape((1, -1)) 
print(mask.shape)

# 테스트셋에서 20번째 이미지 출력
plt.imshow(mask.reshape((28, 28)), cmap='gray')
plt.show()


# 모델에 입력하기 전에 형태를 맞추기 위해 reshape
mask = mask.reshape((1, 28, 28))

predict = np.argmax(model.predict(mask), axis=1)
image = model.predict(mask)

print('손글씨 이미지 예측값 : ', predict)
print('손글씨 이미지 예측값 : ', image)