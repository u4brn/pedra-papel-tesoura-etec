from flask import Flask, render_template, request, session
import random
app = Flask(__name__)
app.secret_key = "chave-do-jogo"
@app.route("/")
def inicio():
    if "pontos_jogador" not in session:
        session["pontos_jogador"] = 0
    if "pontos_computador" not in session:
        session["pontos_computador"] = 0
    return render_template("index.html", jogador=session["pontos_jogador"], computador=session["pontos_computador"])
@app.route("/jogar", methods=["POST"])
def jogar():
    escolha = request.form["escolha"]
    opcoes = ["pedra", "papel", "tesoura"]
    computador = random.choice(opcoes)
    resultado = ""
    if escolha == computador:
        resultado = "empate"
    elif (escolha == "pedra" and computador == "tesoura") or (escolha == "papel" and computador == "pedra") or (escolha == "tesoura" and computador == "papel"):
        resultado = "você ganhou a rodada!"
        session["pontos_jogador"] += 1
    else:
        resultado = "o computador ganhou a rodada!"
        session["pontos_computador"] += 1
    if session["pontos_jogador"] == 5:
        resultado = "você venceu o jogo!"
    elif session["pontos_computador"] == 5:
        resultado = "o computador venceu o jogo!"
    return render_template("index.html", jogador=session["pontos_jogador"], computador=session["pontos_computador"], escolha=escolha, computador_escolha=computador, resultado=resultado)
@app.route("/reiniciar")
def reiniciar():
    session["pontos_jogador"] = 0
    session["pontos_computador"] = 0
    return render_template("index.html", jogador=0, computador=0)
if __name__ == "__main__":
    app.run(debug=True)
input()
