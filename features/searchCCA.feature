Feature: Search for CCA details 
    Scenario Outline:
        Given Chrome browser is Launched
        When Open NP Website
        Then Select Student Life Tab
        Then Select Clubs and Society
        Then Select "<ccaTypePath>"
        Then Select a "<ccaNamePath>"
        Then Verify if selected "<ccaName>" text is same as "<ccaTitlePath>"
        And Close browser

    Examples:
        |ccaName|ccaTypePath|ccaNamePath|ccaTitlePath|
        |Hip Hop|/html/body/main/section[2]/div/div[2]/div[2]/div[1]/div[1]/div/div/a/div|/html/body/main/section[2]/div/div[2]/div[2]/div[1]/div[11]/div[1]/div[1]|/html/body/main/section[2]/div/div[2]/div[2]/div[1]/div[11]/div[2]/div/div/div[1]/p|
        |Peer Helpers Club|/html/body/main/section[2]/div/div[2]/div[2]/div[1]/div[4]/div/div/a/div|/html/body/main/section[2]/div/div[2]/div[2]/div[1]/div[12]/div[1]|/html/body/main/section[2]/div/div[2]/div[2]/div[1]/div[12]/div[2]/div/div/div[1]/p|
        |Badminton|/html/body/main/section[2]/div/div[2]/div[2]/div[1]/div[2]/div/div/a/div|/html/body/main/section[2]/div/div[2]/div[2]/div[1]/div[3]/div[1]|/html/body/main/section[2]/div/div[2]/div[2]/div[1]/div[3]/div[2]/div/div/div[1]/p|                                                 
        