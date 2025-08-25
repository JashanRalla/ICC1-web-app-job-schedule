app = None

try:
    from app import app as _app
    app = _app
except Exception:
    try:
        from application import app as _app
        app = _app
    except Exception:
        try:
            from application import application as _app
            app = _app
        except Exception:
            from application import create_app
            app = create_app()

application = app

if __name__ == "__main__":
    app.run()
