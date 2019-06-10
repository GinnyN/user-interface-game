label politicalGeography:
    show papyrusImg neutral
    papyrus "THERE'S SOMETHING YOU WANT TO KNOW?"
    show gaster trapped oh flip
    gaster "OH!"
    gaster "WELL..."
    show gaster trapped dissapointed flip
    gaster "I'M QUITE CONFUSED ABOUT THE CURRENT..."
    gaster "MAKE UP OF THE KINGDOM..."
    show gaster trapped dissapointed
    gaster "I HAVEN'T SEEN ANYTHING BEYOND THE SUNRISE WHEN THE MONSTERS GOT OUT..."
    show gaster trapped dissapointed flip
    show papyrusImg delight
    papyrus "OH, OK!"
    show papyrusImg explainingPointing
    show gaster trapped neutral flip
    papyrus "THIS IS MOUNT EBOTT"
    papyrus "BEYOND THE MOUNTAIN THERE'S A HUMAN CITY"
    show papyrusImg confused
    papyrus "AND APARENTLY THEIR... MAYOR WAS THE OWNER OF THE LAND..."
    show papyrusImg neutral
    papyrus "AND THEN KING FLUFFYBUNS BROUGHT THE LAND FROM THEM"
    papyrus "WITH THE GOLD OF THE KINGDOM"
    show papyrusImg delight
    papyrus "SO NOW WE LIVE IN THE NEW KINGDOM OF MONSTERS"
    show gaster trapped neutral flip
    gaster "LET ME GUESS"
    gaster "THAT'S EXACTLY THE NAME OF THE KINGDOM"
    show papyrusImg uhh
    papyrus "YESS???"
    show gaster trapped dissapointed flip
    gaster "I REALLY DON'T KNOW IF THAT'S GOOD OR BAD ABOUT THE KING TO BE HONEST"
    if politicalGeography == 0:
        $ politicalGeography = politicalGeography + 1
    return 

label politicalGeography2:
    show gaster trapped neutral flip
    gaster "CAN YOU CONTINUE TELLING ME ABOUT THE KINGDOM?"
    show papyrusImg delight
    papyrus "OH, SURE"
    show papyrusImg neutral
    papyrus "SOME MONSTERS DECIDED TO GO AND TRAVEL AROUND THE WORLD"
    papyrus "OTHER DECIDED TO STAY HERE NEAR MOUNT EBOTT"
    papyrus "WE GOT ORGANIZATED ALMOST THE SAME WAY AS IN THE UNDERGROUND"
    show papyrusImg dissapointed
    papyrus "BECAUSE I GUESS WE HATE VARIETY"
    show gaster trapped maybe flip
    gaster "MAYBE BEEN BAD ON NAMES IS A MONSTER THING AND WE'RE JUST AWFUL TEASING THE KING ABOUT IT"
    show papyrusImg uhh
    papyrus "..."
    show gaster trapped dissapointed flip
    gaster "I'M MESSING WITH YOU"
    show papyrusImg delight
    papyrus "OH!"
    show papyrusImg neutral
    papyrus "WELL"
    show papyrusImg explainingPointing
    papyrus "TO THE OTHER SIDE OF THIS MOUNTAIN THERE'S THE SEA, AND A WATERFALL"
    papyrus "SO THERE IS THE BEACH WATERFALL"
    show papyrusImg explainingPointing flip
    papyrus "AT THE TOP OF THE MOUNTAIN THERE'S SNOW AND IT'S QUITE CHILLY"
    papyrus "THEN THERE IS HIGHER SNOWDIN"
    show papyrusImg neutral
    papyrus "BUT IT'S SO HIGH WE BUILD AN ELEVATOR TO GET THERE..."
    papyrus "SO THERE IS LOWER SNOWDIN"
    papyrus "THEN IS HOTLAND..."
    show papyrusImg dissapointed
    papyrus "WHICH IS STILL IN THE UNDERGROUND BECAUSE WE STILL USING THE CORE..."
    show gaster trapped proud flip
    gaster "THAT MAKE ME ODDLY PROUD..."
    show papyrusImg neutral
    papyrus "AND THEN THERE'S THE CAPITAL..."
    show gaster trapped neutral flip
    gaster "DO NOT TELL ME IS CALLED 'NEWER HOME'"
    show papyrusImg uhh
    papyrus "..."
    show papyrusImg neutral
    papyrus "THEN I WILL NOT TELL YOU"
    show gaster trapped dissapointed flip
    gaster "AHHH... YOUR MAJESTY..."
    gaster "I TOLD YOU SEVERAL TIMES: ASK THE QUEEN"
    gaster "AND NOW YOU CAN'T..."
    if politicalGeography == 1:
        $ politicalGeography = politicalGeography + 1
    return 

label geoSnowdin:
    show gaster trapped neutral flip
    gaster "THOSE FURRY MONSTERS REALLY LIKE THE COLD, DO THEY?"
    show papyrusImg neutral
    papyrus "SOME OF THEM"
    show papyrusImg confused
    papyrus "IT'S WAY BETTER THAN A TON OF LAVA ANYHOW"
    show gaster trapped maybe flip
    gaster "BUT WITH TEMPERATE FORESTS FINALLY AT OUR DISPOSAL"
    papyrus "YES, SOME OF THEM REALLY LIKE THE COLD"
    papyrus "GOT USED TO IT I GUESS"
    gaster "BUT HIGHER SNOWDIN IS REALLY UP THERE"
    show papyrusImg serious
    papyrus "WE MADE AN ELEVATOR"
    papyrus "WE MADE ELEVATORS FOR EVERYTHING!"
    show gaster trapped dissapointed flip
    gaster "I GUESS I JUST DON'T GET IT"
    papyrus "YOU DON'T HAVE TO"
    show gaster trapped dissapointed
    gaster "POINT TAKEN"
    show gaster trapped neutral flip
    gaster "WHO WORKS ON THOSE ELEVATORS ANYWAY?"
    gaster "I DO REMEMBER LEAVING AN AUTOMATED SYSTEM BUT MY DOCUMENTATION DID NOT SURVIVE ME BEEN FORGOTTEN I BELIEVE"
    show papyrusImg neutral
    papyrus "DR. ALPHYS KIND OF LOOKED AFTER THAT IN THE UNDERGROUND"
    papyrus "BUT SINCE SHE WAS BARREN OF DOING SCIENCE FOR THE TIME BEING"
    show papyrusImg checkThis
    papyrus "FRISK AND I NOMINATED SANS"
    show papyrusImg delight
    papyrus "AND OF COURSE THE KING SAID YES"
    gaster "WHY DID HE?"
    show papyrusImg surprised happy
    papyrus "OH!"
    papyrus "THAT'S EASY"
    show papyrusImg proud
    papyrus "IT'S A MYSTERY"
    show gaster trapped oh flip
    gaster "OHHHH"
    show gaster trapped happy flip
    gaster "A MYSTERY!"
    if politicalGeography == 2:
        $ politicalGeography = politicalGeography + 1
    return

label elevatorSnowdin:
    show gaster trapped neutral flip
    gaster "YOU WERE TELLING ME SANS IS IN CHARGE OF THE TRANSPORTATION SYSTEM HERE IN SURFACE"
    show papyrusImg delight
    papyrus "YES, THE ELEVATOR TO HIGHER SNOWDIN"
    show papyrusImg neutral
    papyrus "HE WANTED TO MOVE TO THERE FOR THAT"
    show papyrusImg serious
    papyrus "BUT I TOLD HIM I WANTED TO BE AS NEAR AS POSSIBLE TO NEWER HOME"
    show gaster trapped oh flip
    gaster "DID YOU HAVE A REASON FOR IT?"
    gaster "THE FALLEN HUMAN?..."
    show papyrusImg nope
    papyrus "AH, NO!"
    show papyrusImg proud
    papyrus "NO MATTER WHERE WE LIVE WE STILL GOING TO BE GREAT FRIENDS!"
    papyrus "I JUST WANTED TO HAVE TORIEL NEAR TO US AS MUCH AS POSSIBLE"
    gaster "WHAT THE QUEEN HAS TO DO WITH ANYTHING OF THIS?"
    gaster "IS IT ABOUT..."
    show papyrusImg serious
    papyrus "LOOK"
    show papyrusImg explainingPointing
    papyrus "UNDYNE AND I JOKE ABOUT SHE BEING SANS' GIRLFRIEND BECAUSE IS FUNNY TO PICK ON HIM FOR A CHANGE"
    show gaster trapped happy flip
    gaster "I THOUGHT THAT WASN'T POSSIBLE..."
    show papyrusImg neutral
    papyrus "BUT JUST HAPPENS THAT SANS LOOKS REALLY HAPPY WHEN HE'S WITH HER"
    papyrus "AND TORIEL LOOKS SUPER RELAXED WITH HIM AROUND"
    show papyrusImg uhh
    papyrus "AND I KNOW HE'S KIND OF WAY TOO LAZY FOR A RELATIONSHIP BUT..."
    show papyrusImg delight
    papyrus "JUST, KINDA, MAKE ME HAPPY SEEING THEM LOOKING KINDA CUTE TOGETHER??"
    papyrus "AND LAUGHING AT THEIR OWN TERRIBLE JOKES??"
    papyrus "AND SANS NOT SAD AND TIRED FOR A CHANGE???"
    papyrus "IT'S JUST MAKE ME HAPPY"
    gaster "IF HE'S HAPPY WITH IT, I'M ALSO HAPPY FOR HIM"
    show papyrusImg annoyed
    papyrus "BUT HE DIDN'T WANT TO LOSE, SO HE NAMED OUR HOUSE IN THE FOREST AND THE OFFICE AT THE FOOT OF THE MOUNTAIN 'LOWER SNOWDIN'"
    show papyrusImg proud
    papyrus "AND I'M TOTALLY OKEY WITH THAT"
    show papyrusImg dissapointed
    papyrus "AFTER 3 WEEKS OF GRUMBLING"
    gaster "I THOUGHT YOU WERE GOING TO SAY 3 MONTHS TO HALF A YEAR!"
    gaster "YOU ARE MUCH BETTER AT ACCEPTING YOUR BROTHER'S QUIRKS RIGHT NOW"
    gaster "I'M GLAD"
    show papyrusImg annoyed
    papyrus "I'M SURE THAT'S NOT SOMETHING GOOD"
    gaster "FOR ME IT IS"
    if politicalGeography == 3:
        $ politicalGeography = politicalGeography + 1
    return
    
label aMystery:
    show papyrusImg annoyed
    papyrus "DO YOU KNOW ABOUT THE MYSTERY?"
    show gaster trapped happy flip
    gaster "YES, YES, I DO KNOW ABOUT THE MYSTERY"
    show gaster trapped sad flip
    gaster "WE SHOULDN'T BE TALKING ABOUT THAT AND YOU KNOW IT"
    show papyrusImg sorry
    papyrus "YES, THAT'S RIGHT, I'M SORRY"
    return
