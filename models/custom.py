# Created by        : MyWork
# Created on        : 2024-05-24
from pydantic import BaseModel, Field


class HashModel(BaseModel):
    name: str = Field()
    type: str = Field()

    def hash_code(self):
        prime = 31
        hsh = 17
        hsh = hsh * prime + hash(self.name)
        hsh = hsh * prime + hash(self.type)
        return hsh


mdl = HashModel(name='hash', type='cat')
print(mdl.hash_code())
