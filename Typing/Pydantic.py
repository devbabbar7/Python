from pydantic import BaseModel, EmailStr, Field, HttpUrl, SecretStr, ValidationInfo, field_validator, model_validator, computed_field, ConfigDict
from typing import Literal, Annotated
from functools import partial
from datetime import datetime, UTC
from uuid import UUID, uuid4
import json

class User(BaseModel):
    # frozen = true will make it hashable and immutable
    # extra = allow(will save extra data)/ forbid(will not allow extra data)/ ignore(will ignore extra data)
    # strict = false : by default pydantic will take "123" and make it 123 understanding what you meant but strict = true will not allow other datatypes for those fields.
    # validate_assignment: by default pydantic doesn't validate new assignments once object is created. so we have to manually set it to true.
    model_config = ConfigDict(frozen = False, str_strip_whitespace=True, extra="allow", strict = False, validate_assignment=True)
    name: Annotated[str, Field(min_length = 2, max_length = 20, pattern = r'^[a-zA-Z\s]+$')]
    email: EmailStr
    account_id: UUID = Field(alias="id", default_factory=uuid4)
    age: Annotated[int, Field(ge=0, le=139)]
    website: HttpUrl | None = None
    password: SecretStr
    status: Literal['Employee', 'Ex-Employee'] = 'Employee' # Default value
    projects: list[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=partial(datetime.now)) # IST(local TZ)
    created_at_UTC: datetime = Field(default_factory=partial(datetime.now, tz = UTC))
    @field_validator('name')
    def validate_name(cls, val: str):
        return ' '.join([i.capitalize() for i in val.split()])
    
    @computed_field # This is used to also add this field in our JSON. By default property is just a virtual field so it won't appear when we try to print our object.
    @property
    def display_name(self) -> str:
        return self.name.upper()

class Login(BaseModel):
    email: EmailStr
    password : SecretStr
    confirm_password: SecretStr
    @model_validator(mode='after')
    def password_match(self):
        if self.password != self.confirm_password:
            raise ValueError('Passwords do not match.')
        return self
    
class Manager(BaseModel):
    Account: User
    
if __name__ == "__main__":
    user = User(name="john dOE", email="john@example.com", age = 23, password = SecretStr('John@123'))
    print(user.name) # John Doe
    print(user.account_id) # 8115b6c7-1f4b-4cdc-bd91-548e35900773
    print(user.created_at) # 2026-03-30 11:59:17.213666
    print(user.password) # **********
    print(user.password.get_secret_value()) # John@123
    print(user.display_name) # JOHN DOE
    print(user.model_dump_json(indent = 4, by_alias=True, exclude={"password"}))
    '''
    Output:
    {
        "name": "John Doe",
        "email": "john@example.com",
        "id": "8dc4f7f5-3695-465b-874f-b0e89d217c01",
        "age": 23,
        "website": null,
        "status": "Employee",
        "projects": [],
        "created_at": "2026-03-30T16:42:08.339497",
        "created_at_UTC": "2026-03-30T11:12:08.339517Z",
        "display_name": "JOHN DOE" # Because we used @computed_field, it will appear in our json.
    }'''
    user2_data = {
        "id": "8115b6c7-1f4b-4cdc-bd91-548e35900774",
        "name": "john dOE", 
        "email": "john@example.com", 
        "age": "23",
        "password": 'John@123'
    }
    # user2 = User.model_validate(user2_data)
    user2 = User.model_validate_json(json.dumps(user2_data)) # Same as above
    print(user2.account_id)
    userlogin = Login(email= 'devbabbar@gmail.com', password = 'abc123', confirm_password='abc123')