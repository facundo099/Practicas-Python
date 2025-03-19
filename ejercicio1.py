#Consigna: https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
if __name__ == '__main__':
    main_list = []

    # pedir numero de estudiantes
    num_students = int(input("Ingrese la cantidad de estudiantes: "))
    print(f"Cantidad ingresada: {num_students}")

    for i in range(num_students):
        name = input(f"Ingrese el nombre del estudiante {i+1}: ")
        score = float(input(f"Ingrese la calificacion de {name}: "))
        main_list.append([name, score])
    
    print("\nLista de estudiantes y calificaciones ingresadas:")
    for student in main_list:
        print(f"Nombre: {student[0]}, Calificación: {student[1]}")

    # encontrar el puntaje mas bajo
    min_score = min(student[1] for student in main_list)
    print(f"\nPuntaje mas bajo encontrado: {min_score}")

    # filtrar estudiantes con puntaje mayor al minimo
    filtered_list = [student for student in main_list if student[1] != min_score]

    if not filtered_list:
        print("No hay un segundo puntaje minimo. Finalizando programa.")
        exit()  

    # encontrar el segundo puntaje mas bajo
    second_min_score = min(student[1] for student in filtered_list)
    print(f"Segundo puntaje mas bajo encontrado: {second_min_score}")

    # encontrar los estudiantes con el segundo puntaje mas bajo
    second_min_students = [student for student in main_list if student[1] == second_min_score]

    print("\nEstudiantes con el segundo puntaje mas bajo:")
    for student in second_min_students:
        print(f"Nombre: {student[0]}, Calificación: {student[1]}")

    # ordenar por nombre alfabeticamente
    sorted_students = sorted(second_min_students, key=lambda x: x[0])

    print("\nEstudiantes ordenados alfabeticamente con el segundo puntaje mas bajo:")
    for student in sorted_students:
        print(student[0])

