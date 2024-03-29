df<-read.csv("C:/workspace/hw_study3/data/iris/iris.csv")

head(df)
tail(df)

library(dplyr)

# 필드 제거
df<-df %>% select(-Name)
# 입력데이터 방향 선택(-제외, +추가)

# 데이터의 구조를 봄 structure
str(df)

#Species 변수가 int로 되어 있는데 Factor(범주형) 타입으로 변경해야 함
df$Species <- as.factor(df$Species)

str(df)
head(df)

# 차원 확인
dim(df)

# 기초통계량
summary(df)

# 상관계수 행렬
# 괄호가 있으면 연산하고 바로 출력까지 되는것
(corrmatrix <- cor(df[1:4])) 
# R 1234 인덱스 1부터 시작 / python 123 인덱스 0부터 시작

library(corrplot)
corrplot(cor(df[1:4]), method="circle")
# win.graph(); 창으로 띄워서 바로 볼 수 있음
library(caret)

#랜덤 시드 고정
set.seed(123)

#학습용:검증용 8:2로 구분
#list=FALSE, 인덱스값들의 리스트를 반환하지 않음
idx_train <- createDataPartition(y=df$Species, p=0.8, list=FALSE)
#변수	대입			                     종속변수  학습용

# 학습용
# 데이터프레임[행,렬] 1,3,5,8,10
train <- df[idx_train, ]
X_train <- train[, -5]
y_train <- train[, 5]

# 검증용
# 1,3,5,8,10 제외 나머지들
test <- df[-idx_train, ]
X_test <- test[, -5]
y_test <- test[, 5]

head(X_train)
head(y_train)

library(nnet)

# 학습용 데이터를 이용하여 신경망 모형 생성
# nnet(종속변수 ~ 독립변수), hidden layer 1개
# size 은닉노드의 개수
# . 모든 변수 (a+b+c+d)
model <- nnet(Species ~ ., data = train, size = 10)
summary(model)

# a 4-10-3 network with 83 weights
# 입력-은닉-출력 노드수   with 가중치수
# 입력노드수는 독립변수의 개수로 설정됨

#신경망 모형에 대한 다양한 정보들
names(model)

#최적의 가중치 집합
head(model$wts)

library(devtools)

source_url('https://gist.githubusercontent.com/Peque/41a9e20d6687f2f3108d/raw/85e14f3a292e126f1454864427e3a189c2fe33f3/nnet_plot_update.r')

win.graph(); plot.nnet(model)

# 신경망 모형의 검증(학습용 데이터)
# predict(신경망모델, 데이터셋)
pred <- predict(model, X_train, type="class")

# 예측 결과가 벡터의 형태로 리턴됨
# 오분류표 생성(confusion matrix)
# table(실제결과, 예측결과) 실제결과와 예측결과에 대한 교차표 작성
# result <- ifelse(pred>0.5,1,0)

table(y_train, pred)
mean(y_train == pred)

# 신경망 모형의 검증(검증용 데이터)
pred <- predict(model, X_test, type="class")

# result <- ifelse(pred>0.5,1,0)
table(y_test, pred)
mean(y_test == pred)

