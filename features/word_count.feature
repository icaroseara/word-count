Feature: Count Words in a text
  As a user

  Scenario: Access count words form
    Given system can calculate the number of words in a given text
    When I view the application
    Then I see a form containing a text box to enter a body of text

  Scenario: Count words of a valid text
    Given system can calculate the number of words in a given text
    When I submit the form with some text
    Then I see a result containing the number of words in the text-area

  Scenario: Count words of a empty text
    Given system can calculate the number of words in a given text
    When I submit the form with an empty text
    Then I see a form error telling me that some text input is required
