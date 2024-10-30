from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)
testetestestesteEnricoLeonardo

def conectar_banco():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="marins12",
        database="ATIVIDADE3",
    )


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


@app.route("/politica-privacidade")
def politica_privacidade():
    return render_template("privacidade.html")


@app.route("/quem-somos")
def somos():
    return render_template("somos.html")


@app.route("/termos-servico")
def termos():
    return render_template("termos.html")


@app.route("/contato")
def contato_form():
    return render_template("contato.html")


@app.route("/contato", methods=["POST"])
def contato():
    nome = request.form["nome"]
    email = request.form["email"]
    assunto = request.form["assunto"]
    descricao = request.form["descricao"]

    conn = conectar_banco()
    cursor = conn.cursor()
    sql = (
        "INSERT INTO contatos (nome, email, assunto, descricao) VALUES (%s, %s, %s, %s)"
    )
    cursor.execute(sql, (nome, email, assunto, descricao))
    conn.commit()

    cursor.close()
    conn.close()

    return render_template("sucesso.html")


@app.route("/listar")
def listar_contatos():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contatos")
    contatos = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("listar.html", contatos=contatos)


if __name__ == "__main__":
    app.run(debug=True)
