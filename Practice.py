def show_help(Dict):
    print("(-_-)") 
    print("Hello, I am a helper. 📘")

    num = input("Can I help you? (yes/no): ")
    if num == "no":
        print("Okay, goodbye... ")
        return

    print("\nAvailable keys:")
    for key in Dict:
        if key != "help":
            print(f" - {key}")

    selected = input("\nWhich key do you want information about? Type here: ")

    if selected in Dict:
        value = Dict[selected]
        if isinstance(value, dict):
            print(f"Information under '{selected}':")
            for num2, num3 in value.items():
                print(f" -  {num2}: {num3}")
        else:
            print(f"Information for '{selected}': {value}")
    else:
        print("This key was not found. Please check your spelling.")

country={
    "Name":"German or Deutschland",
    "Capital":"Berlin",
    "Language":"German or Deutschland",
    "Language example":"Halten Sie den Wind aufrecht",
    "Old age":"It has existed since 1871.",
    "States":16,
    "Names of all major cities":"Munich, Hamburg, Frankfurt, Cologne, Dusseldorf, Stuttgart, Nuremberg, Leipzig, Dresden and Hanover.",
    "Summary of history":[
    {

    "1871": "Formation of the German Empire after unification of the states",
    "1918": "End of World War I and beginning of the Weimar Republic",
    "1933": "Rise of the Nazi regime led by Adolf Hitler",
    "1945": "End of World War II and division of Germany into East and West",
    "1990": "Reunification of Germany after the fall of the Berlin Wall",

    }
],
    "start date":[
 {
    "Weimar Republic (1919,1933)":[
          {
              
            "Reason for existence":"The Weimar Republic was established in November 1918 after Germany's defeat in World War I and the November Revolution.",
            "Defeat in World War I":"Public discontent and economic and social crises led to the fall of the empire and the formation of the November Revolution.",
            "November revolution":"It included widespread popular protests and military uprisings that ultimately led to the overthrow of the Kaiser's government and the establishment of the Weimar Republic.",
            "Political and economic stability":"The Weimar Republic was formed with the aim of bringing political and economic stability to Germany.",
           
            "Reasons for the fall of the Weimar government":[
                {
                    "Economic crisis":[
                        {
                            "The Great Depression":"The global economic crisis of 1929 hit Germany hard, leading to widespread unemployment, poverty, and public discontent.",
                            "severe swelling":"The experience of rampant inflation in the early 1920s destroyed people's confidence in money and the economic system.",
                            "Payment of war reparations":"The heavy financial obligations resulting from World War I strained the Weimar government and weakened the economy.",
                        }
                    ],

                    "Political instability":[
                        {
                            "Weak parliamentary system":"The large number of political parties and the inability to form stable coalitions led to government instability and an inability to solve problems.",
                            "The rise of extremist parties":"Nationalist and communist parties gained increasing popularity with populist and radical promises, further destabilizing the political system.",
                            "Coups and riots":"A coup attempt by far-right groups and armed clashes between the left and right destroyed order and stability.",
                        }
                    ],

                    "Social factors":[
                        {
                            "General dissatisfaction":"Defeat in World War I, the humiliation caused by the Treaty of Versailles, and economic difficulties caused widespread discontent among the people.",
                            "Social gap":"Deep class and social differences prevented the formation of a unified national identity and solidarity in society.",
                            "Advertising and Propaganda":"The Nazis were able to sway public opinion and promote their ideology by using effective propaganda and mass media.",
                            
                        }
                    ],

                    "The role of external factors":[
                        {
                            "Treaty of Versailles":"The harsh and humiliating terms of the treaty strengthened anti-Western and nationalist sentiments in Germany and played into the hands of extremist parties.",
                            "Instability in Europe":"The disputes and rivalries of European powers created an opportunity for the emergence and rise of Nazi Germany.",
                        }
                    ],

                }
]
          }
      ]   

     }

    ],

    "Nazi Germany (1933 to 1945)":[
        {
           "Ruler of the government":"Hitler",
           "Cause of formation":"The rise of the Nazi regime in Germany was the result of a combination of historical, social, economic, and political factors.",
           "Key factors":[
                {
                    "Defeat in World War I and the Treaty of Versailles":
                    "Under the Treaty of Versailles,Germany was forced to pay heavy reparations and cede its lands to the victorious powers. This created widespread discontent among the German people and paved the way for the emergence of extremist movements.",
                    "Economic crisis":
                    "The Great Depression, which began in the 1930s, had a devastating impact on the German economy. ""Mass unemployment, high inflation, and poverty fueled public discontent with the governments of the day, prompting them to seek a quick and decisive solution. The Nazis were able to gain support from many people by promising to create jobs and improve the economy.",
                    "Nazi propaganda":"The National Socialist German Workers' Party, led by Adolf Hitler, used widespread and effective propaganda to promote its ideology. They were able to incite nationalist sentiments and hatred among the people by using big lies, victimization, and the creation of a common enemy (the Jews).",
                    "Dissatisfaction with Weimar democracy":"The Weimar democratic political system established in Germany after World War I was weak and ineffective, failing to solve the country's problems. This led to people's disillusionment with democracy and their inclination towards extremist ideologies such as Nazism.",
                    "Anti-Semitism":"Nazism was based on a racist ideology and anti-Semitism. Hitler and the Nazis portrayed Jews as enemies of the Aryan race and used this to incite nationalist sentiment and create unity among the people. This anti-Semitism ultimately led to the Holocaust.",
                    "The ambitions of Hitler and the Nazis":"Hitler and the Nazis had ambitious goals for Germany. They wanted to abolish the Treaty of Versailles, expand German territory (Lebensraum), and establish Aryan supremacy over other races. These goals led them to be belligerent and aggressive towards other countries.",

                }
            ],

            "World War II":[
                {
                    "Start date":"World War II was the second world war between 1939 and 1945.",
                    "َAllies":"Soviet Union, United States, British Empire ,Republic of China",
                    "Axis":"Nazi Germany , Empire of Japan , Kingdom of Italy",
                    "Reason for starting":"As one of the main leaders of World War II, Hitler initiated the war in Europe by invading Poland on September 1, 1939.",

                    "The main reasons":[
                        {
                            "Territorial expansionism":"Hitler sought to expand Germany's territory and create (Lebensraum) for the Germans. He wanted to allow Germany to grow and become more powerful by seizing new territories in Eastern Europe.",
                            "Creating a racial empire":"The Nazis believed in Aryan racial superiority and sought to ethnically cleanse and eliminate Jews and other minorities.",
                            "Revenge of the Treaty of Versailles":"Hitler and the Nazi Party were dissatisfied with the terms of the Treaty of Versailles, which had been imposed on Germany after World War I, and sought to repeal the treaty and restore Germany's power and prestige.",
                            "":"",


                        }
                    ],


                }
            ]

        }
    ]

}
