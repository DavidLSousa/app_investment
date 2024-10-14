# Template
[ ] Paginas(n a main) devem ter uma seta para voltar pra pag anterior

# Security

# Tests
[ ] Checar se os tests estão corretos

# JS e Backend
[ ] all_tickets_page
    # Frontend
    [ ] .js -> rever o que o catch deve fazer;
    [ ] popup de venda de ativos
        [ ] o valor de venda pode ser maior do que oq esta na tabela? 
    
    [ ] Add novo campo para historico de transações;
        # Caso seja feita uma trasação errada e queira reverter (ctrl+z)

[ ] add_tickets_page
    [ ] Field quantidade e valor nao podem ser negativos

    [ ] .js -> rever o que o catch deve fazer;

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

# Refatorar
[ ] service deve ter um raise inves de return None? 
    # Sim
    [ ] Precisa revisar o service, a iterface, o adapter e a forma com que o controler esta tratando tudo;
[ ] Preciso trabalhar com um id para deletar?
    Ex:
        class TicketEntity:
            _id = peewee.AutoField(primary_key=True)
            # ...

[ ] TicketEntite, o def __post_init__ n funciona;

[ ] Load balance na requisção para apis para saber o nome do ticket?
