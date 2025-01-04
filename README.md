

# Desafio Back-end: Construção de uma API RESTful para Gerenciamento de Tarefas

## 📋 Objetivo

Desenvolver uma API RESTful para criar, listar, atualizar e excluir tarefas. A aplicação também deve permitir a filtragem de tarefas com base no status. O projeto segue boas práticas de desenvolvimento, modularização, validação de dados e interação com um banco de dados.

---

## 🚀 Funcionalidades da API

### 1. **Criar Tarefa (POST /tarefas)**
Cria uma nova tarefa com as propriedades:
- **Título**: (String, obrigatório)
- **Descrição**: (String, opcional)
- **Status**: (String, obrigatório — valores possíveis: "pendente", "realizando", "concluída")
- **Data de vencimento**: (Date, opcional, formato `YYYY-MM-DD`)

**Exemplo de Requisição:**
```json
{
  "titulo": "Estudar API",
  "descricao": "Estudar como criar uma API RESTful",
  "status": "pendente",
  "data_vencimento": "2024-12-31"
}
```

**Resposta:**
- `201 Created` em caso de sucesso.

---

### 2. **Listar Tarefas (GET /tarefas)**
Retorna todas as tarefas cadastradas no sistema.

**Exemplo de Resposta:**
```json
[
  {
    "id": 1,
    "titulo": "Estudar API",
    "descricao": "Estudar como criar uma API RESTful",
    "status": "pendente",
    "data_vencimento": "2024-12-31"
  }
]
```

---

### 3. **Buscar Tarefa por ID (GET /tarefas/{id})**
Retorna os detalhes de uma tarefa específica pelo ID.

**Exemplo de Resposta:**
```json
{
  "id": 1,
  "titulo": "Estudar API",
  "descricao": "Estudar como criar uma API RESTful",
  "status": "pendente",
  "data_vencimento": "2024-12-31"
}
```

---

### 4. **Atualizar Tarefa (PUT /tarefas/{id})**
Permite atualizar os dados de uma tarefa existente.

**Exemplo de Requisição:**
```json
{
  "titulo": "Estudar API - Revisão",
  "descricao": "Revisar os conceitos de API RESTful",
  "status": "realizando",
  "data_vencimento": "2024-12-28"
}
```

---

### 5. **Excluir Tarefa (DELETE /tarefas/{id})**
Remove uma tarefa pelo ID.

**Resposta:**
- `204 No Content` em caso de sucesso.

---

### 6. **Filtrar por Status (GET /tarefas?status={status})**
Filtra tarefas pelo status:
- Status permitidos: `pendente`, `realizando`, `concluída`.

**Exemplo de Requisição:**
```
GET /tarefas?status=pendente
```

---

## 🛠️ Tecnologias Utilizadas
- **Linguagem**: Python
- **Framework**: Flask
- **Banco de Dados**: SQLite
- **Bibliotecas**: Flask-RESTful, SQLAlchemy
- **Testes**: Postman/Insomnia
- **Versionamento**: GitHub

---

## 📝 Requisitos de Implementação
1. **Validação de Dados**:
   - Campos obrigatórios: `titulo`, `status`.
   - Validação de data (`YYYY-MM-DD`).

2. **Respostas HTTP**:
   - `200 OK`: Operação bem-sucedida.
   - `201 Created`: Recurso criado.
   - `400 Bad Request`: Erro de validação.
   - `404 Not Found`: Recurso não encontrado.
   - `500 Internal Server Error`: Erros no servidor.

3. **Organização do Código**:
   - Módulos separados para gerenciamento de tarefas e conexão com banco de dados.

---

## 📦 Como Executar o Projeto
1. Clone o repositório:
   ```bash
   git clone https://github.com/ASMdeS/API-RESTful-para-Gerenciamento-de-Tarefas.git
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o servidor:
   ```bash
   python server.py
   ```
4. Acesse a API:
   - URL base: `http://localhost:5000`

---

## 📊 Exemplo de Fluxo
1. **Criar Tarefa**:
   - Enviar um `POST /tarefas` com os dados da tarefa.
2. **Listar Tarefas**:
   - Enviar um `GET /tarefas` para visualizar todas as tarefas.
3. **Buscar por ID**:
   - Enviar um `GET /tarefas/{id}` para detalhes de uma tarefa específica.
4. **Atualizar Tarefa**:
   - Enviar um `PUT /tarefas/{id}` com os dados atualizados.
5. **Excluir Tarefa**:
   - Enviar um `DELETE /tarefas/{id}` para remover uma tarefa.
6. **Filtrar por Status**:
   - Enviar um `GET /tarefas?status=pendente`.

---

## 📜 Licença
Este projeto é de livre uso sob a licença MIT.
```