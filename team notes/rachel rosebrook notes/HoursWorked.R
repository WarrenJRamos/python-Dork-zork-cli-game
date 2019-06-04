rachel <- 8
warren <- 10
jacob <- 12
andres <- 16

group <- c(andres, jacob, rachel, warren)
names <- c("Andres", "Jacob", "Rachel", "Warren")

sprint <- "Sprint 2"

pdf(paste(sprint, ".pdf", sep = ""))
barplot(group, names.arg = names, 
        col = "lightblue", 
        main = "Hours Worked", cex.main = 2,
        sub = sprint, cex.sub = 1.5, 
        cex.lab = 1.4, 
        ylim = c(0, 20))
dev.off()