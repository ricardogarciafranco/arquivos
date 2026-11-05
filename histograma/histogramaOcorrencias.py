import argparse
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt


BYTE_VALUES = range(256)


def contar_bytes(caminho):
    contagens = Counter()
    with caminho.open("rb") as arquivo:
        while bloco := arquivo.read(64 * 1024):
            contagens.update(bloco)
    return contagens


def main():
    parser = argparse.ArgumentParser(
        description="Gera histogramas das ocorrências de cada byte nos arquivos."
    )
    parser.add_argument(
        "arquivos",
        nargs="+",
        type=Path,
        help="arquivos a analisar, por exemplo imagem1.png imagem2.bmp",
    )
    parser.add_argument(
        "-o",
        "--saida",
        type=Path,
        default=Path("histograma_ocorrencias.png"),
        help="caminho da imagem do histograma (padrão: histograma_ocorrencias.png)",
    )
    argumentos = parser.parse_args()

    fig, eixos = plt.subplots(
        len(argumentos.arquivos),
        1,
        figsize=(12, max(3.5, 3.2 * len(argumentos.arquivos))),
        sharex=True,
        squeeze=False,
    )

    for caminho, (eixo,) in zip(argumentos.arquivos, eixos):
        contagens = contar_bytes(caminho)
        eixo.bar(BYTE_VALUES, [contagens[valor] for valor in BYTE_VALUES], width=1.0)
        eixo.set_title(caminho.name)
        eixo.set_ylabel("Ocorrências")
        eixo.grid(axis="y", alpha=0.25)

    eixos[-1][0].set_xlabel("Valor do byte (hexadecimal)")
    eixos[-1][0].set_xticks(range(0, 256, 16))
    eixos[-1][0].set_xticklabels([f"0x{valor:02X}" for valor in range(0, 256, 16)])
    fig.suptitle("Frequência dos bytes por arquivo")
    fig.tight_layout()
    fig.savefig(argumentos.saida, dpi=150)
    plt.close(fig)
    print(f"Histograma salvo em: {argumentos.saida}")


if __name__ == "__main__":
    main()
