# Lab

## Disclaimer
> **As configurações dos Laboratórios é puramente para fins de desenvolvimento local e estudos**


## 💻 Pré-requisitos
* Docker
* Docker-Compose


Nosso tópico produto do kafka será do tipo Compact.

Lembram pra que serve os tópicos do tipo Compact!!??

> [!IMPORTANT]
> Entre no container caso ainda não esteja nele.

```bash

docker exec -it kafka-broker /bin/bash

kafka-topics --create --topic postgres.dbfiafastapi.produtos --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1 --config cleanup.policy=compact

kafka-topics --bootstrap-server localhost:9092 --list 

exit

```



### Desenvolveremos um conector para extrair dados da tabela Produto e publicar mensagens no Kafka de forma eficiente.

No arquivo `conectores/conector-postgres-produto.json` ajuste o atributo `table.include.list` para informar o nome da tabela do postegreSQL que será feito a leitura dos dodos


### Terminal Linux
```bash

curl -X PUT -d @conectores/conector-postgres-produto.json http://localhost:8083/connectors/connector-postgres-produtos/config -H 'Content-Type: application/json' -H 'Accept: application/json'
```

### Terminal PowerShell
```powershell
$response = Invoke-WebRequest -Uri "http://localhost:8083/connectors/connector-postgres-produtos/config" -Method Put -Body (Get-Content -Path "conectores/conector-postgres-produto.json" -Raw) -ContentType "application/json"; $response.Content

```


```bash
docker exec -it kafkaConect curl http://localhost:8083/connectors/connector-postgres-produtos/status
```


Deu certo?? Vamos consumir as mensagens da tabela produto

```bash

docker exec -it kafka-broker /bin/bash

kafka-topics --bootstrap-server localhost:9092 --list 

kafka-console-consumer --bootstrap-server localhost:9092 --topic postgres.dbfiafastapi.produtos --property print.timestamp=true --property print.key=true --property print.value=true --property print.partition=true --from-beginning
	
```


> [!Note]
> Inserindo alguns itens nas tabelas abaixo pelo PgAdmin


```sql
INSERT INTO dbfiafastapi.produtos VALUES (default,'lapis',3.14);

INSERT INTO dbfiafastapi.compra(
	id, valortotal)
	VALUES (default, 100);

INSERT INTO dbfiafastapi.compraitens(
	id, idproduto, valor, quantidade, idcompra)
	VALUES (default, currval(pg_get_serial_sequence('dbfiafastapi.produtos','id')), 10, 1,  currval(pg_get_serial_sequence('dbfiafastapi.compra','id')));
    
```	



5. [Criando nossa primeira transformação com KSql](../transformacao-ksql/README.md)
6. [Criando ambiente MinIO e os Conectores Sink ](../minio/README.md)
7. [Criando Api, gerando evento para o carrinho ](../api/README.md)
8. [Criando ambiente Analytics - Presto ](../presto/README.md)
9. [Criando ambiente Analytics - Criando External tables no Hive](../hive/README.md)
11. [Criando ambiente Analytics - Ingestão de Dados Externos com NIFI](../nifi/README.md)
12. [Analisando Dados com o metabase](../metabase/README.md)