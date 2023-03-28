from pymongo import MongoClient
from dotenv import load_dotenv
import os

# load enviroment variables
load_dotenv()

MONGODB_URI = os.environ['MONGODB_URI_LOCAL']
client = MongoClient(MONGODB_URI)

def callback(session, transfer_id=None,
             account_id_receiver=None,
             account_id_sender=None,
             transfer_amount=None):

    # get reference to 'accounts' collection
    accounts_collection = session.client.bank.accounts

    # get reference to 'transfers' collection
    transfers_collection = session.client.bank.transfers

    transfer = {
        'transfer_id': transfer_id,
        'to_account': account_id_receiver,
        'from_account': account_id_sender,
        'amount': {'$numberDecimal': transfer_amount}
    }

    # transaction operations
    # important: you must pass the session to each operation

    # update sender account: subtract transfer amount from balance and add
    # transfer ID
    accounts_collection.update_one(
        {'account_id': account_id_sender},
        {
            '$inc': {'balance': -transfer_amount},
            '$push': {'transfers_complete': transfer_id},
        },
        session=session,
    )

    # update receiver account: add transfer amount to balance and add transfer
    # ID
    accounts_collection.update_one(
        {'account_id': account_id_receiver},
        {
            '$inc': {'balance': transfer_amount},
            '$push': {'transfers_complete': transfer_id},
        },
        session=session,
    )

    # add new transfer to 'transfers' collection
    transfers_collection.insert_one(transfer, session=session)
    print('Transaction successful')

    return


def callback_wrapper(s):
    callback(
        s,
        transfer_id="TR218721873",
        account_id_receiver="MDB343652528",
        account_id_sender="MDB574189300",
        transfer_amount=100,
    )


# step 2: start a client session
with client.start_session() as session:
    # step 3: use with_transaction to start a transaction, execute the
    # callback, and commit (or cancel on error)
    session.with_transaction(callback_wrapper)

client.close()
