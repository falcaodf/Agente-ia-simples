# Agente IA Simples para Gerar Testes Automáticos

Este projeto é um agente simples que ajuda a criar **testes automáticos para código Python**.  
Você dá um arquivo com funções, e ele gera um arquivo de testes (`test_<nome>.py`) usando **pytest**, de forma rápida e prática.

---

## Como funciona

1. Você fornece um arquivo Python com suas funções.  
2. O agente lê o código e gera os testes automaticamente.  
3. O arquivo de testes inclui `import pytest` e funções `test_*` cobrindo casos de sucesso e erro.  
4. Ele usa **Ollama** para gerar os testes com base no seu código.

---

## Antes de começar

1. **Instalar Ollama**:  
   Baixe e instale o Ollama no seu computador: [https://ollama.com](https://ollama.com)  

2. **Baixar o modelo correto**:  
   O agente funciona com o modelo `llama3:8b`. Certifique-se de que ele está disponível no Ollama local.

3. **Instalar dependências Python**:

```bash
pip install ollama pytest
