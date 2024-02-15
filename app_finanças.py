## 1. Cadastro de Usuários:
class Usuario:
    def __init__(self, nome, cpf, data_nascimento, telefone, email):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}, Data de Nascimento: {self.data_nascimento}, Telefone: {self.telefone}, Email: {self.email}"

# Exemplo de uso:
usuario1 = Usuario("João", "123.456.789-00", "1990-01-01", "(11) 98765-4321", "joao@email.com")
print(usuario1)

## 2. Entrada de Despesas e Receitas:
class Transacao:
    def __init__(self, tipo, categoria, data, valor):
        self.tipo = tipo
        self.categoria = categoria
        self.data = data
        self.valor = valor

    def __str__(self):
        return f"Tipo: {self.tipo}, Categoria: {self.categoria}, Data: {self.data}, Valor: {self.valor}"

# Exemplo de uso:
despesa1 = Transacao("Despesa", "Alimentação", "2024-02-15", 50.00)
print(despesa1)

receita1 = Transacao("Receita", "Salário", "2024-02-01", 2500.00)
print(receita1)

## 3. Cálculo de Orçamento:
class Orcamento:
    def __init__(self, despesas, receitas):
        self.despesas = despesas
        self.receitas = receitas

    def calcular_saldo(self):
        total_despesas = sum(transacao.valor for transacao in self.despesas)
        total_receitas = sum(transacao.valor for transacao in self.receitas)
        return total_receitas - total_despesas

# Exemplo de uso:
despesas = [despesa1]
receitas = [receita1]
orcamento_atual = Orcamento(despesas, receitas)
saldo_atual = orcamento_atual.calcular_saldo()
print(f"Saldo atual: R$ {saldo_atual:.2f}")

import matplotlib.pyplot as plt
import numpy as np

# Dados de exemplo
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun']
receitas = [1500, 1800, 2000, 2200, 1900, 2100]
despesas = [1000, 1200, 1300, 1400, 1100, 1200]

# Gráfico de receitas e despesas por mês
plt.figure(figsize=(10, 5))
plt.plot(meses, receitas, label='Receitas', marker='o')
plt.plot(meses, despesas, label='Despesas', marker='o')
plt.title('Receitas e Despesas por Mês')
plt.xlabel('Mês')
plt.ylabel('Valor (R$)')
plt.legend()
plt.grid(True)
plt.show()

# Dados de exemplo para receitas e despesas por semana
semanas = np.arange(1, 7)
receitas_semana = [300, 400, 500, 450, 600, 550]
despesas_semana = [200, 250, 300, 280, 350, 320]

# Gráfico de receitas e despesas por semana
plt.figure(figsize=(10, 5))
plt.plot(semanas, receitas_semana, label='Receitas', marker='o')
plt.plot(semanas, despesas_semana, label='Despesas', marker='o')
plt.title('Receitas e Despesas por Semana')
plt.xlabel('Semana')
plt.ylabel('Valor (R$)')
plt.legend()
plt.grid(True)
plt.show()
