import smtplib
import email.message

def enviar_email(destinatario):  
    corpo_email = """
    <p>Parágrafo1</p>
    <p>Parágrafo2</p>
    """

    remetente = "email_remetente"
    msg = email.message.Message()
    msg['Subject'] = "Assunto"
    msg['From'] = remetente#'remetente'
    msg['To'] = destinatario#'destinatario1', 'destinatario2', etc.
    password = 'minha_senha_de_app'#'senha'#nao e a senha do seu email
    # criar um senha especifica prara esse codigo, o proprio google gera par vc acessar o gmail
    # 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')
