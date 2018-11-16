$(document).ready(function() {
    $("form").submit(function(e){
        e.preventDefault(e);
    });
    $("#search_button").click(function () {
      var search_by = $("#search_bar").val();
      console.log(search_by);
      $.ajax({
        url: '/api/perform_search/',
        data: {'search_by' : search_by},
        dataType: 'json',
        success: function (data) {
          var tableHeader = "<table><thead><tr><th>Gene</th><th>Nucleotide Change</th><th>Protein Change</th><th>Alias</th><th>Region</th><th>Reported Classifications</th><th>Last Evaluated</th><th>Last Updated</th><th>Url</th></tr></thead>"; 
          var tableContent = "<tbody>";
          for(i = 0; i < data.results.length; i++) {
          tableContent = tableContent + "<tr><td>" + data.results[i].gene + "</td><td>" + data.results[i].nucleotide_change + "</td><td>" + data.results[i].protien_change + "</td><td>"  + data.results[i].alias + "</td><td>" + data.results[i].region + "</td><td>" + data.results[i].reported_classification + "</td><td>" + data.results[i].last_evaluated + "</td><td>" + data.results[i].last_updated + "</td><td><a href=\""+ data.results[i].url + "\">" + data.results[i].source + "</a></td></tr>";
      }
      var tableFooter = "</tbody></table>"

            $("#container").html(tableHeader + tableContent + tableFooter);       
          }

      });
  });
  $.typeahead({
    input: ".js-typeahead",
    order: "asc",
    source: {
        groupName: {
            ajax: {
                url: "/api/type_ahead",
                data: {
                  search_by:'{{query}}'
                },
                path:'results'
            }
        }
    },
    callback: {
        // onClickBefore: function () { ... }
    }
});

});