import xlsxwriter
import random
import smtplib


with open('emails.py', 'r') as e_mails:
    emails_passados = e_mails.read()
    exec(emails_passados)

def main(emails):
    planilha_centavos, pagina_planilha_centavos = cria_planilha_emails('centavos')
    planilha_apelidos, pagina_planilha_apelidos = cria_planilha_emails('apelidos')

    random.seed(1098)
    raiz_apelido = random.randint(200, 300)
    for indice, email in enumerate(emails):

        chave_apelido = indice + 2
        apelido = raiz_apelido + chave_apelido

        linha_email = f'A{chave_apelido}'
        linha_apelido = f'B{chave_apelido}'

        pagina_planilha_apelidos.write(linha_email, email)
        pagina_planilha_centavos.write(linha_email, email)

        pagina_planilha_apelidos.write(linha_apelido, apelido)

    planilha_centavos.close()
    planilha_apelidos.close()


def cria_planilha_emails(nome):
    planilha = xlsxwriter.Workbook(f'{nome}.xlsx')
    pagina_planilha = planilha.add_worksheet()

    bold = planilha.add_format({'bold': True})
    pagina_planilha.set_column('A:A', 50, bold) 

    pagina_planilha.write('A1', 'E-mails')

    return (planilha, pagina_planilha)


if __name__ == '__main__':
    main(emails)


def envia_email(dicionario):

    remetente = 'leandra.silva@ccc.ufcg.edu.br'
    senha = 'leandrinha1717'

    destinatario = 'rodrigo.cavalcanti@ccc.ufcg.edu.br'
    subject = 'Apelido centavos LOAC'
    mensagem = "Seu apelido na planilha centavos.xlsx : "

    email_text = """\
    remetente: %s
    destinatario: %s
    subject: %s

    %s
    """ % (remetente, ", ".join(destinatario), subject, mensagem)

    try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(remetente, senha)
    server.sendmail(remetente, destinatario, email_text)
    server.close()

    print ('Email enviado com sucesso!')
    except:
    print ('O email não foi enviado')