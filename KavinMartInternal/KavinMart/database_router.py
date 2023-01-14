class Router(object):
    '''
    This defines which models to use which database.
    '''

    apps_require_database = {
        "storeuser": "users",
    }

    DEFAULT_DB = "default"

    def db_for_read(self, model, **hints):
        """
        This is specifies which database to use in case of read for a specific model
        :param model:
        :param hints:
        :return:
        """
        app_label = model._meta.app_label
        if app_label in self.apps_require_database:
            return self.apps_require_database[app_label]
        return self.DEFAULT_DB

    def db_for_write(self, model, **hints):
        """
        This specifies which database to use in case of write for a specific model
        :param model:
        :param hints:
        :return:
        """
        app_label = model._meta.app_label
        if app_label in self.apps_require_database:
            return self.apps_require_database[app_label]

        return self.DEFAULT_DB

    def allow_relation(self, obj1, obj2, **hints):
        """
        This specifies if the objects belongs to model that is using mysql
        :param obj1:
        :param obj2:
        :param hints:
        :return:
        """
        if obj1._meta.app_label in self.apps_require_database and obj2._meta.app_label in self.apps_require_database:
            return True
        if obj1._meta.app_label in {'auth', 'contenttypes'} or obj2._meta.app_label in {'auth', 'contenttypes'}:
            return True
        return None

    def allow_syncdb(self, db, model):
        """
        This function specifies which models to sync where
        :param db:
        :param model:
        :return:
        """

        for dbKey, dbValues in self.apps_require_database.items():
            if db == dbValues:
                return model._meta.app_label == dbKey

        if db == self.DEFAULT_DB:
            return model._meta.app_label not in self.apps_require_database

        return None
