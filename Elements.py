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
        
elements = [ # Number  | Symbol      | Element name         | Boiling point 1 atm (°K)| Melting point in 1 atm (°K)| mass (u)
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
    Element(number=  50, symbol= "Sn", name= "Tin"          , boilingPoint=   2876    , meltingPoint=        505.12, mass= 114.82   ),
    Element(number=  51, symbol= "Sb", name= "Antimony"     , boilingPoint=   1860    , meltingPoint=        903.91, mass= 118.71   ),
    Element(number=  52, symbol= "Te", name= "Tellurium"    , boilingPoint=   1261    , meltingPoint=        722.72, mass= 121.757  ),
    Element(number=  53, symbol= "I" , name= "Iodine"       , boilingPoint=    457.5  , meltingPoint=        386.7 , mass= 127.6    ),
    Element(number=  54, symbol= "Xe", name= "Xenon"        , boilingPoint=    165.1  , meltingPoint=        161.39, mass= 126.9045 ),
    Element(number=  55, symbol= "Cs", name= "Caesium"      , boilingPoint=    944    , meltingPoint=        301.54, mass= 131.29   ),
    Element(number=  56, symbol= "Ba", name= "Barium"       , boilingPoint=   2078    , meltingPoint=       1002   , mass= 132.9054 ),
    Element(number=  57, symbol= "La", name= "Lanthanum"    , boilingPoint=   3737    , meltingPoint=       1191   , mass= 137.33   ),
    Element(number=  58, symbol= "Ce", name= "Cerium"       , boilingPoint=   3715    , meltingPoint=       1071   , mass= 138.9055 ),
    Element(number=  59, symbol= "Pr", name= "Praseodymium" , boilingPoint=   3785    , meltingPoint=       1204   , mass= 140.12   ),
    Element(number=  60, symbol= "Nd", name= "Neodymium"    , boilingPoint=   3347    , meltingPoint=       1294   , mass= 140.9077 ),
    Element(number=  61, symbol= "Pm", name= "Promethium"   , boilingPoint=   3273    , meltingPoint=       1315   , mass= 144.24   ),
    Element(number=  62, symbol= "Sm", name= "Samarium"     , boilingPoint=   2067    , meltingPoint=       1347   , mass= 145      ),
    Element(number=  63, symbol= "Eu", name= "Europium"     , boilingPoint=   1800    , meltingPoint=       1095   , mass= 150.36   ),
    Element(number=  64, symbol= "Gd", name= "Gadolinium"   , boilingPoint=   3545    , meltingPoint=       1585   , mass= 151.965  ),
    Element(number=  65, symbol= "Tb", name= "Terbium"      , boilingPoint=   3500    , meltingPoint=       1629   , mass= 157.25   ),
    Element(number=  66, symbol= "Dy", name= "Dysprosium"   , boilingPoint=   2840    , meltingPoint=       1685   , mass= 158.9253 ),
    Element(number=  67, symbol= "Ho", name= "Holmium"      , boilingPoint=   2968    , meltingPoint=       1747   , mass= 162.5    ),
    Element(number=  68, symbol= "Er", name= "Erbium"       , boilingPoint=   3140    , meltingPoint=       1802   , mass= 164.9303 ),
    Element(number=  69, symbol= "Tm", name= "Thulium"      , boilingPoint=   2223    , meltingPoint=       1818   , mass= 167.26   ),
    Element(number=  70, symbol= "Yb", name= "Ytterbium"    , boilingPoint=   1469    , meltingPoint=       1092   , mass= 168.9342 ),
    Element(number=  71, symbol= "Lu", name= "Lutetium"     , boilingPoint=   3668    , meltingPoint=       1936   , mass= 173.04   ),
    Element(number=  72, symbol= "Hf", name= "Hafnium"      , boilingPoint=   4875    , meltingPoint=       2504   , mass= 174.967  ),
    Element(number=  73, symbol= "Ta", name= "Tantalum"     , boilingPoint=   5730    , meltingPoint=       3293   , mass= 178.49   ),
    Element(number=  74, symbol= "W" , name= "Tungsten"     , boilingPoint=   5825    , meltingPoint=       3695   , mass= 180.9479 ),
    Element(number=  75, symbol= "Re", name= "Rhenium"      , boilingPoint=   5870    , meltingPoint=       3455   , mass= 183.85   ),
    Element(number=  76, symbol= "Os", name= "Osmium"       , boilingPoint=   5300    , meltingPoint=       3300   , mass= 186.207  ),
    Element(number=  77, symbol= "Ir", name= "Iridium"      , boilingPoint=   4700    , meltingPoint=       2720   , mass= 190.2    ),
    Element(number=  78, symbol= "Pt", name= "Platinum"     , boilingPoint=   4100    , meltingPoint=       2042.1 , mass= 192.22   ),
    Element(number=  79, symbol= "Au", name= "Gold"         , boilingPoint=   3130    , meltingPoint=       1337.58, mass= 195.08   ),
    Element(number=  80, symbol= "Hg", name= "Mercury"      , boilingPoint=    629.88 , meltingPoint=        234.31, mass= 196.9665 ),
    Element(number=  81, symbol= "Tl", name= "Thallium"     , boilingPoint=   1746    , meltingPoint=        577   , mass= 200.59   ),
    Element(number=  82, symbol= "Pb", name= "Lead"         , boilingPoint=   2023    , meltingPoint=        600.65, mass= 204.383  ),
    Element(number=  83, symbol= "Bi", name= "Bismuth"      , boilingPoint=   1837    , meltingPoint=        544.59, mass= 207.2    ),
    Element(number=  84, symbol= "Po", name= "Polonium"     , boilingPoint=   1235    , meltingPoint=        527.7 , mass= 208.9804 ),
    Element(number=  85, symbol= "At", name= "Astatine"     , boilingPoint=    610    , meltingPoint=        575   , mass= 209      ),
    Element(number=  86, symbol= "Rn", name= "Radon"        , boilingPoint=    211.4  , meltingPoint=        202   , mass= 210      ),
    Element(number=  87, symbol= "Fr", name= "Francium"     , boilingPoint=    950    , meltingPoint=        300   , mass= 222      ),
    Element(number=  88, symbol= "Ra", name= "Radium"       , boilingPoint=   1413    , meltingPoint=        973   , mass= 223      ),
    Element(number=  89, symbol= "Ac", name= "Actinium"     , boilingPoint=   3470    , meltingPoint=       1323   , mass= 226.0254 ),
    Element(number=  90, symbol= "Th", name= "Thorium"      , boilingPoint=   5060    , meltingPoint=       2028   , mass= 227      ),
    Element(number=  91, symbol= "Pa", name= "Protactinium" , boilingPoint=   4300    , meltingPoint=       1845   , mass= 232.0381 ),
    Element(number=  92, symbol= "U" , name= "Uranium"      , boilingPoint=   4407    , meltingPoint=       1408   , mass= 231.0359 ),
    Element(number=  93, symbol= "Np", name= "Neptunium"    , boilingPoint=   4175    , meltingPoint=        912   , mass= 238.029  ),
    Element(number=  94, symbol= "Pu", name= "Plutonium"    , boilingPoint=   3505    , meltingPoint=        913   , mass= 237.0482 ),
    Element(number=  95, symbol= "Am", name= "Americium"    , boilingPoint=   2880    , meltingPoint=       1449   , mass= 244      ),
    Element(number=  96, symbol= "Cm", name= "Curium"       , boilingPoint=   3383    , meltingPoint=       1618   , mass= 243      ),
    Element(number=  97, symbol= "Bk", name= "Berkelium"    , boilingPoint=   2900    , meltingPoint=       1259   , mass= 247      ),
    Element(number=  98, symbol= "Cf", name= "Californium"  , boilingPoint=   1745    , meltingPoint=       1173   , mass= 247      ),
    Element(number=  99, symbol= "Es", name= "Einsteinium"  , boilingPoint=   1269    , meltingPoint=       1133   , mass= 251      ),
    Element(number= 100, symbol= "Fm", name= "Fermium"      , boilingPoint= "Unknown" , meltingPoint=       1800   , mass= 252      ),
    Element(number= 101, symbol= "Md", name= "Mendelevium"  , boilingPoint= "Unknown" , meltingPoint=       1100   , mass= 257      ),
    Element(number= 102, symbol= "No", name= "Nobelium"     , boilingPoint= "Unknown" , meltingPoint=       1100   , mass= 258      ),
    Element(number= 103, symbol= "Lr", name= "Lawrencium"   , boilingPoint= "Unknown" , meltingPoint=       1900   , mass= 259      ),
    Element(number= 104, symbol= "Rf", name= "Rutherfordium", boilingPoint=   5800    , meltingPoint=       2400   , mass= 262      ),
    Element(number= 105, symbol= "Db", name= "Dubnium"      , boilingPoint= "Unknown" , meltingPoint= "Unknown"    , mass= 261      ),
    Element(number= 106, symbol= "Sg", name= "Seaborgium"   , boilingPoint= "Unknown" , meltingPoint= "Unknown"    , mass= 262      ),
    Element(number= 107, symbol= "Bh", name= "Bohrium"      , boilingPoint= "Unknown" , meltingPoint= "Unknown"    , mass= 263.1182 ),
    Element(number= 108, symbol= "Hs", name= "Hassium"      , boilingPoint= "Unknown" , meltingPoint= "Unknown"    , mass= 264      ),
    Element(number= 109, symbol= "Mt", name= "Meitnerium"   , boilingPoint= "Unknown" , meltingPoint= "Unknown"    , mass= 278      ),
    Element(number= 110, symbol= "Ds", name= "Darmstadtium" , boilingPoint= "Unknown" , meltingPoint= "Unknown"    , mass= 278      ),
    Element(number= 111, symbol= "Rg", name= "Roentgenium"  , boilingPoint= "Unknown" , meltingPoint= "Unknown"    , mass= 282      ),
    Element(number= 112, symbol= "Cn", name= "Copernicium"  , boilingPoint= "Unknown" , meltingPoint= "Unknown"    , mass= 284      ),
    Element(number= 113, symbol= "Nh", name= "Nihonium"     , boilingPoint= "Unknown" , meltingPoint= "Unknown"    , mass= 288      ),
    Element(number= 114, symbol= "Fl", name= "Flerovium"    , boilingPoint= "Unknown" , meltingPoint= "Unknown"    , mass= 293      ),
    Element(number= 115, symbol= "Mc", name= "Moscovium"    , boilingPoint= "Unknown" , meltingPoint= "Unknown"    , mass= 289      ),
    Element(number= 116, symbol= "Lv", name= "Livermorium"  , boilingPoint= "Unknown" , meltingPoint= "Unknown"    , mass= 299      ),
    Element(number= 117, symbol= "Ts", name= "Tennessine"   , boilingPoint=    883    , meltingPoint= "ca. 623-823", mass= 302      ),
    Element(number= 118, symbol= "Og", name= "Oganesson"    , boilingPoint= "Unknown" , meltingPoint= "Unknown"    , mass= 294      )] 

        
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
       STVFormula("C","g",716.682,671.257,158.096),
       STVFormula("(Ch3)2O","g",-184.05,-112.59,266.38),
       STVFormula("C2H2","g",226.73,209.2,200.94),
       STVFormula("C2H4","g",,,),
       STVFormula("C2H5OH","g",,,),
       STVFormula("C2H5OH","l",,,),
       STVFormula("C2H6","g",,,),
       STVFormula("C2O4^2-","aq",,,),
       STVFormula("C3H6","g",,,),
       STVFormula("C3H8","g",,,),
       STVFormula("C4H10","g",,,),
       STVFormula("C5H12","g",,,),
       STVFormula("C6H12","l",,,),
       STVFormula("C6H6","g",,,),
       STVFormula("C6H6","l",,,),
       STVFormula("C8H18","g",,,),
       STVFormula("CH3CHO","l",,,),
       STVFormula("CH3Cl","g",,,),
       STVFormula("CH3COO^-","aq",,,),
       STVFormula("CH3COOH","aq",,,),
       STVFormula("CH3COOH","l",,,),
       STVFormula("CH3NH2","aq",,,),
       STVFormula("CH3NH3^+","aq",,,),
       STVFormula("CH3OCH3","g",,,),
       STVFormula("CH3OH","g",,,),
       STVFormula("CH3OH","l",,,),
       STVFormula("CH4","g",,,),
       STVFormula("CHCl3","g",,,),
       STVFormula("CCl4","l",,,),
       STVFormula("CN^-","aq",,,),
       STVFormula("CNS^-","aq",,,),
       STVFormula("CO","g",,,),
       STVFormula("CO2","aq",,,),
       STVFormula("CO2","g",,,),
       STVFormula("CO3^2-",None,,,),
       STVFormula("COCl2","g",,,),
       STVFormula("Ca(OH)2","s",,,),
       STVFormula("Ca^2+","aq",,,),
       STVFormula("Ca3(PO4)2","s",,,),
       STVFormula("CaC2O4","s",,,),
       STVFormula("CaCO3","s",,,),
       STVFormula("CaF2","s",,,),
       STVFormula("CaO","s",,,),
       STVFormula("CaSO4","s",,,),
       STVFormula("Cd","s",,,),
       STVFormula("Cd(CN)4^2-","aq",,,),
       STVFormula("Cd","g",,,),
       STVFormula("Cd(NH3)4^2+","aq",,,),
       STVFormula("Cd(OH)2","s",,,),
       STVFormula("Cd^2+","aq",,,),
       STVFormula("Cd^2+","g",,,),
       STVFormula("CdS","s",,,),
       STVFormula("Ce","s",,,),
       STVFormula("Ce^3+","aq",,,),
       STVFormula("Ce^4+","aq",,,),
       STVFormula("Cl^-","aq",,,),
       STVFormula("Cl","g",,,),
       STVFormula("Cl^-","g",,,),
       STVFormula("Cl2","g",,,),
       STVFormula("Cl3^-","aq",,,),
       STVFormula("ClO2","g",,,),
       STVFormula("ClO4^-","aq",,,),
       STVFormula("Co","s",,,),
       STVFormula("Co(NH3)6^3+","aq",,,),
       STVFormula("Co^2+",None,,,),
       STVFormula("Co^3+",None,,,),
       STVFormula("Cr2O7^2-","aq",,,),
       
       ]