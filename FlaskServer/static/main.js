var refresh = function() {
  var table = $('#torrents_table tbody');
  var output = '';

  $.get("refresh", function(data_raw) {
    var data = JSON.parse(data_raw)
    $.each(data, function(index, torrent) {
      var row = '<tr>';
      if (torrent['status'] == 0) {
        row += '<td>' + torrent['source'] + '</td>';
        row += '<td>?</td>';
        row += '<td><progress value="0" max="100"></progress></td>';
        for (i = 0; i < 3; i++) {
          row += '<td>?</td>';
        }
      } else {
        if(torrent['status'] == 3){
          row += '<td><a href="http://localhost:7999/' + torrent['_id'].$oid + '.zip">' + torrent['name'] + '</a></td>';
        }
        else {
          row += '<td>' + torrent['name'] + '</td>';
        }
        row += '<td>' + (torrent['size'] / 1000000) + ' MB</td>';
        row += '<td><progress value="' + torrent['size_done'] + '" max="' + torrent['size'] + '"></progress></td>';
        row += '<td>' + (torrent['dlrate'] / 1000) + 'KB/s</td>';
        row += '<td>' + torrent['seeds'] + '</td>';
        row += '<td>' + torrent['leech'] + '</td>';
      }

      row += '</tr>';
      output += row;
    });

    table.empty();
    table.append(output);
  });

};

window.setInterval(refresh, 1000);
