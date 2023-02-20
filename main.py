import random


def forca():
  lista_palavras = ('quarto', 'raquete', 'esquilo', 'jaqueta', 'queijo',
                    'peixe', 'habituado', 'holofote', 'hospital', 'abelha',
                    'coelho', 'vermelho', 'telhado', 'gafanhoto', 'desenho',
                    'cachorro', 'geladeira', 'bateria', 'zero', 'borboleta',
                    'martelo', 'urso', 'primavera')
  numero_aleatorio = random.randint(0, 22)
  palavra = lista_palavras[numero_aleatorio]
  tetativa_errada = 0
  estagios = [
    "", "________      ", "|      |      ", "|      0      ", "|     /|\     ",
    "|     / \     ", "|"
  ]
  letras_restantes = list(palavra)
  quadro = ["__"] * len(palavra)
  win = False
  print('<---- Bem-vindo a Forca ---->')
  print(palavra)
  while tetativa_errada < len(estagios) - 1:
    print('\n')
    advinha = input("Adivinhe a letra:").strip().lower()
    if advinha in letras_restantes:
      letra_index = letras_restantes.index(advinha)
      quadro[letra_index] = advinha
      letras_restantes[letra_index] = ''
    else:
      tetativa_errada += 1
    print((' '.join(quadro)))
    print('\n'.join(estagios[0:tetativa_errada + 1]))
    if '__' not in quadro:
      print(f'Você venceu!\nPalavra certa: {palavra}')
      win = True
      break
  if not win:
    print('\n'.join(estagios[0:tetativa_errada]))
    print(f'Você perdeu a palavra certa é: {palavra}')


if __name__ == '__main__':
  forca()
