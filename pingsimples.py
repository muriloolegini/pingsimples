import os #Importando o módulo ou bibliotéca os(integrando programas e recursos do S.O)

print('#' * 60) #Imprimindo '#' 60 vezes
ip_ou_host = input('Digite um ip ou host a ser verificado: ') #variável que vai receber um ip digitado pelo usuário

print('-' * 60) #Imprimindo '-' 60 vezes
os.system('ping -n 6 {}'.format(ip_ou_host))
print('-' * 60) #Imprimindo '#' 60 vezes
