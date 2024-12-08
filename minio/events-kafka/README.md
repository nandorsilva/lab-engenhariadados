# Lab

## Disclaimer
> **As configurações dos Laboratórios é puramente para fins de desenvolvimento local e estudos**


## 💻 Pré-requisitos
* Docker
* Docker-Compose



### Configurando o Minio para gerar evntos

![MinIO](../../content/minio-events-01.png)

### Selecione a Queue Kafka

![MinIO](../../content/minio-events-02.png)

### Informa as seguintes configurações

* Identifier : EventKafkaCarrinho
* Brokers: kafka-broker:29092
* Topic: sink-carrinho


![MinIO](../../content/minio-events-03.png)

### Renicia o serviço e veja depois se ficou online

![MinIO](../../content/minio-events-04.png)
![MinIO](../../content/minio-events-05.png)


### Criando o Subscribe para o bucket raw/topics/carrinho
![MinIO](../../content/minio-events-06.png)


### Configurando o evento para ser acionado para a pasta topics/carrinho/

* ARN : arn:minio:sqs::EventKafkaCarrinho:kafka
* Prefix: topics/carrinho/
* Suffix: .json

![MinIO](../../content/minio-events-07.png)


### Publique mensagens para o topico carrinho pelo fastapi

* http://localhost:8000/docs
