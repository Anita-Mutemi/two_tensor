from pydantic_mongo import AbstractRepository  # type: ignore

from . import InvestingEntity, FundedEntity 
from . import InvestmentSignal


class InvestingCollection(AbstractRepository[InvestingEntity]):
    class Meta:
        collection_name = 'investing_entity'


class RaisingCollection(AbstractRepository[FundedEntity]):
    class Meta:
        collection_name = 'raising_entity'


class SignalCollection(AbstractRepository[InvestmentSignal]):
    class Meta:
        collection_name = 'signals_investment'
