-- Create the schema that we'll use to populate data and watch the effect in the WAL
CREATE SCHEMA dbfiafastapi;
SET search_path TO dbfiafastapi;

-- enable PostGis
-- CREATE EXTENSION postgis;

CREATE TABLE produtos
(
    id SERIAL  NOT NULL PRIMARY KEY,
    nome varchar(250) NOT NULL,
    valor double precision NOT NULL    
);

ALTER SEQUENCE produtos_id_seq RESTART WITH 101;
ALTER TABLE produtos REPLICA IDENTITY FULL;

INSERT INTO produtos
VALUES (default,'Lapis',3.14),
       (default,'Celular',1500),
       (default,'Notebook',2000),
       (default,'Geladeira', 5000);


CREATE TABLE compra
(
    id SERIAL  NOT NULL PRIMARY KEY,
    valorTotal double precision NOT NULL   
);

CREATE TABLE  compraItens
(
     id SERIAL  NOT NULL PRIMARY KEY,
    idproduto integer NOT NULL,
    valor double precision NOT NULL,
    quantidade integer NOT NULL,
    idcompra integer NOT NULL,
   FOREIGN KEY (idcompra) REFERENCES compra(id),
   FOREIGN KEY (idproduto) REFERENCES produtos(id)
);

