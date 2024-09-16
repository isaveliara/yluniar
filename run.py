from app.app import criar_app

app = criar_app()

if __name__ == "__main__":
    #from host:
    #from waitress import serve
    #serve(app, host='0.0.0.0', port=80)

    
    app.run(debug=True)