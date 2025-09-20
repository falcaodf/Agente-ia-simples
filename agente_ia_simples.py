import os
import ollama

# === CONFIGURAÇÃO DO MODELO ===
MODELO_OLLAMA = "llama3:8b"  # ou outro modelo que você estiver usando

# === FUNÇÃO PRINCIPAL ===
def gerar_testes(nome_arquivo_codigo):
    """
    Recebe o caminho de um arquivo Python e retorna o código de testes gerado em string.
    """
    if not os.path.exists(nome_arquivo_codigo):
        return "Arquivo não encontrado."

    with open(nome_arquivo_codigo, "r", encoding="utf-8") as f:
        codigo = f.read()

    prompt = f"""
Você é um gerador de testes unitários para Python.
Crie testes usando pytest para o seguinte código:

{codigo}

- Inclua 'import pytest' na primeira linha
- Crie funções def test_* para casos de sucesso e falha
- Não invente funções que não existem no código
- Retorne apenas o código Python do arquivo de testes
"""

    resposta = ollama.chat(
        model=MODELO_OLLAMA,
        messages=[{"role": "user", "content": prompt}]
    )

    codigo_testes = resposta["message"]["content"]
    return codigo_testes

# === FUNÇÃO AUXILIAR PARA SALVAR ===
def salvar_testes(codigo_testes, nome_arquivo_saida):
    with open(nome_arquivo_saida, "w", encoding="utf-8") as f:
        f.write(codigo_testes)
    print(f"Arquivo de testes salvo em: {nome_arquivo_saida}")

# === EXEMPLO DE USO ===
if __name__ == "__main__":
    arquivo_codigo = "exemplo.py"             # arquivo que você quer gerar testes
    arquivo_testes = f"test_{arquivo_codigo}" # nome do arquivo de saída
