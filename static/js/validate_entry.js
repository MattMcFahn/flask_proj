//DOCTYPE JavaScript
function validateEntry() {
  var x = document.getElementById("emailSubmission");
  if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(x.value))
  { return True}
  else
  alert(`You have entered an invalid email address!
    \nPlease enter an email in the form: username@domain.ext`)

  return (false)
}

function thanksMessage() {
  alert(`Thanks for the submission!
    \nRerouting to display early survey results now.`)
}
