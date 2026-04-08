import pytest

import nhs_notify_letters_onboarding as onboarding

VALID_DOCUMENT_REFERENCE = {
    "resourceType": "DocumentReference",
    "id": "82bfb7f3-4889-4e15-b308-bbe4e3cd431f",
    "status": "current",
    "docStatus": "final",
    "type": {
        "coding": [
            {
                "system": "http://snomed.info/sct",
                "code": "308540004",
                "display": "Appointment",
            }
        ]
    },
    "subject": {
        "identifier": {
            "system": "https://fhir.nhs.uk/Id/nhs-number",
            "value": "9876543210",
        }
    },
    "author": [
        {
            "identifier": {
                "system": "https://fhir.nhs.uk/Id/ods-organization-code",
                "value": "RX809",
            },
            "display": "Example NHS Trust",
        }
    ],
    "custodian": {
        "identifier": {
            "system": "https://fhir.nhs.uk/Id/ods-organization-code",
            "value": "C4L8E",
        },
        "display": "NHS ENGLAND: NHS NOTIFY",
    },
    "date": "2025-11-19T14:30:00Z",
    "description": "Appointment notification letter for outpatient consultation",
    "content": [
        {
            "attachment": {
                "contentType": "application/pdf",
                "title": "Appointment Letter - November 2025",
                "data": "JVBERi0xLjc=",
            }
        }
    ],
}


class TestValidation:
    def test_successful_validation_given_valid_instance(self):
        onboarding.validate(VALID_DOCUMENT_REFERENCE)

    def test_raises_validation_error_when_required_field_missing(self):
        invalid = {**VALID_DOCUMENT_REFERENCE}
        del invalid["subject"]

        with pytest.raises(onboarding.ValidationError):
            onboarding.validate(invalid)
