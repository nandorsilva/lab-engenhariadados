# Lab

## Disclaimer
> **As configurações dos Laboratórios é puramente para fins de desenvolvimento local e estudos**


## Pré-requisitos?
* Docker
* Docker-Compose


Nosso tópico produto do kafka será do tipo Compact.

Lembram pra que serve os tópicos do timpo Compact!!??

```bash

docker exec -it kafka-broker /bin/bash

kafka-topics --create --topic postgres.dbfiafastapi.produtos --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1 --config cleanup.policy=compact

kafka-topics --bootstrap-server localhost:9092 --list 

```



### Vamos criar conector para ler os dados da tabela Produto e produzir no kafka

```bash

http PUT http://localhost:8083/connectors/connector-postgres-produtos/config < conector-postgres-produto.json
	

//Ou via powershell
$response = Invoke-WebRequest -Uri "http://localhost:8083/connectors/connector-postgres-produtos/config" -Method Put -Body (Get-Content -Path "connector-postgres-produtos.json" -Raw) -ContentType "application/json"; $response.Content

```

Deu certo?? Vamos consumir as mensagem da tabela protudo

```bash
kafka-topics --bootstrap-server localhost:9092 --list 

kafka-console-consumer --bootstrap-server localhost:9092 --topic postgres.dbfiafastapi.produtos --property print.timestamp=true --property print.key=true --property print.value=true --property print.partition=true --from-beginning
	
```

Insira alguns registros

> [!IMPORTANT]
> Na tabela `compraitens` insira produtos que já possuem na tabela `produtos`


```sql
INSERT INTO produtos VALUES (default,'nome do produto',3.14);
```	



5. [Criando nossa primeira transformação com KSql](transformacao-ksql/README.md)
6. [Criando ambiente MinIO e os Conectores Sink ](minio/README.md)