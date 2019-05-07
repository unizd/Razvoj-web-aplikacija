$(function() {
    $('a#calculate').bind('click', function() {
      $.getJSON('http://127.0.0.1:5000/_add_numbers', {
        a: $('input[name="a"]').val(),
        b: $('input[name="b"]').val()
      }, function(data) {
        $("#result").text(data.result);
      });
      return false;
    });
});