from pyscript import document

club_members = ["Philip Ponce", "Logan Anaque", "Francis Fernandez", "Edrian Correa", "Juan Dela Cruz"]

def check_club(e):
    first_name = document.getElementById("firstName").value
    last_name = document.getElementById("lastName").value

    full_name = first_name + " " + last_name

    result = document.getElementById("result")

    result.innerText = "Sorry " + full_name + ", your name is not on the list."
<body>

    <div class="container">
        <h1>Varsity Club Checker</h1>

        <label for="firstName">First Name:</label>
        <input type="text" id="firstName" placeholder="e.g. John">

        <label for="lastName">Last Name:</label>
        <input type="text" id="lastName" placeholder="e.g. Doe">

        <button id="checkButton" py-click="check_club">Check Membership</button>

        <p id="result"></p>
    </div>