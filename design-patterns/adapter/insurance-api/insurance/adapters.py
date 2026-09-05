from abc import ABC, abstractmethod
from uuid import uuid4

from .model import *
from .services import TravelGuardApi, AutoProtectApi

class TravelInsuranceAdapter(ABC):
    @abstractmethod
    def add_claim(self, amount):
        raise NotImplementedError()
    
    @abstractmethod
    def get_claim_status(self, claim_id) -> ClaimStatus:
        raise NotImplementedError()


class TravelGuardAdapter(TravelInsuranceAdapter):

    def __init__(self, api: TravelGuardApi):
        self.api = api
        self._result_mapping = {
            "SUCCESS": ClaimStatus.APPROVED,
            "IN_PROGRESS": ClaimStatus.PENDING,
            "FAILURE": ClaimStatus.DENIED
        }
    
    def add_claim(self, amount):
        claim_id = uuid4()
        return self.api.submit_claim(claim_id, amount)
    
    def get_claim_status(self, claim_id) -> ClaimStatus:
        status = self.api.get_claim_status(claim_id)
        try:
            return self._result_mapping[status]
        except KeyError:
            raise ValueError('Key not found: ', status)

class AutoProtectAdapter(TravelInsuranceAdapter):

    def __init__(self, api: AutoProtectApi):
        self.api = api
        self._result_mapping = {
            AutoProtectStatus.APPROVED: ClaimStatus.APPROVED,
            AutoProtectStatus.DENIED: ClaimStatus.DENIED,
            AutoProtectStatus.PENDING: ClaimStatus.PENDING
        }
    
    def add_claim(self, amount):
        return self.api.add_claim(amount)
    
    def get_claim_status(self, claim_id):
        status = self.api.get_status(claim_id)
        try:
            return self._result_mapping[status]
        except KeyError:
            raise ValueError('Key not found: ', status)
