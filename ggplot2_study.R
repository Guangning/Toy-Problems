library("ggplot2")

# 1.line

# 1) use geom_line() to connect dots
ggplot(economics, aes(date, unemploy)) + geom_line()
ggplot(economics_long, aes(date, value01, colour=variable)) + geom_line()

# 2) use geom_step() to highlight the y value changes
recent <- economics[economics$date>as.Date("2013-01-01"),]
ggplot(recent, aes(date, unemploy)) + geom_step()

# 3) use geom_path() to explore how two variables are related over time
ggplot(economics, aes(unemploy/pop, psavert)) + geom_path(aes(colour=as.numeric(date)))

# 4) Change parameters
# change the line colour and add an arrow
ggplot(economics, aes(date, unemploy)) + geom_line(colour="red", arrow=arrow(angle=15, ends="both", type="closed"))


# 2.bar chart

# 1) Number of cars in each class
ggplot(mpg, aes(class)) + geom_bar()

# 2) Total engine displacement of each class
ggplot(mpg, aes(class)) + geom_bar(aes(weight=displ))

# 3) Place multiple bars at the same location
ggplot(mpg, aes(class)) + geom_bar(aes(weight=displ, fill=drv))

# 3) Place multiple bars at the same location separately / fill them
ggplot(mpg, aes(class)) + geom_bar(aes(weight=displ, fill=drv), position="dodge")
ggplot(mpg, aes(class)) + geom_bar(aes(weight=displ, fill=drv), position="fill")

# 4) Change the plot order of the bars
reorder_size <- function(x) {
    factor(x, levels = names(sort(table(x), decreasing=TRUE)))
}
ggplot(mpg, aes(reorder_size(class))) + geom_bar()

