import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase import firebase

cred = credentials.Certificate("db-maskpython-firebase-adminsdk-dwffn-4a5e27458b.json")
firebase_admin.initialize_app(cred)
db = firestore.client().collection("data")

query = db.order_by("id",direction=firestore.Query.DESCENDING).limit(1).get()
if query==[] :
    db.document('1').set({'id':'1','idperson': '1', 'status': 'pending', 'img': "-"})
else :
    for post in query:
        item = u'{}'.format(post.to_dict()['id'])
    new_id=str(int(item)+1)
    db.document(new_id).set({'id':new_id,'idperson': '1', 'status': 'pending', 'img': "-"})


