

def create_ticket_controller(req):
    reqTeste = req.form.get('teste', None)
    
    if reqTeste:
        return f'<h1>Teste: {reqTeste}</h1>'
    else:
        return '<p>O campo "teste" não foi enviado no formulário.</p>'