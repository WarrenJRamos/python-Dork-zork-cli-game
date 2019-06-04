

group <- NULL
hours <- NULL
names <- c("Andres", "Jacob", "Rachel", "Warren")
i <- 1

while(i < length(names) + 1) {
  hours <- readline(paste("How many hours did", names[i], "work?        " ))
  group <- c(group, hours)  
  i <- i + 1
}
group <- as.numeric(group)

sprintNum <- readline(prompt = "Which sprint is this?       ")
sprint <- cat("Sprint", sprintNum)

pdf(paste(sprint, ".pdf", sep = ""))
barplot(group, names.arg = names, 
        col = "lightblue", 
        main = "Hours Worked", cex.main = 2,
        sub = sprint, cex.sub = 1.5, 
        cex.lab = 1.4, 
        ylim = c(0, 40))
abline(a = 24, b = 0)

dev.off()
