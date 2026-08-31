from __future__ import annotations

from dataclasses import dataclass

from .builder import Builder


@dataclass
class Query:
    select: str
    from_: str
    where: str
    join: str
    order_by: str
    group_by: str

    @staticmethod
    def builder() -> QueryBuilder:
        return Query.QueryBuilder()

    class QueryBuilder(Builder["Query"]):
        def __init__(self):
            self._instance = Query(None, None, None, None, None, None)
        
        def with_select(columns: list[str]):
            column_str = ""
            for i in columns:
                if column_str:
                    column_str += f", {i}"
                else:
                    column_str = f"{i}"
            self._instance.select = column_str
        
        def with_from(from_:str):
            self._instance.from_ = from_
        
        def with_where(where:str):
            self._instance.where = where
        
        def with_join(join: str):
            self.join = join
        
        def with_order_by(order_by:str):
            self._instance.order_by = order_by

        def with_group_by(group_by:str):
            self._instance.group_by = group_by

        def build(self) -> Query:
            return Query(self._instance.select,
            self._instance.from_,
            self._instance.where,
            self._instance.join,
            self._instance.order_by,
            self._instance.group_by)
