class AppRouter:
    """
    Routes users/posts app to 'default' DB (users_db.sqlite3)
    Routes products app to 'products_db' DB (products_db.sqlite3)
    """

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'products':
            return 'products_db'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'products':
            return 'products_db'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        # Allow relations within same app
        if obj1._meta.app_label == obj2._meta.app_label:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'products':
            return db == 'products_db'
        return db == 'default'
