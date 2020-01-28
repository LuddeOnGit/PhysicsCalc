"""
author: NRG
"""

class Element:
    
    # TODO: add isotopes
    
    def __init__(self, number, symbol, name, boilingPoint, meltingPoint, mass, isotopes={}):
        self.number = number
        self.symbol = symbol
        self.name = name
        self.boilingPoint = boilingPoint
        self.meltingPoint = meltingPoint
        self.mass = mass
        self.isotopes = isotopes
        
        # group and period are functions here because them being able to return makes things more efficient
        
        def period():
            if self.number <=   2: return 1
            if self.number <=  10: return 2
            if self.number <=  18: return 3
            if self.number <=  36: return 4
            if self.number <=  54: return 5
            if self.number <=  86: return 6
            if self.number <= 118: return 7
        
        # Returns the group of the element
        def group():
            # Redeclaring to shorten
            n = self.number
            
            # Check if the element is each of the elements in each group. 
            # This is proboably not the most efficient solution.
            # This makes a sideways backwards periodic table.
            if n in [1, 3,11,19,37,55, 87]: return  1
            if n in   [ 4,12,20,38,56, 88]: return  2
            if n in         [21,39       ]: return  3
            if n in         [22,40,72,104]: return  4
            if n in         [23,41,73,105]: return  5
            if n in         [24,42,74,106]: return  6
            if n in         [25,43,75,107]: return  7
            if n in         [26,44,76,108]: return  8
            if n in         [27,45,77,109]: return  9
            if n in         [28,46,78,110]: return 10
            if n in         [29,47,79,111]: return 11
            if n in         [30,48,80,112]: return 12
            if n in   [ 5,13,31,49,81,113]: return 13
            if n in   [ 6,14,32,50,82,114]: return 14
            if n in   [ 7,15,33,51,83,115]: return 15
            if n in   [ 8,16,34,52,84,116]: return 16
            if n in   [ 9,17,35,53,85,117]: return 17
            if n in [2,10,18,36,54,86,118]: return 18
            
            # Check if the element is a lanthanoid or an actinoid, as they have no defined group
            if n in range(57,  71+1): return "l" 
            if n in range(89, 103+1): return "a"
        
        
        self.group = group()
        self.period = period()
        
        # Returns the electron configuration in orbitals, assuming the atom is net neutrally charged.
        def electronConfiguration(): 
            shells = ["1s", "2s", "2p", "3s", "3p", "4s", "3d", "4p", "5s", "4d", "5p", "6s", "4f", "5d", "6p", "7s", "5f", "6d", "7p"]
            electrons_in_shells = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
            def find_next_shell(ec, index = 0):
                if ec - electrons_in_shells[index] > 0:
                    return shells[index] + str(electrons_in_shells[index]) + ", " + find_next_shell(ec-electrons_in_shells[index], index + 1)
                else:
                    return shells[index] + str(ec)
            return find_next_shell(self.number)
        
        self.eConfig = electronConfiguration()
        
        
    # Function to return a describing string
    def info(self): 
        return f"{self.name} ({self.symbol}) has atomic number {self.number}, {self.mass}u atomic mass, {self.meltingPoint}K melting point and {self.boilingPoint}K boiling point. It is in group {self.group} and period {self.period}. It has electron configuration {self.eConfig}"
     

    # Returns what state the element is in at a given temperature in Kelvin
    def stateAt(self, temp):
        if type(self.meltingPoint) != str:
            if temp < self.meltingPoint: return "solid"
        if type(self.boilingPoint) != str:
            if temp < self.boilingPoint: return "liquid"
            else: return "gas"
        return "Unknown"

class Isotope:
    def __init__(self, Z, A, mass, decayMode=0):
        self.protons = Z
        self.nucleons = A
        self.neutrons = A - Z
        self.mass = mass
        self.decayMode = decayMode
   
    # Returns the isotope it would be after the given decay
    def radiate(self, mode):
       if self.decayMode & mode == 0: return "This isotope can't radiate at that mode"
       
       A = self.nucleons
       Z = self.protons
       
       if mode == alpha:
           # A helium-4 core is emitted
           A -= 4
           Z -= 2
       elif mode == betaN:
           # A neutron turns into a proton and an electron
           Z += 1
       elif mode == betaP:
           # A proton turns into a neutron and a positron
           Z -= 1
       elif mode == gamma:
           # A gamma ray is emitted
           A -= 0
    
       if A in elements[Z].isotopes: 
           return elements[Z].isotopes[A]
       
       # If we add all possible isotopes, this line should never need to be called
       return Isotope(Z= Z, A= A, mass="?")

def indexBySymbol(symbol):
    for element in elements:
        if element.symbol == symbol: return element.number

    
alpha = 1 << 3
betaN = 1 << 2
betaP = 1 << 1
gamma = 1 << 0
        
elements = [ # Number  | Symbol      | Element name         | Boiling point 1 atm (°K)| Melting point in 1 atm (°K)| mass (u)       | Isotopes 
    Element(number=   0, symbol= "E" , name= "Errorium"     , boilingPoint= "Error"   , meltingPoint= "Error"      , mass= "Error"  ), # So the index is the same as the atomic number
    Element(number=   1, symbol= "H" , name= "Hydrogen"     , boilingPoint=     20.28 , meltingPoint=         13.81, mass=   1.00794, isotopes= { 1:Isotope(Z= 1,A= 1,mass= 1.00783),  2:Isotope(Z=1,A= 2,mass= 2.0141),  3:Isotope(Z=1,A=3,mass=3.01605,decayMode=betaN)}),
    Element(number=   2, symbol= "He", name= "Helium"       , boilingPoint=      4.216, meltingPoint=          0.95, mass=   4.0026 , isotopes= { 3:Isotope(Z= 2,A= 3,mass= 3.01603),  4:Isotope(Z=2,A= 4,mass= 4.0026)}),
    Element(number=   3, symbol= "Li", name= "Lithium"      , boilingPoint=   1615    , meltingPoint=        453.7 , mass=   6.941  , isotopes= { 6:Isotope(Z= 3,A= 6,mass= 6.01512),  7:Isotope(Z=3,A= 7,mass= 7.0160)}),
    Element(number=   4, symbol= "Be", name= "Beryllium"    , boilingPoint=   3243    , meltingPoint=       1560   , mass=   9.01218, isotopes= { 9:Isotope(Z= 4,A= 9,mass= 9.01218)}),
    Element(number=   5, symbol= "B" , name= "Boron"        , boilingPoint=   4275    , meltingPoint=       2365   , mass=  10.811  , isotopes= {10:Isotope(Z= 5,A=10,mass=10.01294), 11:Isotope(Z=5,A=11,mass=11.00931)}),
    Element(number=   6, symbol= "C" , name= "Carbon"       , boilingPoint=   5100    , meltingPoint=       3825   , mass=  12.011  , isotopes= {12:Isotope(Z= 6,A=12,mass=12), 13:Isotope(Z=6,A=13,mass=13.00335), 14:Isotope(Z=6,A=14,mass=14.00324,decayMode=betaN)}),
    Element(number=   7, symbol= "N" , name= "Nitrogen"     , boilingPoint=     77.344, meltingPoint=         63.15, mass=  14.0067 , isotopes= {13:Isotope(Z= 7,A=13,mass=13.00574,decayMode=betaP), 14:Isotope(Z=7,A=14,mass=14.00307), 15:Isotope(Z=7,A=15,mass=15.00011)}),
    Element(number=   8, symbol= "O" , name= "Oxygen"       , boilingPoint=     90.188, meltingPoint=         54.8 , mass=  15.9994 , isotopes= {15:Isotope(Z= 8,A=15,mass=15.00307,decayMode=betaP+gamma), 16:Isotope(Z=8,A=16,mass=15.99491), 17:Isotope(Z=8,A=17,mass=16.99913)}),
    Element(number=   9, symbol= "F" , name= "Fluorine"     , boilingPoint=     85    , meltingPoint=         53.55, mass=  18.9984 , isotopes= {18:Isotope(Z= 9,A=18,mass=18.00094,decayMode=betaP+gamma), 19:Isotope(Z=9,A=19,mass=18.9984)}),
    Element(number=  10, symbol= "Ne", name= "Neon"         , boilingPoint=     27.1  , meltingPoint=         24.55, mass=  20.1797 , isotopes= {20:Isotope(Z=10,A=20,mass=19.99244)}),
    Element(number=  11, symbol= "Na", name= "Sodium"       , boilingPoint=   1156    , meltingPoint=        371   , mass=  22.98977, isotopes= {22:Isotope(Z=11,A=22,mass=21.99443,decayMode=betaP+gamma), 23:Isotope(Z=11,A=23,mass=22.98977), 24:Isotope(Z=11,A=24,mass=23.99096,decayMode=betaN+gamma)}),
    Element(number=  12, symbol= "Mg", name= "Magnesium"    , boilingPoint=   1380    , meltingPoint=        922   , mass=  24.305  , isotopes= {26:Isotope(Z=12,A=26,mass=25.98259)}),
    Element(number=  13, symbol= "Al", name= "Aluminium"    , boilingPoint=   2740    , meltingPoint=        933.5 , mass=  26.98154, isotopes= {26:Isotope(Z=13,A=26,mass=25.98689,decayMode=betaP+gamma), 27:Isotope(Z=13,A=27,mass=26.98154)}),
    Element(number=  14, symbol= "Si", name= "Silicon"      , boilingPoint=   2630    , meltingPoint=       1683   , mass=  28.0855 ),
    Element(number=  15, symbol= "P" , name= "Phosphorus"   , boilingPoint=    553    , meltingPoint=        317.3 , mass=  30.97376),
    Element(number=  16, symbol= "S" , name= "Sulfur"       , boilingPoint=    717.82 , meltingPoint=        392.2 , mass=  32.066  ),
    Element(number=  17, symbol= "Cl", name= "Chlorine"     , boilingPoint=    239.18 , meltingPoint=        172.17, mass=  35.4527 ),
    Element(number=  18, symbol= "Ar", name= "Argon"        , boilingPoint=     87.45 , meltingPoint=         83.95, mass=  39.948  ),
    Element(number=  19, symbol= "K" , name= "Potassium"    , boilingPoint=   1033    , meltingPoint=        336.8 , mass=  39.0983 ),
    Element(number=  20, symbol= "Ca", name= "Calcium"      , boilingPoint=   1757    , meltingPoint=       1112   , mass=  40.078  ),
    Element(number=  21, symbol= "Sc", name= "Scandium"     , boilingPoint=   3109    , meltingPoint=       1814   , mass=  44.9559 ),
    Element(number=  22, symbol= "Ti", name= "Titanium"     , boilingPoint=   3560    , meltingPoint=       1945   , mass=  47.88   ),
    Element(number=  23, symbol= "V" , name= "Vanadium"     , boilingPoint=   3650    , meltingPoint=       2163   , mass=  50.9415 ),
    Element(number=  24, symbol= "Cr", name= "Chromium"     , boilingPoint=   2945    , meltingPoint=       2130   , mass=  51.996  ),
    Element(number=  25, symbol= "Mn", name= "Manganese"    , boilingPoint=   2335    , meltingPoint=       1518   , mass=  54.938  ),
    Element(number=  26, symbol= "Fe", name= "Iron"         , boilingPoint=   3023    , meltingPoint=       1808   , mass=  55.847  ),
    Element(number=  27, symbol= "Co", name= "Cobalt"       , boilingPoint=   3143    , meltingPoint=       1768   , mass=  58.9332 ),
    Element(number=  28, symbol= "Ni", name= "Nickel"       , boilingPoint=   3005    , meltingPoint=       1726   , mass=  58.6934 ),
    Element(number=  29, symbol= "Cu", name= "Copper"       , boilingPoint=   2840    , meltingPoint=       1356.6 , mass=  63.546  ),
    Element(number=  30, symbol= "Zn", name= "Zinc"         , boilingPoint=   1180    , meltingPoint=        692.73, mass=  65.39   ),
    Element(number=  31, symbol= "Ga", name= "Gallium"      , boilingPoint=   2478    , meltingPoint=        302.92, mass=  69.723  ),
    Element(number=  32, symbol= "Ge", name= "Germanium"    , boilingPoint=   3107    , meltingPoint=       1211.5 , mass=  72.61   ),
    Element(number=  33, symbol= "As", name= "Arsenic"      , boilingPoint=    876    , meltingPoint=       1090   , mass=  74.9216 ),
    Element(number=  34, symbol= "Se", name= "Selenium"     , boilingPoint=    958    , meltingPoint=        494   , mass=  78.96   ),
    Element(number=  35, symbol= "Br", name= "Bromine"      , boilingPoint=    331.85 , meltingPoint=        265.95, mass=  79.904  ),
    Element(number=  36, symbol= "Kr", name= "Krypton"      , boilingPoint=    120.85 , meltingPoint=        116   , mass=  83.8    ),
    Element(number=  37, symbol= "Rb", name= "Rubidium"     , boilingPoint=    961    , meltingPoint=        312.63, mass=  85.4678 ),
    Element(number=  38, symbol= "Sr", name= "Strontium"    , boilingPoint=   1655    , meltingPoint=       1042   , mass=  87.62   ),
    Element(number=  39, symbol= "Y" , name= "Yttrium"      , boilingPoint=   3611    , meltingPoint=       1795   , mass=  88.9059 ),
    Element(number=  40, symbol= "Zr", name= "Zirconium"    , boilingPoint=   4682    , meltingPoint=       2128   , mass=  91.224  ),
    Element(number=  41, symbol= "Nb", name= "Niobium"      , boilingPoint=   5015    , meltingPoint=       2742   , mass=  92.9064 ),
    Element(number=  42, symbol= "Mo", name= "Molybdenum"   , boilingPoint=   4912    , meltingPoint=       2896   , mass=  95.94   ),
    Element(number=  43, symbol= "Tc", name= "Technetium"   , boilingPoint=   4538    , meltingPoint=       2477   , mass=  98      ),
    Element(number=  44, symbol= "Ru", name= "Ruthenium"    , boilingPoint=   4425    , meltingPoint=       2610   , mass= 101.07   ),
    Element(number=  45, symbol= "Rh", name= "Rhodium"      , boilingPoint=   3970    , meltingPoint=       2236   , mass= 102.9055 ),
    Element(number=  46, symbol= "Pd", name= "Palladium"    , boilingPoint=   3240    , meltingPoint=       1825   , mass= 106.42   ),
    Element(number=  47, symbol= "Ag", name= "Silver"       , boilingPoint=   2436    , meltingPoint=       1235.08, mass= 107.868  ),
    Element(number=  48, symbol= "Cd", name= "Cadmium"      , boilingPoint=   1040    , meltingPoint=        594.26, mass= 112.41   ),
    Element(number=  49, symbol= "In", name= "Indium"       , boilingPoint=   2350    , meltingPoint=        429.78, mass= 114.82   ),
    Element(number=  50, symbol= "Sn", name= "Tin"          , boilingPoint=   2876    , meltingPoint=        505.12, mass= 118.71   ),
    Element(number=  51, symbol= "Sb", name= "Antimony"     , boilingPoint=   1860    , meltingPoint=        903.91, mass= 121.757  ),
    Element(number=  52, symbol= "Te", name= "Tellurium"    , boilingPoint=   1261    , meltingPoint=        722.72, mass= 127.6    ),
    Element(number=  53, symbol= "I" , name= "Iodine"       , boilingPoint=    457.5  , meltingPoint=        386.7 , mass= 126.9045 ),
    Element(number=  54, symbol= "Xe", name= "Xenon"        , boilingPoint=    165.1  , meltingPoint=        161.39, mass= 131.29   ),
    Element(number=  55, symbol= "Cs", name= "Caesium"      , boilingPoint=    944    , meltingPoint= 	     301.54, mass= 132.9054 ),
    Element(number=  56, symbol= "Ba", name= "Barium"       , boilingPoint=   2078    , meltingPoint=       1002   , mass= 137.33   ),
    Element(number=  57, symbol= "La", name= "Lanthanum"    , boilingPoint=   3737    , meltingPoint=       1191   , mass= 138.9055 ),
    Element(number=  58, symbol= "Ce", name= "Cerium"       , boilingPoint=   3715    , meltingPoint=       1071   , mass= 140.12   ),
    Element(number=  59, symbol= "Pr", name= "Praseodymium" , boilingPoint=   3785    , meltingPoint=       1204   , mass= 140.9077 ),
    Element(number=  60, symbol= "Nd", name= "Neodymium"    , boilingPoint=   3347    , meltingPoint=       1294   , mass= 144.24   ),
    Element(number=  61, symbol= "Pm", name= "Promethium"   , boilingPoint=   3273    , meltingPoint=       1315   , mass= 145      ),
    Element(number=  62, symbol= "Sm", name= "Samarium"     , boilingPoint=   2067    , meltingPoint=       1347   , mass= 150.36   ),
    Element(number=  63, symbol= "Eu", name= "Europium"     , boilingPoint=   1800    , meltingPoint=       1095   , mass= 151.965  ),
    Element(number=  64, symbol= "Gd", name= "Gadolinium"   , boilingPoint=   3545    , meltingPoint=       1585   , mass= 157.25   ),
    Element(number=  65, symbol= "Tb", name= "Terbium"      , boilingPoint=   3500    , meltingPoint=       1629   , mass= 158.9253 ),
    Element(number=  66, symbol= "Dy", name= "Dysprosium"   , boilingPoint=   2840    , meltingPoint=       1685   , mass= 162.5    ),
    Element(number=  67, symbol= "Ho", name= "Holmium"      , boilingPoint=   2968    , meltingPoint=       1747   , mass= 164.9303 ),
    Element(number=  68, symbol= "Er", name= "Erbium"       , boilingPoint=   3140    , meltingPoint=       1802   , mass= 167.26   ),
    Element(number=  69, symbol= "Tm", name= "Thulium"      , boilingPoint=   2223    , meltingPoint=       1818   , mass= 168.9342 ),
    Element(number=  70, symbol= "Yb", name= "Ytterbium"    , boilingPoint=   1469    , meltingPoint=       1092   , mass= 173.04   ),
    Element(number=  71, symbol= "Lu", name= "Lutetium"     , boilingPoint=   3668    , meltingPoint=       1936   , mass= 174.967  ),
    Element(number=  72, symbol= "Hf", name= "Hafnium"      , boilingPoint=   4875    , meltingPoint=       2504   , mass= 178.49   ),
    Element(number=  73, symbol= "Ta", name= "Tantalum"     , boilingPoint=   5730    , meltingPoint=       3293   , mass= 180.9479 ),
    Element(number=  74, symbol= "W" , name= "Tungsten"     , boilingPoint=   5825    , meltingPoint=       3695   , mass= 183.85   ),
    Element(number=  75, symbol= "Re", name= "Rhenium"      , boilingPoint=   5870    , meltingPoint=       3455   , mass= 186.207  ),
    Element(number=  76, symbol= "Os", name= "Osmium"       , boilingPoint=   5300    , meltingPoint=       3300   , mass= 190.2    ),
    Element(number=  77, symbol= "Ir", name= "Iridium"      , boilingPoint=   4700    , meltingPoint=       2720   , mass= 192.22   ),
    Element(number=  78, symbol= "Pt", name= "Platinum"     , boilingPoint=   4100    , meltingPoint=       2042.1 , mass= 195.08   ),
    Element(number=  79, symbol= "Au", name= "Gold"         , boilingPoint=   3130    , meltingPoint=       1337.58, mass= 196.9665 ),
    Element(number=  80, symbol= "Hg", name= "Mercury"      , boilingPoint=    629.88 , meltingPoint=        234.31, mass= 200.59   ),
    Element(number=  81, symbol= "Tl", name= "Thallium"     , boilingPoint=   1746    , meltingPoint=        577   , mass= 204.383  ),
    Element(number=  82, symbol= "Pb", name= "Lead"         , boilingPoint=   2023    , meltingPoint=        600.65, mass= 207.2    ),
    Element(number=  83, symbol= "Bi", name= "Bismuth"      , boilingPoint=   1837    , meltingPoint=        544.59, mass= 208.9804 ),
    Element(number=  84, symbol= "Po", name= "Polonium"     , boilingPoint=   1235    , meltingPoint=        527.7 , mass= 209      ),
    Element(number=  85, symbol= "At", name= "Astatine"     , boilingPoint=    610    , meltingPoint=        575   , mass= 210      ),
    Element(number=  86, symbol= "Rn", name= "Radon"        , boilingPoint=    211.4  , meltingPoint=        202   , mass= 222      ),
    Element(number=  87, symbol= "Fr", name= "Francium"     , boilingPoint=    950    , meltingPoint=        300   , mass= 223      ),
    Element(number=  88, symbol= "Ra", name= "Radium"       , boilingPoint=   1413    , meltingPoint=        973   , mass= 226.0254 ),
    Element(number=  89, symbol= "Ac", name= "Actinium"     , boilingPoint=   3470    , meltingPoint=       1323   , mass= 227      ),
    Element(number=  90, symbol= "Th", name= "Thorium"      , boilingPoint=   5060    , meltingPoint=       2028   , mass= 232.0381 ),
    Element(number=  91, symbol= "Pa", name= "Protactinium" , boilingPoint=   4300    , meltingPoint=       1845   , mass= 231.0359 ),
    Element(number=  92, symbol= "U" , name= "Uranium"      , boilingPoint=   4407    , meltingPoint=       1408   , mass= 238.029  ),
    Element(number=  93, symbol= "Np", name= "Neptunium"    , boilingPoint=   4175    , meltingPoint=        912   , mass= 237.0482 ),
    Element(number=  94, symbol= "Pu", name= "Plutonium"    , boilingPoint=   3505    , meltingPoint=        913   , mass= 244      ),
    Element(number=  95, symbol= "Am", name= "Americium"    , boilingPoint=   2880    , meltingPoint=       1449   , mass= 243      ),
    Element(number=  96, symbol= "Cm", name= "Curium"       , boilingPoint=   3383    , meltingPoint=       1618   , mass= 247      ),
    Element(number=  97, symbol= "Bk", name= "Berkelium"    , boilingPoint=   2900    , meltingPoint=       1259   , mass= 247      ),
    Element(number=  98, symbol= "Cf", name= "Californium"  , boilingPoint=   1745    , meltingPoint=       1173   , mass= 251      ),
    Element(number=  99, symbol= "Es", name= "Einsteinium"  , boilingPoint=   1269    , meltingPoint=       1133   , mass= 252      ),
    Element(number= 100, symbol= "Fm", name= "Fermium"      , boilingPoint= "Unknown" , meltingPoint=       1800   , mass= 257      ),
    Element(number= 101, symbol= "Md", name= "Mendelevium"  , boilingPoint= "Unknown" , meltingPoint=       1100   , mass= 258      ),
    Element(number= 102, symbol= "No", name= "Nobelium"     , boilingPoint= "Unknown" , meltingPoint=       1100   , mass= 259      ),
    Element(number= 103, symbol= "Lr", name= "Lawrencium"   , boilingPoint= "Unknown" , meltingPoint=       1900   , mass= 262      ),
    Element(number= 104, symbol= "Rf", name= "Rutherfordium", boilingPoint=   5800    , meltingPoint=       2400   , mass= 261      ),
    Element(number= 105, symbol= "Db", name= "Dubnium"      , boilingPoint= "Unknown" , meltingPoint=   "Unknown"  , mass= 262      ),
    Element(number= 106, symbol= "Sg", name= "Seaborgium"   , boilingPoint= "Unknown" , meltingPoint=   "Unknown"  , mass= 263.1182 ),
    Element(number= 107, symbol= "Bh", name= "Bohrium"      , boilingPoint= "Unknown" , meltingPoint=   "Unknown"  , mass= 264      ),
    Element(number= 108, symbol= "Hs", name= "Hassium"      , boilingPoint= "Unknown" , meltingPoint=   "Unknown"  , mass= 278      ),
    Element(number= 109, symbol= "Mt", name= "Meitnerium"   , boilingPoint= "Unknown" , meltingPoint=   "Unknown"  , mass= 278      ),
    Element(number= 110, symbol= "Ds", name= "Darmstadtium" , boilingPoint= "Unknown" , meltingPoint=   "Unknown"  , mass= 282      ),
    Element(number= 111, symbol= "Rg", name= "Roentgenium"  , boilingPoint= "Unknown" , meltingPoint=   "Unknown"  , mass= 284      ),
    Element(number= 112, symbol= "Cn", name= "Copernicium"  , boilingPoint= "Unknown" , meltingPoint=   "Unknown"  , mass= 288      ),
    Element(number= 113, symbol= "Nh", name= "Nihonium"     , boilingPoint= "Unknown" , meltingPoint=   "Unknown"  , mass= 293      ),
    Element(number= 114, symbol= "Fl", name= "Flerovium"    , boilingPoint= "Unknown" , meltingPoint=   "Unknown"  , mass= 289      ),
    Element(number= 115, symbol= "Mc", name= "Moscovium"    , boilingPoint= "Unknown" , meltingPoint=   "Unknown"  , mass= 299      ),
    Element(number= 116, symbol= "Lv", name= "Livermorium"  , boilingPoint= "Unknown" , meltingPoint=   "Unknown"  , mass= 302      ),
    Element(number= 117, symbol= "Ts", name= "Tennessine"   , boilingPoint=    883    , meltingPoint= "ca. 623-823", mass= 294      ),
    Element(number= 118, symbol= "Og", name= "Oganesson"    , boilingPoint= "Unknown" , meltingPoint=   "Unknown"  , mass= 294      )]
 
        
class STVFormula:
    
    def __init__(self, formula,state, dEnthalpy, dGibbs, dEntropy):
        self.formula = formula
        self.state = state
        self. dEnthalpy = dEnthalpy
        self.dGibbs = dGibbs
        self.dEntropy = dEntropy

STV = [#formula | state | dEnthalpy | dGibbs | dEntropy |
       STVFormula("Ag","s",0,0,42.55),
       STVFormula("Ag","g",284.55,245.65,172.997),
       STVFormula("Ag(NH3)2^+","aq",-111.29,-17.12,245.2),
       STVFormula("Ag(S2O3)2^3-","aq",-1285.7,-1033.65,98.92),
       STVFormula("Ag^+","aq",105.579,77.107,72.68),
       STVFormula("Ag^+","g",1021.73,None,None),
       STVFormula("Ag2CO3","s",-505.8,-436.8,167.4),
       STVFormula("Ag2CrO4","s",-731.74,-641.76,217.6),
       STVFormula("Ag2O","s",-31.05,-11.2,121.3),
       STVFormula("Ag2S","s",-32.59,-40.67,144.01),
       STVFormula("Ag2SO4","s",-715.88,-618.41,200.4),
       STVFormula("Ag3PO4","s",None,-879,None),
       STVFormula("AgBr","s",-100.37,-96.9,107.1),
       STVFormula("AgCl","s",-127.068,-109.789,96.2),
       STVFormula("AgCl2^-","aq",-245.2,-215.4,231.4),
       STVFormula("AgCN","s",146,156.9,107.19),
       STVFormula("AgCNS","s",87.9,101.39,131),
       STVFormula("AgI","s",-61.83,-66.19,115.5),
       STVFormula("AgNO3","s",-124.39,-33.47,140.92),
       STVFormula("Al","s",0,0,28.33),
       STVFormula("Al","g",326.4,285.7,164.54),
       STVFormula("Al(OH)3","s",-1276,None,None),
       STVFormula("Al2O3","s",-1675.7,-1582.3,50.92),
       STVFormula("Al^3+","aq",-531,-485,-321.7),
       STVFormula("Al^3+","g",5483.17,None,None),
       STVFormula("AlCl3","s",-704.2,-628.8,110.67),
       STVFormula("AlCl3","g",-583.2,None,None),
       STVFormula("Ar","g",0,0,154.843),
       STVFormula("As","s",0,0,35.1),
       STVFormula("B","s",0,0,5.86),
       STVFormula("Ba","s",0,0,62.8),
       STVFormula("Ba^2+","aq",-537.64,-560.77,9.6),
       STVFormula("BaC2O4","s",-1368.6,None,None),
       STVFormula("BaCO3","s",-1216.3,-1137.6,112.1),
       STVFormula("BaCrO4","s",-1446,-1345.22,158.6),
       STVFormula("BaF2","s",-1207.1,-1156.8,96.36),
       STVFormula("BaSo4","s",-1473.2,-1362.2,132.2),
       STVFormula("Be","s",0,0,9.5),
       STVFormula("BeO","s",-609.6,-580.3,14.14),
       STVFormula("BF3","g",-1137,-1120.35,254.01),
       STVFormula("Bi","s",0,0,56.74),
       STVFormula("Bi2S3","s",-143.1,-140.6,200.4),
       STVFormula("Bi^3+","aq",None,82.8,None),
       STVFormula("Br^-","aq",-121.55,-103.96,82.4),
       STVFormula("Br","g",111.88,82.429,174.91),
       STVFormula("Br^-","g",-219.07,None,None),
       STVFormula("Br2","g",30.907,3.11,245.463),
       STVFormula("Br2","l",0,0,152.231),
       STVFormula("Br3^-","aq",-130.42,-107.05,215.5),
       STVFormula("BrO3^-","aq",-67.07,18.6,161.71),
       STVFormula("C","s",0,0,5.74),
       #Another C value. Used Graphite
       STVFormula("C","g",716.682,671.257,158.096),
       STVFormula("(Ch3)2O","g",-184.05,-112.59,266.38),
       STVFormula("C2H2","g",226.73,209.2,200.94),
       STVFormula("C2H4","g",52.25,68.12,219.45),
       STVFormula("C2H5OH","g",-235.1,-168.49,282.7),
       STVFormula("C2H5OH","l",-277.69,-174.78,160.7),
       STVFormula("C2H6","g",-84.68,-32.82,229.6),
       STVFormula("C2O4^2-","aq",-825.1,-673.9,45.6),
       STVFormula("C3H6","g",20.2,62.72,266.9),
       STVFormula("C3H8","g",-104.5,-23.4,269.9),
       STVFormula("C4H10","g",-126.5,-17.15,310.1),
       STVFormula("C5H12","g",-146.6,-8.37,348.9),
       STVFormula("C6H12","l",-156.3,26.7,204.4),
       STVFormula("C6H6","g",82.9,129.7,269.2),
       STVFormula("C6H6","l",49.0,124.7,172.0),
       STVFormula("C8H18","g",-208.5,16.40,466.7),
       STVFormula("CH3CHO","l",-192.3,-128.2,160.2),
       STVFormula("CH3Cl","g",-80.83,-57.37,234.58),
       STVFormula("CH3COO^-","aq",-486.01,-369.31,-6.3),
       STVFormula("CH3COOH","aq",-485.76,-396.46,178.7),
       STVFormula("CH3COOH","l",-484.51,-389.9,159.8),
       STVFormula("CH3NH2","aq",-70.17,20.77,123.4),
       STVFormula("CH3NH3^+","aq",-124.93,-39.86,142.7),
       STVFormula("CH3OCH3","g",-184.05,-112.59,266.38),
       STVFormula("CH3OH","g",-200.66,-162.0,239.7),
       STVFormula("CH3OH","l",-238.66,-166.36,126.8),
       STVFormula("CH4","g",-74.81,-50.72,186.264),
       STVFormula("CHCl3","g",-103.14,-70.34,295.71),
       STVFormula("CCl4","l",-135.44,-65.27,216.4),
       STVFormula("CN^-","aq",150.6,172.4,94.1),
       STVFormula("CNS^-","aq",76.44,92.71,144.3),
       STVFormula("CO","g",-110.525,-137.168,197.674),
       STVFormula("CO2","aq",-413.8,-385.98,117.6),
       STVFormula("CO2","g",-393.509,-394.359,213.74),
       STVFormula("CO3^2-",None,-677.14,-527.81,-56.9),
       STVFormula("COCl2","g",-218.8,-204.6,283.53),
       STVFormula("Ca(OH)2","s",-986.09,-898.49,83.39),
       STVFormula("Ca^2+","aq",-542.83,-553.58,-53.1),
       STVFormula("Ca3(PO4)2","s",-4109.9,-3884.7,240.91),
       STVFormula("CaC2O4","s",-1360.6,None,None),
       STVFormula("CaCO3","s",-1207.13,-1127.75,88.7),
       STVFormula("CaF2","s",-1219.6,-1167.3,68.87),
       STVFormula("CaO","s",-635.09,-604.03,39.75),
       STVFormula("CaSO4","s",-1434.11,-1321.79,106.7),
       STVFormula("Cd","s",0,0,51.76),
       STVFormula("Cd(CN)4^2-","aq",428,507.6,322),
       STVFormula("Cd","g",2623.54,None,None),
       STVFormula("Cd(NH3)4^2+","aq",-450.2,-226.1,336.4),
       STVFormula("Cd(OH)2","s",-560.7,-473.6,96),
       STVFormula("Cd^2+","aq",-75.9,-77.612,-73.2),
       STVFormula("Cd^2+","g",112.01,77.41,167.746),
       STVFormula("CdS","s",-161.9,-156.5,64.9),
       STVFormula("Ce","s",0,0,72),
       STVFormula("Ce^3+","aq",-696.2,-672,-205),
       STVFormula("Ce^4+","aq",-537.2,-503.8,-301),
       STVFormula("Cl^-","aq",-167.159,-131.228,56.5),
       STVFormula("Cl","g",121.679,105.68,165.198),
       STVFormula("Cl^-","g",-233.13,None,None),
       STVFormula("Cl2","g",0,0,223.066),
       STVFormula("Cl3^-","aq",None,-120.4,None),
       STVFormula("ClO2","g",102.5,120.5,256.84),
       STVFormula("ClO4^-","aq",-129.33,-8.52,182),
       STVFormula("Co","s",0,0,30.04),
       STVFormula("Co(NH3)6^3+","aq",-584.9,-157,146),
       STVFormula("Co^2+",None,-58.2,-54.4,-113),
       STVFormula("Co^3+",None,92,134,-305),
       STVFormula("Cr2O7^2-","aq",-149.03,-1301.1,261.9),
       STVFormula("CrO4^2-","aq",-881.15,-727.75,50.21),
       STVFormula("Cs","s",0,0,85.23),
       STVFormula("Cu","s",0,0,33.15),
       STVFormula("Cu(CN)3^2-","aq",None,403.8,None),
       STVFormula("Cu(CN)4^3-","aq",None,566.6,None),
       STVFormula("Cu","g",338.32,298.58,166.38),
       STVFormula("Cu(NH3)4^2+","aq",-348.5,-111.07,273.6),
       STVFormula("Cu(OH)2","s",-449.8,None,None),
       STVFormula("Cu^+","aq",71.67,49.98,40.6),
       STVFormula("Cu^2+","aq",64.77,65.49,-99.6),
       STVFormula("Cu2O","s",-168.6,-146,93.14),
       STVFormula("Cu2S","s",-79.5,-86.2,120.9),
       STVFormula("CuC2O4","s",None,-661.8,None),
       STVFormula("CuCO3*Cu(OH)2","s",-1051.4,-893.6,186.2),
       STVFormula("CuO","s",-157.3,-129.7,42.63),
       STVFormula("CuS","s",-53.1,-53.6,66.5),
       STVFormula("F^-","aq",-332.63,-278.79,-13.8),
       STVFormula("F","g",78.99,61.91,158.754),
       STVFormula("F^-","g",-255.39,None,None),
       STVFormula("F2","g",0,0,202.78),
       STVFormula("Fe","s",0,0,27.28),
       STVFormula("Fe(CN)6^3-","aq",561.9,729.4,270.3),
       STVFormula("Fe(CN)6^4-","aq",455.6,695.08,95),
       STVFormula("Fe(SCN)^2+","aq",23.4,71.1,-130),
       STVFormula("Fe","g",416.3,370.7,180.49),
       STVFormula("Fe(OH)3","s",-823,-696.5,106.7),
       STVFormula("Fe2(SO4)3","s",-2581.5,None,None),
       STVFormula("Fe^2+","aq",-89.1,-78.9,-137.7),
       STVFormula("Fe^2+","g",2749.93,None,None),
       STVFormula("Fe2O3","s",-824.2,-742.2,87.4),
       STVFormula("Fe^3+","aq",-48.5,-4.7,-315.9),
       STVFormula("Fe^3+","g",5712.8,None,None),
       STVFormula("Fe3C","s",25.1,20.1,104.6),
       STVFormula("Fe3O4","s",-1118.4,-1015.4,146.4),
       STVFormula("FeCO3","s",-740.57,-666.67,92.9),
       STVFormula("FeO0.9470","s",-266.27,-245.12,57.49),
       STVFormula("FeS","s",-100,-100.4,60.29),
       STVFormula("FeS2","s",-178.2,-166.9,52.93),
       STVFormula("FeSO4","s",-928.4,-820.8,107.5),
       STVFormula("Ga","s",0,0,40.88),
       STVFormula("Ge","s",0,0,31.09),
       STVFormula("H","g",217.965,203.247,114.713),
       STVFormula("H^+","aq",0,0,0),
       STVFormula("H^+","g",1536.202,None,None),
       STVFormula("H2","aq",-4.2,17.6,57.7),
       STVFormula("H2","g",0,0,130.684),
       STVFormula("H2O","g",-241.818,-228.572,188.825),
       STVFormula("H2O","l",-285.83,-237.129,69.91),
       STVFormula("H2O2","aq",-191.17,-134.03,143.9),
       STVFormula("H2O2","g",-136.31,-105.57,232.7),
       STVFormula("H2O2","l",-187.78,-120.35,109.6),
       STVFormula("H2S","g",-20.63,-33.56,205.79),
       STVFormula("H2SO3","aq",-608.81,-537.81,232.2),
       STVFormula("H2SO4","l",-813.989,-690.003,156.904),
       STVFormula("H3AsO3","aq",-742.2,-639.8,195),
       STVFormula("H3AsO4","aq",-902.5,-766,184),
       STVFormula("HBr","g",-36.4,-53.45,198.695),
       STVFormula("HCl","g",-92.307,-95.299,186.908),
       STVFormula("HCN","g",135.1,124.7,201.78),
       STVFormula("He","aq",-1.7,19.7,54.4),
       STVFormula("He","g",0,0,126.15),
       STVFormula("HF","g",-271.1,-273.2,173.779),
       STVFormula("HI","g",26.48,1.7,206.594),
       STVFormula("HNO2","aq",-119.2,-50.6,135.6),
       STVFormula("HS^-","aq",-17.6,12.08,62.8),
       STVFormula("Hg(CN)4^2-","aq",526.3,618.5,305),
       STVFormula("Hg(CNS)4^2-","aq",326.4,411.4,456),
       STVFormula("Hg","l",0,0,76.02),
       STVFormula("Hg^2+","aq",171.1,164.4,-32.2),
       STVFormula("Hg2^2+","aq",172.4,153.52,84.5),
       STVFormula("Hg2Br2","s",-206.9,-181.075,218),
       STVFormula("Hg2Cl2","s",-265.22,-210.745,192.5),
       STVFormula("Hg2SO4","s",-743.12,-625.815,200.66),
       STVFormula("HgCl2","s",-224.3,-178.6,146),
       STVFormula("HgCl4^2-","aq",-554,-446.8,293),
       STVFormula("HgI4^2-","aq",-235.1,-211.7,360),
       STVFormula("HgS","s",-53.6,-47.7,88.3),
       #Two HgS values, used black. Red available
       STVFormula("I^-","aq",-55.19,-51.57,111.3),
       STVFormula("I","g",106.838,70.25,180.791),
       STVFormula("I^-","g",-197,None,None),
       STVFormula("I2","aq",22.6,16.4,137.2),
       STVFormula("I2","s",0,0,116.135),
       STVFormula("I2","g",62.438,19.327,260.69),
       STVFormula("I3^-","aq",-51.5,-51.4,239.3),
       STVFormula("ICl","g",17.78,-5.46,247.551),
       STVFormula("IO^3-","aq",-221.3,-128,118.4),
       STVFormula("In","s",0,0,57.82),
       STVFormula("Ir","s",0,0,35.48),
       STVFormula("K","s",0,0,64.18),
       STVFormula("K","g",89.24,60.59,160.336),
       STVFormula("K^+","aq",-252.38,-283.27,102.5),
       STVFormula("K^+","g",514.26,None,None),
       STVFormula("K2O2","s",-494.1,-425.1,102.1),
       STVFormula("KBr","s",-393.798,-380.66,95.9),
       STVFormula("KCl","s",-436.747,-409.14,82.59),
       STVFormula("KClO4","s",-432.75,-303.09,151),
       STVFormula("KF","s",-567.27,-537.75,66.57),
       STVFormula("KI","s",-327.9,-324.892,106.32),
       STVFormula("KNO3","s",-494.63,-394.86,133.05),
       STVFormula("KO2","s",-284.93,-239.4,116.7),
       STVFormula("KOH","s",-424.764,-379.08,78.7),
       STVFormula("Kr","g",0,0,164.082),
       STVFormula("Mg","s",0,0,32.68),
       STVFormula("Mg(OH)2","s",-924.54,-833.51,63.18),
       STVFormula("Mg^2+","aq",-466.85,-454.8,-138.1),
       STVFormula("Mg^2+","g",2348.504,None,None),
       STVFormula("MgCO3","s",-1095.8,-1012.1,65.7),
       STVFormula("MgF2","s",-1123.4,-1070.2,57.24),
       STVFormula("MgO","s",-601.7,-569.43,26.94),
       STVFormula("Mn","s",0,0,32.01),
       STVFormula("Mn^2+","aq",-220.75,-228.1,-73.6),
       STVFormula("MnO2","s",-520.03,-465.14,53.05),
       STVFormula("MnO4^-","aq",-541.4,-447.2,191.2),
       STVFormula("MnS","s",-214.2,-218.4,78.2),
       STVFormula("Mo","s",0,0,28.66),
       STVFormula("Na","s",0,0,51.21),
       STVFormula("Na","g",107.32,76.761,153.712),
       STVFormula("Na^+","aq",-240.12,-261.905,59),
       STVFormula("Na^+","g",609.358,None,None),
       STVFormula("Na2CO3","s",-1130.68,-1044.44,134.98),
       STVFormula("Na2O","s",-414.22,-375.46,75.06),
       STVFormula("NaOH","s",-425.6, None, None),
       STVFormula("NaBr","s",-361.062,-348.983,86.82),
       STVFormula("NaCl","s",-411.153,-384.138,72.13),
       STVFormula("NaF","s",-573.647,-543.494,51.46),
       STVFormula("NaI","s",-287.78,-286.06,98.53),
       STVFormula("NaNO2","s",-358.65,-284.55,103.8),
       STVFormula("NaNO3","s",-467.85,-367,116.52),
       STVFormula("Ne","g",0,0,146.328),
       STVFormula("N","g",472.704,455.563,153.298),
       STVFormula("N2","g",0,0,191.61),
       STVFormula("N2O","g",82.05,104.2,219.85),
       STVFormula("N2O4","g",9.16,97.89,304.29),
       STVFormula("N2O4","l",-19.5,97.54,209.2),
       STVFormula("N2O5","s",-43.1,113.9,178.2),
       STVFormula("N2O5","g",11.3,115.1,355.7),
       STVFormula("NH3","aq",-80.29,-26.5,111.3),
       STVFormula("NH3","g",-46.11,-16.45,192.45),
       STVFormula("NH4^+","aq",-132.51,-79.31,113.4),
       STVFormula("NH4Cl","s",-314.43,-202.87,94.6),
       STVFormula("NO","g",90.25,86.55,210.761),
       STVFormula("NO2","g",33.18,51.31,240.06),
       STVFormula("NO3^-","aq",-205,-108.74,146.4),
       STVFormula("NOBr","g",82.17,82.42,273.66),
       STVFormula("NOCl","g",51.71,66.08,261.69),
       STVFormula("Ni","s",0,0,29.87),
       STVFormula("Ni(CN)4^2-","aq",367.8,472.1,218),
       STVFormula("Ni(NH3)4^2+","aq",-438.9,None,258.6),
       STVFormula("Ni(NH3)6^2+","aq",-630.1,-255.7,394.6),
       STVFormula("Ni^2+","aq",-54,-45.6,-128.9),
       STVFormula("NiS","s",-82,-79.5,52.97),
       STVFormula("O","g",249.17,231.731,161.055),
       STVFormula("O2","aq",-11.7,16.4,110.9),
       STVFormula("O2","g",0,0,205.138),
       STVFormula("O3","g",142.7,163.2,238.93),
       STVFormula("OH^-","aq",-229.994,-157.244,-10.75),
       STVFormula("Os","s",0,0,32.6),
       STVFormula("P","s",0,0,41.09),
       STVFormula("P","g",314.64,278.25,163.193),
       STVFormula("PCl3","g",-287,-267.8,311.78),
       STVFormula("PCl5","g",-374.9,-305,364.58),
       STVFormula("PH3","g",5.4,13.4,210.23),
       STVFormula("PO4^3-","aq",-1277.4,-1018.7,-222),
       STVFormula("Pa","s",0,0,51.9),
       STVFormula("Pb","s",0,0,64.81),
       STVFormula("Pb","g",195,161.9,175.373),
       STVFormula("Pb(OH)2","s",None,-452.2,None),
       STVFormula("Pb(OH)3^-","aq",None,-575.6,None),
       STVFormula("Pb^2+","aq",-1.7,-24.43,10.5),
       STVFormula("Pb3O4","s",-718.4,-601.2,211.3),
       STVFormula("PbBr2","s",-278.9,-261.92,161.5),
       STVFormula("PbCl2","s",-359.41,-314.1,-136),
       STVFormula("PbO","s",-218.99,-189.93,66.5),
       #There is another PbO. Value over is red
       STVFormula("PbO2","s",-277.4,-217.33,68.6),
       STVFormula("PbS","s",-100.4,-98.7,91.2),
       STVFormula("PbSO4","s",-919.94,-813.14,148.57),
       STVFormula("Pd","s",0,0,37.57),
       STVFormula("Pt","s",0,0,41.63),
       STVFormula("Ra","s",0,0,71),
       STVFormula("Rb","s",0,0,76.78),
       STVFormula("Re","s",0,0,36.86),
       STVFormula("Rh","s",0,0,31.51),
       STVFormula("Rn","g",0,0,176.21),
       STVFormula("Ru","s",0,0,28.53),
       STVFormula("S","s",0,0,31.8),
       #Monoclinic is available for S, but value over is rhombic
       STVFormula("S","g",278.805,238.25,167.821),
       STVFormula("S^2-","aq",33.1,85.8,-14.6),
       STVFormula("SCN^-","aq",76.44,92.71,144.3),
       STVFormula("S2O3^2-","aq",-648.5,-522.5,67),
       STVFormula("S4O6^2-","aq",-1224.2,-1040.4,257.3),
       STVFormula("SO2","g",-296.83,-300.194,248.22),
       STVFormula("SO2Cl2","g",-364,-320,311.94),
       STVFormula("SO3","g",-395.72,-371.06,256.76),
       STVFormula("SO3","l",-441.04,-373.75,113.8),
       STVFormula("SO4^2-","aq",-909.27,-744.53,20.1),
       STVFormula("SF6","g",-1209,-1105.3,291.82),
       STVFormula("Sb","s",0,0,45.69),
       STVFormula("Sc","s",0,0,34.64),
       STVFormula("Se","s",0,0,42.442),
       STVFormula("Si","s",0,0,18.83),
       STVFormula("SiO2","s",-910.94,-856.64,41.84 ),
       STVFormula("Sn","s",0,0,51.55 ),
       #Value available for Sn. Used grey, quartz not used
       STVFormula("Sn^2+","aq",-8.8,-27.2,-17),
       STVFormula("Sn^4+","aq",30.5,2.5,-117),
       STVFormula("SnO","s",-285.8,-256.9,56.5),
       STVFormula("SnO2","s",-580.7,-519.6,52.3),
       STVFormula("SnS","s",-100,-98.3,77),
       STVFormula("Sr","s",0,0,52.3),
       STVFormula("Sr^2+","aq",-545.8,-559.48,-32.6),
       STVFormula("Ta","s",0,0,41.51 ),
       STVFormula("Tc","s",0,0,None),
       STVFormula("Te","s",0,0,49.71 ),
       STVFormula("Th","s",0,0,53.39),
       STVFormula("ThO2","s",-1226.4,-1168.77,65.23),
       STVFormula("Ti","s",0,0,30.63),
       STVFormula("Tl","s",0,0,64.18),
       STVFormula("Tl^+","aq",5.36,-32.4,125.5),
       STVFormula("Tl^+","g",777.764,None,None),
       STVFormula("Tl^3+","aq",196.6,214.6,-192),
       STVFormula("Tl^3+","g",5639.2,None,None),
       STVFormula("U","s",0,0,50.21),
       STVFormula("U^4+","aq",-591.2,-531,-410),
       STVFormula("UO2","s",-1084.9,-1031.7,77.08),
       STVFormula("UO2^2+","aq",-1019.6,-953.5,-97.5),
       STVFormula("V","s",0,0,28.91),
       STVFormula("VO^2+","aq",-486.6,-446.4,-133.9 ),
       STVFormula("VO2^+","aq",-649.8,-587,-42.3),
       STVFormula("W","s",0,0,32.64),
       STVFormula("WO2","s",-589.69,-533.89,50.54),
       STVFormula("WO3","s",-842.87,-764.03,75.9),
       STVFormula("Xe","g",0,0,169.683),
       STVFormula("Zn","s",0,0,41.63),
       STVFormula("Zn(CN)4^2+","aq",342.3,446.9,226),
       STVFormula("Zn(NH3)4^2+","aq",-533.5,-301.9,301),
       STVFormula("Zn(OH)4^2-","aq",None,-858.52,None),
       STVFormula("Zn^2+","aq",-153.89,-147.06,-112.1),
       STVFormula("Zn^2+","g",2782.78,None,None),
       STVFormula("ZnO","s",-348.28,-318.3,43.64),
       STVFormula("ZnS","s",-205.98,-201.29,57.7),
       #Another is available for ZnS. Used sphalerite over
       STVFormula("Zr","s",0,0,53.39 ),
       
       ]
