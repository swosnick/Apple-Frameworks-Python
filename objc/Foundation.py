'''
Classes from the 'Foundation' framework.
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
    
    
NSLeafProxy = _Class('NSLeafProxy')
NSEncodingDetectionBuffer = _Class('NSEncodingDetectionBuffer')
NSExtensionService_Subsystem = _Class('NSExtensionService_Subsystem')
NSFileWatcher = _Class('NSFileWatcher')
NSFileWatcherObservations = _Class('NSFileWatcherObservations')
NSFileAccessNode = _Class('NSFileAccessNode')
NSFilePresenterManagedProxy = _Class('NSFilePresenterManagedProxy')
NSFileReactorProxy = _Class('NSFileReactorProxy')
NSFileProviderProxy = _Class('NSFileProviderProxy')
NSFilePresenterProxy = _Class('NSFilePresenterProxy')
NSFileProviderXPCMessenger = _Class('NSFileProviderXPCMessenger')
NSFileAccessSubarbiter = _Class('NSFileAccessSubarbiter')
NSFileAccessArbiter = _Class('NSFileAccessArbiter')
NSFilePromiseWriteToken = _Class('NSFilePromiseWriteToken')
NSDocInfo = _Class('NSDocInfo')
NSAKDeserializer = _Class('NSAKDeserializer')
NSDirInfoDeserializer = _Class('NSDirInfoDeserializer')
NSDocumentDeserializer = _Class('NSDocumentDeserializer')
NSAKSerializer = _Class('NSAKSerializer')
NSDirInfoSerializer = _Class('NSDirInfoSerializer')
NSDocumentSerializer = _Class('NSDocumentSerializer')
NSAKDeserializerStream = _Class('NSAKDeserializerStream')
NSAKSerializerStream = _Class('NSAKSerializerStream')
NSLinguisticTagger = _Class('NSLinguisticTagger')
NSFileAccessProcessManager = _Class('NSFileAccessProcessManager')
NSOrderedCollectionDifference = _Class('NSOrderedCollectionDifference')
NSSmartPunctuationController = _Class('NSSmartPunctuationController')
NSSmartQuoteOptions = _Class('NSSmartQuoteOptions')
NSTextCheckingKeyEvent = _Class('NSTextCheckingKeyEvent')
NSOrthography = _Class('NSOrthography')
NSSimpleOrthography = _Class('NSSimpleOrthography')
NSComplexOrthography = _Class('NSComplexOrthography')
NSPortMessage = _Class('NSPortMessage')
NSOrderedCollectionChange = _Class('NSOrderedCollectionChange')
NSURLQueue = _Class('NSURLQueue')
NSURLQueueNode = _Class('NSURLQueueNode')
NSURLKeyValuePair = _Class('NSURLKeyValuePair')
NSURLHostNameAddressInfo = _Class('NSURLHostNameAddressInfo')
NSURLFileTypeMappings = _Class('NSURLFileTypeMappings')
NSURLFileTypeMappingsInternal = _Class('NSURLFileTypeMappingsInternal')
NSSetChange = _Class('NSSetChange')
NSConcreteSetChange = _Class('NSConcreteSetChange')
NSTask = _Class('NSTask')
NSConcreteTask = _Class('NSConcreteTask')
NSBackgroundActivityScheduler = _Class('NSBackgroundActivityScheduler')
NSOrderedSetChange = _Class('NSOrderedSetChange')
NSConcreteOrderedSetChange = _Class('NSConcreteOrderedSetChange')
NSEncodingDetector = _Class('NSEncodingDetector')
NSSingleByteEncodingDetector = _Class('NSSingleByteEncodingDetector')
NSASCIIEncodingDetector = _Class('NSASCIIEncodingDetector')
NSWINDOWS1258EncodingDetector = _Class('NSWINDOWS1258EncodingDetector')
NSWINDOWS1257EncodingDetector = _Class('NSWINDOWS1257EncodingDetector')
NSWINDOWS1251EncodingDetector = _Class('NSWINDOWS1251EncodingDetector')
NSWINDOWS1256EncodingDetector = _Class('NSWINDOWS1256EncodingDetector')
NSWINDOWS1255EncodingDetector = _Class('NSWINDOWS1255EncodingDetector')
NSWINDOWS1254EncodingDetector = _Class('NSWINDOWS1254EncodingDetector')
NSWINDOWS1253EncodingDetector = _Class('NSWINDOWS1253EncodingDetector')
NSWINDOWS874EncodingDetector = _Class('NSWINDOWS874EncodingDetector')
NSWINDOWS1250EncodingDetector = _Class('NSWINDOWS1250EncodingDetector')
NSWINDOWS1252EncodingDetector = _Class('NSWINDOWS1252EncodingDetector')
NSISO885911EncodingDetector = _Class('NSISO885911EncodingDetector')
NSISO88598EncodingDetector = _Class('NSISO88598EncodingDetector')
NSISO88597EncodingDetector = _Class('NSISO88597EncodingDetector')
NSISO88596EncodingDetector = _Class('NSISO88596EncodingDetector')
NSISO88595EncodingDetector = _Class('NSISO88595EncodingDetector')
NSISOLATIN10EncodingDetector = _Class('NSISOLATIN10EncodingDetector')
NSISOLATIN9EncodingDetector = _Class('NSISOLATIN9EncodingDetector')
NSISOLATIN8EncodingDetector = _Class('NSISOLATIN8EncodingDetector')
NSISOLATIN7EncodingDetector = _Class('NSISOLATIN7EncodingDetector')
NSISOLATIN6EncodingDetector = _Class('NSISOLATIN6EncodingDetector')
NSISOLATIN5EncodingDetector = _Class('NSISOLATIN5EncodingDetector')
NSISOLATIN4EncodingDetector = _Class('NSISOLATIN4EncodingDetector')
NSISOLATIN3EncodingDetector = _Class('NSISOLATIN3EncodingDetector')
NSISOLATIN2EncodingDetector = _Class('NSISOLATIN2EncodingDetector')
NSISOLATIN1EncodingDetector = _Class('NSISOLATIN1EncodingDetector')
NSUTF7EncodingDetector = _Class('NSUTF7EncodingDetector')
NSWINDOWS949EncodingDetector = _Class('NSWINDOWS949EncodingDetector')
NSEUCKREncodingDetector = _Class('NSEUCKREncodingDetector')
NSWINDOWS932EncodingDetector = _Class('NSWINDOWS932EncodingDetector')
NSSHIFTJISX0213EncodingDetector = _Class('NSSHIFTJISX0213EncodingDetector')
NSEUCJPEncodingDetector = _Class('NSEUCJPEncodingDetector')
NSWINDOWS950EncodingDetector = _Class('NSWINDOWS950EncodingDetector')
NSWINDOWS936EncodingDetector = _Class('NSWINDOWS936EncodingDetector')
NSISO2022EncodingDetector = _Class('NSISO2022EncodingDetector')
NSISO2022KREncodingDetector = _Class('NSISO2022KREncodingDetector')
NSISO2022JP2EncodingDetector = _Class('NSISO2022JP2EncodingDetector')
NSISO2022JP1EncodingDetector = _Class('NSISO2022JP1EncodingDetector')
NSISO2022JPEncodingDetector = _Class('NSISO2022JPEncodingDetector')
NSHZGB2312EncodingDetector = _Class('NSHZGB2312EncodingDetector')
NSISO2022CNEncodingDetector = _Class('NSISO2022CNEncodingDetector')
NSBigEEncodingDetector = _Class('NSBigEEncodingDetector')
NSBig5HKSCSEncodingDetector = _Class('NSBig5HKSCSEncodingDetector')
NSBig5EncodingDetector = _Class('NSBig5EncodingDetector')
NSEUCTWEncodingDetector = _Class('NSEUCTWEncodingDetector')
NSEUCGB2312EncodingDetector = _Class('NSEUCGB2312EncodingDetector')
NSGB18030EncodingDetector = _Class('NSGB18030EncodingDetector')
NSGBKEncodingDetector = _Class('NSGBKEncodingDetector')
NSUTF8EncodingDetector = _Class('NSUTF8EncodingDetector')
NSUTF16BaseEncodingDetector = _Class('NSUTF16BaseEncodingDetector')
NSUTF16LEEncodingDetector = _Class('NSUTF16LEEncodingDetector')
NSUTF16BEEncodingDetector = _Class('NSUTF16BEEncodingDetector')
NSUTF16EncodingDetector = _Class('NSUTF16EncodingDetector')
NSUTF32BEEncodingDetector = _Class('NSUTF32BEEncodingDetector')
NSUTF32LEEncodingDetector = _Class('NSUTF32LEEncodingDetector')
NSUTF32EncodingDetector = _Class('NSUTF32EncodingDetector')
NSCFType = _Class('NSCFType')
NSPortNameServer = _Class('NSPortNameServer')
NSMessagePortNameServer = _Class('NSMessagePortNameServer')
NSMachBootstrapServer = _Class('NSMachBootstrapServer')
NSArrayChange = _Class('NSArrayChange')
NSConcreteArrayChange = _Class('NSConcreteArrayChange')
NSNotificationQueue = _Class('NSNotificationQueue')
NSMetadataQueryResultGroup = _Class('NSMetadataQueryResultGroup')
NSMetadataQueryAttributeValueTuple = _Class('NSMetadataQueryAttributeValueTuple')
NSMetadataItem = _Class('NSMetadataItem')
NSMultiReadUniWriteLock = _Class('NSMultiReadUniWriteLock')
NSKeyValueProxyShareKey = _Class('NSKeyValueProxyShareKey')
NSObservedValue = _Class('NSObservedValue')
NSStackObservedValue = _Class('NSStackObservedValue')
NSLookupMatch = _Class('NSLookupMatch')
NSKeyValueMutatingCollectionMethodSet = _Class('NSKeyValueMutatingCollectionMethodSet')
NSKeyValueMutatingSetMethodSet = _Class('NSKeyValueMutatingSetMethodSet')
NSKeyValueMutatingOrderedSetMethodSet = _Class('NSKeyValueMutatingOrderedSetMethodSet')
NSKeyValueMutatingArrayMethodSet = _Class('NSKeyValueMutatingArrayMethodSet')
NSKeyValueNonmutatingCollectionMethodSet = _Class('NSKeyValueNonmutatingCollectionMethodSet')
NSKeyValueNonmutatingSetMethodSet = _Class('NSKeyValueNonmutatingSetMethodSet')
NSKeyValueNonmutatingOrderedSetMethodSet = _Class('NSKeyValueNonmutatingOrderedSetMethodSet')
NSKeyValueNonmutatingArrayMethodSet = _Class('NSKeyValueNonmutatingArrayMethodSet')
NSUnit = _Class('NSUnit')
NSDimension = _Class('NSDimension')
NSUnitVolume = _Class('NSUnitVolume')
NSUnitTemperature = _Class('NSUnitTemperature')
NSUnitSpeed = _Class('NSUnitSpeed')
NSUnitPressure = _Class('NSUnitPressure')
NSUnitPower = _Class('NSUnitPower')
NSUnitMass = _Class('NSUnitMass')
NSUnitLength = _Class('NSUnitLength')
NSUnitInformationStorage = _Class('NSUnitInformationStorage')
NSUnitIlluminance = _Class('NSUnitIlluminance')
NSUnitFuelEfficiency = _Class('NSUnitFuelEfficiency')
NSUnitFrequency = _Class('NSUnitFrequency')
NSUnitEnergy = _Class('NSUnitEnergy')
NSUnitElectricResistance = _Class('NSUnitElectricResistance')
NSUnitElectricPotentialDifference = _Class('NSUnitElectricPotentialDifference')
NSUnitElectricCurrent = _Class('NSUnitElectricCurrent')
NSUnitElectricCharge = _Class('NSUnitElectricCharge')
NSUnitDuration = _Class('NSUnitDuration')
NSUnitDispersion = _Class('NSUnitDispersion')
NSUnitConcentrationMass = _Class('NSUnitConcentrationMass')
NSUnitArea = _Class('NSUnitArea')
NSUnitAngle = _Class('NSUnitAngle')
NSUnitAcceleration = _Class('NSUnitAcceleration')
NSUnitConverter = _Class('NSUnitConverter')
NSUnitConverterReciprocal = _Class('NSUnitConverterReciprocal')
NSUnitConverterLinear = _Class('NSUnitConverterLinear')
NSObservationSink = _Class('NSObservationSink')
NSBlockObservationSink = _Class('NSBlockObservationSink')
NSExtensionURLResult = _Class('NSExtensionURLResult')
NSFileProviderMessenger = _Class('NSFileProviderMessenger')
NSFileProviderMessageInterface = _Class('NSFileProviderMessageInterface')
NSFileProviderService = _Class('NSFileProviderService')
NSPipe = _Class('NSPipe')
NSConcretePipe = _Class('NSConcretePipe')
NSObservation = _Class('NSObservation')
NSBoundKeyPath = _Class('NSBoundKeyPath')
NSObserverKeyPath = _Class('NSObserverKeyPath')
NSObservableKeyPath = _Class('NSObservableKeyPath')
NSEncodingDetectionPlaceholder = _Class('NSEncodingDetectionPlaceholder')
NSProgressRegistrar = _Class('NSProgressRegistrar')
NSProgressSubscriberProxy = _Class('NSProgressSubscriberProxy')
NSProgressPublisherProxy = _Class('NSProgressPublisherProxy')
NSObservationSource = _Class('NSObservationSource')
NSNotificationObservable = _Class('NSNotificationObservable')
NSObservationTransformer = _Class('NSObservationTransformer')
NSObservationBuffer = _Class('NSObservationBuffer')
NSConcreteObservationBuffer = _Class('NSConcreteObservationBuffer')
NSOldValueObservationTransformer = _Class('NSOldValueObservationTransformer')
NSFilterObservationTransformer = _Class('NSFilterObservationTransformer')
NSReduceObservationTransformer = _Class('NSReduceObservationTransformer')
NSMapObservationTransformer = _Class('NSMapObservationTransformer')
NSAssertionHandler = _Class('NSAssertionHandler')
NSPredicateOperator = _Class('NSPredicateOperator')
NSBoundedByPredicateOperator = _Class('NSBoundedByPredicateOperator')
NSStringPredicateOperator = _Class('NSStringPredicateOperator')
NSSubstringPredicateOperator = _Class('NSSubstringPredicateOperator')
NSTokenMatchingPredicateOperator = _Class('NSTokenMatchingPredicateOperator')
NSMatchingPredicateOperator = _Class('NSMatchingPredicateOperator')
NSLikePredicateOperator = _Class('NSLikePredicateOperator')
NSUTIPredicateOperator = _Class('NSUTIPredicateOperator')
NSCustomPredicateOperator = _Class('NSCustomPredicateOperator')
NSCompoundPredicateOperator = _Class('NSCompoundPredicateOperator')
NSBetweenPredicateOperator = _Class('NSBetweenPredicateOperator')
NSInPredicateOperator = _Class('NSInPredicateOperator')
NSEqualityPredicateOperator = _Class('NSEqualityPredicateOperator')
NSComparisonPredicateOperator = _Class('NSComparisonPredicateOperator')
NSExpression = _Class('NSExpression')
NSTernaryExpression = _Class('NSTernaryExpression')
NSBlockExpression = _Class('NSBlockExpression')
NSVariableExpression = _Class('NSVariableExpression')
NSVariableAssignmentExpression = _Class('NSVariableAssignmentExpression')
NSSymbolicExpression = _Class('NSSymbolicExpression')
NSSubqueryExpression = _Class('NSSubqueryExpression')
NSSetExpression = _Class('NSSetExpression')
NSAnyKeyExpression = _Class('NSAnyKeyExpression')
NSAggregateExpression = _Class('NSAggregateExpression')
NSConstantValueExpression = _Class('NSConstantValueExpression')
NSFunctionExpression = _Class('NSFunctionExpression')
NSKeyPathExpression = _Class('NSKeyPathExpression')
NSKeyPathSpecifierExpression = _Class('NSKeyPathSpecifierExpression')
NSSelfExpression = _Class('NSSelfExpression')
NSValueTransformer = _Class('NSValueTransformer')
NSSecureUnarchiveFromDataTransformer = _Class('NSSecureUnarchiveFromDataTransformer')
NSMetadataQuery = _Class('NSMetadataQuery')
NSSecurityScopedURLWrapper = _Class('NSSecurityScopedURLWrapper')
NSFileAccessIntent = _Class('NSFileAccessIntent')
NSItemRepresentationLoadResult = _Class('NSItemRepresentationLoadResult')
NSItemProviderRepresentation = _Class('NSItemProviderRepresentation')
NSFilePresenterOperationRecord = _Class('NSFilePresenterOperationRecord')
NSFilePresenterRelinquishment = _Class('NSFilePresenterRelinquishment')
NSFileWrapperMoreIVars = _Class('NSFileWrapperMoreIVars')
NSFileWrapper = _Class('NSFileWrapper')
NSFileCoordinatorAccessorBlockCompletion = _Class('NSFileCoordinatorAccessorBlockCompletion')
NSUndoManager = _Class('NSUndoManager')
NSFilePresenterXPCMessenger = _Class('NSFilePresenterXPCMessenger')
NSFileAccessArbiterProxy = _Class('NSFileAccessArbiterProxy')
NSFileAccessClaim = _Class('NSFileAccessClaim')
NSFileWritingWritingClaim = _Class('NSFileWritingWritingClaim')
NSFileReadingWritingClaim = _Class('NSFileReadingWritingClaim')
NSFileWritingClaim = _Class('NSFileWritingClaim')
NSFileMultipleAccessClaim = _Class('NSFileMultipleAccessClaim')
NSFileReadingClaim = _Class('NSFileReadingClaim')
NSFileSubarbitrationClaim = _Class('NSFileSubarbitrationClaim')
NSURLPromisePair = _Class('NSURLPromisePair')
NSJSONSerialization = _Class('NSJSONSerialization')
NSURLQueryItem = _Class('NSURLQueryItem')
NSURLComponents = _Class('NSURLComponents')
NSMeasurement = _Class('NSMeasurement')
NSDateInterval = _Class('NSDateInterval')
NSIndexPath = _Class('NSIndexPath')
NSTextCheckingResult = _Class('NSTextCheckingResult')
NSTransitInformationCheckingResult = _Class('NSTransitInformationCheckingResult')
NSPhoneNumberCheckingResult = _Class('NSPhoneNumberCheckingResult')
NSSubstitutionCheckingResult = _Class('NSSubstitutionCheckingResult')
NSCompletionCheckingResult = _Class('NSCompletionCheckingResult')
NSCorrectionCheckingResult = _Class('NSCorrectionCheckingResult')
NSEmojiCheckingResult = _Class('NSEmojiCheckingResult')
NSReplacementCheckingResult = _Class('NSReplacementCheckingResult')
NSDashCheckingResult = _Class('NSDashCheckingResult')
NSQuoteCheckingResult = _Class('NSQuoteCheckingResult')
NSLinkCheckingResult = _Class('NSLinkCheckingResult')
NSAddressCheckingResult = _Class('NSAddressCheckingResult')
NSDateCheckingResult = _Class('NSDateCheckingResult')
NSGrammarCheckingResult = _Class('NSGrammarCheckingResult')
NSSpellCheckingResult = _Class('NSSpellCheckingResult')
NSOrthographyCheckingResult = _Class('NSOrthographyCheckingResult')
NSRegularExpressionCheckingResult = _Class('NSRegularExpressionCheckingResult')
NSComplexRegularExpressionCheckingResult = _Class('NSComplexRegularExpressionCheckingResult')
NSExtendedRegularExpressionCheckingResult = _Class('NSExtendedRegularExpressionCheckingResult')
NSSimpleRegularExpressionCheckingResult = _Class('NSSimpleRegularExpressionCheckingResult')
NSRegularExpression = _Class('NSRegularExpression')
NSDataDetector = _Class('NSDataDetector')
NSRLEArray = _Class('NSRLEArray')
NSMutableRLEArray = _Class('NSMutableRLEArray')
NSFileVersion = _Class('NSFileVersion')
NSFileCoordinator = _Class('NSFileCoordinator')
NSDecimalNumberHandler = _Class('NSDecimalNumberHandler')
NSProgressValues = _Class('NSProgressValues')
NSBundleResourceRequest = _Class('NSBundleResourceRequest')
NSCondition = _Class('NSCondition')
NSConditionLock = _Class('NSConditionLock')
NSItemProvider = _Class('NSItemProvider')
NSExtensionItem = _Class('NSExtensionItem')
NSXPCListener = _Class('NSXPCListener')
NSExtensionContext = _Class('NSExtensionContext')
NSUbiquitousKeyValueStore = _Class('NSUbiquitousKeyValueStore')
NSExtension = _Class('NSExtension')
NSUserActivity = _Class('NSUserActivity')
NSPersonNameComponents = _Class('NSPersonNameComponents')
NSFileHandle = _Class('NSFileHandle')
NSConcreteFileHandle = _Class('NSConcreteFileHandle')
NSNullFileHandle = _Class('NSNullFileHandle')
NSProgress = _Class('NSProgress')
NSAutoreleasePool = _Class('NSAutoreleasePool')
NSXPCListenerEndpoint = _Class('NSXPCListenerEndpoint')
NSXPCInterface = _Class('NSXPCInterface')
NSXPCConnection = _Class('NSXPCConnection')
UIKit_PKSubsystem = _Class('UIKit_PKSubsystem')
NSOperationQueue = _Class('NSOperationQueue')
NSKeyValueAccessor = _Class('NSKeyValueAccessor')
NSKeyValueSetter = _Class('NSKeyValueSetter')
NSKeyValueIvarSetter = _Class('NSKeyValueIvarSetter')
NSKeyValueSlowSetter = _Class('NSKeyValueSlowSetter')
NSKeyValueUndefinedSetter = _Class('NSKeyValueUndefinedSetter')
NSKeyValueMethodSetter = _Class('NSKeyValueMethodSetter')
NSKeyValueGetter = _Class('NSKeyValueGetter')
NSKeyValueIvarGetter = _Class('NSKeyValueIvarGetter')
NSKeyValueSlowGetter = _Class('NSKeyValueSlowGetter')
NSKeyValueProxyGetter = _Class('NSKeyValueProxyGetter')
NSKeyValueNotifyingMutableCollectionGetter = _Class('NSKeyValueNotifyingMutableCollectionGetter')
NSKeyValueFastMutableCollection2Getter = _Class('NSKeyValueFastMutableCollection2Getter')
NSKeyValueFastMutableCollection1Getter = _Class('NSKeyValueFastMutableCollection1Getter')
NSKeyValueCollectionGetter = _Class('NSKeyValueCollectionGetter')
NSKeyValueIvarMutableCollectionGetter = _Class('NSKeyValueIvarMutableCollectionGetter')
NSKeyValueSlowMutableCollectionGetter = _Class('NSKeyValueSlowMutableCollectionGetter')
NSKeyValueUndefinedGetter = _Class('NSKeyValueUndefinedGetter')
NSKeyValueMethodGetter = _Class('NSKeyValueMethodGetter')
NSCoder = _Class('NSCoder')
NSUnarchiver = _Class('NSUnarchiver')
NSArchiver = _Class('NSArchiver')
NSXPCCoder = _Class('NSXPCCoder')
NSXPCDecoder = _Class('NSXPCDecoder')
NSXPCEncoder = _Class('NSXPCEncoder')
NSKeyedArchiver = _Class('NSKeyedArchiver')
NSKeyedUnarchiver = _Class('NSKeyedUnarchiver')
NSRecursiveLock = _Class('NSRecursiveLock')
NSPredicate = _Class('NSPredicate')
NSCompoundPredicate = _Class('NSCompoundPredicate')
NSComparisonPredicate = _Class('NSComparisonPredicate')
NSFalsePredicate = _Class('NSFalsePredicate')
NSTruePredicate = _Class('NSTruePredicate')
NSBlockPredicate = _Class('NSBlockPredicate')
NSScanner = _Class('NSScanner')
NSConcreteScanner = _Class('NSConcreteScanner')
NSKeyValueObservationInfo = _Class('NSKeyValueObservationInfo')
NSKeyValueObservance = _Class('NSKeyValueObservance')
NSKeyValueShareableObservanceKey = _Class('NSKeyValueShareableObservanceKey')
NSKeyValueShareableObservationInfoKey = _Class('NSKeyValueShareableObservationInfoKey')
NSKeyValueProperty = _Class('NSKeyValueProperty')
NSKeyValueComputedProperty = _Class('NSKeyValueComputedProperty')
NSKeyValueNestedProperty = _Class('NSKeyValueNestedProperty')
NSKeyValueUnnestedProperty = _Class('NSKeyValueUnnestedProperty')
NSKeyValueContainerClass = _Class('NSKeyValueContainerClass')
NSOperation = _Class('NSOperation')
NSFilesystemItemMoveOperation = _Class('NSFilesystemItemMoveOperation')
NSInvocationOperation = _Class('NSInvocationOperation')
NSFilePresenterAsynchronousOperation = _Class('NSFilePresenterAsynchronousOperation')
NSDirectoryTraversalOperation = _Class('NSDirectoryTraversalOperation')
NSDirectorySubpathsOperation = _Class('NSDirectorySubpathsOperation')
NSFilesystemItemCopyOperation = _Class('NSFilesystemItemCopyOperation')
NSFilesystemItemLinkOperation = _Class('NSFilesystemItemLinkOperation')
NSBlockOperation = _Class('NSBlockOperation')
NSFilesystemItemRemoveOperation = _Class('NSFilesystemItemRemoveOperation')
NSMapTable = _Class('NSMapTable')
NSClassicMapTable = _Class('NSClassicMapTable')
NSConcreteMapTable = _Class('NSConcreteMapTable')
NSHashTable = _Class('NSHashTable')
NSClassicHashTable = _Class('NSClassicHashTable')
NSConcreteHashTable = _Class('NSConcreteHashTable')
NSLock = _Class('NSLock')
NSPointerFunctions = _Class('NSPointerFunctions')
NSConcretePointerFunctions = _Class('NSConcretePointerFunctions')
NSPointerArray = _Class('NSPointerArray')
NSConcretePointerArray = _Class('NSConcretePointerArray')
NSBundle = _Class('NSBundle')
NSKeyValueNilOrderedSetEnumerator = _Class('NSKeyValueNilOrderedSetEnumerator')
NSKeyValueNilSetEnumerator = _Class('NSKeyValueNilSetEnumerator')
NSDirectoryEnumerator = _Class('NSDirectoryEnumerator')
NSURLDirectoryEnumerator = _Class('NSURLDirectoryEnumerator')
NSAllDescendantPathsEnumerator = _Class('NSAllDescendantPathsEnumerator')
NSSimpleAttributeDictionaryEnumerator = _Class('NSSimpleAttributeDictionaryEnumerator')
NSConcreteMapTableValueEnumerator = _Class('NSConcreteMapTableValueEnumerator')
NSSearchPathEnumerator = _Class('NSSearchPathEnumerator')
NSProcessInfo = _Class('NSProcessInfo')
NSPropertyListSerialization = _Class('NSPropertyListSerialization')
NSFileManager = _Class('NSFileManager')
NSNotificationCenter = _Class('NSNotificationCenter')
NSDistributedNotificationCenter = _Class('NSDistributedNotificationCenter')
NSUUID = _Class('NSUUID')
NSThread = _Class('NSThread')
NSAffineTransform = _Class('NSAffineTransform')
NSFormatter = _Class('NSFormatter')
NSEnergyFormatter = _Class('NSEnergyFormatter')
NSPersonNameComponentsFormatter = _Class('NSPersonNameComponentsFormatter')
NSByteCountFormatter = _Class('NSByteCountFormatter')
NSUnitFormatter = _Class('NSUnitFormatter')
NSDateIntervalFormatter = _Class('NSDateIntervalFormatter')
NSISO8601DateFormatter = _Class('NSISO8601DateFormatter')
NSMassFormatter = _Class('NSMassFormatter')
NSLengthFormatter = _Class('NSLengthFormatter')
NSDateComponentsFormatter = _Class('NSDateComponentsFormatter')
NSRelativeDateTimeFormatter = _Class('NSRelativeDateTimeFormatter')
NSListFormatter = _Class('NSListFormatter')
NSMeasurementFormatter = _Class('NSMeasurementFormatter')
NSDateFormatter = _Class('NSDateFormatter')
NSNumberFormatter = _Class('NSNumberFormatter')
NSIndexSet = _Class('NSIndexSet')
NSMutableIndexSet = _Class('NSMutableIndexSet')
NSNotification = _Class('NSNotification')
NSConcreteNotification = _Class('NSConcreteNotification')
NSAttributedString = _Class('NSAttributedString')
NSConcreteAttributedString = _Class('NSConcreteAttributedString')
NSMutableAttributedString = _Class('NSMutableAttributedString')
NSCFAttributedString = _Class('NSCFAttributedString')
NSConcreteMutableAttributedString = _Class('NSConcreteMutableAttributedString')
NSCharacterSet = _Class('NSCharacterSet')
NSMutableCharacterSet = _Class('NSMutableCharacterSet')
NSCFCharacterSet = _Class('NSCFCharacterSet')
NSError = _Class('NSError')
NSURLError = _Class('NSURLError')
NSCFError = _Class('NSCFError')
NSString = _Class('NSString')
NSSimpleCString = _Class('NSSimpleCString')
NSConstantString = _Class('NSConstantString')
NSDebugString = _Class('NSDebugString')
NSPinyinString = _Class('NSPinyinString')
NSLocalizableString = _Class('NSLocalizableString')
NSPathStore2 = _Class('NSPathStore2')
NSPlaceholderString = _Class('NSPlaceholderString')
NSMutableString = _Class('NSMutableString')
NSMutableStringProxyForMutableAttributedString = _Class('NSMutableStringProxyForMutableAttributedString')
NSBigMutableString = _Class('NSBigMutableString')
NSPlaceholderMutableString = _Class('NSPlaceholderMutableString')
NSCheapMutableString = _Class('NSCheapMutableString')
NSSortDescriptor = _Class('NSSortDescriptor')
NSXMLParser = _Class('NSXMLParser')
NSCFOutputStream = _Class('NSCFOutputStream')
NSCFInputStream = _Class('NSCFInputStream')
NSAutoLocale = _Class('NSAutoLocale')
NSCFTimer = _Class('NSCFTimer')
NSPort = _Class('NSPort')
NSMessagePort = _Class('NSMessagePort')
NSMachPort = _Class('NSMachPort')
NSKeyValueOrderedSet = _Class('NSKeyValueOrderedSet')
NSOrderedSetChanges = _Class('NSOrderedSetChanges')
NSConcreteOrderedSetChanges = _Class('NSConcreteOrderedSetChanges')
NSKeyValueMutableOrderedSet = _Class('NSKeyValueMutableOrderedSet')
NSKeyValueNotifyingMutableOrderedSet = _Class('NSKeyValueNotifyingMutableOrderedSet')
NSKeyValueFastMutableOrderedSet = _Class('NSKeyValueFastMutableOrderedSet')
NSKeyValueFastMutableOrderedSet2 = _Class('NSKeyValueFastMutableOrderedSet2')
NSKeyValueFastMutableOrderedSet1 = _Class('NSKeyValueFastMutableOrderedSet1')
NSKeyValueIvarMutableOrderedSet = _Class('NSKeyValueIvarMutableOrderedSet')
NSKeyValueSlowMutableOrderedSet = _Class('NSKeyValueSlowMutableOrderedSet')
NSKeyValueSet = _Class('NSKeyValueSet')
NSSetChanges = _Class('NSSetChanges')
NSConcreteSetChanges = _Class('NSConcreteSetChanges')
NSKeyValueMutableSet = _Class('NSKeyValueMutableSet')
NSKeyValueNotifyingMutableSet = _Class('NSKeyValueNotifyingMutableSet')
NSKeyValueFastMutableSet = _Class('NSKeyValueFastMutableSet')
NSKeyValueFastMutableSet2 = _Class('NSKeyValueFastMutableSet2')
NSKeyValueFastMutableSet1 = _Class('NSKeyValueFastMutableSet1')
NSKeyValueIvarMutableSet = _Class('NSKeyValueIvarMutableSet')
NSKeyValueSlowMutableSet = _Class('NSKeyValueSlowMutableSet')
NSCountedSet = _Class('NSCountedSet')
NSSimpleAttributeDictionary = _Class('NSSimpleAttributeDictionary')
NSOwnedDictionaryProxy = _Class('NSOwnedDictionaryProxy')
NSFileAttributes = _Class('NSFileAttributes')
NSKeyValueChangeDictionary = _Class('NSKeyValueChangeDictionary')
NSDirInfo = _Class('NSDirInfo')
NSRTFD = _Class('NSRTFD')
NSCalendarDate = _Class('NSCalendarDate')
NSPageData = _Class('NSPageData')
NSSubrangeData = _Class('NSSubrangeData')
NSConcreteData = _Class('NSConcreteData')
NSPurgeableData = _Class('NSPurgeableData')
NSConcreteMutableData = _Class('NSConcreteMutableData')
NSValue = _Class('NSValue')
NSWeakObjectValue = _Class('NSWeakObjectValue')
NSConcreteValue = _Class('NSConcreteValue')
NSNumber = _Class('NSNumber')
NSDecimalNumber = _Class('NSDecimalNumber')
NSDecimalNumberPlaceholder = _Class('NSDecimalNumberPlaceholder')
NSPlaceholderValue = _Class('NSPlaceholderValue')
NSPlaceholderNumber = _Class('NSPlaceholderNumber')
NSConstantDoubleNumber = _Class('NSConstantDoubleNumber')
NSConstantFloatNumber = _Class('NSConstantFloatNumber')
NSConstantIntegerNumber = _Class('NSConstantIntegerNumber')
NSKeyValueArray = _Class('NSKeyValueArray')
NSArrayChanges = _Class('NSArrayChanges')
NSConcreteArrayChanges = _Class('NSConcreteArrayChanges')
NSKeyValueMutableArray = _Class('NSKeyValueMutableArray')
NSKeyValueNotifyingMutableArray = _Class('NSKeyValueNotifyingMutableArray')
NSKeyValueFastMutableArray = _Class('NSKeyValueFastMutableArray')
NSKeyValueFastMutableArray2 = _Class('NSKeyValueFastMutableArray2')
NSKeyValueFastMutableArray1 = _Class('NSKeyValueFastMutableArray1')
NSKeyValueIvarMutableArray = _Class('NSKeyValueIvarMutableArray')
NSKeyValueSlowMutableArray = _Class('NSKeyValueSlowMutableArray')
NSProxy = _Class('NSProxy')
NSUndoManagerProxy = _Class('NSUndoManagerProxy')
NSProtocolChecker = _Class('NSProtocolChecker')
NSConcreteProtocolChecker = _Class('NSConcreteProtocolChecker')
NSAutoContentAccessingProxy = _Class('NSAutoContentAccessingProxy')