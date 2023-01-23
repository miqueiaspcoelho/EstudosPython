class Livro:
	codigo = ""
	nome = ""
	editora = ""
	ano = 0
	valor_pago = 0.0

        def _init_ (self):
            def definir_codigo(self):
                    self.codigo = input("Qual o código do livro? ")
		#return self.codigo

            def definir_nome(self):
                    self.nome = input("Qual o nome do livro? ")
		#return self.nome

            def definir_editora(self):
                    self.editora = input("Qual a editora do livro? ")
		#return self.editora

            def definir_ano(self):
                    self.ano = input("Qual o ano do livro? ")
		#return self.ano

            def definir_valor_pago(self):
                    self.valor_pago = input("Qual o valor do livro? ")
		#return self.valor_pago

            def __str__(self):
                    return "{}".format(self.nome)


class Equipamento():
	codigo = ""
	nome = ""
	fabricante = ""
	valor_pago = 0.0

	def definir_codigo(self):
		self.codigo = input("Qual o código do equipamento? ")

	def definir_nome(self):
		self.nome = input("Qual o nome do equipamento? ")
		
	def definir_fabricante(self):
		self.fabricante = input("Qual o fabricante do equipamento? ")

	def definir_valor_pago(self):
		self.valor_pago = input("Qual o valor do equipamento? ")


class Funcionario():
	codigo = ""
	nome = ""
	profissao = ""
	salario = 0.0

	def definir_codigo(self):
		self.codigo = input("Qual o código do funcionário? ")

	def definir_nome(self):
		self.nome = input("Qual o nome do funcionário? ")

	def definir_profissao(self):
		self.profissao = input("Qual a profissão do funcionário? ")

	def definir_salario(self):
		self.salario = input("Qual o salario do funcionário? ")


class DisciplinaCursada():
	codigo = ""
	nome = ""
	periodo = 0
	nota_final = 0.0
	
	def definir_codigo(self):
		self.codigo = input("Qual o código da disciplina? ")

	def definir_nome(self):
		self.nome = input("Qual o nome da disciplina? ")

	def definir_periodo(self):
		self.periodo = input("Qual o periodo da disciplina? ")

	def definir_nota_final(self):
		self.nota_final = input("Qual a nota final da disciplina? ")
