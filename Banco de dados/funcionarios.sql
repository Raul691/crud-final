CREATE TABLE PRODUTOS(
id_produto INT PRIMARY KEY,
Nome VARCHAR(100),
Marca VARCHAR(100),
Modelo VARCHAR(100),
Medida VARCHAR(100),
Tipo VARCHAR(100),
Qnt_atual INT,
Qnt_min INT,
Qnt_Repor INT,
Valor_Custo float,
Valor_venda float
);

select*from PRODUTOS;

INSERT INTO PRODUTOS( id_produto,Nome,Marca,Modelo,Medida,Tipo,Qnt_atual,Qnt_min,Qnt_Repor,Valor_Custo,Valor_Venda)
VALUES
(1,'Diablo Rosso IV 120/70 ZR17','Pirelli','Diablo Rosso IV','120/70 ZR17','pista',18,5,0, 358.92,419.99);

INSERT INTO PRODUTOS( id_produto,Nome,Marca,Modelo,Medida,Tipo,Qnt_atual,Qnt_min,Qnt_Repor,Valor_Custo,Valor_Venda)
VALUES
(2,'Power GP 190/50 ZR17','Michelin','Power GP','190/50 ZR17','pista',29,8,0,355.00,399.99);

INSERT INTO PRODUTOS( id_produto,Nome,Marca,Modelo,Medida,Tipo,Qnt_atual,Qnt_min,Qnt_Repor,Valor_Custo,Valor_Venda)
VALUES
(3,'Power GP 120/70 ZR17','Michelin','Power GP','120/70 ZR17','rua',50,20,0,365.98,415.50);

INSERT INTO PRODUTOS( id_produto,Nome,Marca,Modelo,Medida,Tipo,Qnt_atual,Qnt_min,Qnt_Repor,Valor_Custo,Valor_Venda)
VALUES
(4,'Qualifier II 120/70 ZR17','Dunlop','Qualifier II','120/70 ZR17','slick',40,20,0,350.75,425.78);

INSERT INTO PRODUTOS( id_produto,Nome,Marca,Modelo,Medida,Tipo,Qnt_atual,Qnt_min,Qnt_Repor,Valor_Custo,Valor_Venda)
VALUES
(5,'Qualifier II 180/55 ZR17','Dunlop','Qualifier II','180/55 ZR17','slick',7,16,9,370.19,450.00);

INSERT INTO PRODUTOS( id_produto,Nome,Marca,Modelo,Medida,Tipo,Qnt_atual,Qnt_min,Qnt_Repor,Valor_Custo,Valor_Venda)
VALUES
(6,'Road 5 120/70 ZR17','Michelin','Road 5','120/70 ZR17','pista',40,11,0,412.20,489.99);

INSERT INTO PRODUTOS( id_produto,Nome,Marca,Modelo,Medida,Tipo,Qnt_atual,Qnt_min,Qnt_Repor,Valor_Custo,Valor_Venda)
VALUES
(7,'Diablo Rosso IV 190/55 ZR17','Pirelli','Diablo Rosso IV','190/55 ZR17','slick',32,16,0,410.00,480.80);

INSERT INTO PRODUTOS( id_produto,Nome,Marca,Modelo,Medida,Tipo,Qnt_atual,Qnt_min,Qnt_Repor,Valor_Custo,Valor_Venda)
VALUES
(8,'Road 5 160/60 ZR17','Michelin','Road 5','160/60 ZR17','rua',22,17,0,356.72,415.19);

INSERT INTO PRODUTOS( id_produto,Nome,Marca,Modelo,Medida,Tipo,Qnt_atual,Qnt_min,Qnt_Repor,Valor_Custo,Valor_Venda)
VALUES
(9,'GP Racer D212 190/55 ZR17','Dunlop','GP Racer D212','190/55 ZR17','pista',16,10,0,378.99,445.65);

INSERT INTO PRODUTOS( id_produto,Nome,Marca,Modelo,Medida,Tipo,Qnt_atual,Qnt_min,Qnt_Repor,Valor_Custo,Valor_Venda)
VALUES
(10,'SportSmart TT 190/50 ZR17','Dunlop','SportSmart TT','190/50 ZR17','slick',49,7,0, 423.15,479.99);

INSERT INTO PRODUTOS( id_produto,Nome,Marca,Modelo,Medida,Tipo,Qnt_atual,Qnt_min,Qnt_Repor,Valor_Custo,Valor_Venda)
VALUES
(11,'Diablo Supercorsa 120/70 ZR17','Pirelli','Diablo Supercorsa','120/70 ZR17','pista',27,20,0,426.50,498.75);

INSERT INTO PRODUTOS( id_produto,Nome,Marca,Modelo,Medida,Tipo,Qnt_atual,Qnt_min,Qnt_Repor,Valor_Custo,Valor_Venda)
VALUES
(12,'Diablo Supercorsa 180/55 ZR17','Pirelli','Diablo Supercorsa','180/55 ZR17','pista',0,9,9,325.82,399.99);

INSERT INTO PRODUTOS( id_produto,Nome,Marca,Modelo,Medida,Tipo,Qnt_atual,Qnt_min,Qnt_Repor,Valor_Custo,Valor_Venda)
VALUES
(13,'GP Racer D212 190/55 ZR17','Dunlop','GP Racer D212','190/55 ZR17','pista',34,20,0,425.00,490.00);

INSERT INTO PRODUTOS( id_produto,Nome,Marca,Modelo,Medida,Tipo,Qnt_atual,Qnt_min,Qnt_Repor,Valor_Custo,Valor_Venda)
VALUES
(14,'SportSmart TT 180/55 ZR17','Dunlop','SportSmart TT','180/55 ZR17','rua',28,9,0,329.99, 385.29);

INSERT INTO PRODUTOS( id_produto,Nome,Marca,Modelo,Medida,Tipo,Qnt_atual,Qnt_min,Qnt_Repor,Valor_Custo,Valor_Venda)
VALUES
(15,'Diablo Rosso IV 190/55 ZR17','Pirelli','Diablo Rosso IV','190/55 ZR17','pista',37,7,0,440.00,499.99);

INSERT INTO PRODUTOS( id_produto,Nome,Marca,Modelo,Medida,Tipo,Qnt_atual,Qnt_min,Qnt_Repor,Valor_Custo,Valor_Venda)
VALUES
(16,'GP Racer D212 190/55 ZR17','Dunlop','GP Racer D212','190/55 ZR17','pista', 15,5,0,452.20,489.99);
   
INSERT INTO PRODUTOS( id_produto,Nome,Marca,Modelo,Medida,Tipo,Qnt_atual,Qnt_min,Qnt_Repor,Valor_Custo,Valor_Venda)
VALUES
(17,'Power GP 180/55 ZR17','Michelin','Power GP','180/55 ZR17','pista',19,12,0,278.16,315.45);

INSERT INTO PRODUTOS( id_produto,Nome,Marca,Modelo,Medida,Tipo,Qnt_atual,Qnt_min,Qnt_Repor,Valor_Custo,Valor_Venda)
VALUES
(18,'Road 5 190/50 ZR17','Michelin','Road 5','190/50 ZR17','pista',25,17,0,350.25,405.00);


INSERT INTO PRODUTOS( id_produto,Nome,Marca,Modelo,Medida,Tipo,Qnt_atual,Qnt_min,Qnt_Repor,Valor_Custo,Valor_Venda)
VALUES
(19,'Angel GT 120/70 ZR17','Pirelli','Angel GT','120/70 ZR17','pista',36,7,0,358.22,409.99);

INSERT INTO PRODUTOS( id_produto,Nome,Marca,Modelo,Medida,Tipo,Qnt_atual,Qnt_min,Qnt_Repor,Valor_Custo,Valor_Venda)
VALUES
(20,'GP Racer D212 190/55 ZR17','Dunlop','GP Racer D212','190/55 ZR17','pista',23,14,0,415.16,489.98);