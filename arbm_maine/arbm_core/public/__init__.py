import os

from sqlalchemy import create_engine  # type: ignore
from sqlalchemy.orm import declarative_base, sessionmaker  # type: ignore
from sqlalchemy.schema import MetaData  # type: ignore

from .. import BooleanModel

from ..private import Base
# Base = declarative_base(metadata=MetaData(schema="all_clients"))

_TAG_ATTRS = ['founded', 'location', 'team_size', 'stage', 'funding', 'last_round', 'last_round_amount']

from . import projects, users
from . import schemas
