
from src.repositories.TransactionRepository import TransactionRepository
from src.utils.convert import queryResultToDict
from src.services.Service import Service

transactionRepository = TransactionRepository()    

class TransactionService(Service):
    @staticmethod
    def failedOrSuccessRequest(status, code, data):
        return {
            'status': status,
            "code": code,
            'data': data,
        }
    
    def getAllTransactions(self):
        try:
            data = TransactionRepository.getAllTransaction()
            print(data)
            return self.failedOrSuccessRequest('success', 200, queryResultToDict(data,['user','ticket']))
        except Exception as e:
            return self.failedOrSuccessRequest('failed', 500, str(e))
    def getTransactionByUserId(self,user_id):
        try:
            data = TransactionRepository.getTransactionByUserId(user_id)
            return self.failedOrSuccessRequest('success', 200, queryResultToDict(data,['user','ticket']))
        except Exception as e:
            return self.failedOrSuccessRequest('failed', 500, str(e))
