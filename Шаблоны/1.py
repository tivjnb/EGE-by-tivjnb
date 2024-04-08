from itertools import permutations

need='de ef'
table='13 18 24 25 26 35 38 47 67 68' #вносим таблицу( половину)
graph= 'ae ab bf ef ec ch cd dh hg gf' #связи, не надо дубилровать АБ БА
#Здесь оно само дублируется
table=table + ' ' + table[::-1]
graph=graph + ' ' + graph[::-1]
#это кол-во пунктов
x=8
#не забудьте в пермутате буквы на имена пунктов поменять
for per in permutations('abcdefgh'):
    #Внутри все неизменно, если x поменять конечно
    new_graph = table
    for i in range(1,x+1):
        new_graph=new_graph.replace(str(i),per[i-1])
    if set(new_graph.split())==set(graph.split()):
        #Словарик для того что бы вывести номера наших путей
        d=dict(zip(per,[str(x) for x in range(1,x+1)]))
        d[' ']=' '
        #Соответственно первая часть вывод последовательности, а вторая нужных путей по переменной need
        print(per,''.join([d[x] for x in need]))