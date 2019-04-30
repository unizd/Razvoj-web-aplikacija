(function () {
  var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace);
  var form = document.querySelector("form");
  form.addEventListener("submit", e => {
      e.preventDefault(); // prevents page reloading
      socket.emit('chat_message', { text: document.querySelector('#m').value, user: document.querySelector('#user').value });
      document.querySelector('#m').value = '';
      return false;
  });
  socket.on('chat_message', function (msg) {
      var li = document.createElement("li");
      var poruka = (msg.user === "" ? "Anonymous" : msg.user) + ": " + msg.text;
      li.appendChild(document.createTextNode(poruka));
      notify(msg);
      document.querySelector('#messages').appendChild(li);
  });

  var mentioned = function (msg) {
      var monkeyPos = msg.text.indexOf('@');
      if (monkeyPos >= 0) {
          var spacePos = msg.text.indexOf(' ', monkeyPos);
          if (spacePos > monkeyPos) {
              var name = msg.text.substring(monkeyPos + 1, spacePos);
              var myName = document.querySelector('#user').value;
              if (name === myName) {
                  return true;
              }
          }
      }
      return false;
  }

  var notify = function (msg) {
      if (mentioned(msg)) {
          var note = msg.user + " te je spomenuo.";
          // Let's check whether notification permissions have already been granted
          if (Notification.permission === "granted") {
              spawnNotification(note, 'Flask-Chat');
          }
          // Otherwise, we need to ask the user for permission
          else if (Notification.permission !== "denied") {
              Notification.requestPermission().then(function (permission) {
                  // If the user accepts, let's create a notification
                  if (permission === "granted") {
                    spawnNotification(note, 'Flask-Chat');
                  }
              });
          }
      }
  }

  var spawnNotification = function (body, title) {
      var options = {
          body: body
      };
      var n = new Notification(title, options);
  }

})();