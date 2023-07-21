###############
# 2차함수
###############

# neuralnet : hidden layers 2개 이상 가능
# install.packages('neuralnet')
library(neuralnet)

set.seed(100)

# 행렬 타입 / -2~2 50등분 / 샘플링

# seq(-2,2,50) -2~2 50등분
# sample(데이터, 개수, replace)
# replace=FALSE : 비복원 추출, TRUE = 복원추출
X <- as.matrix(sample(seq(-2,2,length=50),50, replace=FALSE), ncol=1)
y <- X^2 # 2차원 함수
win.graph(); plot(y~X)

df<-as.data.frame(cbind(X,y))
colnames(df) <- c("X","y")
df

# 신경망 모형
# 결과(종속)~ 원인(독립) / 은닉층 2개 노드수 각 10개
nn<-neuralnet(y~X, data=df, hidden=c(10,10))                          
win.graph(); plot(nn) #신경망 그래프
test<- as.matrix(sample(seq(-2,2,length=10),10, replace=FALSE),ncol=1)
pred<-predict(nn,test)
test^2 #실제값
pred #예측값

# Mean Squared Error(평균제곱오차)
mean((pred - test^2)^2)
result<- cbind(test, test^2, pred)
colnames(result) <- c("test","test^2","pred")
result


###############
# 이진분류
###############

df<-read.csv("C:/workspace/hw_study3/data/diabetes/data.csv")

head(df)

library(dplyr)

# 필드 제거 (회귀분석 y 컬럼 제외)
df<-df %>% select(-target)
df

#불균형 데이터셋
tbl<-table(df$target2)
tbl
win.graph(); barplot(tbl, beside = T, legend = T, col = rainbow(2))

# under sampling
#install.packages("ROSE")
library(ROSE)

# method: under,over,both   N: 샘플링 후의 샘플 개수(적은 쪽 x 2) 또는 p=0.5 50:50으로 선택
# 종속~독립(. 모든 독립변수)
# method = over / under
# 195개를 두세트로 만드세요
df_samp <- ovun.sample(target2 ~ . ,data = df, seed=1, method = "under", N=195*2)$data

# 만약 over샘플링하려면
# df_samp <- ovun.sample(target2 ~ . ,data = df, seed=1, method = "over", N=247*2)$data

tbl<-table(df_samp$target2)
tbl

library(caret)

#랜덤 시드 고정
set.seed(123)

#학습용:검증용 8:2로 구분
#list=FALSE, 인덱스값들의 리스트를 반환하지 않음
idx_train <- createDataPartition(y=df_samp$target2, p=0.8, list=FALSE)

#학습용
train <- df_samp[idx_train, ]
X_train <- train[, -11]
y_train <- train[, 11]

#검증용
test <- df_samp[-idx_train, ]
X_test <- test[, -11]
y_test <- test[, 11]

#install.packages('neuralnet')
library(neuralnet)

# threshold : 에러의 감소분이 threshold 값보다 작으면 stop(학습중지기준)
# linear.output 회귀분석인 경우 T, 분류인 경우 F
set.seed(123)

# as.factor(target2) 0과 1 두개로 아웃풋 노드 결정 (원래는 한개)
model <- neuralnet(as.factor(target2) ~ ., data=train, hidden=c(10,10), linear.output = F)

#model$result.matrix #가중치 정보
win.graph(); plot(model)

#변수의 중요도 그래프는 출력층의 노드가 1개일 때만 출력 가능함
#model <- neuralnet(target2 ~ ., data=train, hidden=10, threshold=0.01, linear.output = F)
#library(NeuralNetTools) 
#win.graph(); garson(model)

#세부적인 계산 결과
# pred<-compute(model, X_test)
# pred

# 출력결과(prob - 확률)
pred<-predict(model, X_test, type='prob')
pred

# 각 샘플에 대해 0,1로 출력
# 0 열방향(세로), 1 행방향(가로)
result <- apply(pred, 1, function(x) which.max(x)-1)
result

table(y_test , result)
mean(y_test == result)

# install.packages('Epi')
library(Epi)    
win.graph(); ROC(test=result, stat=y_test, plot="ROC", AUC=T, main="신경망")