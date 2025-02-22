import uuid
from datetime import datetime

from sqlmodel import Field

from api.db.models.base import BaseModel, BaseTable


class TenantSchemaBase(BaseModel):
    tenant_id: uuid.UUID = Field(nullable=False)
    wallet_id: uuid.UUID = Field(nullable=False)
    # workflow_id will be null until the tenant kcks it off
    workflow_id: uuid.UUID = Field(nullable=True, default=None)
    schema_id: str = Field(nullable=True, default=None)
    schema_name: str = Field(nullable=True, default=None)
    schema_version: str = Field(nullable=True, default=None)
    schema_attrs: str = Field(nullable=True, default=None)
    schema_txn_id: uuid.UUID = Field(nullable=True, default=None)
    schema_state: str = Field(nullable=True, default=None)
    cred_def_tag: str = Field(nullable=True, default=None)
    cred_def_txn_id: uuid.UUID = Field(nullable=True, default=None)
    cred_def_id: str = Field(nullable=True, default=None)
    cred_def_state: str = Field(nullable=True, default=None)
    cred_revocation: bool = Field(nullable=True, default=None)
    cred_revoc_reg_size: int = Field(nullable=True, default=None)
    revoc_reg_state: str = Field(nullable=True, default=None)


class TenantSchema(TenantSchemaBase, BaseTable, table=True):
    # This is the class that represents the table
    pass


class TenantSchemaCreate(TenantSchemaBase):
    # This is the class that represents interface for creating a tenant
    # we must set all the required fields,
    # but do not need to set optional (and shouldn't)
    pass


class TenantSchemaRead(TenantSchemaBase):
    # This is the class that represents interface for reading a tenant
    # here we indicate id, created_at and updated_at must be included
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime


class TenantSchemaUpdate(BaseModel):
    # This is our update interface
    # This does NOT inherit from TenantSchemaBase,
    # so no need to worry about accidentally updating id or other fields
    id: uuid.UUID
    workflow_id: uuid.UUID = Field(nullable=True, default=None)
    schema_id: str = Field(nullable=True, default=None)
    schema_txn_id: uuid.UUID = Field(nullable=True, default=None)
    schema_state: str = Field(nullable=True, default=None)
    cred_def_txn_id: uuid.UUID = Field(nullable=True, default=None)
    cred_def_id: str = Field(nullable=True, default=None)
    cred_def_state: str = Field(nullable=True, default=None)
    revoc_reg_state: str = Field(nullable=True, default=None)
