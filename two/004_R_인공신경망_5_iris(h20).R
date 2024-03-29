#설치시간이 오래 걸림
#install.packages('RCurl')
#install.packages('h2o')
#Sys.setenv(JAVA_HOME='C:/Program Files/Java/jdk1.8.0_361')

library(h2o)

#h2o에 접속
# localH2O = h2o.init(ip="localhost", port = 54321, nthreads=-1)
localH2O = h2o.init()

# http://localhost:54321 접속
train <- h2o.importFile("C:/workspace/hw_study3/data/iris/iris.csv")
test <- h2o.importFile("C:/workspace/hw_study3/data/iris/iris.csv")

X <- names(train)[1:4]
y <- names(train)[6]

# 정수형을 범주형으로 바꿔줌
train[,y] <- as.factor(train[,y])
test[,y] <- as.factor(test[,y])

iris_h2o <- as.h2o(iris, destination_frame = "iris_h2o")
h2o.ls() # 변수 목록을 불러옴

class(iris_h2o)
head(iris_h2o)

n_rows <- nrow(iris_h2o) # 행의 수
n_cols <- ncol(iris_h2o) # 열의 수

paste("행의 개수 : ", n_rows)

set.seed(123)

# sample(데이터, 샘플링사이즈, 중복여부 FALSE(비복원 추출))
train_idx <- sample(1:nrow(iris), size = 0.8 * nrow(iris), replace = FALSE)
train_iris <- iris[train_idx, ]
test_iris <- iris[-train_idx, ]

#품종별 비율
with(train_iris, prop.table(table(Species)))

#h2o 타입으로 변환
train_iris_h2o <- as.h2o(train_iris, "train_iris_h2o")
test_iris_h2o <- as.h2o(test_iris, "test_iris_h2o")
target <- "Species"

#독립변수들의 이름
features <- names(train_iris)[!names(train_iris) %in% target]
features

#로지스틱 회귀분석(분류)
glm_model <- h2o.glm(x = features, y = target, training_frame = train_iris_h2o, model_id = "glm_model", family = "multinomial")
# multinomial 다중분류 / 기본 이진분류

summary(glm_model)
#R^2: (Extract with `h2o.r2`) 0.9820152 설명력
#k hit_ratio 정확도
#scaled_importance 변수의 중요도

pred_iris_glm <- as.data.frame(h2o.predict(glm_model, newdata = test_iris_h2o))

#예측값
test_iris$pred_glm <- pred_iris_glm$predict
# virginica는 한개빼고 다 맞음

#오분류표 , dnn(Dimension Names)
# with - 데이터프레임의 필드명으로 직접 접근할 수 있는 함수
with(test_iris, table(Species, pred_glm, dnn = c("Real", "Predict")))

#랜덤 포레스트 모형
rf_model <- h2o.randomForest(x = features, y = target, training_frame = train_iris_h2o, model_id = "rf_model", ntrees = 100)

summary(rf_model)

pred_iris_rf <- as.data.frame(h2o.predict(rf_model, newdata = test_iris_h2o))

#예측값
test_iris$pred_rf <- pred_iris_rf$predict

#오분류표
with(test_iris, table(Species, pred_rf, dnn = c("Real", "Predict")))
with(test_iris, prop.table(table(Species)))

