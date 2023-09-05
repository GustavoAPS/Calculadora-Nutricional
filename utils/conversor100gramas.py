PADRAO_EM_GRAMAS = 100


def ConversorDeQuantidade():
    medida_gramas = float(input("Qual a quantidade do alimento(gr) ?\n"))
    quantidade_proteina = float(
        input("Qual a quantidade de proteina(gr) nessa quantidade de alimento?\n"))

    quantidade_proteina_padronizada = (
        PADRAO_EM_GRAMAS * quantidade_proteina) / medida_gramas

    print(
        f"Em 100(gr) desse aliemento existe {quantidade_proteina_padronizada} gramas de proteina")
