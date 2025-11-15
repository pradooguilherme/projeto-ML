#  Modelo supervisionado de reranqueamento (LambdaRank + BM25)

Este projeto tem como objetivo treinar um modelo supervisionado de **reranqueamento** baseado em **Learning to Rank (LTR)**, combinando features derivadas do **BM25** e outras métricas textuais para ordenar documentos de acordo com consultas.

---

##  Conjunto de documentos e consultas

O dataset utilizado é o **BBC News**, composto por aproximadamente **2.200 documentos** categorizados em cinco temas principais:

- **Business**
- **Entertainment**
- **Politics**
- **Sport**
- **Tech**

Para cada categoria, foram geradas **6 consultas**, totalizando **30 consultas**. Essas consultas serviram como base para a construção do conjunto de treinamento do modelo.

---

## Criação do conjunto de treinamento

Inicialmente, realizamos uma **divisão holdout** na proporção de **70% para treinamento** e **30% para teste**.

Os dados de entrada do modelo seguem o formato **query-documento**, onde cada linha representa um documento retornado por uma consulta e suas respectivas features.

A geração desse conjunto foi feita através de buscas no **Elasticsearch**, que utiliza o **BM25** como algoritmo padrão de ranqueamento.  
Para cada consulta, coletamos os **50 melhores resultados**, registrando as seguintes features:

- **Pontuação BM25** do documento  
- **Número de palavras da consulta presentes no título**  
- **Número de palavras da consulta presentes no corpo do texto**

O resultado foi um **dataset supervisionado** de pares query-documento com três features numéricas por amostra.

---

##  Treinamento do modelo

O modelo foi treinado utilizando o algoritmo **LambdaRank**, implementado na biblioteca **LightGBM**.  
Esse algoritmo aprende a ordenar documentos com base em **rótulos de relevância supervisionados**.

O rótulo de relevância foi definido como binário:

- **1**: documento pertence à mesma categoria da consulta  
- **0**: documento pertence a uma categoria diferente  

---

##  Resultados

No conjunto de teste, o modelo **LambdaRank** obteve um **NDCG@10 médio de 0.6576**, representando um **ganho relativo de aproximadamente 4%** em relação à baseline baseada exclusivamente no BM25 (**NDCG@10 = 0.6158**).

---

##  Conclusão e próximos passos

Apesar do **tamanho reduzido do dataset** e do **número limitado de features**, o modelo apresentou uma **melhora significativa** em relação ao BM25 puro.

Os resultados indicam que o uso de **Learning to Rank** é promissor mesmo em cenários simples.

**Próximos passos:**

- Incorporar **novas features semânticas** (ex: embeddings)  
- Avaliar desempenho em **coleções maiores** e com **consultas reais**  

---

##  Tecnologias utilizadas

- Python  
- Elasticsearch  
- LightGBM  
- NumPy  
- Pandas
