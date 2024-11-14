library(plspm)

v.n = function(a,b)
{ # a - variable, b - a x number of times
    a = as.character(a)
    b = as.numeric(b)
    x = rep(a,b)
    y = 1:b
    z = paste0(x,y)
}

p = pspp_csv[,c(v.n("EU",3),v.n("SFO",4),v.n("IO",4),v.n("SO",4),v.n("SNF",6),v.n("DIS",4),v.n("DUI",4))] # table of data

head(p,n=5)

EU = c(0,0,0,0,0,0,0)
SFO = c(1,0,0,0,0,0,0)
IO = c(1,0,0,0,0,0,0)
SO = c(1,0,0,0,0,0,0)
SNF = c(0,1,1,1,0,0,0)
DIS = c(0,0,0,0,1,0,0)
DUI = c(0,0,0,0,1,1,0)

path = rbind(EU,SFO,IO,SO,SNF,DIS,DUI)
colnames(path) = rownames(path)
#innerplot(path, box.size = 0.1)
#plot(edu_pls3, arr.pos = 0.35)

innerplot(path)

l.v = list(1:3,4:7,8:11,12:15,16:21,22:25,26:29)
lv.m = c("A","A","A","A","A","A","A") # rep("A", 6)

pls.r = plspm(p,path,l.v,modes=lv.m,scheme="path",boot.val=T,br=500)

#dim(p) # 0x0
#summary(p[, 1:29]) # Median/Mean
