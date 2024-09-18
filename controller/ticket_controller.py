# transformar em uma classe

def get_ticket_controller():
    pass

def add_ticket_controller(req):
    reqTeste = req.form.get('teste', None)
    
    if reqTeste:
        return f'<h1>Teste: {reqTeste}</h1>'
    else:
        return '<p>O campo "teste" não foi enviado no formulário.</p>'

def delete_ticket_controller():
    pass

def put_ticket_controller():
    pass