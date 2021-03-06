'''
Classes from the 'BaseBoard' framework.
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

    
BSCopyingCacheSet = _Class('BSCopyingCacheSet')
BSPersistentTimer = _Class('BSPersistentTimer')
_BSProtobufTranslator_BSAuditToken = _Class('_BSProtobufTranslator_BSAuditToken')
BSDateFormatterCache = _Class('BSDateFormatterCache')
BSProcessDeathWatcher = _Class('BSProcessDeathWatcher')
BSSignal = _Class('BSSignal')
BSAuditHistory = _Class('BSAuditHistory')
BSLogStateCaptureEntry = _Class('BSLogStateCaptureEntry')
BSStateCaptureInvalidator = _Class('BSStateCaptureInvalidator')
BSSystemContainerForCurrentProcessPathProvider = _Class('BSSystemContainerForCurrentProcessPathProvider')
BSCurrentContainerPathProvider = _Class('BSCurrentContainerPathProvider')
BSPathProviderFactory = _Class('BSPathProviderFactory')
BSBuildVersion = _Class('BSBuildVersion')
BSMonotonicReferenceTime = _Class('BSMonotonicReferenceTime')
BSDescriptionStream = _Class('BSDescriptionStream')
BSMIGServer = _Class('BSMIGServer')
BSBlockSentinel = _Class('BSBlockSentinel')
BSBlockSentinelSignalContext = _Class('BSBlockSentinelSignalContext')
BSStackFrameInfo = _Class('BSStackFrameInfo')
BSTimer = _Class('BSTimer')
BSCFBundle = _Class('BSCFBundle')
BSActionListenerController = _Class('BSActionListenerController')
BSActionListenerToken = _Class('BSActionListenerToken')
_BSDefaultObserver = _Class('_BSDefaultObserver')
BSBasicServerClient = _Class('BSBasicServerClient')
BSRelativeDateTimer = _Class('BSRelativeDateTimer')
BSDateTimeCache = _Class('BSDateTimeCache')
BSEventQueueEvent = _Class('BSEventQueueEvent')
BSPowerMonitor = _Class('BSPowerMonitor')
BSWatchdog = _Class('BSWatchdog')
BSXPCReply = _Class('BSXPCReply')
BSXPCMessage = _Class('BSXPCMessage')
BSPluginManager = _Class('BSPluginManager')
BSPortDeathSentinel = _Class('BSPortDeathSentinel')
BSPortDeathWatcher = _Class('BSPortDeathWatcher')
BSPluginSpecification = _Class('BSPluginSpecification')
BSEventQueue = _Class('BSEventQueue')
BSPluginManagerCoordinator = _Class('BSPluginManagerCoordinator')
BSXPCConnectionListenerManager = _Class('BSXPCConnectionListenerManager')
BSXPCConnectionListener = _Class('BSXPCConnectionListener')
BSPluginBundle = _Class('BSPluginBundle')
BSDispatchSource = _Class('BSDispatchSource')
BSCompoundAssertion = _Class('BSCompoundAssertion')
_BSCompoundAssertionAcquisition = _Class('_BSCompoundAssertionAcquisition')
_BSCompoundAssertionState = _Class('_BSCompoundAssertionState')
BSEventQueueLock = _Class('BSEventQueueLock')
BSSqliteDatabaseConnection = _Class('BSSqliteDatabaseConnection')
BSTransaction = _Class('BSTransaction')
BSBlockTransaction = _Class('BSBlockTransaction')
_BSTransactionChildRelationship = _Class('_BSTransactionChildRelationship')
_BSTransactionParentRelationship = _Class('_BSTransactionParentRelationship')
BSSharedMemoryStore = _Class('BSSharedMemoryStore')
BSBaseXPCServer = _Class('BSBaseXPCServer')
BSActionListener = _Class('BSActionListener')
BSAuditHistoryItem = _Class('BSAuditHistoryItem')
BSTransactionBlockObserver = _Class('BSTransactionBlockObserver')
BSPlatform = _Class('BSPlatform')
BSSqlitePreparedStatement = _Class('BSSqlitePreparedStatement')
_BSSqlitePreparedCompoundStatement = _Class('_BSSqlitePreparedCompoundStatement')
_BSSqlitePreparedSimpleStatement = _Class('_BSSqlitePreparedSimpleStatement')
_BSSqliteDeferredPreparedSimpleStatement = _Class('_BSSqliteDeferredPreparedSimpleStatement')
BSSqliteResultRow = _Class('BSSqliteResultRow')
_BSSqliteFrozenResultRow = _Class('_BSSqliteFrozenResultRow')
BSCGImageFromIOSurfaceBuilder = _Class('BSCGImageFromIOSurfaceBuilder')
BSXPCBundle = _Class('BSXPCBundle')
BSBaseXPCClient = _Class('BSBaseXPCClient')
BSProtobufSchema = _Class('BSProtobufSchema')
BSProtobufSerialization = _Class('BSProtobufSerialization')
BSActionResponse = _Class('BSActionResponse')
BSAnimationSettings = _Class('BSAnimationSettings')
BSSpringAnimationSettings = _Class('BSSpringAnimationSettings')
BSMutableSpringAnimationSettings = _Class('BSMutableSpringAnimationSettings')
BSMutableAnimationSettings = _Class('BSMutableAnimationSettings')
BSAtomicFlag = _Class('BSAtomicFlag')
BSPropertyMetadata = _Class('BSPropertyMetadata')
BSAbstractDefaultDomainClassMetadata = _Class('BSAbstractDefaultDomainClassMetadata')
BSAbstractDefaultDomain = _Class('BSAbstractDefaultDomain')
_BSTransactionDefaults = _Class('_BSTransactionDefaults')
BSEqualsBuilder = _Class('BSEqualsBuilder')
BSDescriptionBuilder = _Class('BSDescriptionBuilder')
BSXPCCodingArray = _Class('BSXPCCodingArray')
BSCornerRadiusConfiguration = _Class('BSCornerRadiusConfiguration')
BSSettingsDiff = _Class('BSSettingsDiff')
BSColor = _Class('BSColor')
BSHashBuilder = _Class('BSHashBuilder')
BSSettings = _Class('BSSettings')
BSKeyedSettings = _Class('BSKeyedSettings')
BSMutableKeyedSettings = _Class('BSMutableKeyedSettings')
BSMutableSettings = _Class('BSMutableSettings')
BSAuditToken = _Class('BSAuditToken')
BSMachPortRight = _Class('BSMachPortRight')
BSMachPortReceiveRight = _Class('BSMachPortReceiveRight')
BSMachPortSendRight = _Class('BSMachPortSendRight')
BSMachPortTransferableSendRight = _Class('BSMachPortTransferableSendRight')
BSMachPortTaskNameRight = _Class('BSMachPortTaskNameRight')
BSProcessHandle = _Class('BSProcessHandle')
BSZeroingWeakReference = _Class('BSZeroingWeakReference')
BSAction = _Class('BSAction')
BSXPCCoder = _Class('BSXPCCoder')
BSObjCArgument = _Class('BSObjCArgument')
BSObjCBlockArgument = _Class('BSObjCBlockArgument')
BSObjCMethod = _Class('BSObjCMethod')
BSObjCProtocol = _Class('BSObjCProtocol')
BSUIApplicationSupport = _Class('BSUIApplicationSupport')
BSIntegerSet = _Class('BSIntegerSet')
BSMutableIntegerSet = _Class('BSMutableIntegerSet')
BSIntegerMap = _Class('BSIntegerMap')
BSMutableIntegerMap = _Class('BSMutableIntegerMap')
BSDispatchQueueAttributes = _Class('BSDispatchQueueAttributes')
BSAtomicSignal = _Class('BSAtomicSignal')
BSSimpleAssertion = _Class('BSSimpleAssertion')
BSUserDefaultsTestDoubleDictionaryImpl = _Class('BSUserDefaultsTestDoubleDictionaryImpl')
BSError = _Class('BSError')
