'''
Classes from the 'AppStoreDaemon' framework.
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

    
ASDBetaAppFeedbackMetadata = _Class('ASDBetaAppFeedbackMetadata')
ASDJobActivity = _Class('ASDJobActivity')
ASDApplicationMetadata = _Class('ASDApplicationMetadata')
ASDClipCardMetricsEvent = _Class('ASDClipCardMetricsEvent')
ASDClipSession = _Class('ASDClipSession')
ASDEnterpriseAppMetadata = _Class('ASDEnterpriseAppMetadata')
ASDTestFlightServiceTransaction = _Class('ASDTestFlightServiceTransaction')
ASDJobSchedulerJobMetadata = _Class('ASDJobSchedulerJobMetadata')
ASDNotification = _Class('ASDNotification')
ASDGatherLogsRequest = _Class('ASDGatherLogsRequest')
ASDRepairService = _Class('ASDRepairService')
ASDRepairApplicationRequest = _Class('ASDRepairApplicationRequest')
ASDPurchaseManager = _Class('ASDPurchaseManager')
ASDRegisterListenerOptions = _Class('ASDRegisterListenerOptions')
ASDJob = _Class('ASDJob')
ASDPurchaseHistoryApp = _Class('ASDPurchaseHistoryApp')
ASDPurchase = _Class('ASDPurchase')
ASDPromise = _Class('ASDPromise')
ASDLazyPromise = _Class('ASDLazyPromise')
ASDSubscriptionEntitlement = _Class('ASDSubscriptionEntitlement')
ASDRequestBroker = _Class('ASDRequestBroker')
ASDBetaAppFeedback = _Class('ASDBetaAppFeedback')
ASDPersonalizationStore = _Class('ASDPersonalizationStore')
ASDManagedAppService = _Class('ASDManagedAppService')
ASDSystemAppMetadata = _Class('ASDSystemAppMetadata')
ASDManifestRequest = _Class('ASDManifestRequest')
ASDStoreItemMetadata = _Class('ASDStoreItemMetadata')
ASDUpdatePollMetrics = _Class('ASDUpdatePollMetrics')
ASDLogConfig = _Class('ASDLogConfig')
ASDMutableLogConfig = _Class('ASDMutableLogConfig')
ASDInGameAnalytics = _Class('ASDInGameAnalytics')
ASDNotificationCenter = _Class('ASDNotificationCenter')
ASDTestFlightAppMetadata = _Class('ASDTestFlightAppMetadata')
ASDJobResult = _Class('ASDJobResult')
ASDTestFlightServiceExtension = _Class('ASDTestFlightServiceExtension')
ASDWatchAppMetadata = _Class('ASDWatchAppMetadata')
ASDCellularIdentity = _Class('ASDCellularIdentity')
ASDUpdateWatchApps = _Class('ASDUpdateWatchApps')
ASDBetaAppVersion = _Class('ASDBetaAppVersion')
ASDLogFileOptions = _Class('ASDLogFileOptions')
ASDCoding = _Class('ASDCoding')
ASDJobOptions = _Class('ASDJobOptions')
ASDInstallAppsObserver = _Class('ASDInstallAppsObserver')
ASDDiagnosticService = _Class('ASDDiagnosticService')
ASDAppEvent = _Class('ASDAppEvent')
ASDVPPRequest = _Class('ASDVPPRequest')
ASDPurchaseResult = _Class('ASDPurchaseResult')
ASDIAPHistory = _Class('ASDIAPHistory')
ASDInstallApps = _Class('ASDInstallApps')
ASDInstallAttribution = _Class('ASDInstallAttribution')
ASDPromiseObserver = _Class('ASDPromiseObserver')
ASDMediaClipTaskResponseDecoder = _Class('ASDMediaClipTaskResponseDecoder')
ASDJobAsset = _Class('ASDJobAsset')
ASDPurchaseHistory = _Class('ASDPurchaseHistory')
ASDJobManifest = _Class('ASDJobManifest')
ASDDispatchQueue = _Class('ASDDispatchQueue')
ASDAppReviewAppMetadata = _Class('ASDAppReviewAppMetadata')
ASDProgressMonitor = _Class('ASDProgressMonitor')
ASDUpdatesService = _Class('ASDUpdatesService')
ASDRollableLog = _Class('ASDRollableLog')
ASDClipMetricsCoordinator = _Class('ASDClipMetricsCoordinator')
ASDInstallAttributionParamsConfig = _Class('ASDInstallAttributionParamsConfig')
ASDPromiseResult = _Class('ASDPromiseResult')
ASDApp = _Class('ASDApp')
ASDRepairOptions = _Class('ASDRepairOptions')
ASDAppQueryExecutor = _Class('ASDAppQueryExecutor')
ASDManagedRequestStatus = _Class('ASDManagedRequestStatus')
ASDPurchaseResponseItem = _Class('ASDPurchaseResponseItem')
ASDUpdateMetricsStore = _Class('ASDUpdateMetricsStore')
ASDBagKeySetAggregator = _Class('ASDBagKeySetAggregator')
ASDTestFlightServiceHost = _Class('ASDTestFlightServiceHost')
ASDServiceBroker = _Class('ASDServiceBroker')
ASDAppUsageStore = _Class('ASDAppUsageStore')
ASDUnfairLock = _Class('ASDUnfairLock')
ASDTestFlightServiceExtensionPushMessage = _Class('ASDTestFlightServiceExtensionPushMessage')
ASDBetaAppLaunchInfo = _Class('ASDBetaAppLaunchInfo')
ASDProgress = _Class('ASDProgress')
ASDPurgeableApp = _Class('ASDPurgeableApp')
ASDAppClusterMapping = _Class('ASDAppClusterMapping')
ASDAppStoreService = _Class('ASDAppStoreService')
ASDAccountStatusTask = _Class('ASDAccountStatusTask')
ASDIAPInfo = _Class('ASDIAPInfo')
ASDMutableIAPInfo = _Class('ASDMutableIAPInfo')
ASDMediaClipTaskURLBuilder = _Class('ASDMediaClipTaskURLBuilder')
ASDBetaAppDisplayNames = _Class('ASDBetaAppDisplayNames')
ASDScreenSyncAppMetadata = _Class('ASDScreenSyncAppMetadata')
ASDPurchaseHistoryQuery = _Class('ASDPurchaseHistoryQuery')
ASDPurchaseHistoryQuerySortOption = _Class('ASDPurchaseHistoryQuerySortOption')
ASDClipRestrictionsTask = _Class('ASDClipRestrictionsTask')
ASDCrossfireStore = _Class('ASDCrossfireStore')
ASDAppUsageStats = _Class('ASDAppUsageStats')
ASDRepairApplicationRequestOptions = _Class('ASDRepairApplicationRequestOptions')
ASDSoftwareUpdateMetrics = _Class('ASDSoftwareUpdateMetrics')
ASDCellularSettings = _Class('ASDCellularSettings')
ASDSubscriptionEntitlements = _Class('ASDSubscriptionEntitlements')
ASDJobManagerOptions = _Class('ASDJobManagerOptions')
ASDTestFlightFeedback = _Class('ASDTestFlightFeedback')
ASDClipRequest = _Class('ASDClipRequest')
ASDClipService = _Class('ASDClipService')
ASDGatherLogsRequestOptions = _Class('ASDGatherLogsRequestOptions')
ASDBaseClient = _Class('ASDBaseClient')
ASDJobManager = _Class('ASDJobManager')
ASDSoftwareUpdatesStore = _Class('ASDSoftwareUpdatesStore')
ASDManagedApplicationRequest = _Class('ASDManagedApplicationRequest')
ASDClaimApplicationsRequest = _Class('ASDClaimApplicationsRequest')
ASDCheckQueueRequest = _Class('ASDCheckQueueRequest')
ASDSoftwareUpdate = _Class('ASDSoftwareUpdate')
ASDAccountStatusResponse = _Class('ASDAccountStatusResponse')
ASDAppLibrary = _Class('ASDAppLibrary')
ASDRequest = _Class('ASDRequest')
ASDPersistentRequest = _Class('ASDPersistentRequest')
ASDSystemAppRequest = _Class('ASDSystemAppRequest')
ASDEphemeralRequest = _Class('ASDEphemeralRequest')
ASDPurgeableAppRequest = _Class('ASDPurgeableAppRequest')
ASDLaunchableAppsRequest = _Class('ASDLaunchableAppsRequest')
ASDIAPInfoUpdateRequest = _Class('ASDIAPInfoUpdateRequest')
ASDCompleteCoordinatorsRequest = _Class('ASDCompleteCoordinatorsRequest')
ASDAccountLookupRequest = _Class('ASDAccountLookupRequest')
ASDMigrationRequest = _Class('ASDMigrationRequest')
ASDPostBulletinRequest = _Class('ASDPostBulletinRequest')
ASDRestoreApplicationsRequest = _Class('ASDRestoreApplicationsRequest')
ASDExternalManifestRequest = _Class('ASDExternalManifestRequest')
ASDInstallManifestRequest = _Class('ASDInstallManifestRequest')
ASDIAPInfoRequest = _Class('ASDIAPInfoRequest')
ASDPushCacheDeleteUpdateRequest = _Class('ASDPushCacheDeleteUpdateRequest')
ASDCreatePlaceholdersRequest = _Class('ASDCreatePlaceholdersRequest')
ASDRestoreDemotedApplicationsRequest = _Class('ASDRestoreDemotedApplicationsRequest')
ASDJobSchedulerRequest = _Class('ASDJobSchedulerRequest')
ASDPurchaseRequest = _Class('ASDPurchaseRequest')
ASDPurgeAppsRequest = _Class('ASDPurgeAppsRequest')
ASDRequestResponse = _Class('ASDRequestResponse')
ASDInstallManifestRequestResponse = _Class('ASDInstallManifestRequestResponse')
ASDJobSchedulerResponse = _Class('ASDJobSchedulerResponse')
ASDPurchaseResponse = _Class('ASDPurchaseResponse')
ASDPurgeAppsResponse = _Class('ASDPurgeAppsResponse')
ASDExternalManifestResponse = _Class('ASDExternalManifestResponse')
ASDPurgeableAppResponse = _Class('ASDPurgeableAppResponse')
ASDIAPInfoResponse = _Class('ASDIAPInfoResponse')
ASDRestoreApplicationsRequestResponse = _Class('ASDRestoreApplicationsRequestResponse')
ASDAccountLookupResponse = _Class('ASDAccountLookupResponse')
ASDLaunchableAppsResponse = _Class('ASDLaunchableAppsResponse')
ASDAppQuery = _Class('ASDAppQuery')
ASDSyncTaskScheduler = _Class('ASDSyncTaskScheduler')
ASDRequestOptions = _Class('ASDRequestOptions')
ASDRestoreDemotedApplicationsRequestOptions = _Class('ASDRestoreDemotedApplicationsRequestOptions')
ASDPurchaseRequestOptions = _Class('ASDPurchaseRequestOptions')
ASDCreatePlaceholdersRequestOptions = _Class('ASDCreatePlaceholdersRequestOptions')
ASDInstallManifestRequestOptions = _Class('ASDInstallManifestRequestOptions')
ASDMigrationRequestOptions = _Class('ASDMigrationRequestOptions')
ASDAccountLookupRequestOptions = _Class('ASDAccountLookupRequestOptions')
ASDClaimApplicationsRequestOptions = _Class('ASDClaimApplicationsRequestOptions')
ASDManagedApplicationRequestOptions = _Class('ASDManagedApplicationRequestOptions')
ASDPostBulletinRequestOptions = _Class('ASDPostBulletinRequestOptions')
ASDIAPInfoRequestOptions = _Class('ASDIAPInfoRequestOptions')
ASDJobSchedulerRequestOptions = _Class('ASDJobSchedulerRequestOptions')
ASDLaunchableAppsRequestOptions = _Class('ASDLaunchableAppsRequestOptions')
ASDExternalManifestRequestOptions = _Class('ASDExternalManifestRequestOptions')
ASDPurgeAppsRequestOptions = _Class('ASDPurgeAppsRequestOptions')
ASDDownloadQueueRequestOptions = _Class('ASDDownloadQueueRequestOptions')
ASDPurgeableAppRequestOptions = _Class('ASDPurgeableAppRequestOptions')
ASDRestoreApplicationsRequestOptions = _Class('ASDRestoreApplicationsRequestOptions')
ASDCheckQueueRequestOptions = _Class('ASDCheckQueueRequestOptions')
ASDOcelotStore = _Class('ASDOcelotStore')
ASDMediaClipTask = _Class('ASDMediaClipTask')
ASDAggregateClusterMappingData = _Class('ASDAggregateClusterMappingData')
ASDTestFlightServiceExtensionContext = _Class('ASDTestFlightServiceExtensionContext')
ASDTestFlightServiceExtensionHostContext = _Class('ASDTestFlightServiceExtensionHostContext')
ASDTestFlightServiceExtensionRemoteContext = _Class('ASDTestFlightServiceExtensionRemoteContext')
ASDStoreKitServiceBroker = _Class('ASDStoreKitServiceBroker')
ASDStoreKitClientBroker = _Class('ASDStoreKitClientBroker')
