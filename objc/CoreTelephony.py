'''
Classes from the 'CoreTelephony' framework.
'''
    
try:
    from rubicon.objc import ObjCClass
except ValueError:
    def ObjCClass(name):
        return None
        
def _Class(name):
    try:
        return ObjCClass(name)
    except NameError:
        return None
    
    
CTDisplayPlanList = _Class('CTDisplayPlanList')
CTDisplayPlan = _Class('CTDisplayPlan')
CTEmergencyModeResult = _Class('CTEmergencyModeResult')
CTDeviceDataUsage = _Class('CTDeviceDataUsage')
CTPerAppDataUsage = _Class('CTPerAppDataUsage')
CTAppDataUsage = _Class('CTAppDataUsage')
CTDataUsed = _Class('CTDataUsed')
CTDataUsage = _Class('CTDataUsage')
CTXPCContexts = _Class('CTXPCContexts')
CTXPCContextInfo = _Class('CTXPCContextInfo')
CTXPCSimLessContexts = _Class('CTXPCSimLessContexts')
CTXPCSimLessContextInfo = _Class('CTXPCSimLessContextInfo')
CTXPCServiceSubscriptionInfo = _Class('CTXPCServiceSubscriptionInfo')
CTXPCServiceSubscriptionContext = _Class('CTXPCServiceSubscriptionContext')
CTBandInfo = _Class('CTBandInfo')
CTRadioAccessTechnology = _Class('CTRadioAccessTechnology')
CTSweetgumUsageAccountMetrics = _Class('CTSweetgumUsageAccountMetrics')
CTLocalDevice = _Class('CTLocalDevice')
CTSubscriber = _Class('CTSubscriber')
CTBundle = _Class('CTBundle')
CTCellularData = _Class('CTCellularData')
CTSubscriberInfo = _Class('CTSubscriberInfo')
CTCallForwardingValue = _Class('CTCallForwardingValue')
CTVoicemailInfoType = _Class('CTVoicemailInfoType')
CTSweetgumDataPlanMetrics = _Class('CTSweetgumDataPlanMetrics')
CTBinarySMS = _Class('CTBinarySMS')
CTSMSDataType = _Class('CTSMSDataType')
CTPlanList = _Class('CTPlanList')
CTSuppServicesNotificationData = _Class('CTSuppServicesNotificationData')
CTInstalledPlan = _Class('CTInstalledPlan')
CTRemoteDeviceList = _Class('CTRemoteDeviceList')
CTSubscriberAuthDataHolder = _Class('CTSubscriberAuthDataHolder')
CTDataSettings = _Class('CTDataSettings')
CTSweetgumCapabilities = _Class('CTSweetgumCapabilities')
CTPhoneBookEntry = _Class('CTPhoneBookEntry')
CTSweetgumUsagePlanItemMessages = _Class('CTSweetgumUsagePlanItemMessages')
CTIMSRegistrationTransportInfo = _Class('CTIMSRegistrationTransportInfo')
CTCallCapabilities = _Class('CTCallCapabilities')
CTDeviceIdentifier = _Class('CTDeviceIdentifier')
CTActivationPolicyState = _Class('CTActivationPolicyState')
CTSweetgumAppsInfo = _Class('CTSweetgumAppsInfo')
CTEmergencyMode = _Class('CTEmergencyMode')
CTPhoneNumberInfo = _Class('CTPhoneNumberInfo')
CTCellInfo = _Class('CTCellInfo')
CTSubscriberAuthResult = _Class('CTSubscriberAuthResult')
CTSubscriberAuthRequest = _Class('CTSubscriberAuthRequest')
CTSubscriberAlgorithm = _Class('CTSubscriberAlgorithm')
CTSubscriberAlgorithmEAPAKA = _Class('CTSubscriberAlgorithmEAPAKA')
CTSubscriberAlgorithmEAPSIM = _Class('CTSubscriberAlgorithmEAPSIM')
CTRemoteDevice = _Class('CTRemoteDevice')
CTSweetgumPlan = _Class('CTSweetgumPlan')
CTNetworkList = _Class('CTNetworkList')
CTSweetgumPlansInfo = _Class('CTSweetgumPlansInfo')
CTSIMToolkitMenu = _Class('CTSIMToolkitMenu')
CoreTelephonyClient = _Class('CoreTelephonyClient')
CTSignalStrengthMeasurements = _Class('CTSignalStrengthMeasurements')
CTSignalStrengthInfo = _Class('CTSignalStrengthInfo')
CTCall = _Class('CTCall')
CTCallCenter = _Class('CTCallCenter')
CoreTelephonyClientMux = _Class('CoreTelephonyClientMux')
CTRadioFrequencyFrontEndScanData = _Class('CTRadioFrequencyFrontEndScanData')
CTNetworkSelectionInfo = _Class('CTNetworkSelectionInfo')
CTEncryptionStatusInfo = _Class('CTEncryptionStatusInfo')
CTRemotePlanIdentifierList = _Class('CTRemotePlanIdentifierList')
CTPlanIdentifier = _Class('CTPlanIdentifier')
CTRemotePlanIdentifier = _Class('CTRemotePlanIdentifier')
CTXPCError = _Class('CTXPCError')
CTTelephonyNetworkInfo = _Class('CTTelephonyNetworkInfo')
CTPhoneNumber = _Class('CTPhoneNumber')
CTCarrier = _Class('CTCarrier')
CTCellularPlanProvisioningRequest = _Class('CTCellularPlanProvisioningRequest')
CTMobileEquipmentInfoList = _Class('CTMobileEquipmentInfoList')
CTMobileEquipmentInfo = _Class('CTMobileEquipmentInfo')
CTDataStatus = _Class('CTDataStatus')
CTEnhancedLinkQualityMetric = _Class('CTEnhancedLinkQualityMetric')
CTEnhancedDataLinkQualityMetric = _Class('CTEnhancedDataLinkQualityMetric')
CTVoiceLinkQualityMetric = _Class('CTVoiceLinkQualityMetric')
CTCellularPlanManagerCameraScanAction = _Class('CTCellularPlanManagerCameraScanAction')
CTCellularPlanProvisioning = _Class('CTCellularPlanProvisioning')
CTIMSRegistrationStatus = _Class('CTIMSRegistrationStatus')
CTServiceDescriptorContainer = _Class('CTServiceDescriptorContainer')
CTServiceDescriptor = _Class('CTServiceDescriptor')
CTEmailAddress = _Class('CTEmailAddress')
CTSIMToolkitItemList = _Class('CTSIMToolkitItemList')
CTSIMToolkitItem = _Class('CTSIMToolkitItem')
CTMessageStatus = _Class('CTMessageStatus')
CTCellularPlanProvisioningOnDeviceActivationRequest = _Class('CTCellularPlanProvisioningOnDeviceActivationRequest')
CTPNRContextInfo = _Class('CTPNRContextInfo')
CTPNRRequestSentInfo = _Class('CTPNRRequestSentInfo')
CTPNRRequestType = _Class('CTPNRRequestType')
CTPNRDataType = _Class('CTPNRDataType')
CTDataConnectionStatus = _Class('CTDataConnectionStatus')
CTAudioCodecInfo = _Class('CTAudioCodecInfo')
CTSimLabel = _Class('CTSimLabel')
CTMessagePart = _Class('CTMessagePart')
CTMmsEncoder = _Class('CTMmsEncoder')
CTCellIdInfo = _Class('CTCellIdInfo')
CTMmsRegistrationFailureInfoType = _Class('CTMmsRegistrationFailureInfoType')
CTMessageCenter = _Class('CTMessageCenter')
CTPlan = _Class('CTPlan')
CTRemotePlan = _Class('CTRemotePlan')
CTRemoteBlacklistPlan = _Class('CTRemoteBlacklistPlan')
CTPendingPlan = _Class('CTPendingPlan')
CTSweetgumUsagePlanItemData = _Class('CTSweetgumUsagePlanItemData')
CTSweetgumUserConsentFlowInfo = _Class('CTSweetgumUserConsentFlowInfo')
CTNetwork = _Class('CTNetwork')
CTSweetgumDataPlanMetricsItem = _Class('CTSweetgumDataPlanMetricsItem')
CTRegistrationDisplayStatus = _Class('CTRegistrationDisplayStatus')
CTRatSelection = _Class('CTRatSelection')
CTAsciiAddress = _Class('CTAsciiAddress')
CTSweetgumPlanGroup = _Class('CTSweetgumPlanGroup')
CTDataConnectionAvailabilityStatus = _Class('CTDataConnectionAvailabilityStatus')
CTSweetgumUsageInfo = _Class('CTSweetgumUsageInfo')
CTSupportedMaxDataRates = _Class('CTSupportedMaxDataRates')
CTMessage = _Class('CTMessage')
CTSweetgumUsagePlanMetrics = _Class('CTSweetgumUsagePlanMetrics')
CTServiceDisconnectionStatus = _Class('CTServiceDisconnectionStatus')
CTPlanTransferAttributes = _Class('CTPlanTransferAttributes')
CTTetheringStatus = _Class('CTTetheringStatus')
CTPriVersion = _Class('CTPriVersion')
CTSweetgumUsagePlanItemVoice = _Class('CTSweetgumUsagePlanItemVoice')
CTSweetgumDataPlanMetricsError = _Class('CTSweetgumDataPlanMetricsError')
MuxNotificationSink = _Class('MuxNotificationSink')
CoreTelephonyClientRemoteAsyncProxy = _Class('CoreTelephonyClientRemoteAsyncProxy')
CoreTelephonyClientDelegateProxy = _Class('CoreTelephonyClientDelegateProxy')