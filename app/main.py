from flask import Flask, render_template, request, session, redirect, url_for
from app.components.retriever import create_qa_chain

import os
from dotenv import load_dotenv
from markupsafe import Markup
load_dotenv()

app = Flask(__name__)



app.secret_key = os.urandom(24)
# def nl2br(value):
#     return Markup(value.replace("\n","<br>\n"))

# app.jinja_env.filters["nl2br"] = nl2br



@app.route("/", methods=["GET", "POST"])
def index():
    answer = None
    question = None
    if "messages" not in session:
        session["messages"] = []

    if request.method == "POST":
        question = request.form["query"]
        print("Question:===",question)
        if question:
            session["messages"].append({"role":"user","content":question})
            print("Session Messages::::=====",session["messages"])
            try:
                qa_chain = create_qa_chain()
                answer = qa_chain.invoke(session["messages"][-1]["content"])
                if answer:
                    session["messages"].append({"role":"assistant","content":answer})

                return render_template("index.html",messages = session["messages"])
            except Exception as e:
                print(f"Error while answering question:={answer}",e)
                return render_template("index.html",messages = session["messages"],error=e)
        
        return redirect(url_for("index"))
    
    else:
        return render_template("index.html",messages=session["messages"] )


@app.route("/clear",methods=["GET"])
def clear():
    session.pop("messages")
    return redirect(url_for("index"))


if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,use_reloader=False)