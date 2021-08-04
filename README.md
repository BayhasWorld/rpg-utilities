# RPG Utilities

## Use Cases

[Diagram](diagrams/use_cases.drawio.svg)

|Use Case          |User Type                      |
|------------------|-------------------------------|
|Create Character  |Game Master, Player            |
|View Character    |Game Master, Player, Observer  |
|Edit Character    |Game Master, Player            |
|Retire Character  |Game Master, Player            |
|Delete Character  |Game Master                    |
|Create Content    |Game Master                    |
|View Content      |Game Master, Player, Observer  |
|Edit Content      |Game Master                    |
|Retire Content    |Game Master                    |
|Delete Content    |Game Master                    |
|Direct Game       |Game Master                    |

## Data Elements

[Diagram](diagrams/data_elements.drawio.svg)

|Type     |Description                                              |Children                                    |
|---------|---------------------------------------------------------|--------------------------------------------|
|Person   |Any person involved in the RPG in any capacity           |Game Master (GM), Player, Observer          |
|Character|An entity which represents an individual actor in the RPG. Could be considered a child of content.|Player Character, Character                 |
|Content  |Any content that is relevant to the RPG                  |Campaign, Game, Adventure, Blog Post, Wiki Entry, game components (E.g.: attributes, books, equipment, classes, races, etc.)|

## Data Attributes
