# Lab

## Disclaimer
> **As configurações dos Laboratórios é puramente para fins de desenvolvimento local e estudos**


## Pré-requisitos?
* Docker
* Docker-Compose


### criando nosso KTable do tópico `postgres.dbfiafastapi.produtos`

> [!IMPORTANT]
> Não esqueça de sair do Container 


```bash

docker-compose up -d  ksqldb-server ksqldb-cli 

docker-compose exec ksqldb-cli ksql http://ksqldb-server:8088

SET 'auto.offset.reset'='earliest';
   
create table produtosTable (id int primary key, nome varchar, valor double) with (KAFKA_TOPIC='postgres.dbfiafastapi.produtos', KEY_FORMAT = 'JSON', VALUE_FORMAT = 'JSON');
```

### Criando nosso KStream do tópico `postgres.dbfiafastapi.compraitens`

```bash

 create stream compraitens_stream (id int, idproduto int, valor double, quantidade int, idcompra int) with (kafka_topic='postgres.dbfiafastapi.compraitens', value_format='json');
 
```

### Gerando  join entre Ktable `produtosTable` e KStream  `compraitens_stream`

```bash

create stream comprasItemProduto as 
select  p.id  as id,  ci.idproduto , p.nome, ci.idcompra
from compraitens_stream ci 
left join produtosTable p on ci.idproduto = p.id  emit changes;
 
```

Em outro terminal vamos listar todos os tópicos

```bash
docker exec -it kafka-broker /bin/bash

kafka-topics --bootstrap-server localhost:9092 --list 

kafka-console-consumer --bootstrap-server localhost:9092 --topic COMPRASITEMPRODUTO  --property print.timestamp=true --property print.key=true --property print.value=true --property print.partition=true --from-beginning
	 
```


6. [Criando ambiente MinIO e os Conectores Sink ](../minio/README.md)
7. [Criando APi, gerando evento para o carrinho ](../api/README.md)
8. [Criando ambiente Analytics - Presto ](../presto/README.md)
9. [Criando ambiente Analytics - Criando External tables no Hive](../hive/README.md)
10. [Criando ambiente Analytics - Ingestão de Dados Externos com NIFI](../nifi/README.md)
11. [Analisando Dados com o metabase](../metabase/README.md)