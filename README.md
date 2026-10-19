# Controle de Níveis de Água

**Agenda 11 — Desenvolvimento de Sistemas I**  
**Aluno:** Guilherme Gomes Justi

Programa de terminal que simula o monitoramento do reservatório R-01 e
apresenta cinco situações com as cores solicitadas no enunciado.

## Comportamento esperado

| Nível | Situação | Cor | Constante do Colorama |
|---|---|---|---|
| 1 | Muito baixo (crítico) | Vermelho | `Fore.RED` |
| 2 | Baixo | Amarelo | `Fore.YELLOW` |
| 3 | Médio | Verde | `Fore.GREEN` |
| 4 | Alto | Ciano | `Fore.CYAN` |
| 5 | Muito alto (alerta) | Azul | `Fore.BLUE` |

As leituras são simuladas na sequência `[1, 2, 3, 4, 5]`. Cada linha
representa a situação atual em um instante da simulação. O programa não
pede entrada do usuário e não acessa sensores reais.

As cores seguem exatamente a tabela da atividade. Os valores de 1 a 5
são categorias; não foram atribuídos percentuais ou volumes que o enunciado
não especificou.

## Como executar

É necessário ter **Python 3.9 ou superior** e um terminal com suporte a cores.
A dependência externa está fixada em `colorama==0.4.6`.

1. Baixe e extraia o projeto ou clone o repositório.
2. Abra o terminal na pasta do projeto.
3. Crie um ambiente virtual:

   ```sh
   python -m venv .venv
   ```

4. Ative o ambiente:

   Windows (Prompt de Comando):
   ```bat
   .venv\Scripts\activate.bat
   ```

   Windows (PowerShell):
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   Linux ou macOS:
   ```sh
   source .venv/bin/activate
   ```

5. Instale a biblioteca e execute:

   ```sh
   python -m pip install -r requirements.txt
   python Guilherme_Ag11_DSI.py
   ```

No Windows, se o comando `python` não estiver disponível, use `py`.
No Linux/macOS, pode ser necessário usar `python3` para criar o ambiente.
Se o PowerShell bloquear a ativação, use o Prompt de Comando ou execute
diretamente `.venv\Scripts\python.exe`; não é necessário mudar a política
de segurança.

## Resultado da simulação

```text
CONTROLE DE NÍVEIS DE ÁGUA
Reservatório R-01 | Simulação de monitoramento
----------------------------------------------------------
Nível 1/5 | Situação: Muito baixo (crítico)
Nível 2/5 | Situação: Baixo
Nível 3/5 | Situação: Médio
Nível 4/5 | Situação: Alto
Nível 5/5 | Situação: Muito alto (alerta)
----------------------------------------------------------
Simulação concluída. Terminal com estilo padrão.
```

O bloco acima mostra o texto. No terminal, as cinco linhas de situação
aparecem, respectivamente, em vermelho, amarelo, verde, ciano e azul.
O cabeçalho, os separadores e a mensagem final usam o estilo padrão.

## Organização e decisões técnicas

- `MENSAGENS`: lista com as cinco situações, da menor para a maior leitura.
- `NIVEIS_SIMULADOS`: lista com as leituras fictícias usadas na execução.
- `validar_nivel()`: aceita apenas inteiros de 1 a 5. Rejeita valores fora
  do intervalo, textos, decimais, booleanos e outros tipos.
- `definir_cor()`: valida o nível e retorna a constante de cor correspondente.
- `formatar_mensagem()`: associa a situação ao nível e acrescenta
  `Style.RESET_ALL` ao final de cada mensagem.
- `exibir_nivel()`: imprime a leitura formatada.
- `main()`: prepara o terminal e percorre as leituras com um laço `for`.

O acesso às listas usa `nivel - 1`, pois as posições em Python começam em
zero. A validação ocorre antes do acesso, evitando que um nível inválido
seja interpretado como uma situação válida por indexação negativa.

`just_fix_windows_console()` prepara a saída colorida no Windows e pode
ser chamado em outros sistemas. O uso explícito de `Style.RESET_ALL`
restaura a cor de texto, a cor de fundo e a intensidade ao final de cada
situação. O programa mantém programação estruturada, sem classes no
código principal.

## Verificação

Execute a suíte com a biblioteca padrão do Python:

```sh
python -m unittest discover -s tests -v
```

**Validação local:** cinco testes aprovados em 19/10/2026, com Python 3.12.14 e Colorama 0.4.6. Veja o [registro de verificação](docs/VERIFICACAO.md).

Os testes verificam:

1. A correspondência exata dos cinco níveis com as mensagens e cores.
2. A restauração do estilo em cada linha impressa.
3. A rejeição de níveis abaixo de 1 e acima de 5, sem produzir uma leitura.
4. A rejeição de tipos inválidos, incluindo booleanos.
5. A execução completa, em ordem, sem solicitar entrada de dados.

## Atendimento ao enunciado

| Requisito | Implementação |
|---|---|
| Lista para níveis ou mensagens | `MENSAGENS` e `NIVEIS_SIMULADOS` |
| Importar e usar Colorama | `Fore`, `Style` e `just_fix_windows_console` |
| Função para definir a cor conforme o nível | `definir_cor(nivel)` |
| Exibir a situação atual na cor correspondente | `exibir_nivel(nivel)` |
| Restaurar o estilo padrão | `Style.RESET_ALL` ao final de cada situação |
| Usar listas, funções e bibliotecas | Estrutura do programa principal |
| Simular com valores definidos no código | Sequência de níveis de 1 a 5 |
| Nome de arquivo solicitado | `Guilherme_Ag11_DSI.py` |
| Projeto completo no GitHub | Código, dependência, documentação e testes neste repositório |

## Estrutura do projeto

```text
Guilherme_Ag11_DSI/
├── Guilherme_Ag11_DSI.py
├── requirements.txt
├── README.md
├── .gitignore
├── tests/
│   └── test_monitoramento.py
└── docs/
    └── VERIFICACAO.md
```

## Referência técnica

[Documentação oficial do Colorama no PyPI](https://pypi.org/project/colorama/).
Consultada em 19/10/2026 para inicialização do terminal, constantes de cores
e restauração do estilo.
