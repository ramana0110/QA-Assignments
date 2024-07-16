from pyats import aetest
from parser_func import parse_ap_summary

class APTest(aetest.Testcase):
    @aetest.setup
    def setup(self):

        self.raw_output = """ewlc#show ap summary 
        Number of APs: 3

        CC = Country Code
        RD = Regulatory Domain

        AP Name                          Slots AP Model             Ethernet MAC   Radio MAC      CC   RD   IP Address             State        Location
        -------------------------------------------------------------------------------------------------------------------------------------------------------------
        APBC26.C7A3.1970                 2     AIR-AP3802E-B-K9     bc26.c7a3.1970 00b7.7166.bea0 US   -B   192.165.7.199          Registered   default location                
        APA4B2.3904.1F0C                 3     C9130AXI-B           a4b2.3904.1f0c 2c57.4156.9000 US   -B   192.165.3.119          Registered   default location                
        AP6849.92F9.8930                 3     CW9163E-B            6849.92f9.8930 ecf4.0c4f.3360 US   -B   192.165.8.139          Registered   default location"""
        
        self.parsed_output = parse_ap_summary(self.raw_output)

    @aetest.test
    def fetch_and_print_ap_details(self):
        print(self.parsed_output)
        for ap_details in self.parsed_output:
            print(f"AP Name: {ap_details['ap_name']}")
            print(f"  Number of Slots: {ap_details['slots']}")
            print(f"  AP Model: {ap_details['ap_model']}")
            print(f"  Ethernet MAC: {ap_details['ethernet_mac']}")
            print(f"  Radio MAC: {ap_details['radio_mac']}")
            print(f"  Country Code: {ap_details['cc']}")
            print(f"  Regulatory Domain: {ap_details['rd']}")
            print(f"  IP Address: {ap_details['ip_address']}")
            print(f"  State: {ap_details['state']}")
            print(f"  Location: {ap_details['location']}")
            print()

    @aetest.test
    def verify_ap_states(self):
        for ap_details in self.parsed_output:
            assert ap_details['state'] == 'Registered', f"AP {ap_name} is not registered, state: {ap_details['state']}"
        
        print("All APs are registered.")

if __name__ == '__main__':
    import sys
    from pyats.aetest import TestRunner

    # Create a test runner
    runner = TestRunner()

    # Run the test suite
    runner.run()

