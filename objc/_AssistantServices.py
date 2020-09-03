'''
Classes from the 'AssistantServices' framework.
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

    
AFAccessibilityObserver = _Class('AFAccessibilityObserver')
AFSiriTask = _Class('AFSiriTask')
AFClientInfo = _Class('AFClientInfo')
AFPeerInfo = _Class('AFPeerInfo')
AFSyncSnapshot = _Class('AFSyncSnapshot')
AFContextDonationService = _Class('AFContextDonationService')
AFPowerAssertionManager = _Class('AFPowerAssertionManager')
AFClockAlarm = _Class('AFClockAlarm')
AFApplicationInfo = _Class('AFApplicationInfo')
AFRequestCompletionOptions = _Class('AFRequestCompletionOptions')
AFChildConversationItemList = _Class('AFChildConversationItemList')
AFInterstitialCommandWrapper = _Class('AFInterstitialCommandWrapper')
AFMediaPlaybackStateSnapshot = _Class('AFMediaPlaybackStateSnapshot')
AFConversationInsertion = _Class('AFConversationInsertion')
AFPairedBluetoothDevicesObserver = _Class('AFPairedBluetoothDevicesObserver')
AFConnectionEntitlementCache = _Class('AFConnectionEntitlementCache')
AFSiriActivationResult = _Class('AFSiriActivationResult')
AFAnalyticsEvent = _Class('AFAnalyticsEvent')
STSiriContext = _Class('STSiriContext')
AFMultiUserConnection = _Class('AFMultiUserConnection')
AFInterstitialConfiguration = _Class('AFInterstitialConfiguration')
AFMyriadEmergencyCallPunchout = _Class('AFMyriadEmergencyCallPunchout')
AFSpeechSynthesisRecord = _Class('AFSpeechSynthesisRecord')
AFSiriActivationRequest = _Class('AFSiriActivationRequest')
AFSiriAceRequest = _Class('AFSiriAceRequest')
AFSiriMusicSmartPlayRequest = _Class('AFSiriMusicSmartPlayRequest')
AFSiriMusicSubscriptionLeaseTakenRequest = _Class('AFSiriMusicSubscriptionLeaseTakenRequest')
AFSiriAcousticIDRequest = _Class('AFSiriAcousticIDRequest')
AFSiriClientStateManager = _Class('AFSiriClientStateManager')
AFAnalyticsObserverConnection = _Class('AFAnalyticsObserverConnection')
AFAppContextAggregator = _Class('AFAppContextAggregator')
AFBluetoothWirelessSplitterSessionStateObserver = _Class('AFBluetoothWirelessSplitterSessionStateObserver')
STPersonContactHandle = _Class('STPersonContactHandle')
AFNotifyStatePublisher = _Class('AFNotifyStatePublisher')
AFAudioPowerUpdater = _Class('AFAudioPowerUpdater')
AFSharedConfidenceScore = _Class('AFSharedConfidenceScore')
AFMyriadCoordinator = _Class('AFMyriadCoordinator')
AFApplicationContext = _Class('AFApplicationContext')
AFConversationItem = _Class('AFConversationItem')
AFBundleResource = _Class('AFBundleResource')
AFAudioPlaybackRequest = _Class('AFAudioPlaybackRequest')
AFSiriTether = _Class('AFSiriTether')
AFAggregator = _Class('AFAggregator')
AFSpeechAudioAnalytics = _Class('AFSpeechAudioAnalytics')
AFSpeechAcousticFeature = _Class('AFSpeechAcousticFeature')
AFClockAlarmObserver = _Class('AFClockAlarmObserver')
AFInstrumentationObserverConnection = _Class('AFInstrumentationObserverConnection')
AFMachServiceSiriTaskDeliverer = _Class('AFMachServiceSiriTaskDeliverer')
AFAnalyticsTurnBasedInstrumentationContext = _Class('AFAnalyticsTurnBasedInstrumentationContext')
AFDialogPhase = _Class('AFDialogPhase')
AFBulletin = _Class('AFBulletin')
AFMyriadEmergencyManager = _Class('AFMyriadEmergencyManager')
AFUIApplicationSiriTaskDeliverer = _Class('AFUIApplicationSiriTaskDeliverer')
AFClockTimerObserver = _Class('AFClockTimerObserver')
AFUtteranceSuggestions = _Class('AFUtteranceSuggestions')
AFDeviceRingerSwitchObserver = _Class('AFDeviceRingerSwitchObserver')
AFSiriActivationListener = _Class('AFSiriActivationListener')
AFSiriActivationContext = _Class('AFSiriActivationContext')
AFMemoryInfo = _Class('AFMemoryInfo')
STSiriLocation = _Class('STSiriLocation')
AFDisambiguationStore = _Class('AFDisambiguationStore')
AFAssertionCoordinator = _Class('AFAssertionCoordinator')
AFTreeNodePropertyListSerialization = _Class('AFTreeNodePropertyListSerialization')
AFSiriTaskmaster = _Class('AFSiriTaskmaster')
AFSiriTaskDeliveryHandler = _Class('AFSiriTaskDeliveryHandler')
AFSiriTaskService = _Class('AFSiriTaskService')
AFDeviceCapabilities = _Class('AFDeviceCapabilities')
AFExperimentContext = _Class('AFExperimentContext')
AFClockTimerSnapshot = _Class('AFClockTimerSnapshot')
AFPluginManager = _Class('AFPluginManager')
AFClientPluginManager = _Class('AFClientPluginManager')
AFPluginBundle = _Class('AFPluginBundle')
AFSpeechRequestOptions = _Class('AFSpeechRequestOptions')
AFClockAlarmSnapshot = _Class('AFClockAlarmSnapshot')
AFAudioDeviceInfo = _Class('AFAudioDeviceInfo')
AFLocationSnapshot = _Class('AFLocationSnapshot')
AFSiriActivationHandlerCoreSpeechDaemon = _Class('AFSiriActivationHandlerCoreSpeechDaemon')
AFServiceContextSnapshot = _Class('AFServiceContextSnapshot')
AFServiceMediaPlaybackStateSnapshot = _Class('AFServiceMediaPlaybackStateSnapshot')
AFLinkedListItem = _Class('AFLinkedListItem')
STCity = _Class('STCity')
AFSiriActivationHandlerFrontendProcess = _Class('AFSiriActivationHandlerFrontendProcess')
AFSettingsConnectionServiceDelegate = _Class('AFSettingsConnectionServiceDelegate')
AFSettingsConnection = _Class('AFSettingsConnection')
AFSiriUserNotificationRequestCapabilityManager = _Class('AFSiriUserNotificationRequestCapabilityManager')
AFSiriUserNotificationRequest = _Class('AFSiriUserNotificationRequest')
AFSiriNotificationRequest = _Class('AFSiriNotificationRequest')
AFMetrics = _Class('AFMetrics')
AFMyriadSession = _Class('AFMyriadSession')
AFOpportuneSpeakingModelFeedbackManager = _Class('AFOpportuneSpeakingModelFeedbackManager')
AFOpportuneSpeakingModelFeedback = _Class('AFOpportuneSpeakingModelFeedback')
AFThreeArgumentSafetyBlock = _Class('AFThreeArgumentSafetyBlock')
AFTwoArgumentSafetyBlock = _Class('AFTwoArgumentSafetyBlock')
AFOneArgumentSafetyBlock = _Class('AFOneArgumentSafetyBlock')
AFSafetyBlock = _Class('AFSafetyBlock')
AFFuture = _Class('AFFuture')
AFRemoteRequestWatcher = _Class('AFRemoteRequestWatcher')
AFManagedStorageConnection = _Class('AFManagedStorageConnection')
AFAccount = _Class('AFAccount')
AFTriggerlessListeningOptions = _Class('AFTriggerlessListeningOptions')
AFMemoryPressureObserver = _Class('AFMemoryPressureObserver')
AFAnalyticsEventRecord = _Class('AFAnalyticsEventRecord')
AFAssertionContext = _Class('AFAssertionContext')
AFSpeechCorrectionInfo = _Class('AFSpeechCorrectionInfo')
AFConversationStore = _Class('AFConversationStore')
AFAudioAnalyzer = _Class('AFAudioAnalyzer')
AFBluetoothHeadphoneInEarDetectionState = _Class('AFBluetoothHeadphoneInEarDetectionState')
AFDataStore = _Class('AFDataStore')
AFImagePNGData = _Class('AFImagePNGData')
AFDictationOptions = _Class('AFDictationOptions')
AFLocalization = _Class('AFLocalization')
AFMediaRemoteDeviceInfo = _Class('AFMediaRemoteDeviceInfo')
AFClientLite = _Class('AFClientLite')
AFSynchronousClientLite = _Class('AFSynchronousClientLite')
AFClientLiteInternal = _Class('AFClientLiteInternal')
AFClockItemStorage = _Class('AFClockItemStorage')
AFRequestInfo = _Class('AFRequestInfo')
AFExperiment = _Class('AFExperiment')
AFSpeechRecordingAlertPolicy = _Class('AFSpeechRecordingAlertPolicy')
AFFeatureFlags = _Class('AFFeatureFlags')
AFSiriTaskUsageResult = _Class('AFSiriTaskUsageResult')
AFBluetoothDeviceInfo = _Class('AFBluetoothDeviceInfo')
AFSiriActivationHandlerAssistantDaemon = _Class('AFSiriActivationHandlerAssistantDaemon')
AFDictationConnectionServiceDelegate = _Class('AFDictationConnectionServiceDelegate')
AFNotifyObserver = _Class('AFNotifyObserver')
AFSpeakableUtteranceParser = _Class('AFSpeakableUtteranceParser')
AFSUPFunctionProvider = _Class('AFSUPFunctionProvider')
AFClientConfiguration = _Class('AFClientConfiguration')
AFMyriadMonitor = _Class('AFMyriadMonitor')
AFMyriadAdvertisementContext = _Class('AFMyriadAdvertisementContext')
AFConversation = _Class('AFConversation')
AFCoercion = _Class('AFCoercion')
AFSiriTaskContextProvider = _Class('AFSiriTaskContextProvider')
AFAssistedDisambiguationRules = _Class('AFAssistedDisambiguationRules')
AFTreeNode = _Class('AFTreeNode')
AFAudioState = _Class('AFAudioState')
AFSpeechRecognition = _Class('AFSpeechRecognition')
AFOpportuneSpeakingModuleDataCollection = _Class('AFOpportuneSpeakingModuleDataCollection')
AFOpportuneSpeakingModuleDataCollectionSanitizedSpeakable = _Class('AFOpportuneSpeakingModuleDataCollectionSanitizedSpeakable')
AFConnectionUserInteractionAssertion = _Class('AFConnectionUserInteractionAssertion')
AFMyriadRecord = _Class('AFMyriadRecord')
AFDeleteSiriHistoryContext = _Class('AFDeleteSiriHistoryContext')
AFSpeechToken = _Class('AFSpeechToken')
AFSpeechInterpretation = _Class('AFSpeechInterpretation')
AFSpeechUtterance = _Class('AFSpeechUtterance')
AFSpeechPhrase = _Class('AFSpeechPhrase')
AFDictionarySchema = _Class('AFDictionarySchema')
AFMyriadPerceptualAudioHash = _Class('AFMyriadPerceptualAudioHash')
AFSpeechRecordingAlertBehavior = _Class('AFSpeechRecordingAlertBehavior')
AFSpeechPackage = _Class('AFSpeechPackage')
AFSyncInfo = _Class('AFSyncInfo')
AFAnalyticsConnection = _Class('AFAnalyticsConnection')
AFClockTimer = _Class('AFClockTimer')
AFUserUtteranceSelectionResults = _Class('AFUserUtteranceSelectionResults')
AFUserUtterance = _Class('AFUserUtterance')
AFPersonalUserSettings = _Class('AFPersonalUserSettings')
AFAccessibilityState = _Class('AFAccessibilityState')
AFUserNotificationProvider = _Class('AFUserNotificationProvider')
AFNowPlayingObserver = _Class('AFNowPlayingObserver')
AFContextManager = _Class('AFContextManager')
AFAudioPowerXPCProvider = _Class('AFAudioPowerXPCProvider')
AFError = _Class('AFError')
AFConversationTransaction = _Class('AFConversationTransaction')
AFLanguageDetectionUserContext = _Class('AFLanguageDetectionUserContext')
AFXPCWrapper = _Class('AFXPCWrapper')
AFPhonemeMapper = _Class('AFPhonemeMapper')
AFSiriActivationConnection = _Class('AFSiriActivationConnection')
AFMyriadContext = _Class('AFMyriadContext')
AFMultiUserStateSnapshot = _Class('AFMultiUserStateSnapshot')
AFDisambiguationEvent = _Class('AFDisambiguationEvent')
AFDisambiguationInfo = _Class('AFDisambiguationInfo')
AFWatchdogTimer = _Class('AFWatchdogTimer')
AFSiriResponse = _Class('AFSiriResponse')
AFSetSettingsResponse = _Class('AFSetSettingsResponse')
AFObjectUpdatedSiriResponse = _Class('AFObjectUpdatedSiriResponse')
AFGetSettingsResponse = _Class('AFGetSettingsResponse')
AFContextResponse = _Class('AFContextResponse')
AFCreateAlarmResponse = _Class('AFCreateAlarmResponse')
AFUpdateAlarmResponse = _Class('AFUpdateAlarmResponse')
AFSearchAlarmsResponse = _Class('AFSearchAlarmsResponse')
AFObjectCreatedSiriResponse = _Class('AFObjectCreatedSiriResponse')
AFGetTimerResponse = _Class('AFGetTimerResponse')
AFSiriRequestSucceededResponse = _Class('AFSiriRequestSucceededResponse')
AFExperimentGroup = _Class('AFExperimentGroup')
AFSiriTaskExecution = _Class('AFSiriTaskExecution')
AFRemoteRequest = _Class('AFRemoteRequest')
AFMyriadAdvertisementContextRecord = _Class('AFMyriadAdvertisementContextRecord')
AFPhonemeTranscription = _Class('AFPhonemeTranscription')
AFFlowServiceConnection = _Class('AFFlowServiceConnection')
AFBundleResourceManager = _Class('AFBundleResourceManager')
AFMutableConversationItem = _Class('AFMutableConversationItem')
AFVoiceInfo = _Class('AFVoiceInfo')
STSiriModelObject = _Class('STSiriModelObject')
STPerson = _Class('STPerson')
STSetting = _Class('STSetting')
STCall = _Class('STCall')
STAlarm = _Class('STAlarm')
STSiriMessage = _Class('STSiriMessage')
STSettingChange = _Class('STSettingChange')
STTimer = _Class('STTimer')
STContactAddress = _Class('STContactAddress')
AFBluetoothWirelessSplitterSessionInfo = _Class('AFBluetoothWirelessSplitterSessionInfo')
AFMyriadAdvertisementContextManager = _Class('AFMyriadAdvertisementContextManager')
AFQueue = _Class('AFQueue')
AFSecurityConnection = _Class('AFSecurityConnection')
AFExperimentConfiguration = _Class('AFExperimentConfiguration')
AFDeviceStateConnection = _Class('AFDeviceStateConnection')
AFSiriPhoneticContactNames = _Class('AFSiriPhoneticContactNames')
AFSiriRingtone = _Class('AFSiriRingtone')
AFSiriRequest = _Class('AFSiriRequest')
AFShowAlarmRequest = _Class('AFShowAlarmRequest')
AFContextRequest = _Class('AFContextRequest')
AFInitiateCallRequest = _Class('AFInitiateCallRequest')
AFSearchAlarmsRequest = _Class('AFSearchAlarmsRequest')
AFCreateAlarmRequest = _Class('AFCreateAlarmRequest')
AFShowTimerRequest = _Class('AFShowTimerRequest')
AFShowNextEventRequest = _Class('AFShowNextEventRequest')
AFShowSettingRequest = _Class('AFShowSettingRequest')
AFCreateMessageRequest = _Class('AFCreateMessageRequest')
AFUpdateMessageRequest = _Class('AFUpdateMessageRequest')
AFDeleteAlarmRequest = _Class('AFDeleteAlarmRequest')
AFDismissTimerRequest = _Class('AFDismissTimerRequest')
AFSiriDebugUIRequest = _Class('AFSiriDebugUIRequest')
AFSetTimerRequest = _Class('AFSetTimerRequest')
AFGetTimerRequest = _Class('AFGetTimerRequest')
AFDismissAlarmRequest = _Class('AFDismissAlarmRequest')
AFSetSettingsRequest = _Class('AFSetSettingsRequest')
AFGetSettingsRequest = _Class('AFGetSettingsRequest')
AFUpdateAlarmRequest = _Class('AFUpdateAlarmRequest')
AFInterstitialProvider = _Class('AFInterstitialProvider')
AFConnectionClientServiceDelegate = _Class('AFConnectionClientServiceDelegate')
AFConnection = _Class('AFConnection')
AFConnectionAvailabilityObserver = _Class('AFConnectionAvailabilityObserver')
SISchemaClientAnyEvent = _Class('SISchemaClientAnyEvent')
SISchemaClientTurnContext = _Class('SISchemaClientTurnContext')
SISchemaClientTurnBasedEvent = _Class('SISchemaClientTurnBasedEvent')
AFNetworkAvailability = _Class('AFNetworkAvailability')
AFAnalytics = _Class('AFAnalytics')
AFCallSiteInfo = _Class('AFCallSiteInfo')
AFPreferences = _Class('AFPreferences')
AFDictationConnection = _Class('AFDictationConnection')
AFConversationError = _Class('AFConversationError')
