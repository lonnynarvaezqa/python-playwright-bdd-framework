# features/navigation.feature
Feature: General Site Navigation

  Scenario: Verify link navigation to the Horizontal Slider page
    Given the user is on the main landing page
    When the user clicks the link titled "Horizontal Slider"
    Then the user should be redirected to the URL containing "/horizontal_slider"
    And the page header should display "Horizontal Slider"