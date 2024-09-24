# Template
[ ] render with jinja
[ ] usar include para reutilizar componentes

[ ] Paginas(n a main) devem ter uma seta para voltar pra pag anterior

# JS e Backend
[ ] all_tickets_page
    [ ] Btns
        [ ] Edição
        [ ] Deleção
    [ ] Carregar tickets do BD

    [ ] Editar -> Deve ser apenas para venda de ativos?
        # deve permitir do diminiuir o numero de ativos e informar o valor da venda?
        # Como esse calculo é feito? O valor da venda vem do usuário ou de uma API?

    [ ] .js -> rever o que o catch deve fazer;

[ ] add_tickets_page
    [ ] Salvar tickets no BD

    [ ] Deve ser para add um ativo novo OU uma nova compra de um ativo que ja existe
        # Se o ativo ja existe, ele deve ser atualizado
            [ ] incrementar a quantidade de ativos
            [ ] atualizar o valor total investido
            [ ] atualizar o valor mais alto
            [ ] atualizar o valor mais baixo
            [ ] atualizar o valor medio
            [ ] adicionar a nova compra ao historico

    [ ] Field Ticker busca se o Ticker é valido
        # Se não for valido, exibir mensagem de erro
        # Não permitir o envio da requisição
    [ ] Field quantidade e valor nao podem ser negativos

    [ ] Se o ticker ja existir no BD, deve add o novo valor ao valor existente

    [ ] .js -> rever o que o catch deve fazer;

<!-- 
MODELS

history:
  Deve ter: 
  - a data da compra, 
  - a quantidade de foi comprada nessa data e 
  - o valor pelo qual foi comprado
 -->