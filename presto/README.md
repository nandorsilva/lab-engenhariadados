## Disclaimer
> **Esta configuração é puramente para fins de desenvolvimento local e estudos**
> 

---

## Pré-requisitos?
* Docker
* Docker-Compose


# Subindo o Hadoop


```bash
docker-compose up -d namenode datanode metastore
``` 

## Verificando o namenode entrou em modo de segurança

```bash
docker exec -it namenode /bin/bash

hdfs dfsadmin -safemode get
``` 

Se o resultado for `Safe mode is ON`, vamos mudar.

```bash
hdfs dfsadmin -safemode leave

hdfs fsck -delete

exit
``` 




# Subindo o Hive

```bash
docker-compose up -d hive
```

# Subindo o Presto

```bash
docker-compose up -d presto
```


#### Ir para o Proximo lab:

9. [Criando ambiente Analytics - Criando External tables no Hive](../hive/README.md)
10. [Criando ambiente Analytics - Ingestão de Dados Externos com NIFI](../nifi/README.md)
11. [Analisando Dados com o metabase](../metabase/README.md)