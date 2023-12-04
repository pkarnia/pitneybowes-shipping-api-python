# PitneyBowesShippingAPI
Shipping API

- API version: 1.0.0
- Package version: 1.0.3
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/PitneyBowes/pitneybowes-shipping-api-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import pbshipping
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import pbshipping
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function

import time
import pbshipping
from pbshipping.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-sandbox.pitneybowes.com/shippingservices
# See configuration.py for a list of all supported configuration parameters.
configuration = pbshipping.Configuration(
    host = "https://api-sandbox.pitneybowes.com/shippingservices"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2ClientCredentials

configuration.access_token = 'YOUR_ACCESS_TOKEN'


# Enter a context with an instance of the API client
with pbshipping.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pbshipping.AddressValidationApi(api_client)
    address = pbshipping.Address(address_lines=['1 Atwell rd','bldg 2','apt 302'],city_town ='Cooperstown',state_province = 'NJ',postal_code = '13326',country_code = 'US',name = 'James Brother',company = 'Mary Imogene Basset Hospital',phone = '555-924-2428',email = 'james.b@email.com'	) # Address | Address object that needs to be validated.
x_pb_unified_error_structure = True # bool | Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. (optional) (default to True)
minimal_address_validation = True # bool | When set to true, the complete address (delivery line and last line) is validated but only the last line (city, state, and postal code) would be changed by the validation check. (optional)

try:
	# Address validation
    api_response = api_instance.verify_address(address, x_pb_unified_error_structure=x_pb_unified_error_structure, minimal_address_validation=minimal_address_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressValidationApi->verify_address: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *https://api-sandbox.pitneybowes.com/shippingservices*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AddressValidationApi* | [**verify_address**](docs/AddressValidationApi.md#verify_address) | **POST** /v1/addresses/verify | Address validation
*AddressValidationApi* | [**verify_and_suggest_address**](docs/AddressValidationApi.md#verify_and_suggest_address) | **POST** /v1/addresses/verify-suggest | Address Suggestion
*CarrierInfoApi* | [**get_carrier_facilities**](docs/CarrierInfoApi.md#get_carrier_facilities) | **POST** /v1/carrier-facility | Find Carrier Facilities
*CarrierInfoApi* | [**get_carrier_license_agreement**](docs/CarrierInfoApi.md#get_carrier_license_agreement) | **GET** /v1/carrier/license-agreements | This operation retrieves a carrier&#39;s license agreement.
*CarrierInfoApi* | [**get_carrier_service_rules**](docs/CarrierInfoApi.md#get_carrier_service_rules) | **GET** /v1/information/rules/rating-services | Retrieves the rules governing the carrier&#39;s services.
*CarrierInfoApi* | [**get_carrier_supported_destination**](docs/CarrierInfoApi.md#get_carrier_supported_destination) | **GET** /v1/countries | This operation returns a list of supported destination countries to which the carrier offers international shipping services.
*ContainerApi* | [**get_containerized_parcels_labels**](docs/ContainerApi.md#get_containerized_parcels_labels) | **POST** /v1/container-manifest | Create Container Manifest Label
*CrossBorderQuotesApi* | [**get_cross_border_quotes**](docs/CrossBorderQuotesApi.md#get_cross_border_quotes) | **POST** /v1/crossborder/checkout/quotes | Cross-Border Quotes
*CrossBorderQuotesApi* | [**predicted_hs_code**](docs/CrossBorderQuotesApi.md#predicted_hs_code) | **POST** /v1/crossborder/hs-classification/items | Predicts the HS Code for a parcel
*ManifestsApi* | [**create_manifest**](docs/ManifestsApi.md#create_manifest) | **POST** /v1/manifests | This operation creates an end-of-day manifest
*ManifestsApi* | [**reprint_manifest**](docs/ManifestsApi.md#reprint_manifest) | **GET** /v1/manifests/{manifestId} | reprintManifest
*ManifestsApi* | [**retry_manifest**](docs/ManifestsApi.md#retry_manifest) | **GET** /v1/manifests | retryManifest
*ParcelProtectionApi* | [**cancel_parcel_protection**](docs/ParcelProtectionApi.md#cancel_parcel_protection) | **POST** /v1/parcel-protection/void | Parcel Protection Coverage
*ParcelProtectionApi* | [**get_parcel_protection_coverage**](docs/ParcelProtectionApi.md#get_parcel_protection_coverage) | **POST** /v1/parcel-protection/create | Parcel Protection Coverage
*ParcelProtectionApi* | [**get_parcel_protection_quote**](docs/ParcelProtectionApi.md#get_parcel_protection_quote) | **POST** /v1/parcel-protection/quote | Parcel Protection Quote
*ParcelProtectionApi* | [**get_parcel_protection_reports**](docs/ParcelProtectionApi.md#get_parcel_protection_reports) | **GET** /v1/parcel-protection/{developerId}/policies | Parcel Protection Reports
*PickupApi* | [**cancel_pickup**](docs/PickupApi.md#cancel_pickup) | **POST** /v1/pickups/{pickupId}/cancel | Cancel Pickup
*PickupApi* | [**get_pickupschedule**](docs/PickupApi.md#get_pickupschedule) | **POST** /v1/pickups/schedule | Address validation
*RateParcelsApi* | [**rate_parcel**](docs/RateParcelsApi.md#rate_parcel) | **POST** /v1/rates | Use this operation to rate a parcel before you print and purchase a shipment label. You can rate a parcel for multiple services and multiple parcel types with a single API request.
*ShipmentApi* | [**cancel_shipment**](docs/ShipmentApi.md#cancel_shipment) | **DELETE** /v1/shipments/{shipmentId} | cancelShipment
*ShipmentApi* | [**create_shipment_label**](docs/ShipmentApi.md#create_shipment_label) | **POST** /v1/shipments | This operation creates a shipment and purchases a shipment label.
*ShipmentApi* | [**reprint_shipment**](docs/ShipmentApi.md#reprint_shipment) | **GET** /v1/shipments/{shipmentId} | reprintShipment
*ShipmentApi* | [**retry_shipment**](docs/ShipmentApi.md#retry_shipment) | **GET** /v1/shipments | retryShipment
*TrackingApi* | [**add_tracking_events**](docs/TrackingApi.md#add_tracking_events) | **POST** /v2/track/events | getTrackingDetails
*TrackingApi* | [**get_tracking_details**](docs/TrackingApi.md#get_tracking_details) | **GET** /v1/tracking/{trackingNumber} | getTrackingDetails
*TransactionReportsApi* | [**get_transaction_report**](docs/TransactionReportsApi.md#get_transaction_report) | **GET** /v4/ledger/developers/{developerId}/transactions/reports | This operation retrieves all transactions for a specified period of time.


## Documentation For Models

 - [AddTrackingEvents](docs/AddTrackingEvents.md)
 - [AddTrackingEventsEvents](docs/AddTrackingEventsEvents.md)
 - [AddTrackingEventsReferences](docs/AddTrackingEventsReferences.md)
 - [AdditionalAddress](docs/AdditionalAddress.md)
 - [Address](docs/Address.md)
 - [AddressSuggestionResponse](docs/AddressSuggestionResponse.md)
 - [AddressSuggestionResponseSuggestions](docs/AddressSuggestionResponseSuggestions.md)
 - [AddressVerifySuggest](docs/AddressVerifySuggest.md)
 - [BatteryDetails](docs/BatteryDetails.md)
 - [CancelShipment](docs/CancelShipment.md)
 - [Carrier](docs/Carrier.md)
 - [CarrierFacilityRequest](docs/CarrierFacilityRequest.md)
 - [CarrierFacilityRequestAddress](docs/CarrierFacilityRequestAddress.md)
 - [CarrierFacilityResponse](docs/CarrierFacilityResponse.md)
 - [CarrierFacilityResponseCarrierFacilityOptions](docs/CarrierFacilityResponseCarrierFacilityOptions.md)
 - [CarrierFacilityResponseCarrierFacilitySuggestions](docs/CarrierFacilityResponseCarrierFacilitySuggestions.md)
 - [CarrierFacilityResponseFacilityHours](docs/CarrierFacilityResponseFacilityHours.md)
 - [CarrierFacilityResponseFacilityTimings](docs/CarrierFacilityResponseFacilityTimings.md)
 - [CarrierPayment](docs/CarrierPayment.md)
 - [CarrierRule](docs/CarrierRule.md)
 - [CommodityInfo](docs/CommodityInfo.md)
 - [ContainerDetails](docs/ContainerDetails.md)
 - [ContainerManifestResponse](docs/ContainerManifestResponse.md)
 - [ContainerManifestResponseData](docs/ContainerManifestResponseData.md)
 - [CrossBorderQuotesErrors](docs/CrossBorderQuotesErrors.md)
 - [CrossBorderQuotesErrorsErrors](docs/CrossBorderQuotesErrorsErrors.md)
 - [CrossBorderQuotesErrorsErrorsErrors](docs/CrossBorderQuotesErrorsErrorsErrors.md)
 - [CrossBorderQuotesErrorsQuote](docs/CrossBorderQuotesErrorsQuote.md)
 - [CrossBorderQuotesErrorsQuoteLines](docs/CrossBorderQuotesErrorsQuoteLines.md)
 - [CrossBorderQuotesErrorsUnitErrors](docs/CrossBorderQuotesErrorsUnitErrors.md)
 - [CrossBorderQuotesRequest](docs/CrossBorderQuotesRequest.md)
 - [CrossBorderQuotesRequestAttributes](docs/CrossBorderQuotesRequestAttributes.md)
 - [CrossBorderQuotesRequestBasketItems](docs/CrossBorderQuotesRequestBasketItems.md)
 - [CrossBorderQuotesRequestCategories](docs/CrossBorderQuotesRequestCategories.md)
 - [CrossBorderQuotesRequestDescriptions](docs/CrossBorderQuotesRequestDescriptions.md)
 - [CrossBorderQuotesRequestIdentifiers](docs/CrossBorderQuotesRequestIdentifiers.md)
 - [CrossBorderQuotesRequestItemDimension](docs/CrossBorderQuotesRequestItemDimension.md)
 - [CrossBorderQuotesRequestPricing](docs/CrossBorderQuotesRequestPricing.md)
 - [CrossBorderQuotesRequestPricingCodPrice](docs/CrossBorderQuotesRequestPricingCodPrice.md)
 - [CrossBorderQuotesRequestRates](docs/CrossBorderQuotesRequestRates.md)
 - [CrossBorderQuotesRequestUnitWeight](docs/CrossBorderQuotesRequestUnitWeight.md)
 - [CrossBorderQuotesResponse](docs/CrossBorderQuotesResponse.md)
 - [CrossBorderQuotesResponseLineRates](docs/CrossBorderQuotesResponseLineRates.md)
 - [CrossBorderQuotesResponseQuote](docs/CrossBorderQuotesResponseQuote.md)
 - [CrossBorderQuotesResponseQuoteLines](docs/CrossBorderQuotesResponseQuoteLines.md)
 - [CrossBorderQuotesResponseTotalRates](docs/CrossBorderQuotesResponseTotalRates.md)
 - [CrossBorderQuotesResponseUnitRates](docs/CrossBorderQuotesResponseUnitRates.md)
 - [CrossBorderQuotesResponseUnitRatesDeliveryCommitment](docs/CrossBorderQuotesResponseUnitRatesDeliveryCommitment.md)
 - [Customs](docs/Customs.md)
 - [CustomsInfo](docs/CustomsInfo.md)
 - [CustomsItem](docs/CustomsItem.md)
 - [DeliveryCommitment](docs/DeliveryCommitment.md)
 - [DimensionRules](docs/DimensionRules.md)
 - [DimensionRulesMaxParcelDimensions](docs/DimensionRulesMaxParcelDimensions.md)
 - [DimensionRulesMinParcelDimensions](docs/DimensionRulesMinParcelDimensions.md)
 - [Discount](docs/Discount.md)
 - [DocTabItem](docs/DocTabItem.md)
 - [Document](docs/Document.md)
 - [DocumentPage](docs/DocumentPage.md)
 - [Errors](docs/Errors.md)
 - [HazmatDetails](docs/HazmatDetails.md)
 - [ISOCountryCode](docs/ISOCountryCode.md)
 - [InfectiousSubstanceContact](docs/InfectiousSubstanceContact.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [Manifest](docs/Manifest.md)
 - [PageRealTransactionDetailReport](docs/PageRealTransactionDetailReport.md)
 - [Parameter](docs/Parameter.md)
 - [Parcel](docs/Parcel.md)
 - [ParcelDimension](docs/ParcelDimension.md)
 - [ParcelProtectionCreateRequest](docs/ParcelProtectionCreateRequest.md)
 - [ParcelProtectionCreateRequestShipmentInfo](docs/ParcelProtectionCreateRequestShipmentInfo.md)
 - [ParcelProtectionCreateRequestShipmentInfoConsigneeInfo](docs/ParcelProtectionCreateRequestShipmentInfoConsigneeInfo.md)
 - [ParcelProtectionCreateRequestShipmentInfoParcelInfo](docs/ParcelProtectionCreateRequestShipmentInfoParcelInfo.md)
 - [ParcelProtectionCreateRequestShipmentInfoParcelInfoCommodityList](docs/ParcelProtectionCreateRequestShipmentInfoParcelInfoCommodityList.md)
 - [ParcelProtectionCreateRequestShipmentInfoShipperInfo](docs/ParcelProtectionCreateRequestShipmentInfoShipperInfo.md)
 - [ParcelProtectionCreateRequestShipmentInfoShipperInfoAddress](docs/ParcelProtectionCreateRequestShipmentInfoShipperInfoAddress.md)
 - [ParcelProtectionCreateResponse](docs/ParcelProtectionCreateResponse.md)
 - [ParcelProtectionCreateResponseParcelProtectionFeesBreakup](docs/ParcelProtectionCreateResponseParcelProtectionFeesBreakup.md)
 - [ParcelProtectionPolicyResponse](docs/ParcelProtectionPolicyResponse.md)
 - [ParcelProtectionPolicyResponseContent](docs/ParcelProtectionPolicyResponseContent.md)
 - [ParcelProtectionPolicyResponsePolicyDetails](docs/ParcelProtectionPolicyResponsePolicyDetails.md)
 - [ParcelProtectionPolicyResponseShipmentDetails](docs/ParcelProtectionPolicyResponseShipmentDetails.md)
 - [ParcelProtectionPolicyResponseShipperInfo](docs/ParcelProtectionPolicyResponseShipperInfo.md)
 - [ParcelProtectionPolicyResponseShipperInfoAddress](docs/ParcelProtectionPolicyResponseShipperInfoAddress.md)
 - [ParcelProtectionPolicyResponseSort](docs/ParcelProtectionPolicyResponseSort.md)
 - [ParcelProtectionQuoteRequest](docs/ParcelProtectionQuoteRequest.md)
 - [ParcelProtectionQuoteRequestShipmentInfo](docs/ParcelProtectionQuoteRequestShipmentInfo.md)
 - [ParcelProtectionQuoteRequestShipmentInfoConsigneeInfo](docs/ParcelProtectionQuoteRequestShipmentInfoConsigneeInfo.md)
 - [ParcelProtectionQuoteRequestShipmentInfoParcelInfo](docs/ParcelProtectionQuoteRequestShipmentInfoParcelInfo.md)
 - [ParcelProtectionQuoteRequestShipmentInfoParcelInfoCommodityList](docs/ParcelProtectionQuoteRequestShipmentInfoParcelInfoCommodityList.md)
 - [ParcelProtectionQuoteRequestShipmentInfoShipperInfo](docs/ParcelProtectionQuoteRequestShipmentInfoShipperInfo.md)
 - [ParcelProtectionQuoteRequestShipmentInfoShipperInfoAddress](docs/ParcelProtectionQuoteRequestShipmentInfoShipperInfoAddress.md)
 - [ParcelProtectionQuoteResponse](docs/ParcelProtectionQuoteResponse.md)
 - [ParcelProtectionQuoteResponseParcelProtectionFeesBreakup](docs/ParcelProtectionQuoteResponseParcelProtectionFeesBreakup.md)
 - [ParcelType](docs/ParcelType.md)
 - [ParcelTypeRules](docs/ParcelTypeRules.md)
 - [ParcelWeight](docs/ParcelWeight.md)
 - [PrerequisiteRules](docs/PrerequisiteRules.md)
 - [RadioActiveParcelDimension](docs/RadioActiveParcelDimension.md)
 - [RadioActivityDetail](docs/RadioActivityDetail.md)
 - [RadioNuclideDetail](docs/RadioNuclideDetail.md)
 - [Rate](docs/Rate.md)
 - [RealTransactionDetailReport](docs/RealTransactionDetailReport.md)
 - [SchedulePickup](docs/SchedulePickup.md)
 - [SchedulePickupPickupSummary](docs/SchedulePickupPickupSummary.md)
 - [SchedulePickupResponse](docs/SchedulePickupResponse.md)
 - [SchedulePickupTotalWeight](docs/SchedulePickupTotalWeight.md)
 - [SearchCriteria](docs/SearchCriteria.md)
 - [Services](docs/Services.md)
 - [ServicesParameterRule](docs/ServicesParameterRule.md)
 - [Shipment](docs/Shipment.md)
 - [Signatory](docs/Signatory.md)
 - [SpecialService](docs/SpecialService.md)
 - [SpecialServiceCodes](docs/SpecialServiceCodes.md)
 - [SpecialServicesRule](docs/SpecialServicesRule.md)
 - [Surcharge](docs/Surcharge.md)
 - [Tax](docs/Tax.md)
 - [Trackable](docs/Trackable.md)
 - [TrackingAddress](docs/TrackingAddress.md)
 - [TrackingResponse](docs/TrackingResponse.md)
 - [TrackingResponseScanDetailsList](docs/TrackingResponseScanDetailsList.md)
 - [UnitOfDimension](docs/UnitOfDimension.md)
 - [UnitOfWeight](docs/UnitOfWeight.md)
 - [VoidParcelProtectionRequest](docs/VoidParcelProtectionRequest.md)
 - [VoidParcelProtectionResponse](docs/VoidParcelProtectionResponse.md)
 - [WeightRules](docs/WeightRules.md)


## Documentation For Authorization


## oAuth2ClientCredentials

- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: 
- **Scopes**: N/A


## Author

support@pb.com


