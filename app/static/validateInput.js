function validate() {
  var error="";

  if(document.getElementById('faculty').value == "-1")
	   error += "Please choose a faculty/school\n\n";
  if(document.getElementById('type').value == "-1")
	   error += "Please choose a Type";
  if (error == "")
  		return true;
  else {
	   alert("Error(s):\n\n\n"+error);
	   return false;
  }
}