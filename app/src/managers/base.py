from sqlalchemy import MetaData


class BaseModel:
    @property
    def json(self):
        columns = [c.name for c in self.__table__.columns]
        columnitems = dict([ (c, getattr(self, c)) for c in columns])
        return columnitems
