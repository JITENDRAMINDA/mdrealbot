from pyrogram import Client, Filters

app = Client('663574960:AAGWfrBnjGYGSczuGHGLG60RVLMp6ebWteM',605563,"7f2c2d12880400b88764b9b304e14e0b")



u = '-1001157455913'

s =  '-1001171781537'


@app.on_message(Filters.chat(int(s))& Filters.text & ~Filters.edited)
def forward(client, message):
   
   client.send_message(int(u), message.text + message.message_id )
   mes = client.send_message
   print(mes.message_id)


app.run()
