# Lab

## Disclaimer
> **As configurações dos Laboratórios é puramente para fins de desenvolvimento local e estudos**


## Pré-requisitos?
* Docker
* Docker-Compose

## Configurando o Conector PostgreSql

### Criando os Conectores para as tabelas Compra e Compra Itens

*API rest do kafka Connect*
https://docs.confluent.io/platform/current/connect/references/restapi.html


No arquivo `conector-postgres.json` onde está o conector está faltando os dados de login e senha, pegue-o no arquivo `docker-compose.yaml` serviço postgres e preencha com os valores.

```bash

http PUT http://localhost:8083/connectors/connector-postgres/config < conector-postgres.json

//Ou via powershell
$response = Invoke-WebRequest -Uri "http://localhost:8083/connectors/connector-postgres/config" -Method Put -Body (Get-Content -Path "conector-postgres.json" -Raw) -ContentType "application/json"; $response.Content


```

### Deu certo?

```bash
	docker exec -it kafkaConect curl http://localhost:8083/connectors/connector-postgres-produtos/status
```

Insira alguns registros

> [!IMPORTANT]
> Na tabela `compraitens` insira produtos que já possuem na tabela `produtos`


```sql
INSERT INTO dbfiafastapi.compra(
	id, valortotal)
	VALUES (default, 100);

INSERT INTO dbfiafastapi.compraitens(
	id, idproduto, valor, quantidade, idcompra)
	VALUES (default, 101, 10, 1,  currval(pg_get_serial_sequence('dbfiafastapi.compra','id')));
```	

Vamos listar os tópicos?? 

```bash
docker exec -it kafka-broker /bin/bash

kafka-topics --bootstrap-server localhost:9092 --list 
```

Está chagendo mensagens?

```bash
kafka-console-consumer --bootstrap-server localhost:9092 --topic postgres.dbfiafastapi.compra --from-beginning
	
kafka-console-consumer --bootstrap-server localhost:9092 --topic postgres.dbfiafastapi.compraitens --from-beginning
	
```



4. [Tópico Produto](topico-produto//README.md)
5. [Criando nossa primeira transformação com KSql](transformacao-ksql/README.md)
6. [Criando ambiente MinIO e os Conectores Sink ](minio/README.md)