from src.models.Transaction import Transaction,db
class TransactionRepository:
  def getAllTransaction():
    return Transaction.query.all()  
  def getTransactionByUserId(user_id):
    return Transaction.query.filter_by(user_id=user_id).all()
  def createNewTransaction(self,type,nominal,user_id,ticket_id=None):
    newTransaction = Transaction(
      type=type, 
      user_id=user_id,
      nominal=nominal
      )
    if(type == 'buy'):
      newTransaction.setTIcketId(ticket_id)
      
    db.session.add(newTransaction)
    db.session.commit()
    return newTransaction
  