# Minas de Dados
Ferramentas e estratégias para incentivar a cultura de criação e utilização de dados no Estado de Minas Gerais

Note:
- Agradecer a oportunidade e o convite.
- Crédito à apresentação feita por Francisco no evento CodaBr2021 (Conferência Brasileira de Jornalismo de Dados e Métodos Digitais).
- Convidar para visitar os links que serão mostrados ao longo da apresentação.
- Perguntas ao longo da apresentação.
- Tempo Estimado de uma hora.



## Agenda
- Contextualização
- Mão na massa
- Aprendizados
- Aonde queremos chegar
- Questões para discusssão



## Vamos fazer um experimento mental...

Se uma informação só existe com a pessoa que a gerou, e essa pessoa não está disponível, essa informação realmente existe?

Note:
- Documentar é um ato de auxílio a si próprio, pois você de meses atrás não responde e-mails, segundo este [twitter de Karen Cranston](https://twitter.com/kcranstn/status/370914072511791104?s=20), você, de 6 meses atrás, não está mais disponível).


## Contextualização

```mermaid
mindmap
  root((Dores))
    CONSUMIDOR
      1° Procura
        Dados online?
        Licença aberta?
        Legíveis por máquina?
      2° Utilização
        Formato tabular?
        Nomes de variáveis
        Encoding
        Delimitadores
        Confiáveis após atualizações
    PRODUTOR
      1° Preparação
        ETL
      2° Documentação
        Qual padrão adotar?
        Como identificar erros?
        Como publicar?
      3° Publicação
        Ferramentas
        Treinamento
```


## Contextualização

```mermaid
mindmap
  root((Filosofias <br/> e Ferramentas))
    Princípios e Diretrizes
      Dados online
        CKAN
      Legíveis por máquina
      Licença aberta
      Formato tabular
    Frictionless
      Nomes e tipos de variáveis
      Encoding
      Delimitadores
      Verificação sintática
    Docs Like Code
      Formato de texto
      Versionamento
      Construção colaborativa
```

Note:
- Escrita: Armazena o código fonte em sistema de controle de versão.
- Revisão: Processo criterioso de revisão.
- Construção: Feita de maneira automática.
- Publicação: Sem interferência humana.



## Mão na massa
![mao_na_massa](assets/mao_na_massa.jpg)


## Mão na massa
Documentando um [dado](http://www.seguranca.mg.gov.br/2018-08-22-13-39-06/dados-abertos) que já está disponível online.

Note:
- Mostrar fricção como enconding e delimitador na prática.


## Mão na massa - Produtor

    # Iniciando trabalho com controle de versão
    mkdir apresentacao-minas-de-dados
    cd apresentacao-minas-de-dados
    mkdir data/ # Adicionando arquivos de dados (crimes_violentos)
    touch requirements.txt # incluindo ipdb e frictionless[pandas]==4.16.6
    touch .gitignore # incluindo pasta venv
    git init
    git branch -M main
    git add .
    git commit -m "Commit Inicial"

    # Ambiente virtual
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

    # Documentação Inicial do conjunto
    frictionless describe data/* --type package --json > datapackage.json

Note:
- Partir do describe e explicar que o log das ações estão descritas no código de bloco.
- Boa prática durante a organização do conjunto utilizando controle de versão para evitar erros ou perda de informações.


## Mão na massa - Produtor

    # Novo arquivo main.py
    from frictionless import Package

    package = Package('datapackage.json')
    recurso = package.get_resource('crimes_violentos')
    data_frame = recurso.to_pandas()


## Mão na massa - Consumidor

    import locale
    import calendar

    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

    for ano in range(2018, 2024):
      for mes in range(1,13):
        numero_registros = data_frame.loc[(data_frame['Ano'] == ano) & (data_frame['Mês'] == mes )]
        numero_registros = numero_registros['Registros'].sum()
        numero_registros = format(numero_registros, "6,d").replace(",", ".")
        print(f'Foram registrados {numero_registros} crimes violentos em todo Estado de Minas (RISP) em {calendar.month_name[mes].capitalize()} de {ano}.')


## Mão na massa - Consumidor

- Disponibilização via [GitHub](https://github.com/transparencia-mg/crimes-violentos) e [CKAN](https://dados.mg.gov.br/dataset/crimes-violentos) com auxílio da ferramenta [dpckan](https://github.com/transparencia-mg/dpckan).
- [Exemplo de documentação colaborativa](https://github.com/transparencia-mg/violencia-contra-mulher-old/pull/1/commits/3c492efbe101769fc9c58700005794e1ff5d93b4) utilizando as ferramentas mostradas até aqui.

> Apenas uma correção no significado de rmbh.
Eu estava procurando um dicionário de dados e encontrei essa duplicação no YAML.



## Aprendizados

![poliglotas](assets/poliglotas.jpg)
Documentação na [interface do CKAN](http://projetockan.cge.mg.gov.br/dataset/crimes-violentos-dpckan).

Note:
- Publicar mesmo conjunto projeto ckan para acessar link datapackage.json gerado.


## Aonde queremos chegar
    import calendar
    import locale
    from frictionless import Package
    from requests import get

    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

    ckan_datapackage = get('http://projetockan.cge.mg.gov.br/datapackage-creator/show-datapackage-json/fd3619b2-db62-45c2-8c15-52cba375a290')
    package = Package(ckan_datapackage.json())
    resource = package.get_resource('crimes-violentos-2022-1')
    data_frame = resource.to_pandas()

    for ano in range(2022, 2023):
      for mes in range(1,13):
        numero_registros = data_frame.loc[(data_frame['ANO'] == ano) & (data_frame['MES'] == mes )]
        numero_registros = numero_registros['REGISTROS'].sum()
        numero_registros = format(numero_registros, "6,d").replace(",", ".")
        print(f'Foram registrados {numero_registros} crimes violentos em todo Estado de Minas (RISP) em {calendar.month_name[mes].capitalize()} de {ano}.')



### Questões para discussão
- Faz sentido usar o padrão de metadados demonstrado? isso é uma dor comum no compartilhamento e (re)uso dos dados?
- Temos a necessidade de popular o PdA, em escala, por adesão. Neste sentido, um dos produtos deste grupo pode ser a publicação de dados no PdA utilizando as ferramentas aqui apresentadas?


### Questões para discussão
- Quem do grupo conhece/usa rotineiramente o portal PdA? é possível compartilhar uma percepção da experiência do uso?
- O grupo compartilha a percepção relativa ao gap de conhecimento tanto de publicadores quanto de usuários? Quais estratégias podemos utilizar para minimizar o problema como, por exemplo, estratégias para o data literacy?
- Quais outras sugestões do grupo para ativação deste ecossistema?



## Fim

Muito Obrigado
