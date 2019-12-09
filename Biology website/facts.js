function UpdateAnimals() {
    var select = document.getElementById("class")
    select.options[select.options.length] = new Option("hello")
    select.options[select.selectedIndex] = null // This just sets it to the top value
}
// Maybe have the class itself be ignorant of kingdom and shit, and categorize that in a nested ditionary? 
//okay

// Depends on how many unique types there are, might just want a fuckton of bools

class Organism {
    // Do we need to declare these before initialization as well, or is that just Swift?
    // should i just add it here then?
    // Yea
    constructor(kingdom, division, aclass, order, family, genus, species, circl, resp, waste, reprod, picture){
        this.circl  = circl
        this.resp   = resp
        this.waste  = waste
        this.reprod = reprod
    }


}
snek = new Organism("SnekKingdom", "snekDivision")
console.log(snek.kingdom)

// Info it we need for every instance, written in biological and scientifically advanced language:
// * Circulatory system
// * Respiratory system
// * Shit system
// * Fuck system

// I think object for categorization might work
// We just need Object.getOwnPropertyNames(object1) to get the keys

// alright how do we do that

// We only need to specify down to the level at which the organ systems differ
//that is just down below kingdom kinda isn't it? on average
// In that case, we'll have string values at that level

const taxonomy = {
    // Domain
    prokaryote: {
        // Kingdom
        bacteria: {
            // Whatever kinds of bacteria exist
        },
        archea: {
            // Noahs ark
            // A4
        }
    },
    eukaryote: {
        // Kingdom
        animal: { // I guess most of what we've learnt falls under here
            //animals
            //yup
            porifera: { // im gonna have no idea how to use this site with all these big boy words
                //spongebob
            },
            cnidaria: {
                //
            }
        },
        plant: { // how do plants poop
            //plants
            //chernobyl nuclear power plant 5
        },
        protozoa: {
            //shoeanimal
        },
        fungi: {
            //shrooms
        },
        chromista: {
            //ocean plant
            //wikipedia said it
        }
    }
};