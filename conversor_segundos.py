#declaração de variáveis
segundosIniciais = 0
horas = 0
minutos = 0
segundos = 0

#entrada de dados
segundosIniciais = int(input("Digite a quantidade de segundos iniciais:")) 

#processamento 
horas = segundosIniciais//3600
resto_segundos = segundosIniciais%3600
minutos = resto_segundos//60
resto_segundos = resto_segundos%60
segundos = resto_segundos

# minutos = segundosIniciais/60
# horas = minutos/60
# if minutos > 60:
# 	minutos -= round(horas, 0)*60
# segundos = minutos%60


#saída de dados
print("%dh:%dm:%ds" % (horas,minutos,segundos))