function sendInputs() {
    let chosenFunction = document.getElementById("function").value
    let value1 = document.getElementById("item").value
    let value2 = document.getElementById("item2").value
    let outputObject = document.getElementById("output")
    $.ajax({
        type: "POST",
        contentType: "application/JSON",
        url: "/input",
        data: JSON.stringify([chosenFunction, value1, value2]),
        success: function(result){
            outputObject.value = result 
        }
    })
}

// Function to update placeholder text and other UI
function updateUI() {
    let chosenFunction = document.getElementById("function").value
    let field1 = document.getElementById("item")
    let field2 = document.getElementById("item2")
    document.getElementById("output").value = ""

    switch (chosenFunction) {
        case "einstein":
            field1.placeholder = "Mass"
            field2.style.display = "none"
            break;
        case "wl":
            field1.placeholder = "Wave Frequency"
            field2.style.display = "none"
            break;
        case "eHyd":
            field1.placeholder = "Electron shell"
            field2.style.display = "none"
            break;
        case "wavespeed":
            field1.placeholder = "Wavelength"
            field2.style.display = "inline"
            field2.placeholder = "Frequency"
            break;
        case "eHydDiff":
            field1.placeholder = "Start shell"
            field2.style.display = "inline"
            field2.placeholder = "End shell"
            break;
        case "photonEnergy":
            field1.placeholder = "Frequency"
            field2.style.display = "none"
            break;
        case "freq":
            field1.placeholder = "Wavelength"
            field2.style.display = "inline"
            field2.placeholder = "Wave Speed"
            break;
        case "uToKg":
            field1.placeholder = "mass in u"
            field2.style.display = "none"
            break;
        case "kgToU":
            field1.placeholder = "mass in Kg"
            field2.style.display = "none"
            break;
        case "extraEnergy":
            field1.placeholder = "mass start"
            field2.style.display = "inline"
            field2.placeholder = "mass end"
            break;
        case "el":
            field1.placeholder = "wavelength"
            field2.style.display = "none"
            break; 
        case "freqOld":
            field1.placeholder = "waves"
            field2.style.display = "inline"
            field2.placeholder = "seconds, default = 1"
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

function wavespeed(value1, value2) {
    return (value1 * value2).toExponential(2)
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
        value2 = c;
    }

    return value2 / value1;
}

function uToKg(value) {
    return (value * u).toExponential(3);
}

function kgToU(value) {
    return (value / u).toExponential(3);
}

function extraEnergy(value1, value2) {
    return einstein(uToKg(value2 - value1));
}

let physicsTitle   = "Welcome to NRG's Physics Calculator";
let chemistryTitle = "Welcome to NRG's Chemistry Calculator";

function updateWelcome(){
	document.getElementById("welcome").innerHTML = (document.getElementById("welcome").innerHTML === physicsTitle) ? chemistryTitle : physicsTitle;
}

function thereIsAnother() {
    let clone = document.querySelector('.PhysicsCalculator').cloneNode( true );
    document.querySelector('body').appendChild(clone);
}

function copyToClipboard(){
    var copyText = document.getElementById("output");

    copyText.select();
    copyText.setSelectionRange(0,99999)

    document.execCommand("copy")
}