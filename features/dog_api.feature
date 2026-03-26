# language: pt
Funcionalidade: Validação da Dog API
  Como um analista de QA
  Eu quero validar os endpoints da Dog API
  Para garantir a integridade dos dados de raças e imagens.

  Cenário: 01 - Listar todas as raças de cães (GET /list/all)
    Dado que eu acesso o endpoint de listagem de todas as raças
    Então o código de status da resposta deve ser 200
    E o corpo da resposta deve conter a lista de raças com status "success"

  Cenário: 02 - Buscar imagens de uma raça específica (GET /images)
    Dado que eu busco as imagens da raça "husky"
    Então o código de status da resposta deve ser 200
    E a lista de imagens não deve estar vazia

  Cenário: 03 - Buscar uma imagem aleatória (GET /image/random)
    Dado que eu solicito uma imagem aleatória de qualquer cão
    Então o código de status da resposta deve ser 200
    E o campo "message" deve conter uma URL válida de imagem
