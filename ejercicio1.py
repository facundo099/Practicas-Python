#Consigna: https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    main_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        main_list.append([name, score])
          
    min_score = main_list[0][1]  #asumo que el primer elemento es el minimmo
    for student in main_list:
        if student[1] < min_score:
            min_score = student[1]
            
    filtered_list = []
    for student in main_list:
        if student[1] != min_score: #busco un score distinto al minimo
            filtered_list.append(student)   #si lo encuentro lo agrego a mi lista filtrada
            
    second_min_score = min([student[1] for student in filtered_list])   #aca busco el SEGUNDO menor valor
    second_min_students = [student for student in main_list if student[1] == second_min_score] #aca busco el segundo menor estudiante
    
    
sorted_students = sorted(second_min_students)   #ordeno alfabaticamente

for student in sorted_students:
    print(student[0])
