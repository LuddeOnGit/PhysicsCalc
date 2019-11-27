var script = document. createElement('script');
script. src = 'https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js';
document. getElementsByTagName('head')[0]. appendChild(script);

function findFunction() {
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
        case "uToKg":
            outputObject.value = uToKg(value1)
            break;
        case "kgToU":
            outputObject.value = kgToU(value1)
            break;
        case "extraEnergy":
            outputObject.value = extraEnergy(value1, value2)
            break;
        case "el":
            console.log("hello")
            $.ajax({
                type: "POST",
                contentType: "application/json",
                url: "/input",
                data: JSON.stringify(["el", parseFloat(value1), 1]),
                success: function(result){
                    outputObject.value = result
                }
            })
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
    let outputField = document.getElementById("output")

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
        default:
            break;
    }
    outputField.value = ""
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