# MVP: Sistema de Gerenciamento de Eventos

## i) Descrição do Projeto
Este projeto é um Produto Mínimo Viável (MVP) desenvolvido para o gerenciamento do ciclo de vida de eventos. O sistema foi construído aplicando princípios de arquitetura de software limpa, separação de responsabilidades em camadas e persistência de dados.
**Tecnologias:** Python 3 (Backend), PostgreSQL (Modelagem Física) e HTML/CSS (Wireframing).

## ii) Explicação das Classes e Arquitetura
O código segue uma arquitetura baseada em camadas para garantir modularidade:
* **`models.Evento`**: Entidade de domínio. Encapsula os atributos (id, nome, data, local, descricao) usando getters e setters para garantir que os dados sejam válidos em sua origem.
* **`repositories.EventoRepository`**: Isola a lógica de acesso a dados. É a única classe que sabe como os eventos são armazenados e buscados.
* **`services.GerenciadorEventos`**: Atua como a camada de negócio. Orquestra a criação, leitura, atualização e deleção (CRUD), conectando os inputs à camada de persistência.

## iii) Projeto Físico do Banco de Dados
A modelagem física (`projeto_banco.sql`) estruturou a tabela `eventos` com `SERIAL PRIMARY KEY` para IDs únicos e tipos adequados (`VARCHAR`, `TIMESTAMP`, `TEXT`). 
**Justificativa de Índice:** Foi adicionado um `INDEX` na coluna `data`. Como sistemas de eventos lidam com cronologia constante (listar eventos do dia, eventos futuros), este índice otimiza o *query plan* do banco, acelerando as buscas por datas.

## iv) Wireframe e Sitemap
O sitemap é direto: `Início -> Listagem de Eventos -> Formulário de Evento (Criar/Editar)`.

* **Tela Inicial / Listagem:**
  ![]
* **Tela de Cadastro / Edição:**
  ![]

## v) Instruções de Execução
No terminal, a partir da raiz do projeto, execute o módulo principal que demonstrará o funcionamento do CRUD em memória:
```bash
python main.py