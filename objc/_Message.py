'''
Classes from the 'Message' framework.
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

    
MFWebAttachmentSource = _Class('MFWebAttachmentSource')
MFWebMessageDocument = _Class('MFWebMessageDocument')
MFSqliteMessageIDStore = _Class('MFSqliteMessageIDStore')
MFSMTPResponse = _Class('MFSMTPResponse')
MFProgressiveMimeParser = _Class('MFProgressiveMimeParser')
MFPlainTextDocument = _Class('MFPlainTextDocument')
MFPlainTextFragment = _Class('MFPlainTextFragment')
MFMessageURLConnectionDelegate = _Class('MFMessageURLConnectionDelegate')
MFMessageKeychainManager = _Class('MFMessageKeychainManager')
MFMimeEnrichedReader = _Class('MFMimeEnrichedReader')
MFWeakObjectCache = _Class('MFWeakObjectCache')
MFUserDefaultMigrator = _Class('MFUserDefaultMigrator')
MFUnreadCountProbe = _Class('MFUnreadCountProbe')
MFThreadFuzzyMatcher = _Class('MFThreadFuzzyMatcher')
MFTaskAssertion = _Class('MFTaskAssertion')
MFSignatures = _Class('MFSignatures')
MFSecureMIMECompositionManager = _Class('MFSecureMIMECompositionManager')
MFRFC822AttachmentDataProvider = _Class('MFRFC822AttachmentDataProvider')
MFPowerController = _Class('MFPowerController')
MFOutgoingMessageContent = _Class('MFOutgoingMessageContent')
MFOutgoingRichtextMessageContent = _Class('MFOutgoingRichtextMessageContent')
MFOutgoingMultipartRelatedContent = _Class('MFOutgoingMultipartRelatedContent')
MFOutgoingLibraryMessageContent = _Class('MFOutgoingLibraryMessageContent')
MFNetworkController = _Class('MFNetworkController')
MFMigrationPersistence = _Class('MFMigrationPersistence')
MFMessageTransformer = _Class('MFMessageTransformer')
MFMessageSignerEMMessageSignerTransformer = _Class('MFMessageSignerEMMessageSignerTransformer')
MFMessageReferenceContext = _Class('MFMessageReferenceContext')
MFMessageLoadingContextToEMSecurityInformationTransformer = _Class('MFMessageLoadingContextToEMSecurityInformationTransformer')
MFMessageLoadingContext = _Class('MFMessageLoadingContext')
MFMessageLoadingContextEvent = _Class('MFMessageLoadingContextEvent')
MFMessageInfoOrderedSet = _Class('MFMessageInfoOrderedSet')
MFMessageInfo = _Class('MFMessageInfo')
MFMessageDetails = _Class('MFMessageDetails')
MFMessageCriterionConverter = _Class('MFMessageCriterionConverter')
MFMessageContentRequest = _Class('MFMessageContentRequest')
MFMessageCollectionInfo = _Class('MFMessageCollectionInfo')
MFMessageBodyMigrator = _Class('MFMessageBodyMigrator')
MFMailMessageStoreSearchResult = _Class('MFMailMessageStoreSearchResult')
MFMailMessageLibraryThreadFlagColorsUpgradeStep = _Class('MFMailMessageLibraryThreadFlagColorsUpgradeStep')
MFMailMessageLibrarySetThreadSendersRecipientsConflictResolutionUpgradeStep = _Class('MFMailMessageLibrarySetThreadSendersRecipientsConflictResolutionUpgradeStep')
MFMailMessageLibraryResetSequenceNumberMigrationStep = _Class('MFMailMessageLibraryResetSequenceNumberMigrationStep')
MFMailMessageLibraryRecreateMessageIndicesUpgradeStep = _Class('MFMailMessageLibraryRecreateMessageIndicesUpgradeStep')
MFMailMessageLibraryRebuildThreadsTableUpgradeStep = _Class('MFMailMessageLibraryRebuildThreadsTableUpgradeStep')
MFMailMessageLibraryQueryTransformer = _Class('MFMailMessageLibraryQueryTransformer')
MFMailMessageLibraryModifyColumnDefinitionsMigrationStep = _Class('MFMailMessageLibraryModifyColumnDefinitionsMigrationStep')
MFMailMessageLibraryMigrator = _Class('MFMailMessageLibraryMigrator')
MFMailMessageLibraryMailboxURLMigrationStep = _Class('MFMailMessageLibraryMailboxURLMigrationStep')
MFDADeferredStoreDraftOperation = _Class('MFDADeferredStoreDraftOperation')
MFDADeferredMessageMoveOperation = _Class('MFDADeferredMessageMoveOperation')
MFMailMessageLibraryLocalActionsTablesMigrationStep = _Class('MFMailMessageLibraryLocalActionsTablesMigrationStep')
MFMailMessageLibraryGlobalDataUpgradeStep = _Class('MFMailMessageLibraryGlobalDataUpgradeStep')
MFMailMessageLibraryFixPopUidsUniquenessConstraintUpgradeStep = _Class('MFMailMessageLibraryFixPopUidsUniquenessConstraintUpgradeStep')
MFMailMessageLibraryAdoptSharedSchemaMigrationStep = _Class('MFMailMessageLibraryAdoptSharedSchemaMigrationStep')
MFMailMessageLibraryAddSearchableIndexTablesUpgradeStep = _Class('MFMailMessageLibraryAddSearchableIndexTablesUpgradeStep')
MFMailMessageLibraryAddJournaledConversationIDDateReceivedUpgradeStep = _Class('MFMailMessageLibraryAddJournaledConversationIDDateReceivedUpgradeStep')
MFMailDropMailParser = _Class('MFMailDropMailParser')
MFOutgoingMessageDelivery = _Class('MFOutgoingMessageDelivery')
MFMailDropMailDelivery = _Class('MFMailDropMailDelivery')
MFMailboxUidTransformer = _Class('MFMailboxUidTransformer')
MFMailboxProvider = _Class('MFMailboxProvider')
MFLockStateMonitor = _Class('MFLockStateMonitor')
MFLocalActionReplayHandler = _Class('MFLocalActionReplayHandler')
MFListUnsubscribeMessageGenerator_iOS = _Class('MFListUnsubscribeMessageGenerator_iOS')
MFLibraryThreadReconciler = _Class('MFLibraryThreadReconciler')
MFLibraryReconciler = _Class('MFLibraryReconciler')
MFLibraryMessageReconciler = _Class('MFLibraryMessageReconciler')
MFFileCompressionQueueActivityManager = _Class('MFFileCompressionQueueActivityManager')
MFFileCompressionQueue = _Class('MFFileCompressionQueue')
MFFileArchiveEntry = _Class('MFFileArchiveEntry')
MFFileArchiveDirectory = _Class('MFFileArchiveDirectory')
MFFileArchive = _Class('MFFileArchive')
MFFile = _Class('MFFile')
MFFetchLimits = _Class('MFFetchLimits')
MFFakeAccountsProvider = _Class('MFFakeAccountsProvider')
MFDeliveryResult = _Class('MFDeliveryResult')
MFDecryptedAttachmentDataProvider = _Class('MFDecryptedAttachmentDataProvider')
MFDebugAccountState = _Class('MFDebugAccountState')
MFDbJournal = _Class('MFDbJournal')
MFDATransferActionReplayer = _Class('MFDATransferActionReplayer')
MFDAStoreDraftConsumer = _Class('MFDAStoreDraftConsumer')
MFDAMessageContentConsumer = _Class('MFDAMessageContentConsumer')
MFDAFolderChangeResult = _Class('MFDAFolderChangeResult')
MFDAFolderChangeConsumer = _Class('MFDAFolderChangeConsumer')
MFContentErrorDocument = _Class('MFContentErrorDocument')
MFComposeAttachmentDataProvider = _Class('MFComposeAttachmentDataProvider')
MFCertificateTrustInformationKeychainManager = _Class('MFCertificateTrustInformationKeychainManager')
MFCertificateTrustInfoEMCertificateTrustInformationTransformer = _Class('MFCertificateTrustInfoEMCertificateTrustInformationTransformer')
MFCertificateTrustInfo = _Class('MFCertificateTrustInfo')
MFAttachmentSecurityScope = _Class('MFAttachmentSecurityScope')
MFAttachmentBundle = _Class('MFAttachmentBundle')
MFAttachmentUtilities = _Class('MFAttachmentUtilities')
MFAttachmentRaw = _Class('MFAttachmentRaw')
MFAttachmentPlaceholder = _Class('MFAttachmentPlaceholder')
MFAttachmentLibraryDataProvider = _Class('MFAttachmentLibraryDataProvider')
MFMailDropAttachmentPreviewDataProvider = _Class('MFMailDropAttachmentPreviewDataProvider')
MFMailDropAttachmentDataProvider = _Class('MFMailDropAttachmentDataProvider')
MFAttachmentDataProvider = _Class('MFAttachmentDataProvider')
MFAttachmentCompositionContext = _Class('MFAttachmentCompositionContext')
MFAttachmentManager = _Class('MFAttachmentManager')
MFAttachmentComposeManager = _Class('MFAttachmentComposeManager')
MFAttachmentLibraryManager = _Class('MFAttachmentLibraryManager')
MFAttachmentCapabilities = _Class('MFAttachmentCapabilities')
MFAttachment = _Class('MFAttachment')
MFAppStateMonitor = _Class('MFAppStateMonitor')
MFActivityCondition = _Class('MFActivityCondition')
MFAccountStore = _Class('MFAccountStore')
MFAccountLoader = _Class('MFAccountLoader')
MFAccountFactory_iOS = _Class('MFAccountFactory_iOS')
MFMessageWriter = _Class('MFMessageWriter')
MFMessageSigner = _Class('MFMessageSigner')
MFBasicMessageDataSection = _Class('MFBasicMessageDataSection')
MFMessageCriterion = _Class('MFMessageCriterion')
MFMessageTransferResult = _Class('MFMessageTransferResult')
MFMessageLibrary = _Class('MFMessageLibrary')
MFMailMessageLibrary = _Class('MFMailMessageLibrary')
MFInvocationQueue = _Class('MFInvocationQueue')
MFDAMessagePayloadFetchResponseImpl = _Class('MFDAMessagePayloadFetchResponseImpl')
MFRequestQueue = _Class('MFRequestQueue')
MFDARequestQueue = _Class('MFDARequestQueue')
MFMailboxUid = _Class('MFMailboxUid')
MFFakeMailboxUid = _Class('MFFakeMailboxUid')
MFDAMailbox = _Class('MFDAMailbox')
MFMailDelivery = _Class('MFMailDelivery')
MFSMTPDelivery = _Class('MFSMTPDelivery')
MFDADelivery = _Class('MFDADelivery')
MFDAMailAccountConsumer = _Class('MFDAMailAccountConsumer')
MFDAMoveResponseConsumer = _Class('MFDAMoveResponseConsumer')
MFDAMailAccountSyncConsumer = _Class('MFDAMailAccountSyncConsumer')
MFDADeliveryConsumer = _Class('MFDADeliveryConsumer')
MFCRAM_MD5Authenticator = _Class('MFCRAM_MD5Authenticator')
MFConnectionSettings = _Class('MFConnectionSettings')
MFConnection = _Class('MFConnection')
MFSMTPConnection = _Class('MFSMTPConnection')
MFBufferedQueue = _Class('MFBufferedQueue')
MFPlainAuthScheme = _Class('MFPlainAuthScheme')
MFNTLMAuthScheme = _Class('MFNTLMAuthScheme')
MFDigestMD5AuthScheme = _Class('MFDigestMD5AuthScheme')
MFCRAM_MD5AuthScheme = _Class('MFCRAM_MD5AuthScheme')
MFAuthScheme = _Class('MFAuthScheme')
MFAccountValidator = _Class('MFAccountValidator')
MFAccount = _Class('MFAccount')
MailAccount = _Class('MailAccount')
MFFakeMailAccount = _Class('MFFakeMailAccount')
LocalAccount = _Class('LocalAccount')
DAMailAccount = _Class('DAMailAccount')
DeliveryAccount = _Class('DeliveryAccount')
SMTPAccount = _Class('SMTPAccount')
DADeliveryAccount = _Class('DADeliveryAccount')
MFMailMimeTextAttachment = _Class('MFMailMimeTextAttachment')
MFMailMimePart = _Class('MFMailMimePart')
MFMailMessageStore = _Class('MFMailMessageStore')
MFLibraryStore = _Class('MFLibraryStore')
MFDAMessageStore = _Class('MFDAMessageStore')
MFMailDataMessageStore = _Class('MFMailDataMessageStore')
MFLocalizedMessageHeaders = _Class('MFLocalizedMessageHeaders')
MFMailMessage = _Class('MFMailMessage')
MFFakeMailMessage = _Class('MFFakeMailMessage')
MFDAMessage = _Class('MFDAMessage')
MFOutgoingMessage = _Class('MFOutgoingMessage')
MFLibraryMessage = _Class('MFLibraryMessage')
MFFakeLibraryMessage = _Class('MFFakeLibraryMessage')
MFActivityMonitor = _Class('MFActivityMonitor')
MFDADraftMessage = _Class('MFDADraftMessage')
MFDAMessageStoreSaveDraftRequest = _Class('MFDAMessageStoreSaveDraftRequest')
MFServerMessagePersistenceFactory_iOS = _Class('MFServerMessagePersistenceFactory_iOS')
MFSearchableIndexPersistence_iOS = _Class('MFSearchableIndexPersistence_iOS')
MFSearchableIndexManager_iOS = _Class('MFSearchableIndexManager_iOS')
MFSearchableIndexItem_iOS = _Class('MFSearchableIndexItem_iOS')
MFSearchableIndex_iOS = _Class('MFSearchableIndex_iOS')
MFProtectedDatabasePersistence_iOS = _Class('MFProtectedDatabasePersistence_iOS')
MFPersistenceDatabaseSchema_iOS = _Class('MFPersistenceDatabaseSchema_iOS')
MFPersistenceDatabaseConnection_iOS = _Class('MFPersistenceDatabaseConnection_iOS')
MFPersistenceDatabase_iOS = _Class('MFPersistenceDatabase_iOS')
MFPersistence_iOS = _Class('MFPersistence_iOS')
MFMessagePersistence_iOS = _Class('MFMessagePersistence_iOS')
MFMessageChangeManager_iOS = _Class('MFMessageChangeManager_iOS')
MFMailboxPersistence_iOS = _Class('MFMailboxPersistence_iOS')
MFLocalActionPersistence_iOS = _Class('MFLocalActionPersistence_iOS')
MFMonitoredInvocation = _Class('MFMonitoredInvocation')
MFError = _Class('MFError')
