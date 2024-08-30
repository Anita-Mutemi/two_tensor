import abc

from pydantic_mongo import ObjectIdField  # type: ignore

from . import PyMongoBase


class GraphEntity(PyMongoBase, abc.ABC):
    pass


class InvestingEntity(GraphEntity):
    id: ObjectIdField = None


class FundedEntity(GraphEntity):
    id: ObjectIdField = None
