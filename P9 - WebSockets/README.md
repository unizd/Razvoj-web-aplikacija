# WebSockets, SocketIO i Flask-SocketIO
Od današnjih web aplikacija očekujemo da nam isporučuju informacije bez dodatnog osvježavanja web stranice.  Tu tzv. real-time funkcionalnost mora nam omogućiti poslužitelj na način da dostavlja informacije klijentima čim se pojave, u stvarnom vremenu. Kako to postići pokazat ćemo u ovom predavanju o WebSockets, SocketIO i Flask-SocketIO, kroz radionicu izrade "chat" web aplikacije.

## Napomene
- Ukoliko aplikacija javlja grešku pri pokretanju, pokrenite je s `flask run --no-reload`
- Ukoliko želite da i drugi u vašoj mreži imaju pristup aplikaciji pokrenite je s `flask run --host '0.0.0.0'`, a zatim im dajte IP4 adresu vašeg računala. Npr: `http://192.168.2.101:5000`

## Dodatne informacije
- [WebSockets](https://en.wikipedia.org/wiki/WebSocket)
- [WebSockets API](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)
- [SocketIO](https://socket.io/)
- [SocketIO chat aplikacija u Node.js](https://socket.io/get-started/chat/)
- [Flask-SocketIO](https://flask-socketio.readthedocs.io)
- [Easy WebSockets with Flask and Gevent](https://blog.miguelgrinberg.com/post/easy-websockets-with-flask-and-gevent)
- [Notification API](https://developer.mozilla.org/en-US/docs/Web/API/notification)
