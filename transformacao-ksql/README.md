# Lab

## Disclaimer
> **As configurações dos Laboratórios é puramente para fins de desenvolvimento local e estudos**


## Pré-requisitos?
* Docker
* Docker-Compose


### criando nosso KTable do tópico `postgres.dbfiafastapi.produtos`

```bash

SET 'auto.offset.reset'='earliest';
   
create table produtosTable (id int primary key, nome varchar, valor double) with (KAFKA_TOPIC='postgres.dbfiafastapi.produtos', KEY_FORMAT = 'JSON', VALUE_FORMAT = 'JSON');
```

### criando nosso KStream do tópico `postgres.dbfiafastapi.compraitens`

```bash

 create stream compraitens_stream (id int, idproduto int, valor double, quantidade int, idcompra int) with (kafka_topic='postgres.dbfiafastapi.compraitens', value_format='json');
 
```

### Gerando um join entre Ktable `produtosTable` e KStream  `compraitens_stream`

```bash

create stream comprasItemProduto as 
select p.id as idproduto, p.nome, ci.idcompra
from compraitens_stream ci 
left join produtosTable p on ci.idproduto = p.id  emit changes;
 
```

6. [Criando ambiente MinIO e os Conectores Sink ](minio/README.md)