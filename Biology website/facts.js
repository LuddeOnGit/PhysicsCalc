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
let lungs = "<a href='#resp:lungs'>Lungs</a>"
let kidneys = "<a href='#exc:kidneys'> Kidneys</a> to dispose of <a href='exc:medium:urea'>urea</a>"
let intFert = "<a href='#reprod:gendered'>Gendered reproduction</a>"

// I'll make an inheretance system later

const taxonomy = {
    // Domain
    "Prokaryote": {
        // Kingdom
        "Bacteria": new Organism("<a href='#circ:diffusion'>Diffusion</a>", "<a href='#resp:diffusion'>Diffusion</a>", "<a href='#exc:diffusion'>Diffusion</a>", "Mitosis", "<img src='https://images.ctfassets.net/cnu0m8re1exe/1GK7c53yovuQSAqxYtlhyU/e0c50965178b6329c0de767bbd072af9/shutterstock_1026248248.jpg?w=650&h=433&fit=fill'>"),
        "Archea":   new Organism("<a href='#circ:diffusion'>Diffusion</a>", "<a href='#resp:diffusion'>Diffusion</a>", "<a href='#exc:diffusion'>Diffusion</a>", "Mitosis", "<img src='http://cheyanneslifeproject.weebly.com/uploads/1/0/1/8/10188800/589420358.jpg'>")
    },
    "Eukaryote": {
        // Kingdom
        "Animal": {
            //animals
            "Platyhelminthes": {
                "Turbellaria": {
                    "Polycladida": new Organism("<a href='#circ:diffusion'>Diffusion</a>", "<a href='#resp:diffusion'>Diffusion</a>", "<a href='#exc:medium:ammonia'>Ammonia</a>, <a href='#exc:protoNephridium'>Proto Nephridium</a>", "<a href='#reprod:hermaphrodite'>Hermaphrodite</a>, <a href='#reprod:gendered'>Eggs</a>", "<img src='https://i.pinimg.com/originals/59/78/f6/5978f694949f6186eaa9a37511cf0dff.jpg'>")
                }
            },
            "Porifera": new Organism("None", "<a href='#resp:diffusion'>Diffusion</a>", "<a href='#exc:osm:diffusion'>Diffusion</a>", "<a href='#reprod:hemophrodite'>Hemophrodite</a>", "<img src='https://vignette.wikia.nocookie.net/sulleycinematicuniverse/images/0/07/SpongeBob_SquarePants.png/revision/latest?cb=20190729055447'>"),
            "Cnidaria": new Organism("None", "<a href='#resp:diffusion'>Diffusion</a>", ""),
            "Arthropoda": {
                "Insecta": new Organism("<a href='#circ:open'>Open system</a>", "<a href='#resp:diffusion'>Diffusion</a>, <a href='#resp:lungs'>lungs</a>", "<a href='#exc:malphigianTubes'>Malphigian tubules</a>", "<a href='#reprod:gendered'>Eggs</a>", "<img src='https://media.nature.com/lw1024/magazine-assets/d41586-019-03241-9/d41586-019-03241-9_17308910.jpg'>")
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
                                "Vulpes": new Organism(dcw4ch, lungs, kidneys, intFert, "<img src='https://previews.123rf.com/images/byrdyak/byrdyak1503/byrdyak150302116/37849985-red-fox-vulpes-vulpes-in-winter-time.jpg'>")
                            }
                        },
                        "Felidae": {
                            "Felis": {
                                "Catus": new Organism(dcw4ch, lungs, kidneys, intFert, "<img src='https://upload.wikimedia.org/wikipedia/en/thumb/b/bc/Garfield_the_Cat.svg/1200px-Garfield_the_Cat.svg.png'>")
                            },
                            "Lynx": {
                                "Lynx": new Organism(dcw4ch, lungs, kidneys, intFert, "<img src='https://upload.wikimedia.org/wikipedia/commons/1/1a/Lynx_lynx_%28geypa%29-cropped.jpg'>")
                            }
                        }
                    }
                    
                },
                "Aves": {
                    "Accipitriformes": {
                        "Accipitridae": {
                            "Haliaeetus": new Organism("<a href='#circ:fourChamber'>4-chambered heart</a>", "<a href='#resp:airSacks'>Air sacks</a> to assist the <a href='#resp:lungs'>lungs</a>", "Get rid of <a href='#exc:medium:uricAcid'>uric acid</a> through mute", "<a href='#reprod:gendered'>Eggs</a>", "<img src='https://vignette.wikia.nocookie.net/angry-birds-universe/images/4/4f/MovieMightyEagle.png/revision/latest?cb=20181121061955'>")
                        }
                    }
                },
                "Actinopterygii": {
                    "Salmonifores": {
                        "Salmonidae": {
                            "Salmo": new Organism("<a href='#circ:twoChamber'>2-chambered heart</a>", "<a href='#resp:gills'>Gills</a>", "Get rid of ammonia with gills and kidneys", "Externally <a href='#reprod:gendered'>fertilized</a> <a href='#reprod:soft-shell'>soft shell eggs</a>", "<img src='https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Atlantic_salmon_Atlantic_fish.jpg/1024px-Atlantic_salmon_Atlantic_fish.jpg'>")
                        }
                    }
                },
                "Amphibia": {
                    "Anura": {
                        "Frog": new Organism("<a href='#circ:closed'>Closed</a>, <a href='#circ:threeChamber'>Three-chambered heart</a>", "<a href='#resp:diffusion'>Diffusion</a>, <a href='#resp:lungs'>Lungs</a>", "Pair of <a href='#exc:kidneys'>kidneys</a>, reabsorb water from urine", "<a href='#reprod:gendered'>Gendered reproduction</a>", "<img src='https://en.wikipedia.org/wiki/Frog#/media/File:Variegated_golden_frog_(Mantella_baroni)_Ranomafana.jpg'>")
                    }
                },
                "Reptilia": {
                    "Snek": {
                        "Titanboa": new Organism("<a href='#circ:threeChamber:'>Three-chambered heart</a>, kinda like <a href='#circ:fourChamber'>four-chambered heart</a>", "<a href='resp:lungs'>Lungs</a>", "<a href='#exc:kidneys'>Kidneys</a>, <a href='#exc:medium:uricAcid'>Uric acid</a>", "<a href='#reprod:gendered'>Gendered reproduction</a>, <a href='#reprod:hard-shell'>Hard-shell eggs</a>")
                    }
                }
            }
        },
        "Plantea": { // how do plants poop
            //plants
            //chernobyl nuclear power plant 5
            "Angiosperms":{
                "Asterids":{
                    "Asterales":{
                        "Asteraceae":{
                            "Tussilago":{
                                "Farfara": new Organism("None","Uses a modified kind of <a href='#circ:diffusion'>Diffusion</a> to absorb the Oxygen", "CO<sub>2</sub> produced in photosyntesis is disposed by releasing the substance through the skin.", "<a href='#reprod:asexual'>Asexual reproduction</a>", "<a href='https://en.wikipedia.org/wiki/Tussilago'><img src='https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Coltsfoot.jpg/330px-Coltsfoot.jpg'></a>")
                            }
                        }
                    }
            
                }
            }
        },
        "Protozoa": {
            //shoeanimal
            "Ciliophora":{
                "Oligohymenophorea":{
                    "Peniculida":{
                        "Parameciidae":{
                            "Paramecium":{
                                "Aurelia": new Organism("<a href='#circ:diffusion'>Diffusion</a>","<a href='#resp:diffusion'>Diffusion</a>","<a href='#waste:diffusion'>Diffusion</a>", "<a href='#reprod:asexual'>Asexual reproduction</a> and <a href='#wordList'>mitosis</a>", "<a href='https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Paramecium.jpg/330px-Paramecium.jpg'><img src='https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Paramecium.jpg/330px-Paramecium.jpg'></a>")
                            }
                        }
                    }
                }
            }
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
