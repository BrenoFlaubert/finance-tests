# Sistema de Gestão de Lançamentos Financeiros

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/pytest-testing%20framework-orange)](https://docs.pytest.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Sistema para gestão de lançamentos financeiros com funcionalidades CRUD completo e testes automatizados.

## Funcionalidades Principais

- Cadastro de lançamentos financeiros
- Listagem completa de transações
- Atualização e exclusão de registros
- Testes automatizados de unidade, integração e performance
- Arquitetura escalável e modular

## Requisitos do Sistema

- Python 3.8+
- pip (gerenciador de pacotes Python)
- Virtualenv (recomendado)

## Instalação

pip install -r requirements.txt

## executar todos os testes

python -m pytest tests/ -v

## executar os testes unitarios

python -m pytest tests/unit -v

## executar os testes de integração

python -m pytest tests/integration -v

## executar os testes de sistema

python -m pytest tests/system -v

## executar os testes de performance

python -m pytest tests/performance -v

## executar os testes de refressão

python -m pytest tests/regression -v

## gerar relatorio HTML

python -m pytest --html=report.html