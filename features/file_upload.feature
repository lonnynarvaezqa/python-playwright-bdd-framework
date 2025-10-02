# features/file_upload.feature
Feature: File Upload Functionality

  Scenario: Successful file upload and validation
    Given the user is on the File Upload page
    When the user selects a file named "my_test_file.txt"
    And the user clicks the upload button
    Then the user should be redirected to the URL containing "/upload"
    And the uploaded file name "my_test_file.txt" should be displayed