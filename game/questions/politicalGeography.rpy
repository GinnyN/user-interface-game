label politicalGeography:
    papyrus "THERE'S SOMETHING YOU WANT TO KNOW?"
    gaster "OH!"
    gaster "WELL..."
    gaster "I'M QUITE CONFUSED ABOUT THE CURRENT..."
    gaster "MAKE UP OF THE KINGDOM..."
    gaster "I HAVEN'T SEEN ANYTHING BEYOND THE SUNRISE WHEN THE MONSTERS GOT OUT..."
    papyrus "OH, OK!"
    papyrus "THIS IS MOUNT EBOTT"
    papyrus "BEYOND THE MOUNTAIN THERE'S A HUMAN CITY"
    papyrus "AND APARENTLY THEIR... MAYOR WAS THE OWNER OF THE LAND..."
    papyrus "AND THEN KING FLUFFYBUNS BROUGHT THE LAND FROM THEM"
    papyrus "WITH THE GOLD OF THE KINGDOM"
    papyrus "SO NOW WE LIVE IN THE NEW KINGDOM OF MONSTERS"
    gaster "LET ME GUESS"
    gaster "THAT'S EXACTLY THE NAME OF THE KINGDOM"
    papyrus "YESS???"
    gaster "I REALLY DON'T KNOW IF THAT'S GOOD OR BAD ABOUT THE KING TO BE HONEST"
    if politicalGeography == 0:
        $ politicalGeography = politicalGeography + 1
    return 

label politicalGeography2:
    gaster "CAN YOU CONTINUE TELLING ME ABOUT THE KINGDOM?"
    papyrus "OH, SURE"
    papyrus "SOME MONSTERS DECIDED TO GO AND TRAVEL AROUND THE WORLD"
    papyrus "OTHER DECIDED TO STAY HERE NEAR MOUNT EBOTT"
    papyrus "WE GOT ORGANIZATED ALMOST THE SAME WAY AS IN THE UNDERGROUND"
    papyrus "BECAUSE I GUESS WE HATE VARIETY"
    gaster "MAYBE BEEN BAD ON NAMES IS A MONSTER THING AND WE'RE JUST AWFUL TEASING THE KING ABOUT IT"
    papyrus "..."
    gaster "I'M MESSING WITH YOU"
    papyrus "OH!"
    papyrus "WELL"
    papyrus "TO THE OTHER SIDE OF THIS MOUNTAIN THERE'S THE SEA, AND A WATERFALL"
    papyrus "SO THERE IS THE BEACH WATERFALL"
    papyrus "AT THE TOP OF THE MOUNTAIN THERE'S SNOW AND IT'S QUITE CHILLY"
    papyrus "THEN THERE IS HIGHER SNOWDIN"
    papyrus "BUT IT'S SO HIGH WE BUILD AN ELEVATOR TO GET THERE..."
    papyrus "SO THERE IS LOWER SNOWDIN"
    papyrus "THEN IS HOTLAND..."
    papyrus "WHICH IS STILL IN THE UNDERGROUND BECAUSE WE STILL USING THE CORE..."
    gaster "THAT MAKE ME ODDLY PROUD..."
    papyrus "AND THEN THERE'S THE CAPITAL..."
    gaster "DO NOT TELL ME IS CALLED 'NEWER HOME'"
    papyrus "..."
    papyrus "THEN I WILL NOT TELL YOU"
    gaster "AHHH... YOUR MAJESTY..."
    gaster "I TOLD YOU SEVERAL TIMES: ASK THE QUEEN"
    gaster "AND NOW YOU CAN'T..."
    if politicalGeography == 1:
        $ politicalGeography = politicalGeography + 1
    return 

label geoSnowdin:
    gaster "THOSE FURRY MONSTERS REALLY LIKE THE COLD, DO THEY?"
    papyrus "SOME OF THEM"
    papyrus "IT'S WAY BETTER THAN A TON OF LAVA ANYHOW"
    gaster "BUT WITH TEMPERATE FORESTS FINALLY AT OUR DISPOSAL"
    papyrus "YES, SOME OF THEM REALLY LIKE THE COLD"
    papyrus "GOT USED TO IT I GUESS"
    gaster "BUT HIGHER SNOWDIN IS REALLY UP THERE"
    papyrus "WE MADE AN ELEVATOR"
    papyrus "WE MADE ELEVATORS FOR EVERYTHING!"
    gaster "I GUESS I JUST DON'T GET IT"
    papyrus "YOU DON'T HAVE TO"
    gaster "POINT TAKEN"
    gaster "WHO WORKS ON THOSE ELEVATORS ANYWAY?"
    gaster "I DO REMEMBER LEAVING AN AUTOMATED SYSTEM BUT MY DOCUMENTATION DID NOT SURVIVE ME BEEN FORGOTTEN I BELIEVE"
    papyrus "DR. ALPHYS KIND OF LOOKED AFTER THAT IN THE UNDERGROUND"
    papyrus "BUT SINCE SHE WAS BARREN OF DOING SCIENCE FOR THE TIME BEING"
    papyrus "FRISK AND I NOMINATED SANS"
    papyrus "AND OF COURSE THE KING SAID YES"
    gaster "WHY DID HE?"
    papyrus "OH!"
    papyrus "THAT'S EASY"
    papyrus "IT'S A MYSTERY"
    gaster "OHHHH"
    gaster "A MYSTERY!"
    if politicalGeography == 2:
        $ politicalGeography = politicalGeography + 1
    return

label aMystery:
    papyrus "DO YOU KNOW ABOUT THE MYSTERY?"
    gaster "YES, YES, I DO KNOW ABOUT THE MYSTERY"
    gaster "WE SHOULDN'T BE TALKING ABOUT THAT AND YOU KNOW IT"
    papyrus "YES, THAT'S RIGHT, I'M SORRY"
    return
