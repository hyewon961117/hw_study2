df<-read.csv("C:/workspace/hw_study3/data/iris/iris.csv") 
head(df) 

library(dplyr) # 필드 제거 
df<-df %>% select(-Name)

#install.packages('fpc')  
library(fpc)          
iris2 <- df[-5]    # 5번 필드 제외

#밀도기반 군집화   eps 중심점과의 거리, MinPts 최소 샘플 개수  
ds <- dbscan(iris2, eps=0.42, MinPts=5)

#클러스터링 결과값과 실제 라벨과의 비교표
table(ds$cluster, iris$Species)      

# 클러스터 0: 할당되지 않은 값(outlier)
win.graph(); plot(ds, iris2)
win.graph(); plot(ds, iris2[c(1,4)]) #4행 1열의 그래프만 출력
win.graph(); plot(ds, iris2[c(2,1)]) #1행 2열의 그래프만 출력

#fpc 패키지
# 0 - outlier(밀도 조건에 맞지 않는 샘플들)
win.graph(); plotcluster(iris2, ds$cluster) 
