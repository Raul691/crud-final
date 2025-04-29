CREATE TABLE funcionarios(
Registro INT PRIMARY KEY,
Nome VARCHAR(100),''
Cargo VARCHAR(100),
Data_admissao date
);
select*from funcionarios;

INSERT INTO funcionarios (Registro,Nome, Cargo,Data_admissao)
VALUES
(0123, 'SAMUEL FERREIRA RIBEIBO', 'GERENTE', 20200215);

INSERT INTO funcionarios (Registro,Nome, Cargo,Data_admissao)
VALUES
(1234, 'RAUL RODRIGUES JUSTO', 'VENDEDOR', 20200416);

INSERT INTO funcionarios (Registro,Nome, Cargo,Data_admissao)
VALUES
(2345, 'MURILLO VIANA COELHO', 'VENDEDOR', 20220714);

INSERT INTO funcionarios (Registro,Nome, Cargo,Data_admissao)
VALUES
(3456, 'VITOR VIANA DE JESUS', 'VENDEDOR', 20211202);

INSERT INTO funcionarios (Registro,Nome, Cargo,Data_admissao)
VALUES
(4567, 'JULIA DOS SANTOS MATIAS', 'VENDEDOR', 20210510);