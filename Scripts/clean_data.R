#Load the CSV file into data variable one after the other
data = read.csv(file.choose(),na.strings=c(""),encoding="UTF-8")

#Remove all the messy characters from the Title column 
data$Title <- gsub("[^[:alnum:]]"," ",data$Title)
data$Title <- gsub("[0-9]+", "", data$Title)
data$Title <- gsub("\\n*\\t*\\r*\\s+"," ",data$Title)

nrow(data)

#Export the cleaned data
write.csv(data,"C:\\Users\\prath\\Desktop\\train_data.csv")
