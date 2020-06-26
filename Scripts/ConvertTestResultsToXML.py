import simplejson
import dicttoxml
from junit_xml import TestSuite, TestCase

# Open the Json file
with open("..\\Project_Exhibited\\Saved\\UnitTestsReport\\index.json", 'rb') as f:
    file = simplejson.loads(f.read())

    # Convert to JUnit
    test_suites = []

for tests in file["tests"]:

    test_cases = []
    tc = TestCase(tests["testDisplayName"], tests["fullTestPath"])
    tc.allow_multiple_subalements = True

    if tests["state"] == "Fail":

        tc.file = tests["entries"][0]["filename"]
        tc.line = tests["entries"][0]["lineNumber"]

        for entry in tests["entries"]:
            tc.add_failure_info(entry["event"]["message"], None, entry["event"]["type"])

    test_cases.append(tc)

    ts = TestSuite(tests["testDisplayName"], test_cases)
    test_suites.append(ts)

xml = TestSuite.to_xml_string(test_suites, True, "utf-8").encode("utf-8")

print(xml)

    # Write XML to new file
with open("..\\Project_Exhibited\\Saved\\UnitTestsReport\\index.xml", "wb") as xml_file:
    xml_file.write(xml)

print("Conversion done")