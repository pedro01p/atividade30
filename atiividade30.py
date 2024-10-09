# crie uma duncao que calcule a nota a media de 3 notas em seguida verifique se ele esta aprovado ou reprovado para notas acima de 7

def calcula_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3)/3
    return media
    
def verificar_resultados(media):
    if media >= 7:
        return 'Aprovado'
    else:
        return 'Reprovado'

nota1 = float(input("digite a nota "))
nota2 = float(input("digite a nota "))
nota3 = float(input("digite a nota "))

resultado_media = calcula_media(nota1, nota2, nota3)
print(resultado_media)

resultado_final = verificar_resultados(resultado_media)
print(resultado_final)
