"""Verifica cores, mensagens, validação e execução sem interação."""

import contextlib
import io
import unittest
from unittest.mock import patch

from colorama import Fore, Style

import Guilherme_Ag11_DSI as sistema


class TestMonitoramento(unittest.TestCase):
    def test_cada_nivel_exibe_a_situacao_e_a_cor_exigidas(self):
        casos = [
            (1, Fore.RED, "Muito baixo (crítico)"),
            (2, Fore.YELLOW, "Baixo"),
            (3, Fore.GREEN, "Médio"),
            (4, Fore.CYAN, "Alto"),
            (5, Fore.BLUE, "Muito alto (alerta)"),
        ]
        for nivel, cor, situacao in casos:
            with self.subTest(nivel=nivel):
                self.assertEqual(sistema.definir_cor(nivel), cor)
                self.assertEqual(
                    sistema.formatar_mensagem(nivel),
                    f"{cor}Nível {nivel}/5 | Situação: {situacao}{Style.RESET_ALL}",
                )

    def test_cada_linha_restaura_o_estilo_antes_da_quebra(self):
        saida = io.StringIO()
        with contextlib.redirect_stdout(saida):
            for nivel in range(1, 6):
                sistema.exibir_nivel(nivel)
        linhas = saida.getvalue().splitlines()
        self.assertEqual(len(linhas), 5)
        for linha in linhas:
            self.assertTrue(linha.endswith(Style.RESET_ALL))
            self.assertEqual(linha.count(Style.RESET_ALL), 1)

    def test_rejeita_niveis_fora_dos_limites_sem_imprimir(self):
        saida = io.StringIO()
        with contextlib.redirect_stdout(saida):
            for nivel in [-10, 0, 6, 100]:
                with self.subTest(nivel=nivel):
                    with self.assertRaises(ValueError):
                        sistema.exibir_nivel(nivel)
        self.assertEqual(saida.getvalue(), "")

    def test_rejeita_tipos_que_nao_representam_niveis_inteiros(self):
        for nivel in [True, False, 1.0, 3.5, "3", None, [], {}]:
            with self.subTest(nivel=nivel):
                with self.assertRaises(TypeError):
                    sistema.definir_cor(nivel)

    def test_simulacao_completa_na_ordem_sem_pedir_entrada(self):
        saida = io.StringIO()
        with patch("builtins.input", side_effect=AssertionError("Entrada inesperada")):
            with contextlib.redirect_stdout(saida):
                sistema.main()
        texto = saida.getvalue()
        posicoes = [texto.index(f"Nível {nivel}/5") for nivel in range(1, 6)]
        self.assertEqual(posicoes, sorted(posicoes))
        self.assertEqual(texto.count("Situação:"), 5)
        self.assertIn("Simulação concluída. Terminal com estilo padrão.", texto)


if __name__ == "__main__":
    unittest.main()
