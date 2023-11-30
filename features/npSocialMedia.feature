Feature: NP Website Social Media
    Background: Common Steps
        Given   Chrome Browser is launched
        When    Open NP page

    Scenario Outline: Check Social Media Link
        Then    Click "<socialicon>" link
        Then    Verify new tab is "<socialmediaPage>"
        And     Close browser

    Examples: Social Medias
        |socialicon                                                   |socialmediaPage                                          |
        |/html/body/footer/div[1]/div/div[4]/div[2]/ul/li[2]/a/em     |https://www.instagram.com/ngeeannpoly/                   |
        |/html/body/footer/div[1]/div/div[4]/div[2]/ul/li[3]/a/em     |https://www.youtube.com/user/NgeeAnnPolytechnic          |
        |/html/body/footer/div[1]/div/div[4]/div[2]/ul/li[4]/a/em     |https://www.facebook.com/ngeeannpoly                     |
        |/html/body/footer/div[1]/div/div[4]/div[2]/ul/li[5]/a/em     |https://sg.linkedin.com/school/ngee-ann-polytechnic/     |
        |/html/body/footer/div[1]/div/div[4]/div[2]/ul/li[6]/a/em     |https://t.me/ngeeannpoly                                 |
