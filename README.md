## Projeto ibge-api 

Esta ideia engloba uma forma mais direta de lidar com os dados do IBGE

Os dados carregados no momento pela API são:

* Países 
* Estados

As URLs base são as seguintes

* /paises
* /estados

Todos os endpoints serão os mesmos a depender da sua url base

* /{base} - lista todos os dados sobre
* /{base}/{id} - lista os dados de um especiificamente
* /{base}/nomes - retorna apenas os nomes de cada um