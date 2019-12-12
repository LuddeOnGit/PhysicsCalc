// Made in like a week by Ludvik, Jakob and Victor. Don't believe the git blame.

//select.options[select.options.length] = new Option("hello") (Adds new item to end of dropdown)
//select.options[select.selectedIndex] = null  (Removes selected item)

function emptySelect(selectObject) {
    selectObject.options.length = 0
    return selectObject
}

function findLevel() {
    // Find the level to which the path is specified, basically the index of the last used select
    for (var i = 0; i < levels.length; i++) {
        if (document.getElementById(levels[i]).style.display == "none") {
            return i
        }
    } 
    return 8
}

function findSelectedPath(level) {
    // Path is an array of the selected taxonomy levels so far
    var path = []
    for (var i = 0; i < level; i++) {
        var levelName = levels[i]
        var value = document.getElementById(levelName).value
        if (value !== "") {
            path.push(value)            
        }
    }   
    return path
}

function populateSelect(level) {

    let path = findSelectedPath(level)
    let object = objectAt(path)

    // Hide the rest of the selects
    for (var i = level; i < levels.length; i++) {
        document.getElementById(levels[i]).style.display = "none"
    }

    // Check if the current level contains an organism object to determine whether to show the add button
    if (object instanceof Organism) {
        setAddButtonState(true)
        return // Don't show the rest of the selects
    }else {
        setAddButtonState(false)
    }

    // Get the apporopriate select and replace its values with the options
    var select = document.getElementById(levels[path.length])
    
    select.style.display = "inline"
    emptySelect(select)
    
    // Set the options of the select to a null value and the options
    var options = [""]
    try {
        var names = Object.getOwnPropertyNames(object)
        for (var i = 0; i < names.length; i++) {
            options.push(names[i])
        }
    }
    catch (TypeError){
    }

    for (var i = 0; i < options.length; i++) {
        select.options[i] = new Option(options[i])
    }
    
}

function displayInfo() {
    //print some text to the user about the organ systems in the chosen animal
}

function addToTable() {
    var path = findSelectedPath(findLevel())
    var table = document.getElementById("comTable")
    var newRow = table.insertRow(-1)

    // Add the path to the table
    for (var i = 1; i < path.length; i++) {
        var newCell = newRow.insertCell(-1)
        if (i == 7) {continue}
        newCell.innerHTML = path[i]

        if ((i == 6) && (path.length == 8)) {
            // Combine the Genus and the Species because that's how it's usually written
            newCell.innerHTML = path[6].toString() + " " + path[7].toString()
        }
    }

    // Add cells for the missing levels, and a spacing cell
    for (var i = path.length; i < levels.length; i++) {
        newRow.insertCell(-1)
    }
    let data = Object.values(objectAt(path)) //find the data for the selected species

    // Insert the data
    for (j = 0; j <= 4; j++){
        var newCell = newRow.insertCell(-1)
        newCell.innerHTML = data[j]
    }

    // Add a remove button
    
}

function setAddButtonState(state) {
    // true is enabled, false is disabled
    document.getElementById("addToTableButton").disabled = !state
}


function startUp() {
    populateSelect(0)
    
}

function objectAt(path) {
    var object = taxonomy
    for (var i = 0; i < path.length; i++) {
        object = object[path[i]]
    }
    console.log(object)
    return object
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

let levels = ["Domain", "Kingdom", "Phylum", "Class", "Order", "Family", "Genus", "Species"]

// The string for the basic mammmal systems, because I'm sick of copying them and they take up a lot of space
let dcw4ch = "<a href='#circ:double'>Double circulation</a> with a <a href='#circ:fourChamber'>4-chambered heart</a>"
let lungs = "<a href='resp:lungs'>Lungs</a>"
let kidneys = "Kidneys to dispose of <a href='exc:medium:urea'>urea</a>"
let intFert = "Internal Fertilization (no egg)"

// I'll make an inheretance system later

const taxonomy = {
    // Domain
    "Prokaryote": {
        // Kingdom
        "Bacteria": new Organism("<a href='#circ:diffusion'>Diffusion</a>", "<a href='#resp:diffusion'>Diffusion</a>", "Diffusion", "Mitosis", "Archaea.jpg"),
        "Archea":   new Organism("<a href='#circ:diffusion'>Diffusion</a>", "<a href='#resp:diffusion'>Diffusion</a>", "Diffusion", "Mitosis", "Bacterium.jpg")
    },
    "Eukaryote": {
        // Kingdom
        "Animal": {
            //animals
            "Porifera": new Organism("None", "<a href='#resp:diffusion'>Diffusion</a>", "Diffusion", "fragments regrow, two genders at the same time", "Spongebob.jpg"),
            "Cnidaria": {
                // Anders
            },
            "Chordata": {
                "Mammals": {
                    "Primates": {
                        "Homonidae": {
                            "Homo": {
                                "Sapiens": new Organism(dcw4ch, lungs, kidneys, intFert, "<img src='https://static.tildacdn.com/tild3338-6436-4031-b039-323439643964/Ansatt_bilde_2SssSss.JPG'>")
                            }
                        }
                    },
                    "Carnivora": {
                        "Canidae": {
                            "Canis": {
                                "Lupus": new Organism(dcw4ch, lungs, kidneys, intFert, "<img src='https://imgur.com/RVcmipS.jpg'>")
                            },
                            "Vulpes": {
                                "Vulpes": new Organism(dcw4ch, lungs, kidneys, intFert, "")
                            }
                        },
                        "Felidae": {
                            "Felis": {
                                "Catus": new Organism(dcw4ch, lungs, kidneys, intFert, "<img src='https://upload.wikimedia.org/wikipedia/en/thumb/b/bc/Garfield_the_Cat.svg/1200px-Garfield_the_Cat.svg.png'>")
                            }
                        }
                    }
                    
                },
                "Aves": {
                    "Accipitriformes": {
                        "Accipitridae": {
                            "Haliaeetus": new Organism("<a href='#circ:fourChamber'>4-chambered heart</a>", "Two <a href='#resp:airSacks'>air sacks</a>", "Get rid of <a href='#exc:medium:uricAcid'>uric acid</a> through mute", "External Fertilization (hard eggs)", "<img src='https://vignette.wikia.nocookie.net/angry-birds-universe/images/4/4f/MovieMightyEagle.png/revision/latest?cb=20181121061955'>")
                        }
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
