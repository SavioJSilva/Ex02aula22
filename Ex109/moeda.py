def aumentar(preco=0, taxa=0, formato=False):
    '''

    :param preco: Valor recebido pelo input
    :param taxa: Taxa inserida pelo usuario
    :param formato: Confirmação de formatação ou não, em moeda.
    :return:
    '''
    res = preco + (preco * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if not formato else moeda(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if not formato else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco}'.replace('.',',')