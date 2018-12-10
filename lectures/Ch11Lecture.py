def get_grades():
    name = input("Enter student name: ")
    grades = [] 
    
    while True:
        grade = input("Enter student's grade. q to quit: ")
        
        if grade == 'q':
            break    
        
        grade = float(grade)
        grades.append(grade)
        
    return name, grades
        
def main():
    
    main_dict = {}
    
    while True:
        print("1. Enter name and grades")
        print("2. Print averages")
        selection = input("Enter selection - q to quit: ")

        if selection == "q":
            break
            
        if selection == "1":
            name, grades = get_grades()
            main_dict[name] = grades
			
		elif selection == "2":
            for key in main_dict:
                grades = main_dict[key]
                total = sum(grades)
                print("{0}: {1}".format(key, total/len(grades))
        
	print(main_dict)			  
					  
if __name__ == "__main__":
    main()



