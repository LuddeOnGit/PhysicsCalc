//select.options[select.options.length] = new Option("hello") (Adds new item to end of dropdown)
//select.options[select.selectedIndex] = null  (Removes selected item)
function emptySelect(selectObject) {
    selectObject.options.length = 0
    return selectObject
}

let levels = ["Domain", "Kingdom", "Phylum", "Class", "Order", "Family", "Genus", "Species"]

function findPath(level = 8) {
    // Path is an array of the selected taxonomy levels so far
    var path = []
    for (var i = 0; i < level; i++) {
        var levelName = levels[i]
        var value = document.getElementById(levelName).value
        if (value !== " ") {
            path.push(value)            
        }
    }
    return path
}

function populateSelect(level) {
    document.getElementById("addToTableButton").disabled = true
    var path = findPath(level)
    
    // Get the apporopriate select and replace its values with the options
    var select = document.getElementById(levels[path.length])
    select.style.display = "inline"
    emptySelect(select)

    var values = taxonomy
    for (var i = 0; i < path.length; i++){
        values = values[path[i]]
    }

    // Set the options of the select to a null value and the options
    var options = [" "]
    try {
        var names = Object.getOwnPropertyNames(values)
        for (var i = 0; i < names.length; i++) {
            options.push(names[i])
        }
    }
    catch (TypeError){
    }

    for (var i = 0; i < options.length; i++) {
        select.options[i] = new Option(options[i])
    }

    // Hide the rest
    for (var i = level + 1; i < levels.length; i++) {
        document.getElementById(levels[i]).style.display = "none"
    }

    // Check if the current level contains an organism object to determine whether to show the add button
    //setAddButtonState(typeof(Object.values(organismAt(path)[0]) == Organism))
}

function displayInfo() {
    //print some text to the user about the organ systems in the chosen animal
}

function addToTable() {
    var path = findPath()
    var table = document.getElementById("comTable")
    var newRow = table.insertRow(-1)

    // Add the path to the right side of the divider
    for (var i = 1; i < path.length - 2; i++) {
        var newCell = newRow.insertCell(-1)
        newCell.innerHTML = path[i]
    }
    // Combine the Genus and the Species because that's how it's usually written
    var lastCell = newRow.insertCell(-1)
    lastCell.innerHTML = path[6].toString() + " " + path[7].toString()
    newRow.insertCell(-1) // Spacing cell
    var data = Object.values(organismAt(path))
    console.log(data)

    // Insert the data
    for (j = 0; j <= 4; j++){
        var newCell = newRow.insertCell(-1)
        newCell.innerHTML = data[j]
    }
}
    

    //appends characteristics of current animal in table of comparison

function setAddButtonState(state) {
    // true is shown, false is hidden
    document.getElementById("addToTableButton").disabled = !state
}


function startUp() {
    populateSelect(0)
    
}

function organismAt(path) {
    var values = taxonomy
    for (var i = 0; i < path.length; i++) {
        values = values[path[i]]
    }
    console.log(values)
    return values
}

class Organism {
    constructor(circl, resp, waste, reprod, picture){
        this.circl = circl
        this.resp = resp
        this.waste = waste
        this.reprod = reprod
        this.picture = picture
    }
}
// Info it we need for every instance, written in biological and scientifically advanced language:
// * Circulatory system
// * Respiratory system
// * Shit system
// * Fuck system

// Does the order matter?
// Circulatory system interferes a lot with resp and waste, might want it between them

const taxonomy = {
    // Domain
    "Prokaryote": {
        // Kingdom
        "Bacteria": {
            // Whatever kinds of bacteria exist
        },
        "Archea": {
            // Noahs ark
            // A4
        }
    },
    "Eukaryote": {
        // Kingdom
        "Animal": { // I guess most of what we've learnt falls under here
            //animals
            //yup
            "Porifera": new Organism(circl = "dunno", resp = "", waste = "Osmosis", reprod = "", picture = "Spongebob.jpg"),
            "Cnidaria": {
                // Anders
            },
            "Chordata": {
                "Mammals": {
                    "Gay Sapiens": {

                    },
                    "Carnivora": {
                        "Canidae": {
                            "Canis": {
                                "Lupus": new Organism(circl = "Lung", resp = "air", waste = "PeePeePooPoo", reprod = "sex", picture = "/fant.png")
                            },
                        }
                    }
                    
                },
                "Birds": {
                    "Eagle": {
                        
                    }
                },
                "Fish": {
                    "Salmon": {
                        
                    }
                },
                "Amphibia": {
                    "Frog": {
                        
                    }
                },
                "Reptilia": {
                    "Snek": {
                        "Titanboa": new Organism()
                    }
                }
            }
        },
        "Plant": { // how do plants poop
            //plants
            //chernobyl nuclear power plant 5
        },
        "Protozoa": {
            //shoeanimal
        },
        "Fungi": {
            //shrooms
        },
        "Chromista": {
            //ocean plant
            //wikipedia said it
        }
    }
};