🐶 Dog API Automation 

Focado em Integração e BDD.
Título: 🐶 Dog API Automation - BDD Framework

Descrição: Validação dos endpoints de listagem de raças e imagens da Dog API.
Tecnologias: Python 3, Behave (Gherkin), Requests.
Destaque: "Projeto estruturado com Gherkin para facilitar a leitura por analistas de negócio e desenvolvedores de outras linguagens."
Como rodar: pip install behave requests e depois behave.


**Objetivo:** Validar a integridade dos endpoints da Dog CEO API através de testes de integração e contrato utilizando BDD.

**URL:** [https://dog.ceo/dog-api/documentation](https://dog.ceo/dog-api/documentation)
**Critério:** Status 200 OK / Validação de Schema / Integridade de Imagens.

 📊 Análise Técnica:

* **Arquitetura:** Desenvolvido em **Python + Behave (Gherkin)** para garantir que a automação sirva como documentação viva.
* **Cobertura:** Validação dos endpoints de listagem global de raças, busca por raça específica (Husky) e geração de imagens aleatórias.
* **Diferencial:** Estrutura modular que permite a tradução rápida da lógica para desenvolvedores Java, reduzindo o custo de manutenção e facilitando o entendimento de requisitos por toda a equipe.

🛠️ Como Executar:

1.  **Instalar dependências:**
    ```bash
    pip install behave requests
    ```

2.  **Executar os testes (BDD):**
    ```bash
    behave
    ```

3.  **Visualizar Resultados:**
    Os resultados detalhados de cada cenário (Pass/Fail)"Relatório gerado em HTML via pytest-html".após a execução do comando acima.
    
📊 Evidências de Execução

O projeto está configurado para gerar um resumo visual diretamente no GitHub Actions. 
Para visualizar os resultados:
1. Vá na aba **Actions** deste repositório.
2. Clique na execução mais recente (Workflow Run).
3. Role até o final da página para ver a tabela de **Job Summary**.

*Este projeto foi desenvolvido seguindo as melhores práticas de Clean Code e Testes de API.*


**Desenvolvido  por Luciana Orli (Lux by Or) 💎🛡️**

