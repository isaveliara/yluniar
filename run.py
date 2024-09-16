from app.app import create_app

app = create_app()

if __name__ == "__main__":
    #from host:
    #from waitress import serve
    #serve(app, host='0.0.0.0', port=80)

    
    app.run(debug=True)