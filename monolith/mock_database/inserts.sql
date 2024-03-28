-- monolith_estacionamento:
delete from monolith_estacionamento; -- LIMPA A TABELA

-- Insere novos registros
insert into monolith_estacionamento (id, nome, endereco, telefone, email, cnpj, ativo) values (1, 'Hickle-Stokes', '19 Carioca Parkway', '5195174543', 'acolley0@illinois.edu', '10532197834154', true);
insert into monolith_estacionamento (id, nome, endereco, telefone, email, cnpj, ativo) values (2, 'Marvin and Sons', '016 Glacier Hill Drive', '1785662147', 'cdussy1@mozilla.com', '54923670058386', true);
insert into monolith_estacionamento (id, nome, endereco, telefone, email, cnpj, ativo) values (3, 'Runolfsdottir and Sons', '5 Duke Park', '1711917076', 'narnall2@cargocollective.com', '14054097377418', true);
insert into monolith_estacionamento (id, nome, endereco, telefone, email, cnpj, ativo) values (4, 'Macejkovic-Wolf', '336 Express Parkway', '4289692313', 'trix3@home.pl', '54670187493858', false);
insert into monolith_estacionamento (id, nome, endereco, telefone, email, cnpj, ativo) values (5, 'Robel LLC', '9 Bunker Hill Park', '5172856682', 'dhoudmont4@icio.us', '93841192915756', true);
insert into monolith_estacionamento (id, nome, endereco, telefone, email, cnpj, ativo) values (6, 'Predovic Group', '00 Petterle Hill', '2081220426', 'ctittershill5@ucoz.com', '97717470788602', true);
insert into monolith_estacionamento (id, nome, endereco, telefone, email, cnpj, ativo) values (7, 'Durgan, Simonis and Stokes', '39 Towne Point', '1743834346', 'fwhardley6@1und1.de', '44525599628428', false);
insert into monolith_estacionamento (id, nome, endereco, telefone, email, cnpj, ativo) values (8, 'Miller-Mayert', '08 Larry Lane', '4757165488', 'cbartles7@yahoo.co.jp', '81790673716953', false);
insert into monolith_estacionamento (id, nome, endereco, telefone, email, cnpj, ativo) values (9, 'Funk, Fay and Trantow', '15267 Larry Park', '3518309299', 'bhamill8@e-recht24.de', '03781990132514', true);
insert into monolith_estacionamento (id, nome, endereco, telefone, email, cnpj, ativo) values (10, 'Feil, Feil and Wintheiser', '65137 Nevada Alley', '2935791802', 'aturpey9@people.com.cn', '09705346746006', false);

-- monolith_vaga:
delete from monolith_vaga; -- LIMPA A TABELA

-- Insere novos registros
insert into monolith_vaga (id, tipo, numero, criada_em, atualizada_em, ocupada, estacionamento_id) values (1, 'M', 1, '2023-03-27 03:55:10', '2023-10-07 10:41:30', false, 1);
insert into monolith_vaga (id, tipo, numero, criada_em, atualizada_em, ocupada, estacionamento_id) values (2, 'C', 2, '2023-10-16 23:21:08', '2023-09-19 17:40:17', false, 1);
insert into monolith_vaga (id, tipo, numero, criada_em, atualizada_em, ocupada, estacionamento_id) values (3, 'M', 3, '2023-06-10 11:46:54', '2024-01-15 01:52:58', false, 1);
insert into monolith_vaga (id, tipo, numero, criada_em, atualizada_em, ocupada, estacionamento_id) values (4, 'C', 4, '2023-06-13 04:00:47', '2024-03-13 13:54:53', true, 1);
insert into monolith_vaga (id, tipo, numero, criada_em, atualizada_em, ocupada, estacionamento_id) values (5, 'M', 5, '2023-09-09 22:28:52', '2023-09-12 07:36:19', false, 1);
insert into monolith_vaga (id, tipo, numero, criada_em, atualizada_em, ocupada, estacionamento_id) values (6, 'D', 6, '2023-12-29 14:11:30', '2023-07-22 07:36:01', true, 2);
insert into monolith_vaga (id, tipo, numero, criada_em, atualizada_em, ocupada, estacionamento_id) values (7, 'D', 7, '2023-09-15 21:19:48', '2023-05-23 22:14:42', false, 2);
insert into monolith_vaga (id, tipo, numero, criada_em, atualizada_em, ocupada, estacionamento_id) values (8, 'C', 8, '2024-02-11 23:32:39', '2023-10-16 14:53:11', false, 2);
insert into monolith_vaga (id, tipo, numero, criada_em, atualizada_em, ocupada, estacionamento_id) values (9, 'D', 9, '2023-04-08 08:10:13', '2023-12-23 05:45:00', false, 2);
insert into monolith_vaga (id, tipo, numero, criada_em, atualizada_em, ocupada, estacionamento_id) values (10, 'M', 10, '2023-09-01 21:18:32', '2023-07-24 17:05:32', false, 2);

-- monolith_funcionario:
delete from monolith_funcionario; -- LIMPA A TABELA

-- Insere novos registros
insert into monolith_funcionario (id, nome, cpf, email, telefone, endereco, salario, data_nascimento, data_admissao, criado_em, atualizado_em, cargo, ativo) values (1, 'Corey Bushen', '17-5837433', 'cbushen0@gmpg.org', '9946607836', '2 Westridge Crossing', 2110.16, '2023-12-10', '2023-06-07', '2023-05-24 18:01:54', '2023-04-28 18:36:05', 'Project Manager', true);
insert into monolith_funcionario (id, nome, cpf, email, telefone, endereco, salario, data_nascimento, data_admissao, criado_em, atualizado_em, cargo, ativo) values (2, 'Ranna Stidston', '48-5007177', 'rstidston1@businesswire.com', '6573317294', '3 Lotheville Circle', 2710.83, '2023-04-21', '2023-04-23', '2023-06-25 20:45:24', '2023-10-25 11:19:20', 'Project Manager', true);
insert into monolith_funcionario (id, nome, cpf, email, telefone, endereco, salario, data_nascimento, data_admissao, criado_em, atualizado_em, cargo, ativo) values (3, 'Gardie Gwyer', '53-6039319', 'ggwyer2@amazon.co.uk', '9435634309', '1380 Maryland Parkway', 1670.64, '2024-03-07', '2023-11-26', '2024-03-05 18:35:04', '2023-02-18 20:11:22', 'Construction Foreman', true);
insert into monolith_funcionario (id, nome, cpf, email, telefone, endereco, salario, data_nascimento, data_admissao, criado_em, atualizado_em, cargo, ativo) values (4, 'Patrice Dell ''Orto', '67-9276858', 'pdell3@nifty.com', '4915436523', '684 Spohn Junction', 642.52, '2024-03-15', '2023-03-17', '2023-01-09 10:07:16', '2023-08-02 02:13:02', 'Construction Manager', true);
insert into monolith_funcionario (id, nome, cpf, email, telefone, endereco, salario, data_nascimento, data_admissao, criado_em, atualizado_em, cargo, ativo) values (5, 'Lurline Purchall', '05-0094281', 'lpurchall4@independent.co.uk', '7321434606', '6 Lerdahl Plaza', 3315.89, '2023-06-07', '2024-03-01', '2023-05-12 05:42:07', '2023-07-12 07:28:41', 'Construction Expeditor', true);
insert into monolith_funcionario (id, nome, cpf, email, telefone, endereco, salario, data_nascimento, data_admissao, criado_em, atualizado_em, cargo, ativo) values (6, 'Christophe Dent', '69-7632127', 'cdent5@netvibes.com', '7831703409', '37 Shelley Trail', 3177.54, '2023-02-13', '2023-09-11', '2023-12-26 19:36:06', '2024-01-30 01:51:34', 'Construction Worker', false);
insert into monolith_funcionario (id, nome, cpf, email, telefone, endereco, salario, data_nascimento, data_admissao, criado_em, atualizado_em, cargo, ativo) values (7, 'Jud Gooderham', '46-5143501', 'jgooderham6@nhs.uk', '6932337257', '8 Golf Course Way', 941.89, '2023-06-08', '2023-06-17', '2023-04-23 15:17:03', '2023-01-28 19:51:11', 'Construction Manager', true);
insert into monolith_funcionario (id, nome, cpf, email, telefone, endereco, salario, data_nascimento, data_admissao, criado_em, atualizado_em, cargo, ativo) values (8, 'Viv Poleykett', '14-5260150', 'vpoleykett7@nymag.com', '3966409598', '480 Schmedeman Junction', 813.94, '2024-03-09', '2023-09-07', '2023-04-10 02:32:49', '2023-05-18 10:16:47', 'Engineer', false);
insert into monolith_funcionario (id, nome, cpf, email, telefone, endereco, salario, data_nascimento, data_admissao, criado_em, atualizado_em, cargo, ativo) values (9, 'Christophorus Ackland', '02-8441626', 'cackland8@php.net', '2749100226', '13793 Center Alley', 3704.37, '2023-12-07', '2024-03-22', '2023-07-16 11:19:18', '2023-08-24 05:05:44', 'Subcontractor', true);
insert into monolith_funcionario (id, nome, cpf, email, telefone, endereco, salario, data_nascimento, data_admissao, criado_em, atualizado_em, cargo, ativo) values (10, 'Britta Futter', '76-5447749', 'bfutter9@umn.edu', '7753056533', '47 Pepper Wood Point', 1105.76, '2023-09-28', '2023-03-09', '2024-02-05 19:38:25', '2023-02-14 02:08:25', 'Engineer', true);

-- monolith_veiculo:
delete from monolith_veiculo; -- LIMPA A TABELA

-- Insere novos registros
insert into monolith_veiculo (id, marca, modelo, placa, cadastrado_em, atualizado_em, cor_primaria, cor_secundaria, ano, proprietario_id, vaga_id) values (1, 'Nissan', 'Altima', 'QIO7496', '2023-08-13 15:31:12', '2023-08-14 11:29:01', 'Goldenrod', 'Turquoise', 1999, 1, 1);
insert into monolith_veiculo (id, marca, modelo, placa, cadastrado_em, atualizado_em, cor_primaria, cor_secundaria, ano, proprietario_id, vaga_id) values (2, 'Mercury', 'Topaz', 'CQS5F78', '2023-07-09 22:26:27', '2023-04-09 23:35:48', 'Goldenrod', 'Violet', 1987, 2, 2);
insert into monolith_veiculo (id, marca, modelo, placa, cadastrado_em, atualizado_em, cor_primaria, cor_secundaria, ano, proprietario_id, vaga_id) values (3, 'Ford', 'Econoline E250', 'IRI7146', '2023-08-25 17:22:07', '2023-05-06 17:17:39', 'Goldenrod', 'Fuscia', 1997, 3, 3);
insert into monolith_veiculo (id, marca, modelo, placa, cadastrado_em, atualizado_em, cor_primaria, cor_secundaria, ano, proprietario_id, vaga_id) values (4, 'Nissan', '300ZX', 'QGF7579', '2023-08-08 22:02:01', '2023-04-09 19:50:44', 'Khaki', 'Pink', 1996, 4, 4);
insert into monolith_veiculo (id, marca, modelo, placa, cadastrado_em, atualizado_em, cor_primaria, cor_secundaria, ano, proprietario_id, vaga_id) values (5, 'Mitsubishi', 'Galant', 'NGJ4K45', '2023-11-22 09:18:22', '2023-11-02 14:14:59', 'Maroon', 'Teal', 2000, 5, 5);
insert into monolith_veiculo (id, marca, modelo, placa, cadastrado_em, atualizado_em, cor_primaria, cor_secundaria, ano, proprietario_id, vaga_id) values (6, 'GMC', 'Savana 1500', 'IMH6N45', '2024-02-14 09:47:52', '2023-11-07 10:15:23', 'Goldenrod', 'Orange', 2007, 6, 6);
insert into monolith_veiculo (id, marca, modelo, placa, cadastrado_em, atualizado_em, cor_primaria, cor_secundaria, ano, proprietario_id, vaga_id) values (7, 'Oldsmobile', 'Silhouette', 'LSR8F49', '2023-05-24 15:59:34', '2023-09-18 16:07:22', 'Khaki', 'Turquoise', 1999, 7, 7);
insert into monolith_veiculo (id, marca, modelo, placa, cadastrado_em, atualizado_em, cor_primaria, cor_secundaria, ano, proprietario_id, vaga_id) values (8, 'Honda', 'Accord', 'QXM6492', '2023-09-20 22:10:34', '2023-10-20 11:43:24', 'Pink', 'Orange', 1984, 8, 8);
insert into monolith_veiculo (id, marca, modelo, placa, cadastrado_em, atualizado_em, cor_primaria, cor_secundaria, ano, proprietario_id, vaga_id) values (9, 'Mercedes-Benz', 'E-Class', 'EUR8394', '2024-02-14 22:56:50', '2023-12-25 22:31:21', 'Red', 'Purple', 2005, 9, 9);
insert into monolith_veiculo (id, marca, modelo, placa, cadastrado_em, atualizado_em, cor_primaria, cor_secundaria, ano, proprietario_id, vaga_id) values (10, 'Audi', 'A3', 'OXF8009', '2024-03-06 01:53:43', '2024-03-26 01:50:28', 'Aquamarine', 'Red', 2008, 10, 10);

-- monolith_pagamento:
delete from monolith_pagamento; -- LIMPA A TABELA

-- Insere novos registros
insert into monolith_pagamento (id, valor, pago_em, status, metodo_pagamento, veiculo_id) values (1, 61.19, '2023-11-24 11:27:55', 'C', 'B', 1);
insert into monolith_pagamento (id, valor, pago_em, status, metodo_pagamento, veiculo_id) values (2, 61.21, '2024-02-25 20:50:34', 'E', 'C', 2);
insert into monolith_pagamento (id, valor, pago_em, status, metodo_pagamento, veiculo_id) values (3, 35.28, '2023-11-19 12:31:44', 'R', 'P', 3);
insert into monolith_pagamento (id, valor, pago_em, status, metodo_pagamento, veiculo_id) values (4, 6.62, '2023-04-07 08:36:46', 'E', 'P', 4);
insert into monolith_pagamento (id, valor, pago_em, status, metodo_pagamento, veiculo_id) values (5, 53.95, '2023-10-12 07:01:26', 'C', 'P', 5);
insert into monolith_pagamento (id, valor, pago_em, status, metodo_pagamento, veiculo_id) values (6, 89.16, '2024-01-30 12:51:12', 'R', 'C', 6);
insert into monolith_pagamento (id, valor, pago_em, status, metodo_pagamento, veiculo_id) values (7, 40.68, '2023-11-05 01:38:01', 'P', 'D', 7);
insert into monolith_pagamento (id, valor, pago_em, status, metodo_pagamento, veiculo_id) values (8, 54.29, '2024-03-26 11:21:23', 'P', 'C', 8);
insert into monolith_pagamento (id, valor, pago_em, status, metodo_pagamento, veiculo_id) values (9, 78.36, '2023-10-24 14:31:55', 'R', 'D', 9);
insert into monolith_pagamento (id, valor, pago_em, status, metodo_pagamento, veiculo_id) values (10, 82.0, '2024-03-05 16:05:36', 'E', 'C', 10);