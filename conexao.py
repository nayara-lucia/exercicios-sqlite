import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

'''
1. Crie uma tabela chamada "alunos" com os seguintes campos: id
(inteiro), nome (texto), idade (inteiro) e curso (texto).
'''
cursor.execute('CREATE TABLE alunos(id INT,nome VARCHAR(100),idade INT,curso VARCHAR(50));')

'''
2. Insira pelo menos 5 registros de alunos na tabela que você criou no
exercício anterior.
'''
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(1,"Alice",19,"Ciência de Dados")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(2,"Roberta",22,"Ciência da Computação")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(3,"Amanda",21,"Analise e Desenvolvimento de Sistemas")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(4,"Pedro",25,"Segurança da Inormação")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(5,"Eurico",25,"Segurança da Inormação")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(6,"Aluminio",25,"Engenharia")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(7,"Broca",25,"Engenharia")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(8,"Cardinal",22,"Engenharia")')

'''
3. Consultas Básicas
Escreva consultas SQL para realizar as seguintes tarefas:
    a) Selecionar todos os registros da tabela "alunos".
    b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
    c) Selecionar os alunos do curso de "Engenharia" em ordem
    alfabética.
    d) Contar o número total de alunos na tabela
'''
a = cursor.execute('SELECT * FROM alunos')
for dado in a:
    #print(dado)

b = cursor.execute('SELECT nome,idade FROM alunos WHERE idade > 20')
for dado in b:
    #print(dado)

c = cursor.execute('SELECT * FROM alunos WHERE curso="Engenharia" ORDER BY nome asc')
for dado in c:
    #print(dado)

d = cursor.execute('SELECT COUNT(*) FROM alunos')
for dado in d:
    #print(dado)

'''
4. Atualização e Remoção
a) Atualize a idade de um aluno específico na tabela.
b) Remova um aluno pelo seu ID.
'''
cursor.execute('UPDATE alunos SET idade=18 where id=5')

cursor.execute('DELETE FROM alunos WHERE id=4')

'''
5. Criar uma Tabela e Inserir Dados
Crie uma tabela chamada "clientes" com os campos: id (chave
primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns
registros de clientes na tabela.
'''
cursor.execute('CREATE TABLE clientes(id INT PRIMARY KEY,nome VARCHAR(100),idade INT,saldo FLOAT);')

cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(15,"Travis",33,15650.99)')
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(18,"Lorran",39,59650.50)')
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(19,"Ana Paula",39,88650.50)')
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(20,"Cristo",39,99650.50)')
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(21,"Cristo",18,1650.50)')
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(22,"Isabela",18,4650.50)')

'''
6. Consultas e Funções Agregadas
Escreva consultas SQL para realizar as seguintes tarefas:
a) Selecione o nome e a idade dos clientes com idade superior a
30 anos.
b) Calcule o saldo médio dos clientes.
c) Encontre o cliente com o saldo máximo.
d) Conte quantos clientes têm saldo acima de 59000
'''
a = cursor.execute('SELECT nome,idade FROM clientes WHERE idade>30')
for dado in a:
    #print(dado)

b = cursor.execute('SELECT AVG(saldo) FROM clientes')
for dado in b:
    #print(dado)

c = cursor.execute('SELECT nome,MAX(saldo) FROM clientes')
for dado in c:
    #print(dado)

d = cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo > 59000')
for dado in d:
    #print(dado)

'''
7. Atualização e Remoção com Condições
a) Atualize o saldo de um cliente específico.
b) Remova um cliente pelo seu ID.
'''
cursor.execute('UPDATE clientes set saldo=999.15 where id=22')

cursor.execute('DELETE FROM clientes where id=21')

'''
8. Junção de Tabelas
Crie uma segunda tabela chamada "compras" com os campos: id
(chave primária), cliente_id (chave estrangeira referenciando o id
da tabela "clientes"), produto (texto) e valor (real). 

Insira algumas compras associadas a clientes existentes na tabela "clientes".

Escreva uma consulta para exibir o nome do cliente, o produto e o
valor de cada compra.
'''

cursor.execute('CREATE TABLE compras(id INT PRIMARY KEY, cliente_id INT, produto VARCHAR(100), valor FLOAT, FOREIGN KEY(cliente_id)  REFERENCES clientes(id));')

cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES(1,15,"Calça beje",130.50)')
cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES(4,15,"Moletom beje",639.99)')
cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES(2,22,"Vestido florido",290.50)')
cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES(3,19,"Blusa básica",39.90)')

select = cursor.execute('SELECT clientes.nome, compras.produto, compras.valor FROM clientes INNER JOIN compras ON clientes.id == compras.cliente_id')
for dado in select:
    print(dado)






conexao.commit()

conexao.close

