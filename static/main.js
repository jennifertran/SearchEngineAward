$(document).ready(function () {
  $('#duedate').datetimepicker({
    format: 'DD/MM/YYYY'
  });
});

function loading() {
  $("#loadingContent").show();
  $("#content").hide();
}