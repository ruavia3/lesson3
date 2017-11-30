import csv
answers = [
    {'привет': 'Привет!'},
    {'как дела': 'Отлично, а у тебя как?'},
    {'пока': 'еще увидимся'}
]
 
with open("answers.csv","w", encoding ="utf-8") as f:
    writer = csv.DictWriter(f, answers, delimiter=';')
    writer.writeheader()
    for user in user_list:
        writer.writerow(user)