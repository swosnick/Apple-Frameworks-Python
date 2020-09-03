'''
Classes from the 'WebKit' framework.
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

    
WKShareSheet = _Class('WKShareSheet')
WKDragSessionContext = _Class('WKDragSessionContext')
WKFocusedElementInfo = _Class('WKFocusedElementInfo')
WKFormInputSession = _Class('WKFormInputSession')
WKAnimationDelegate = _Class('WKAnimationDelegate')
WKAccessibilityWebPageObjectBase = _Class('WKAccessibilityWebPageObjectBase')
WKAccessibilityWebPageObject = _Class('WKAccessibilityWebPageObject')
WKWebProcessPlugInBrowserContextController = _Class('WKWebProcessPlugInBrowserContextController')
WKWebProcessPlugInController = _Class('WKWebProcessPlugInController')
WKDOMTextIterator = _Class('WKDOMTextIterator')
WKDOMRange = _Class('WKDOMRange')
WKDOMNode = _Class('WKDOMNode')
WKDOMText = _Class('WKDOMText')
WKDOMElement = _Class('WKDOMElement')
WKDOMDocument = _Class('WKDOMDocument')
WKDOMDocumentParserYieldToken = _Class('WKDOMDocumentParserYieldToken')
WKWebProcessPlugInScriptWorld = _Class('WKWebProcessPlugInScriptWorld')
WKWebProcessPlugInRangeHandle = _Class('WKWebProcessPlugInRangeHandle')
WKWebProcessPlugInPageGroup = _Class('WKWebProcessPlugInPageGroup')
WKWebProcessPlugInNodeHandle = _Class('WKWebProcessPlugInNodeHandle')
WKWebProcessPlugInHitTestResult = _Class('WKWebProcessPlugInHitTestResult')
WKWebProcessPlugInFrame = _Class('WKWebProcessPlugInFrame')
WKWebProcessBundleParameters = _Class('WKWebProcessBundleParameters')
WKFullScreenWindowController = _Class('WKFullScreenWindowController')
WKFullScreenInteractiveTransition = _Class('WKFullScreenInteractiveTransition')
WKFullscreenAnimationController = _Class('WKFullscreenAnimationController')
WKColorPicker = _Class('WKColorPicker')
WKRotatingPopover = _Class('WKRotatingPopover')
WKFormRotatingAccessoryPopover = _Class('WKFormRotatingAccessoryPopover')
WKSelectPopover = _Class('WKSelectPopover')
WKColorPopover = _Class('WKColorPopover')
WKFormPeripheralBase = _Class('WKFormPeripheralBase')
WKFormSelectControl = _Class('WKFormSelectControl')
WKFormColorControl = _Class('WKFormColorControl')
WKDateTimeInputControl = _Class('WKDateTimeInputControl')
WKDateTimePicker = _Class('WKDateTimePicker')
WKAirPlayRoutePicker = _Class('WKAirPlayRoutePicker')
WKDataListSuggestionsControl = _Class('WKDataListSuggestionsControl')
WKDataListSuggestionsPopover = _Class('WKDataListSuggestionsPopover')
WKDataListSuggestionsPicker = _Class('WKDataListSuggestionsPicker')
WKScrollViewDelegateForwarder = _Class('WKScrollViewDelegateForwarder')
WKKeyboardScrollViewAnimator = _Class('WKKeyboardScrollViewAnimator')
WKKeyboardScrollingAnimator = _Class('WKKeyboardScrollingAnimator')
WKWebAllowDenyPolicyListener = _Class('WKWebAllowDenyPolicyListener')
WKLegacyCoreLocationProvider = _Class('WKLegacyCoreLocationProvider')
WKGeolocationProviderIOS = _Class('WKGeolocationProviderIOS')
WKActionSheetAssistant = _Class('WKActionSheetAssistant')
WKSwipeTransitionController = _Class('WKSwipeTransitionController')
WKRBSAssertionDelegate = _Class('WKRBSAssertionDelegate')
WKProcessAssertionBackgroundTaskManager = _Class('WKProcessAssertionBackgroundTaskManager')
WKMockNFTag = _Class('WKMockNFTag')
WKNFReaderSessionDelegate = _Class('WKNFReaderSessionDelegate')
WKScrollingNodeScrollViewDelegate = _Class('WKScrollingNodeScrollViewDelegate')
WKOneShotDisplayLinkHandler = _Class('WKOneShotDisplayLinkHandler')
WKSOAuthorizationDelegate = _Class('WKSOAuthorizationDelegate')
WKSOSecretDelegate = _Class('WKSOSecretDelegate')
WKWebViewContentProviderRegistry = _Class('WKWebViewContentProviderRegistry')
WKReloadFrameErrorRecoveryAttempter = _Class('WKReloadFrameErrorRecoveryAttempter')
WKFullKeyboardAccessWatcher = _Class('WKFullKeyboardAccessWatcher')
WKEditorUndoTarget = _Class('WKEditorUndoTarget')
WKEditCommand = _Class('WKEditCommand')
WKCustomProtocolLoader = _Class('WKCustomProtocolLoader')
WKWindowFeatures = _Class('WKWindowFeatures')
WKWebsiteDataStore = _Class('WKWebsiteDataStore')
WKWebsiteDataRecord = _Class('WKWebsiteDataRecord')
WKWebpagePreferences = _Class('WKWebpagePreferences')
WKWebViewConfiguration = _Class('WKWebViewConfiguration')
WKUserScript = _Class('WKUserScript')
WKUserContentController = _Class('WKUserContentController')
WKURLSchemeTaskImpl = _Class('WKURLSchemeTaskImpl')
WKTypeRefWrapper = _Class('WKTypeRefWrapper')
WKSnapshotConfiguration = _Class('WKSnapshotConfiguration')
WKSecurityOrigin = _Class('WKSecurityOrigin')
WKScriptMessage = _Class('WKScriptMessage')
WKProcessPool = _Class('WKProcessPool')
WKProcessGroup = _Class('WKProcessGroup')
WKPreviewElementInfo = _Class('WKPreviewElementInfo')
WKPreferences = _Class('WKPreferences')
WKPDFConfiguration = _Class('WKPDFConfiguration')
WKNavigationResponse = _Class('WKNavigationResponse')
WKNavigationData = _Class('WKNavigationData')
WKNavigationAction = _Class('WKNavigationAction')
WKNavigation = _Class('WKNavigation')
WKNSURLAuthenticationChallengeSender = _Class('WKNSURLAuthenticationChallengeSender')
WKHTTPCookieStore = _Class('WKHTTPCookieStore')
WKFrameInfo = _Class('WKFrameInfo')
WKFindResult = _Class('WKFindResult')
WKFindConfiguration = _Class('WKFindConfiguration')
WKContextMenuElementInfo = _Class('WKContextMenuElementInfo')
WKContentWorld = _Class('WKContentWorld')
WKContentRuleListStore = _Class('WKContentRuleListStore')
WKContentRuleList = _Class('WKContentRuleList')
WKConnection = _Class('WKConnection')
WKBrowsingContextGroup = _Class('WKBrowsingContextGroup')
WKBrowsingContextController = _Class('WKBrowsingContextController')
WKBackForwardListItem = _Class('WKBackForwardListItem')
WKBackForwardList = _Class('WKBackForwardList')
WKObservablePageState = _Class('WKObservablePageState')
WKRemoteObject = _Class('WKRemoteObject')
WKBrowsingContextHandle = _Class('WKBrowsingContextHandle')
WKPaymentAuthorizationDelegate = _Class('WKPaymentAuthorizationDelegate')
WKPaymentAuthorizationControllerDelegate = _Class('WKPaymentAuthorizationControllerDelegate')
WKPaymentAuthorizationViewControllerDelegate = _Class('WKPaymentAuthorizationViewControllerDelegate')
WKNetworkSessionDelegate = _Class('WKNetworkSessionDelegate')
WKQLThumbnailQueueManager = _Class('WKQLThumbnailQueueManager')
WKProcessTaskStateObserverDelegate = _Class('WKProcessTaskStateObserverDelegate')
WKPreferenceObserver = _Class('WKPreferenceObserver')
WKAutocorrectionRects = _Class('WKAutocorrectionRects')
WKAutocorrectionContext = _Class('WKAutocorrectionContext')
WKDataListTextSuggestion = _Class('WKDataListTextSuggestion')
WebResource = _Class('WebResource')
WebArchive = _Class('WebArchive')
WKTextPlaceholder = _Class('WKTextPlaceholder')
WKWebEvent = _Class('WKWebEvent')
WKSyntheticFlagsChangedWebEvent = _Class('WKSyntheticFlagsChangedWebEvent')
WKQuirkyNSUndoManager = _Class('WKQuirkyNSUndoManager')
WKTextSelectionRect = _Class('WKTextSelectionRect')
WKTextRange = _Class('WKTextRange')
WKTextPosition = _Class('WKTextPosition')
WKPreviewAction = _Class('WKPreviewAction')
WKCustomProtocol = _Class('WKCustomProtocol')
WKDownloadProgress = _Class('WKDownloadProgress')
WKTouchActionGestureRecognizer = _Class('WKTouchActionGestureRecognizer')
WKDeferringGestureRecognizer = _Class('WKDeferringGestureRecognizer')
WKInspectorNodeSearchGestureRecognizer = _Class('WKInspectorNodeSearchGestureRecognizer')
WKSyntheticTapGestureRecognizer = _Class('WKSyntheticTapGestureRecognizer')
WKHighlightLongPressGestureRecognizer = _Class('WKHighlightLongPressGestureRecognizer')
WKMouseGestureRecognizer = _Class('WKMouseGestureRecognizer')
WKRemoteObjectDecoder = _Class('WKRemoteObjectDecoder')
WKRemoteObjectEncoder = _Class('WKRemoteObjectEncoder')
WKVideoLayerRemote = _Class('WKVideoLayerRemote')
WKPlainRemoteLayer = _Class('WKPlainRemoteLayer')
WKUserDefaults = _Class('WKUserDefaults')
WKQLThumbnailLoadOperation = _Class('WKQLThumbnailLoadOperation')
WKSafeBrowsingBox = _Class('WKSafeBrowsingBox')
WKSafeBrowsingExclamationPoint = _Class('WKSafeBrowsingExclamationPoint')
WKInspectorIndicationView = _Class('WKInspectorIndicationView')
WKFullScreenPlaceholderView = _Class('WKFullScreenPlaceholderView')
WKColorMatrixView = _Class('WKColorMatrixView')
WKPasswordView = _Class('WKPasswordView')
WKPDFPageNumberIndicator = _Class('WKPDFPageNumberIndicator')
WKApplicationStateTrackingView = _Class('WKApplicationStateTrackingView')
WKContentView = _Class('WKContentView')
WKSystemPreviewView = _Class('WKSystemPreviewView')
WKPDFView = _Class('WKPDFView')
WKInspectorHighlightView = _Class('WKInspectorHighlightView')
WKLayerHostView = _Class('WKLayerHostView')
WKEmbeddedView = _Class('WKEmbeddedView')
WKCompositingView = _Class('WKCompositingView')
WKRemoteView = _Class('WKRemoteView')
WKShapeView = _Class('WKShapeView')
WKSimpleBackdropView = _Class('WKSimpleBackdropView')
WKTransformView = _Class('WKTransformView')
WKWebView = _Class('WKWebView')
WKOptionPickerCell = _Class('WKOptionPickerCell')
WKOptionGroupPickerCell = _Class('WKOptionGroupPickerCell')
WKBackdropView = _Class('WKBackdropView')
WKSelectSinglePicker = _Class('WKSelectSinglePicker')
WKMultipleSelectPicker = _Class('WKMultipleSelectPicker')
WKDataListSuggestionsPickerView = _Class('WKDataListSuggestionsPickerView')
WKFullscreenStackView = _Class('WKFullscreenStackView')
WKUIRemoteView = _Class('WKUIRemoteView')
WKSafeBrowsingWarning = _Class('WKSafeBrowsingWarning')
WKScrollView = _Class('WKScrollView')
WKChildScrollView = _Class('WKChildScrollView')
WKSafeBrowsingTextView = _Class('WKSafeBrowsingTextView')
WKColorButton = _Class('WKColorButton')
WKFullScreenViewController = _Class('WKFullScreenViewController')
WKFileUploadPanel = _Class('WKFileUploadPanel')
WKRichFileUploadPanel = _Class('WKRichFileUploadPanel')
WKDateTimeContextMenuViewController = _Class('WKDateTimeContextMenuViewController')
WKVideoFullScreenViewController = _Class('WKVideoFullScreenViewController')
WKImagePreviewViewController = _Class('WKImagePreviewViewController')
WKActionSheet = _Class('WKActionSheet')
WKSelectTableViewController = _Class('WKSelectTableViewController')
WKDataListSuggestionsViewController = _Class('WKDataListSuggestionsViewController')
WKNSDictionary = _Class('WKNSDictionary')
WKNSData = _Class('WKNSData')
WKNSNumber = _Class('WKNSNumber')
WKNSArray = _Class('WKNSArray')
WKObject = _Class('WKObject')
WKNSURLAuthenticationChallenge = _Class('WKNSURLAuthenticationChallenge')
WKNSURLRequest = _Class('WKNSURLRequest')
WKNSURL = _Class('WKNSURL')
WKNSString = _Class('WKNSString')
WKNSError = _Class('WKNSError')
