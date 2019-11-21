function find_function() {
    let chosenFunction = document.getElementById("function").value
    let value1 = document.getElementById("item").value
    let value2 = document.getElementById("item2").value
    let outputObject = document.getElementById("output")

    switch (chosenFunction) {
        case "einstein":
            outputObject.value = einstein(value1)
            break;
        case "wl":
            outputObject.value = wl(value1)
            break;
        case "eHyd":
            outputObject.value = eHyd(value1)
            break;
        case "wavespeed":
            outputObject.value = wavespeed(value1, value2)
            break;
        case "eHydDiff":
            outputObject.value = eHydDiff(value1, value2)
            break;
        case "photonEnergy":
            outputObject.value = photonEnergy(value1, value2)
            break;
        case "freq":
            outputObject.value = freq(value1, value2)
            break;
        default:
            break;
    }
}

// Function to update placeholder text and other UI
function updateUI() {
    let chosenFunction = document.getElementById("function").value
    let field1 = document.getElementById("item")
    let field2 = document.getElementById("item2")


    switch (chosenFunction) {
        case "einstein":
            field1.placeholder = "mass"
            if (field2.style.display != "none"){
                field2.style.display = "none"
            }
            field2.placeholder = ""
            break;
        case "wl":
            field1.placeholder = "frequency"
            if (field2.style.display != "none"){
                field2.style.display = "none"
            }
            field2.placeholder = ""
            break;
        case "eHyd":
            field1.placeholder = "Electron shell"
            if (field2.style.display != "none"){
                field2.style.display = "none"
            }
            field2.placeholder = ""
            break;
        case "wavespeed":
            field1.placeholder = "Wavelength"
            if (field2.style.display === "none"){
                field2.style.display = "inline"
            }
            field2.placeholder = "Frequency"
            break;
        case "eHydDiff":
            field1.placeholder = "Start shell"
            if (field2.style.display === "none"){
                field2.style.display = "inline"
            }
            field2.placeholder = "End shell"
            break;
        case "photonEnergy":
            field1.placeholder = "Frequency"
            if (field2.style.display != "none"){
                field2.style.display = "none"
            }
            field2.placeholder = ""
            break;
        case "freq":
            field1.placeholder = "Wavelength"
            if (field2.style.display === "none"){
                field2.style.display = "inline"
            }
            field2.placeholder = "Speed"
            break;
        default:
            break;
    }
}

const c = 3e+8, h = 6.63e-34, B = 2.18e-18, u = 1.66e-27, mn = 1.00866491595, mp = 1.007825032241

function einstein(value) {
    return (value * c ** 2).toExponential(2)
}

function wl(value) {
    return (c / value).toExponential(2)
}

function eHyd(value) {	
    return (- B / value ** 2).toExponential(2)
}

function wavespeed(value1, value2) {
    return (value1 * value2).toExponential(2)
}

function eHydDiff(value1, value2) {
    return Math.abs((eHyd(value1) - eHyd(value2)).toExponential(2))
}

function photonEnergy(value1 = "", value2 = "") {
    if (value1 === "" && value2 === "") { 
        return "Insufficient data"
    }

    if (value1 === "") {
        value1 = freq(value2)
    }

    return value1 * h
}

function freq(value1, value2 = "") {
    if (value2 === "") {
        value2 = c
    }

    return value2 / value1
}
let physicsTitle   = "Welcome to NRG's Physics Calculator"
let chemistryTitle = "Welcome to NRG's Chemistry Calculator"

function updateWelcome(){
	document.getElementById("welcome").innerHTML = (document.getElementById("welcome").innerHTML === physicsTitle) ? chemistryTitle : physicsTitle;
}

//setInterval(updateWelcome(), 3000); 


function thereIsAnother() {
    let clone = document.querySelector('#PhysicsOriginal').cloneNode( true );
    document.querySelector('.PhysicsCalculator').appendChild(clone)
}
