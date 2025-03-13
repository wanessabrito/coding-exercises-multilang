'''
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
'''
arquivo_tamanho = float(input('Digite o tamaho do arquivo para download em (MB): '))
velocidade_link = float(input('Digite a velocidade do link em (Mbps): '))
megabits = arquivo_tamanho * 8 
segundos = megabits / velocidade_link
minutos = segundos/60
print(f'O download estará pronto em {minutos:.2f}m.')