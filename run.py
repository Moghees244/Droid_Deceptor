from droid_deceptor import create_app, db

if __name__ == '__main__':
    app = create_app()

    with app.app_context():
        db.create_all()
        
    app.run(host='localhost', port=5000, debug=True)