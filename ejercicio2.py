#https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split() #aca tengo los nombres
        scores = list(map(float, line)) #aca tengo las notas
        student_marks[name] = scores #aca tengo ambas cosas
        
    query_name = input() #aca consulto alumno
    
    if query_name in student_marks:
        scores = student_marks[query_name]
        average = sum(scores) / len(scores)
        print(f"{average:.2f}")
