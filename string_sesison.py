from telethon.sync import TelegramClient
from telethon.sessions import StringSession
print("")
print("""šÆšššāāā š»ššš šš šŗššššššŗšššššš š®šššššššš ššš šŗššššš©šš šš @SuperBotOT """)
print("""š²ššššš ššššš ššš ššššššš ššššš šš ššššššš āā """)

API_KEY = input("API_KEY: ")
API_HASH = input("API_HASH: ")

while True:
 try:
  with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
   print(
       "šŗššššššŗšššššš ššš šššš šš šššš š»ššššššš šŗšššš š“ššššššš, š®š ššš ššš šš, ššš š²ššš šš šŗššš ššš š«ššāš šššššš šš šššššš. "
   )
   print("")
   session = client.session.save()
   client.send_message(
       "me",
       f"šÆššš šš ššš šŗššššššŗšššššš ššš šŗššššš©šš\n(**ššš„ š¤š£ š©šš šš©š§šš£š š©š¤ š¾š¤š„š® šš©**)š\n\n`{session}`\n\nš½šššš @SuperBotOT ššš ššš ššššššš šš šššš."
   )
 except Exception as e:
  print(str(e))
  print(
      "\nā ļø ššš«š§š¢š§š  ā ļø\nš¾šššš š·šššš šµš. šššššššš āā \nš“ššš šššš šššš ššš šššššššš š·šššš šµš. šš šššš ššš ššššššš šŖšššššš šŖššš. šš­šš¢š„š”š : +91 9*6*3 4*2*1\n\nš²ššššš š¹šš»šš"
  )
  print("")
  continue
 break
