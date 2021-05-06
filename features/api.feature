Feature DnD Classes:
  As a non-player,
  I want to know what a
  class' hit die is and their
  saving throw stats.

  Scenario: Incorrect API Calls
  When The DnD API is queried with Wizard
  Then The Response code is not 200

  Scenario Outline: DnD Class Hit Dies
    When The DnD API is queried with "<dnd_class>"
    Then The response code is 200
    And The hit_die is "<hit_die>"

    Examples: Classes
      | dnd_class  | hit_die  |
      | wizard     | 6        |
      | rogue      | 8        |
      | barbarian  | 12       |
      | bard       | 8        |
      | warlock    | 8        |
      | cleric     | 8        |
      | druid      | 8        |
      | fighter    | 10       |
      | monk       | 8        |
      | paladin    | 10       |
      | ranger     | 10       |
      | sorcerer   | 6        |


  Scenario Outline: DnD Class Saving Throws
    When The DnD API is queried with "<dnd_class>"
    Then The response code is 200
    And The saving throws are "<saving_throws>"

    Examples: Classes
      | dnd_class  | saving_throws  |
      | wizard     | int, wis       |
      | rogue      | dex, int       |
      | barbarian  | str, con       |
      | bard       | dex, cha       |
      | warlock    | wis, cha       |
      | cleric     | wis, cha       |
      | druid      | int, wis       |
      | fighter    | str, con       |
      | monk       | str, dex       |
      | paladin    | wis, cha       |
      | ranger     | str, dex       |
      | sorcerer   | con, cha       |
