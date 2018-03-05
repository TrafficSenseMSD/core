from lxml import objectify
from lxml import etree

city = etree.Element("city")

general_params = {
    'inhabitants': str(10),
    'households': "500",
    "childrenAgeLimits": "18",
    "retirementAgeLimits": "65",
    "carRate": "0.58",
    "unemploymentRate": "0.05",
    "footDistanceLimits": "350",
    "incomingTraffic": "200",
    "outgoingTraffic": "50"
}

general = etree.SubElement(city, 'general', general_params)


parameter_params = dict(
    carPreference = "0.50",
    meanTimePerKmInCity = "360",
    freeTimeActivityRate = "0.15",
    uniformRandomTraffic = "0.20",
    departureVariation = "120"
)

parameters = etree.SubElement(city, "parameters", parameter_params)

############## POPULATION ###################
population = etree.SubElement(city, "population")

population.insert(
    0,
    etree.Element(
        "bracket",
        dict(
            beginAge="0",
            endAge="15",
            peopleNbr="5000"
        )
    ))

population.insert(
    0,
    etree.Element(
        "bracket",
        dict(
            beginAge="15",
            endAge = "30",
            peopleNbr = "10000"
        )
    ))

population.insert(
    0,
    etree.Element(
        "bracket",
        dict(
            beginAge="31",
            endAge = "60",
            peopleNbr = "17450"
        )
    ))

population.insert(
    0,
    etree.Element(
        "bracket",
        dict(
            beginAge="60",
            endAge = "90",
            peopleNbr = "9780"
        )
    ))



############## WORKHOURS #################
workhours_params = dict(

)

workhours = etree.SubElement(city, "workHours", workhours_params)

workhours.insert(0,
                 etree.Element(
                     "opening",
                     dict(
                         hour="600",
                         proportion="0.30"
                     )
                 )
)

workhours.insert(0,
                 etree.Element(
                     "closing",
                     dict(
                         hour="43200",
                         proportion = "0.20"
                     )
                 )
)


############# STREETS ##############



#city.set("general = etree.Element("general")

# city = objectify.Element("city")
# el = objectify.Element("yet_another_child")
#
# city.general= el

print(etree.tostring(city, pretty_print=True).decode('utf-8'))