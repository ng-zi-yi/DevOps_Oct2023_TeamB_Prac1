Feature: SignUpFeature

    Scenario: Successful Email Subcription Sign up on NP website
        Given Chrome browser is launched
        When Open NP homepage
        Then Input Email "saposo1330@dpsols.com"
        Then Verify Successful Subcription
        And Close browser