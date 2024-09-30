# Template
[ ] Paginas(n a main) devem ter uma seta para voltar pra pag anterior

# MainPage 
    [ ] Add novo campo para historico de transações;

# Security
    [ ] Sanitização de dados no python (backend)
        # Da pra fazer no front sem npm?

# JS e Backend
[ ] all_tickets_page
    [ ] Carregar tickets do BD

    [ ] Editar -> Deve ser apenas para venda de ativos?
        # deve permitir do diminiuir o numero de ativos e informar o valor da venda?
        # Como esse calculo é feito? O valor da venda vem do usuário ou de uma API?

    # Frontend
    [ ] .js -> rever o que o catch deve fazer;
    [ ] html -> Mudar deleção e edição de tickets para um icone de carrinho de compras
        # Deve abrir um popup onde vai pedir o numero de tickets vendidos e o valor total da venda
        # isso muda o js tbm
    [ ] popup de venda de ativos
        [ ] o valor de venda pode ser maior do que oq esta na tabela?
    
    [ ] Manter um historico de compras e vendas?
        # Caso seja feita uma trasação errada e queira reverter

[ ] add_tickets_page
    [ ] Field quantidade e valor nao podem ser negativos

    [ ] .js -> rever o que o catch deve fazer;

    # Frontend
    [ ] html -> Btn de adicionar deve mudar enquanto aguarda o retorno do backend
        # E voltar ao normal quando o retorno chega

[ ] Ajustar retorno das mensagens a ser mostra no frontend vindo do backend a depender do que foi executado
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

[ ] service deve ter um raise inves de return None?

APIS:
[x] Brapi
    Para ações no Brasil
[x] CoinGecko API
    Para criptomoedas
[x] yfinance
    Para mercado americano