# Template
[ ] Paginas(n a main) devem ter uma seta para voltar pra pag anterior

# JS e Backend
[ ] all_tickets_page
    [ ] Carregar tickets do BD

    [ ] Editar -> Deve ser apenas para venda de ativos?
        # deve permitir do diminiuir o numero de ativos e informar o valor da venda?
        # Como esse calculo é feito? O valor da venda vem do usuário ou de uma API?

    [ ] .js -> rever o que o catch deve fazer;

[ ] add_tickets_page
    [ ] Field quantidade e valor nao podem ser negativos

    [ ] .js -> rever o que o catch deve fazer;

[ ] Ajustar retorno das mensagens
    # Sucesso
        [ ] informar oq foi feito
            # EX: { 'status'= 200, 'message'=<MGS> }
            MGS = f'Ticker {ticket} adicionado!'
            MGS = f'Ticker {ticket} atualizado!'
    # Erro
        [ ] informar oq deu errado
            # EX: { 'status'= 500, 'message'=<MGS> }
            MGS = f'Erro ao add o {ticket}!'
            MGS = f'Erro ao atualizar o {ticket}!'