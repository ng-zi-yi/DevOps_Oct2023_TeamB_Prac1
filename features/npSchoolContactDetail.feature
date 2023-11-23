Feature: NP Website School Contact Details
    Background: Common Steps
        Given   Chrome Browser is launched
        When    Open NP page

    Scenario: Navigate to School Contact Details
        Then    Hover over Schools and Courses
        Then    Go to "{schoolPath} page"
        Then    Go to Contact Details
        And     Close browser


# Examples: Schools
#     |school                                         |schoolPath                                                                             |schoolLink                                                                                         |
#     |School of Business & Accountancy               |/html/body/header/nav/div[2]/div/div/ul/li[2]/div/div/div/div[2]/div/div[1]/ul/li[1]/a |https://www.np.edu.sg/schools-courses/academic-schools/school-of-business-accountancy              |
#     |School of Design & Environment                 |/html/body/header/nav/div[2]/div/div/ul/li[2]/div/div/div/div[2]/div/div[1]/ul/li[2]/a |https://www.np.edu.sg/schools-courses/academic-schools/school-of-design-environment                |
#     |School of Engineering                          |/html/body/header/nav/div[2]/div/div/ul/li[2]/div/div/div/div[2]/div/div[1]/ul/li[3]/a |https://www.np.edu.sg/schools-courses/academic-schools/school-of-engineering                       |
#     |School of Film & Media Studies                 |/html/body/header/nav/div[2]/div/div/ul/li[2]/div/div/div/div[2]/div/div[1]/ul/li[4]/a |https://www.np.edu.sg/schools-courses/academic-schools/school-of-film-media-studies                |
#     |School of Health Sciences                      |/html/body/header/nav/div[2]/div/div/ul/li[2]/div/div/div/div[2]/div/div[1]/ul/li[5]/a |https://www.np.edu.sg/schools-courses/academic-schools/school-of-health-sciences                   |
#     |School of Humanities & Social Sciences         |/html/body/header/nav/div[2]/div/div/ul/li[2]/div/div/div/div[2]/div/div[1]/ul/li[6]/a |https://www.np.edu.sg/schools-courses/academic-schools/school-of-humanities-social-sciences        |
#     |School of InfoComm Technology                  |/html/body/header/nav/div[2]/div/div/ul/li[2]/div/div/div/div[2]/div/div[1]/ul/li[7]/a |https://www.np.edu.sg/schools-courses/academic-schools/school-of-infocomm-technology               |
#     |School of Life Sciences & Chemical Technology  |/html/body/header/nav/div[2]/div/div/ul/li[2]/div/div/div/div[2]/div/div[1]/ul/li[8]/a |https://www.np.edu.sg/schools-courses/academic-schools/school-of-life-sciences-chemical-technology |
#     |School of Interdisciplinary Studies            |/html/body/header/nav/div[2]/div/div/ul/li[2]/div/div/div/div[2]/div/div[1]/ul/li[9]/a |https://www.np.edu.sg/schools-courses/academic-schools/school-of-life-sciences-chemical-technology |