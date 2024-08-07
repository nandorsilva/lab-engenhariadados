## Disclaimer
> **As configurações dos Laboratórios é puramente para fins de desenvolvimento local e estudos**


## Pré-requisitos?
* Docker
* Docker-Compose

### Subindo o ambiente do Kafka

```bash
docker-compose up -d zookeeper kafka-broker

```

### Vamos configurar nosso cluster de Kafka Connect ??

```bash
docker image build -t <<usuario>>/kafka-connet-lab:v1  -f Dockerfile .
```


## No arquivo `docker-compose.yaml`, altere o serviço connect para a imagem que acabou de criar.


```bash
docker-compose up -d akhq connect
```


Listando os plugins existentes, os padrões da imagem e do debezium que foram inseridos na imagem, via arquivo `Dockerfile`

```bash
docker exec -it kafkaConect curl  http://localhost:8083/connector-plugins
```

### Até aqui está tudo certinho??
