class ValidadorCPF:
    # Construtor da classe
    def __init__(self, cpf):
        self.cpf = cpf.replace(".", "").replace("-", "").strip()

    # Verificar se o CPF possui 11 dígitos
    def verificar_tamanho(self):
        return len(self.cpf) == 11 and self.cpf.isdigit()

    # Verificar se todos os números são iguais
    def verificar_repetidos(self):
        return self.cpf != self.cpf[0] * 11

    # Calcular um dígito verificador
    def calcular_digito(self, quantidade):
        soma = 0
        peso = quantidade + 1
        for i in range(quantidade):
            soma += int(self.cpf[i]) * peso
            peso -= 1

        resto = (soma * 10) % 11
        if resto == 10:
            return 0
        return resto

    # Validar o CPF completo
    def validar(self):
        if not self.verificar_tamanho():
            return False

        if not self.verificar_repetidos():
            return False

        primeiro = self.calcular_digito(9)
        segundo = self.calcular_digito(10)

        if primeiro == int(self.cpf[9]) and segundo == int(self.cpf[10]):
            return True

        return False


# Programa principal
while True:
    cpf_digitado = input("\nDigite o CPF: ")

    # Criando o objeto
    validador = ValidadorCPF(cpf_digitado)

    # Chamando o método de validação
    if validador.validar():
        print("CPF VÁLIDO!")
    else:
        print("CPF INVÁLIDO!")

    # Perguntar se deseja validar outro CPF
    while True:
        continuar = input("\nDeseja validar outro CPF? (S/N): ").strip().upper()
        if continuar in ("S", "N"):
            break
        print("Opção inválida! Digite S ou N.")

    if continuar == "N":
        print("\nPrograma encerrado!")
        break
