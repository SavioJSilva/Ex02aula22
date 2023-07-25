import utilidadesCeV.moeda as moeda
import utilidadesCeV.dados as dados
p = dados.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(p, 20, 12)