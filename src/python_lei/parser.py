from python_lei.exceptions import RecordNotFound


class LEIParser:
    """
    Helper class to parse LEI response returned from the API
    """

    def __init__(self, lei_responses):
        """
        Get the output from the API and assign them to variables

        Args:
            lei_responses: List of raw LEI reponse from the API
        """
        # Initialize empty lists
        self.lei_list = []
        self.lei_names = []
        self.lei_legal_jurisdictions = []
        self.lei_legal_forms = []
        self.lei_other_legal_forms = []
        self.lei_entity_status = []
        self.lei_entity_expiration_dates = []
        self.lei_entity_expiration_reasons = []
        self.lei_successor_entities = []
        self.lei_initial_registration_dates = []
        self.lei_last_update_dates = []
        self.lei_registration_status = []
        self.lei_next_renewal_dates = []
        self.lei_managing_LOU = []
        self.lei_validation_sources = []
        self.lei_associated_lei = []
        self.lei_associated_entity_names = []
        self.lei_associated_entity_types = []
        self.lei_registration_authority_ids = []
        self.lei_other_registration_ids = []
        self.lei_registration_authority_entite_ids = []
        self.lei_entity_categories = []
        self.lei_address_1_line_1 = []
        self.lei_address_1_line_2 = []
        self.lei_address_1_line_3 = []
        self.lei_address_1_line_4 = []
        self.lei_address_1_city = []
        self.lei_address_1_region = []
        self.lei_address_1_country = []
        self.lei_address_1_postal_code = []
        self.lei_address_1_other_type = []
        self.lei_address_1_address_type = []
        self.lei_address_2_line_1 = []
        self.lei_address_2_line_2 = []
        self.lei_address_2_line_3 = []
        self.lei_address_2_line_4 = []
        self.lei_address_2_city = []
        self.lei_address_2_region = []
        self.lei_address_2_country = []
        self.lei_address_2_postal_code = []
        self.lei_address_2_other_type = []
        self.lei_address_2_address_type = []
        self.lei_other_name_name = []
        self.lei_other_name_language = []
        self.lei_other_name_type = []
        self.lei_reporting_exception_1_lei = []
        self.lei_reporting_exception_1_category = []
        self.lei_reporting_exception_2_lei = []
        self.lei_reporting_exception_2_category = []
        self.lei_relationships_1_parent_lei = []
        self.lei_relationships_1_parent_relationship_type = []
        self.lei_relationships_1_parent_relationship_status = []
        self.lei_relationships_1_parent_initial_registration_date = []
        self.lei_relationships_1_parent_last_updated = []
        self.lei_relationships_1_parent_registration_status = []
        self.lei_relationships_1_parent_next_renewal_date = []
        self.lei_relationships_1_parent_managing_LOU = []
        self.lei_relationships_1_parent_validation_sources = []
        self.lei_relationships_1_parent_validation_documents = []
        self.lei_relationships_1_parent_validation_reference = []
        self.lei_relationships_2_parent_lei = []
        self.lei_relationships_2_parent_relationship_type = []
        self.lei_relationships_2_parent_relationship_status = []
        self.lei_relationships_2_parent_initial_registration_date = []
        self.lei_relationships_2_parent_last_updated = []
        self.lei_relationships_2_parent_registration_status = []
        self.lei_relationships_2_parent_next_renewal_date = []
        self.lei_relationships_2_parent_managing_LOU = []
        self.lei_relationships_2_parent_validation_sources = []
        self.lei_relationships_2_parent_validation_documents = []
        self.lei_relationships_2_parent_validation_reference = []

        if not lei_responses:
            raise IndexError("No LEI found")

        for lei_response in lei_responses:
            if not lei_response.get("records"):
                raise RecordNotFound("No record found")
                continue
            self.lei_list.append(lei_response["records"][0].get("LEI"))
            self.lei_names.append(lei_response["records"][0].get("LegalName"))
            self.lei_legal_jurisdictions.append(
                lei_response["records"][0].get("LegalJurisdiction")
            )
            self.lei_legal_forms.append(lei_response["records"][0].get("LegalForm"))
            self.lei_other_legal_forms.append(
                lei_response["records"][0].get("OtherLegalForm")
            )
            self.lei_entity_status.append(
                lei_response["records"][0].get("EntityStatus")
            )
            self.lei_entity_expiration_dates.append(
                lei_response["records"][0].get("EntityExpirationDate")
            )
            self.lei_entity_expiration_reasons.append(
                lei_response["records"][0].get("EntityExpirationReason")
            )
            self.lei_successor_entities.append(
                lei_response["records"][0].get("SuccessorEntity")
            )
            self.lei_initial_registration_dates.append(
                lei_response["records"][0].get("InitialRegistrationDate")
            )
            self.lei_last_update_dates.append(
                lei_response["records"][0].get("LastUpdateDate")
            )
            self.lei_registration_status.append(
                lei_response["records"][0].get("RegistrationStatus")
            )
            self.lei_next_renewal_dates.append(
                lei_response["records"][0].get("NextRenewalDate")
            )
            self.lei_managing_LOU.append(lei_response["records"][0].get("ManagingLOU"))
            self.lei_validation_sources.append(
                lei_response["records"][0].get("ValidationSources")
            )
            self.lei_associated_lei.append(
                lei_response["records"][0].get("AssociatedLEI")
            )
            self.lei_associated_entity_names.append(
                lei_response["records"][0].get("AssociatedEntityName")
            )
            self.lei_associated_entity_types.append(
                lei_response["records"][0].get("AssociatedEntityType")
            )
            self.lei_registration_authority_ids.append(
                lei_response["records"][0].get("RegistrationAuthorityID")
            )
            self.lei_other_registration_ids.append(
                lei_response["records"][0].get("OtherRegistrationAuthorityID")
            )
            self.lei_registration_authority_entite_ids.append(
                lei_response["records"][0].get("RegistrationAuthorityEntityID")
            )
            self.lei_entity_categories.append(
                lei_response["records"][0].get("EntityCategory")
            )
            self.lei_address_1_line_1.append(
                lei_response["records"][0].get("Addresses")[0].get("Line1")
            )
            self.lei_address_1_line_2.append(
                lei_response["records"][0].get("Addresses")[0].get("Line2")
            )
            self.lei_address_1_line_3.append(
                lei_response["records"][0].get("Addresses")[0].get("Line3")
            )
            self.lei_address_1_line_4.append(
                lei_response["records"][0].get("Addresses")[0].get("Line4")
            )
            self.lei_address_1_city.append(
                lei_response["records"][0].get("Addresses")[0].get("City")
            )
            self.lei_address_1_region.append(
                lei_response["records"][0].get("Addresses")[0].get("Region")
            )
            self.lei_address_1_country.append(
                lei_response["records"][0].get("Addresses")[0].get("Country")
            )
            self.lei_address_1_postal_code.append(
                lei_response["records"][0].get("Addresses")[0].get("PostalCode")
            )
            self.lei_address_1_other_type.append(
                lei_response["records"][0].get("Addresses")[0].get("OtherType")
            )
            self.lei_address_1_address_type.append(
                lei_response["records"][0].get("Addresses")[0].get("AddressType")
            )
            self.lei_address_2_line_1.append(
                lei_response["records"][0].get("Addresses")[1].get("Line1")
            )
            self.lei_address_2_line_2.append(
                lei_response["records"][0].get("Addresses")[1].get("Line2")
            )
            self.lei_address_2_line_3.append(
                lei_response["records"][0].get("Addresses")[1].get("Line3")
            )
            self.lei_address_2_line_4.append(
                lei_response["records"][0].get("Addresses")[1].get("Line4")
            )
            self.lei_address_2_city.append(
                lei_response["records"][0].get("Addresses")[1].get("City")
            )
            self.lei_address_2_region.append(
                lei_response["records"][0].get("Addresses")[1].get("Region")
            )
            self.lei_address_2_country.append(
                lei_response["records"][0].get("Addresses")[1].get("Country")
            )
            self.lei_address_2_postal_code.append(
                lei_response["records"][0].get("Addresses")[1].get("PostalCode")
            )
            self.lei_address_2_other_type.append(
                lei_response["records"][0].get("Addresses")[1].get("OtherType")
            )
            self.lei_address_2_address_type.append(
                lei_response["records"][0].get("Addresses")[1].get("AddressType")
            )
            if lei_response["records"][0].get("OtherNames"):
                self.lei_other_name_name.append(
                    lei_response["records"][0].get("OtherNames")[0].get("Name")
                )
                self.lei_other_name_language.append(
                    lei_response["records"][0].get("OtherNames")[0].get("LanguageType")
                )
                self.lei_other_name_type.append(
                    lei_response["records"][0].get("OtherNames")[0].get("NameType")
                )
            else:
                self.lei_other_name_name.append(None)
                self.lei_other_name_language.append(None)
                self.lei_other_name_type.append(None)

            if lei_response["records"][0].get("ReportingExceptions"):
                self.lei_reporting_exception_1_lei.append(
                    lei_response["records"][0].get("ReportingExceptions")[0].get("LEI")
                )
                self.lei_reporting_exception_1_category.append(
                    lei_response["records"][0]
                    .get("ReportingExceptions")[0]
                    .get("ExceptionCategory")
                )
                self.lei_reporting_exception_2_lei.append(
                    lei_response["records"][0].get("ReportingExceptions")[1].get("LEI")
                )
                self.lei_reporting_exception_2_category.append(
                    lei_response["records"][0]
                    .get("ReportingExceptions")[1]
                    .get("ExceptionCategory")
                )
            else:
                self.lei_reporting_exception_1_lei.append(None)
                self.lei_reporting_exception_1_category.append(None)
                self.lei_reporting_exception_2_lei.append(None)
                self.lei_reporting_exception_2_category.append(None)
            if lei_response["records"][0].get("Relationships"):
                self.lei_relationships_1_parent_lei.append(
                    lei_response["records"][0].get("Relationships")[0].get("ParentLEI")
                )
                self.lei_relationships_1_parent_relationship_type.append(
                    lei_response["records"][0]
                    .get("Relationships")[0]
                    .get("RelationshipType")
                )
                self.lei_relationships_1_parent_relationship_status.append(
                    lei_response["records"][0]
                    .get("Relationships")[0]
                    .get("RelationshipStatus")
                )
                self.lei_relationships_1_parent_initial_registration_date.append(
                    lei_response["records"][0]
                    .get("Relationships")[0]
                    .get("InitialRegistrationDate")
                )
                self.lei_relationships_1_parent_last_updated.append(
                    lei_response["records"][0]
                    .get("Relationships")[0]
                    .get("LastUpdateDate")
                )
                self.lei_relationships_1_parent_registration_status.append(
                    lei_response["records"][0]
                    .get("Relationships")[0]
                    .get("RegistrationStatus")
                )
                self.lei_relationships_1_parent_next_renewal_date.append(
                    lei_response["records"][0]
                    .get("Relationships")[0]
                    .get("NextRenewalDate")
                )
                self.lei_relationships_1_parent_managing_LOU.append(
                    lei_response["records"][0]
                    .get("Relationships")[0]
                    .get("ManagingLou")
                )
                self.lei_relationships_1_parent_validation_sources.append(
                    lei_response["records"][0]
                    .get("Relationships")[0]
                    .get("ValidationSources")
                )
                self.lei_relationships_1_parent_validation_documents.append(
                    lei_response["records"][0]
                    .get("Relationships")[0]
                    .get("ValidationDocuments")
                )
                self.lei_relationships_1_parent_validation_reference.append(
                    lei_response["records"][0]
                    .get("Relationships")[0]
                    .get("ValidationReference")
                )
                self.lei_relationships_2_parent_lei.append(
                    lei_response["records"][0].get("Relationships")[0].get("ParentLEI")
                )
                self.lei_relationships_2_parent_relationship_type.append(
                    lei_response["records"][0]
                    .get("Relationships")[0]
                    .get("RelationshipType")
                )
                self.lei_relationships_2_parent_relationship_status.append(
                    lei_response["records"][0]
                    .get("Relationships")[0]
                    .get("RelationshipStatus")
                )
                self.lei_relationships_2_parent_initial_registration_date.append(
                    lei_response["records"][0]
                    .get("Relationships")[0]
                    .get("InitialRegistrationDate")
                )
                self.lei_relationships_2_parent_last_updated.append(
                    lei_response["records"][0]
                    .get("Relationships")[0]
                    .get("LastUpdateDate")
                )
                self.lei_relationships_2_parent_registration_status.append(
                    lei_response["records"][0]
                    .get("Relationships")[0]
                    .get("RegistrationStatus")
                )
                self.lei_relationships_2_parent_next_renewal_date.append(
                    lei_response["records"][0]
                    .get("Relationships")[0]
                    .get("NextRenewalDate")
                )
                self.lei_relationships_2_parent_managing_LOU.append(
                    lei_response["records"][0]
                    .get("Relationships")[0]
                    .get("ManagingLou")
                )
                self.lei_relationships_2_parent_validation_sources.append(
                    lei_response["records"][0]
                    .get("Relationships")[0]
                    .get("ValidationSources")
                )
                self.lei_relationships_2_parent_validation_documents.append(
                    lei_response["records"][0]
                    .get("Relationships")[0]
                    .get("ValidationDocuments")
                )
                self.lei_relationships_2_parent_validation_reference.append(
                    lei_response["records"][0]
                    .get("Relationships")[0]
                    .get("ValidationReference")
                )
            else:
                self.lei_relationships_1_parent_lei.append(None)
                self.lei_relationships_1_parent_relationship_type.append(None)
                self.lei_relationships_1_parent_relationship_status.append(None)
                self.lei_relationships_1_parent_initial_registration_date.append(None)
                self.lei_relationships_1_parent_last_updated.append(None)
                self.lei_relationships_1_parent_registration_status.append(None)
                self.lei_relationships_1_parent_next_renewal_date.append(None)
                self.lei_relationships_1_parent_managing_LOU.append(None)
                self.lei_relationships_1_parent_validation_sources.append(None)
                self.lei_relationships_1_parent_validation_documents.append(None)
                self.lei_relationships_1_parent_validation_reference.append(None)
                self.lei_relationships_2_parent_lei.append(None)
                self.lei_relationships_2_parent_relationship_type.append(None)
                self.lei_relationships_2_parent_relationship_status.append(None)
                self.lei_relationships_2_parent_initial_registration_date.append(None)
                self.lei_relationships_2_parent_last_updated.append(None)
                self.lei_relationships_2_parent_registration_status.append(None)
                self.lei_relationships_2_parent_next_renewal_date.append(None)
                self.lei_relationships_2_parent_managing_LOU.append(None)
                self.lei_relationships_2_parent_validation_sources.append(None)
                self.lei_relationships_2_parent_validation_documents.append(None)
                self.lei_relationships_2_parent_validation_reference.append(None)
