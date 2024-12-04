# Lab

## Disclaimer
> **As configurações dos Laboratórios é puramente para fins de desenvolvimento local e estudos**


## 💻 Pré-requisitos
* Docker
* Docker-Compose

### Subindo o ambiente do Kafka

```bash
docker-compose up -d zookeeper kafka-broker

```

### Vamos configurar nosso cluster de Kafka Connect ??

> [!IMPORTANT]
> Trocar a informação  `<<usuario>>` para o seu do DockerHub, e o nome `kafka-connet-lab:v1`, pode ser alterado caso prefira.


```bash
docker image build -t <<usuario>>/kafka-connet-lab:v1  -f kafka/Dockerfile .
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


3. [Criando os primeiros conectores - Source](../conectores/README.md)
4. [Tópico Produto](../topico-produto//README.md)
5. [Criando nossa primeira transformação com KSql](../transformacao-ksql/README.md)
6. [Criando ambiente MinIO e os Conectores Sink ](../minio/README.md)
7. [Criando APi, gerando evento para o carrinho ](../api/README.md)
8. [Criando ambiente Analytics - Presto ](../presto/README.md)
9. [Criando ambiente Analytics - Criando External tables no Hive](../hive/README.md)
11. [Criando ambiente Analytics - Ingestão de Dados Externos com NIFI](../nifi/README.md)
12. [Analisando Dados com o metabase](../metabase/README.md)