# Diariamente

## Instruções de Execução

1. Clone o repositório.
2. Instale as dependências com `pip install -r requirements.txt`. No caso, todas as dependências do projeto são relacionadas ao FastAPI, que foi utilizado para criar as rotas e renderizar as páginas web da aplicação.
3. Execute o programa principal com `python main.py`.

## Estrutura do Projeto

- `data/`: Dados em JSON para salvar as entradas do diário e usuários cadastrados de forma permanente. Durante a execução da aplicação, os usuários são inseridos em uma árvore AVL e posteriormente, salvos em JSON.
- `docs/`: Diretório que contém este arquivo README.txt e o HTML com a documentação do Pydoc.
- `models/`: Diretório com a classe Usuario, criada para representar os usuários do sistema.
- `server/`: Diretório com os arquivos das rotas e do app FastAPI.
- `static/`: Diretório com arquivos estáticos, incluindo imagens, css, js e o áudio usado na rota de meditação.
- `templates/`: Diretório com os templates HTML das rotas.
- `utils/`: Diretório com as classes que criam os Nós e Árvores AVL. 

## Justificativas Técnicas

- **Linguagem de Programação:** Escolhi Python e FastAPI por ter mais familiaridade e por querer me desafiar com a criação de um sistema web com autenticação.
- **Estrutura de Dados:** Utilizei árvores AVL para otimizar as operações de busca e inserção. Todos os usuários são inseridos em Árvores AVL e a busca também é feita por árvores AVL. Apenas utilizo json para realizar a permanência dos dados. Também utilizo o algoritmo quicksort para ordenar as entradas dos diários. 
- **Segurança e performance:** Implementei autenticação de usuários, hash de senhas dos usuárois, proteção contra acesso não autorizado (um usuário não pode acessar os registros de outros usuários) e garanti a performance ideal para o registro e busca de usuários com as cargas de testes envolvendo 1000, 10000 e 100000 usuários. Todas as inserções ocorreram em menos de um segundo, usando algortimos eficientes e otimizados. 
- **Documentação:** Criei este arquivo README.txt e documentei todas as classes, funções, métodos e arquivos `.py` usando docstrings e além disso, também gerei um HTML com o documento Pydoc, no caminho `docs/fiap2sioa-gs-diariamente.html`.