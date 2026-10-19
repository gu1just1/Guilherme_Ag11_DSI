# Verificação da atividade

Execução local em 19/10/2026, com Python 3.12.14, Windows e Colorama 0.4.6.

## Resultado dos testes

Comando: `python -m unittest discover -s tests -v`

```text
test_cada_linha_restaura_o_estilo_antes_da_quebra ... ok
test_cada_nivel_exibe_a_situacao_e_a_cor_exigidas ... ok
test_rejeita_niveis_fora_dos_limites_sem_imprimir ... ok
test_rejeita_tipos_que_nao_representam_niveis_inteiros ... ok
test_simulacao_completa_na_ordem_sem_pedir_entrada ... ok

Ran 5 tests
OK
```

A execução do arquivo principal também terminou com código de saída zero.
A saída capturada apresentou as cinco situações, em ordem, usando os códigos
ANSI de vermelho (31), amarelo (33), verde (32), ciano (36) e azul (34).
Cada mensagem terminou com o comando de restauração `ESC[0m`.

A inspeção da saída capturada e os testes confirmam as sequências de cor.
A aparência visual depende da paleta e do suporte ANSI do terminal utilizado.

## Escopo

A simulação não lê sensores, não calcula volumes e não aciona bombas.
Os níveis são categorias fixas conforme o enunciado.
O repositório contém o projeto para revisão; a atividade não foi enviada
ao fichário da Etec durante a preparação.
