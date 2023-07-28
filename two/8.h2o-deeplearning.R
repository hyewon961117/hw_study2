df<-read.csv("c:/data/concrete/concrete.csv")
head(df)
library(dplyr)
# 필드 제거
df<-df %>% select(-strength)
df$class <- as.factor(df$class)
#불균형 데이터셋
tbl<-table(df$class)
tbl
win.graph(); barplot(tbl, beside = T, legend = T, col = rainbow(2))


library(ROSE)
# method: under,over,both   N: 샘플링 후의 샘플 개수(적은 쪽 x 2) 또는 p=0.5 50:50으로 선택
df_samp <- ovun.sample(class ~ . ,data = df, seed=1, method = "under", 
                       N=507*2)$data
tbl<-table(df_samp$class)
tbl

library(caret)
#랜덤 시드 고정
set.seed(123)
#학습용:검증용 8:2로 구분
#list=FALSE, 인덱스값들의 리스트를 반환하지 않음
idx_train <- createDataPartition(y=df$class, p=0.8, list=F)

#학습용
train <- df[idx_train, ]
X_train <- train[, -9]
y_train <- train[, 9]
#검증용
test <- df[-idx_train, ]
X_test <- test[, -9]
y_test <- test[, 9]

head(train)
head(test)

#install.packages("h2o")
#install.packages('bit64', repos = "https://cran.rstudio.com")
library(h2o)
h2o.init()                            
set.seed(123)
tr_data <- as.h2o(train)
te_data <- as.h2o(test)
target <- "class"
#독립변수들의 이름
features <- names(train)[1:8]
features

model <- h2o.deeplearning(x = features, y = target, 
  activation = "Rectifier",
  training_frame = tr_data, ignore_const_cols = FALSE, 
  hidden = c(50,50))
summary(model)
# 예측값
pred <- h2o.predict(model, te_data)


perf <- h2o.performance(model, te_data)
h2o.confusionMatrix(perf)
h2o.accuracy(perf, thresholds = 0.422770956861397)
h2o.F1(perf, thresholds = 0.422770956861397)







