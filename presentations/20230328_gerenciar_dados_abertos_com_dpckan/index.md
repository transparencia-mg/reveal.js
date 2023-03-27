## Datapackage ManagerS - Ferramentas de gerenciamento de dados no CKAN

Como Gerenciar Dados Abertos com o [DPCKAN](https://pypi.org/project/dpckan/).

Note:
- Agradecer a oportunidade e o convite.
- Falar que fizemos os dois cursos a importância em nosso trabalho.
- Tempo Estimado de 1:15 de apresentação com 15 minutos para perguntas e respostas.
- Convidar para visitar os links que serão mostrados.
- Perguntas no chat.
- Dois momentos para responder perguntas ao longo da apresentação e um ao final.



## Agenda

- Quem somos
- Princípios e diretrizes
- Mão na massa
- Aprendizados
- Novas soluções
- Próximos desafios
- Perguntas e respostas



## Quem somos

- Servidores Públicos na Controladoria-Geral do Estado de Minas Gerais - [CGE-MG](https://cge.mg.gov.br/). 
- Lotados na Diretoria Central de Transparência Ativa:
	- [Portal da Transparência MG](https://www.transparencia.mg.gov.br/)
	- [Portal de Dados Abertos MG](https://dados.mg.gov.br/)



## Princípios e diretrizes

- Dados públicos, referenciados na internet.
- Disponibilizados sob licença aberta.
- Estruturado em formato aberto.
- Processáveis por máquina.
![normalized_table](assets/normalized_table.jpg)

Note:
- Licença Aberta: Reutilização em apps e visualizações atribuindo a mesma licença.
- Formato aberto: Não proprietários como arquivos csv.
- Legível por máquina: Dados normalizados.



## Mão na massa
![mao_na_massa](assets/mao_na_massa.jpg) 

Note: 
- Vamos publicar nosso primeiro conjunto de dados no utilizando a interface gráfica do [CKAN](https://treinamento.dadosabertos.cge.mg.gov.br/).
- Utilizaremos como exemplo a base de [Crimes Violentos](https://dados.mg.gov.br/dataset/crimes-violentos), publicada seguindo os princípios e diretrizes mencionados.


## Mão na massa - Experimento mental

- [Se uma informação só existe com a pessoa que a gerou, e essa pessoa não está disponível, essa informação realmente existe?](https://www.youtube.com/watch?v=JUW60w1jDdM&t=1346s) 

- Parafraseando [@mtholder](https://twitter.com/kcranstn/status/370914072511791104?s=20), você, de 6 meses atrás, não está mais disponível.

Note:
- Experimento mental feito por Francisco CODA 2021.
- Mostrar ambiente de produção crimes violentos e convidar para visita do site.
- Primeira pausa para perguntas.


## Mão na massa - Fontes de Fricção

- Nomes de variáveis
- Encoding
- Delimitadores
- Os dados estão corretos? [Frictionless Data Specifications](https://specs.frictionlessdata.io/#overview)

Note:
- Metadados do conjunto utilizado estão na versão em produção.
- 
- Encoding e delimitadores no padrão internacional.
- Separador de milhar e decimal no padrão internacional.
- Padrão csv brasileiro com ';'.


## Mão na massa - Docs Like Code

[Anne Gentle](https://www.docslikecode.com/)
![docs_like_code](assets/docs_like_code.jpg)

Note:
- [sugestões de melhoria crimes violentos](https://dados.mg.gov.br/dataset/crimes-violentos#:~:text=tamb%C3%A9m%20ser%C3%A3o%20inclu%C3%ADdos.-,Como%20participar,-Saiba%20como%20contribuir).
- SOMENTE SE QUESTIONADO: Exemplo COD_MUNICIPIO pouco documentado.


## Mão na massa - dpckan

[CKAN](https://ckan.org/) + [Frictionless](https://frictionlessdata.io/) = [dpckan](https://github.com/transparencia-mg/dpckan)

CLI Python disponível no [Pypi](https://pypi.org/project/dpckan/)

	# Utilização Linux
	python3 -m venv venv
	source venv/bin/activate
	pip install dpckan
	pip list

	# Utilização Windows
	python -m venv venv
	source venv/Scripts/activate
	pip install dpckan
	pip list

Note:
- Ganhador do hackaton frictionless em 2021
- Utilização da GitBash para Windows
- venv como boa prática.
- CKAN garante a disponibilização na Web.
- Frictionless garante leitura por máquina e qualidade.
- dpckan garante a publicação em escala de vários recursos para um único conjunto.


## Mão na massa - dpckan

[CKAN](https://ckan.org/) + [Frictionless](https://frictionlessdata.io/) = [dpckan](https://github.com/transparencia-mg/dpckan)
	
	# Inferência de metadados - datapackage.json
	frictionless describe crimes_violentos.csv --type package --json > datapackage.json

	# Validando meus dados
	frictionless validate datapackage.json

	# Publicação de um conjunto de dados
	# Leitura das mensagens de erro
	dpckan --ckan-host https://treinamento.cge.mg.gov.br --ckan-key <ckan-key> dataset create
	dpckan dataset update
	dpckan resource create
	dpckan resource update

Note:
- [Datapackage creator](https://create.frictionlessdata.io/).
- Prós e contras de cada alternativa.



## Aprendizados

![poliglotas](assets/poliglotas.jpg)

Note:
- E difícil contar com a disposição das pessoas em operar a linha de comando, pois são poucos os poliglotas.
- Baixa adesão ao modelo proposto.
- Ficamos ilhados neste contexto.



## Novas soluções

- [CKANEXT DATAPACKAGE CREATOR](https://pypi.org/project/ckanext-datapackage-creator/) = dpckan na interface gráfica do CKAN!

[Demonstração](http://projetockan.cge.mg.gov.br/)

Note:
- Futura GUI a ser instalado em nossa instância do CKAN.
- Para personas não poliglotas em dados.
- Melhora interação com processo de documentação.
- dpckan não continuará em utilização.
- Segunda pausa para perguntas.



## Próximos desafios

- Ecossistema de demanda e oferta de dados incipiente em MG.
- Gap de conhecimento tanto de publicadores quanto de usuários - Data Literacy.
- Conhecimentos específicos até para o pessoas que trabalham na área.
- Tamanho do banco necessário para comportar bases complexas (dados geospaciais).



## Mais perguntas do que respostas

![question_mark](assets/question_mark.jpg)

[Perguntas recebidas no chat](https://transparencia-mg.github.io/handbook/0.1/posts/20230328_apresentacao_dpckan_curso_ckan/#perguntas-e-respostas)


## Contatos

andre.amorim@cge.mg.gov.br
flavia.vilela@cge.mg.gov.br
gabriel.dornas@cge.mg.gov.br

https://github.com/transparencia-mg/



## Muito Obrigado
