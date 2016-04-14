# 生成90个连续的日期
start.date <- as.Date("2015-01-01")
dates <- seq(from=start.date, by=1, length.out=90)

nrow(data) # 查看数据框的行数
ncol(data) # 查看数据框的列数
dim(data)  # 查看数据框的行数和列数
