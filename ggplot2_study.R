library("ggplot2")

# 1.bar chart

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

