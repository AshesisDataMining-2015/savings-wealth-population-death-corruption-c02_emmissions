setwd ("C:/Users/Shamir/Copy/School/Data Mining/project/modified")
list.files()
data = read.csv("death_rate_vrs_corruption.csv",header=TRUE)

#logistic model
logistcModel = glm(corruption.score ~.,family=poisson,data=data)

#linear model
lm = lm(corruption.score~.,data=data)


newdata = read.csv("death_rate_vrs_corruption_test.csv",header=TRUE)


#test logistic
glfit = predict(logistcModel,newdata,type="response")
glpred = prediction(glfit,newdata$corruption.score)
glperf = performance(glpred,"tpr","fpr")




plot(glperf,xlim=c(0,1),ylim=c(0,1),xaxs="i",yaxs="i",lwd=2)
#plot(lperf,add=TRUE,col=2,lwd=2)


#test linear
lmfit = predict(lm,newdata=newdata)
lprec = prediction(lm,newdata$corruption.score)
lpref = performance(lprec,"tpr","fpr")
