function checkCode() {
  try {
    // Get the value from the input field
    var code = document.getElementById("codeInput").value;
    var ans = document.getElementById("answer").value;
    var dest = document.getElementById("destination").value;
    // Check if the code is correct
    if (code.toLowerCase().trim() === ans.toLowerCase()) {
      // Redirect to another page if the code is correct
      window.location.href = dest;
    } else {
      // Display an error message or perform other actions if the code is incorrect
      alert("Incorrect answer.");
    }
  } catch (error) {
    alert("Error, reload page.");
  }
  }