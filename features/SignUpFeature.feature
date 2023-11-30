Feature: SignUpFeature

    Scenario: Successful Email Subcription Sign up on NP website
        Given Chrome browser is launched
        When Open NP Website
        Then Input Email "tamebiw303@bustayes.com"
        Then Verify Successful Subcription
        Then Close browser