## Disclaimer
> **Esta configuração é puramente para fins de desenvolvimento local e estudos**
> 

---

## Pré-requisitos?
* Docker
* Docker-Compose


## Subindo o Metabase
```bash
docker-compose up -d metabase
```

### Abrir o Metabase
Abra aqui o [Metabase](http://localhost:3000/)


### Logando

#### User:
```bash
userlab@fiadatalab.com.br
```
#### Password:
```bash
datalab
```
![Lab](../content/login_metabase.png)


### Tela inicial

![Lab](../content/tela_inicial.png)



### Configurando o Presto

Selecione a engranagem ao lado esquerdo da tela e depois click na opcção **Admin settings**:
![Lab](../content/config_metabase.png)


Acesse a opção **Databases** e caso não tenha Database **Presto_HIVE** clicar **Add Database**   ![Lab](../content/config_metabase_1.png)


- Configuração

**Database type**
```bash
Presto
```
**Display name**
```bash
Presto_HIVE
```

**Host**
```bash
presto
```

**Port**
```bash
8080
```

**Catalog**
```bash
hive
```

**Username**
```bash
hive
```
![Lab](../content/config_metabase_2.png)

- Após a configuração "Salvar" e sair da configuração Admin.


Criando o dash utilizando X-Ray. Databases > Presto_HIVE > raw_topics
![Lab](../content/config_metabase_3.png)



Na tabela Crrinho, clicar no raio para a criação do dsah proposto pelo próprio metabase e divirtan-se!
![Lab](../content/config_metabase_4.png)








