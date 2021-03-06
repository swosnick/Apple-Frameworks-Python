'''
Classes from the 'UIFoundation' framework.
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

    
_NSTextAttachmentLayoutContext = _Class('_NSTextAttachmentLayoutContext')
_NSTextViewportLayoutObserver = _Class('_NSTextViewportLayoutObserver')
_UIPointVector = _Class('_UIPointVector')
_NSTextRunStorage = _Class('_NSTextRunStorage')
_NSAttributeRun = _Class('_NSAttributeRun')
_NSAttributes = _Class('_NSAttributes')
_NSCGTextGraphicsContext = _Class('_NSCGTextGraphicsContext')
__NSTextSelectionLineFragmentInfo = _Class('__NSTextSelectionLineFragmentInfo')
__NSTextAppearanceEffectContext = _Class('__NSTextAppearanceEffectContext')
_NSUIKitTextGraphicsContext = _Class('_NSUIKitTextGraphicsContext')
_NSStandardTextGraphicsContextProvider = _Class('_NSStandardTextGraphicsContextProvider')
NSDataAsset = _Class('NSDataAsset')
NSTextTab = _Class('NSTextTab')
NSTextAttachment = _Class('NSTextAttachment')
NSTextGraphicsContextProvider = _Class('NSTextGraphicsContextProvider')
NSTextAlternatives = _Class('NSTextAlternatives')
NSTextLayoutFragment = _Class('NSTextLayoutFragment')
NSLineFragmentRenderingContext = _Class('NSLineFragmentRenderingContext')
NSTextSelectionNavigation = _Class('NSTextSelectionNavigation')
NSTextLayoutManager = _Class('NSTextLayoutManager')
UINibCoderValue = _Class('UINibCoderValue')
NSGlyphInfo = _Class('NSGlyphInfo')
NSIdentityGlyphInfo = _Class('NSIdentityGlyphInfo')
NSGlyphNameGlyphInfo = _Class('NSGlyphNameGlyphInfo')
NSCIDGlyphInfo = _Class('NSCIDGlyphInfo')
NSCTGlyphInfo = _Class('NSCTGlyphInfo')
NSTextElement = _Class('NSTextElement')
NSTextParagraph = _Class('NSTextParagraph')
NSLayoutManagerTextBlockHelper = _Class('NSLayoutManagerTextBlockHelper')
NSLayoutManagerTextBlockRowArrayCache = _Class('NSLayoutManagerTextBlockRowArrayCache')
NSTextRange = _Class('NSTextRange')
NSCountableTextRange = _Class('NSCountableTextRange')
NSCountableTextLocation = _Class('NSCountableTextLocation')
NSTextLineFragment = _Class('NSTextLineFragment')
NSTextContentManager = _Class('NSTextContentManager')
NSTextContentStorage = _Class('NSTextContentStorage')
NSStringDrawingTextStorageSettings = _Class('NSStringDrawingTextStorageSettings')
NSTextList = _Class('NSTextList')
NSTextBlockLayoutHelper = _Class('NSTextBlockLayoutHelper')
NSTextBlock = _Class('NSTextBlock')
NSTextTableBlock = _Class('NSTextTableBlock')
NSTextTable = _Class('NSTextTable')
UIPointFIFO = _Class('UIPointFIFO')
UIBoxcarFilterPointFIFO = _Class('UIBoxcarFilterPointFIFO')
UIQuadCurvePointFIFO = _Class('UIQuadCurvePointFIFO')
NSTextViewportLayoutController = _Class('NSTextViewportLayoutController')
NSTextAttachmentViewProvider = _Class('NSTextAttachmentViewProvider')
NSRTFReaderTableState = _Class('NSRTFReaderTableState')
NSRTFReader = _Class('NSRTFReader')
NSTextCorrectionMarkerRendering = _Class('NSTextCorrectionMarkerRendering')
NSSubstituteWebResource = _Class('NSSubstituteWebResource')
NSHTMLWebDelegate = _Class('NSHTMLWebDelegate')
NSHTMLReader = _Class('NSHTMLReader')
NSHTMLWriter = _Class('NSHTMLWriter')
NSRTFWriter = _Class('NSRTFWriter')
NSTextSelection = _Class('NSTextSelection')
NSInsertionPointHelper = _Class('NSInsertionPointHelper')
_NSCoreTypesetterLayoutCache = _Class('_NSCoreTypesetterLayoutCache')
NSATSGlyphStorage = _Class('NSATSGlyphStorage')
NSATSLineFragment = _Class('NSATSLineFragment')
NSGlyphGenerator = _Class('NSGlyphGenerator')
_NSATSTypesetterGuts = _Class('_NSATSTypesetterGuts')
NSTextContainer = _Class('NSTextContainer')
NSParagraphArbitrator = _Class('NSParagraphArbitrator')
NSExtraLMData = _Class('NSExtraLMData')
NSRunStorage = _Class('NSRunStorage')
NSIdRunStorage = _Class('NSIdRunStorage')
NSStorage = _Class('NSStorage')
_NSTextStorageSideData = _Class('_NSTextStorageSideData')
UINibStringIDTable = _Class('UINibStringIDTable')
NSLayoutManager = _Class('NSLayoutManager')
NSTypesetter = _Class('NSTypesetter')
NSATSTypesetter = _Class('NSATSTypesetter')
NSSingleLineTypesetter = _Class('NSSingleLineTypesetter')
NSCoreTypesetter = _Class('NSCoreTypesetter')
NSStringDrawingContext = _Class('NSStringDrawingContext')
NSShadow = _Class('NSShadow')
NSParagraphStyleExtraData = _Class('NSParagraphStyleExtraData')
__NSFontExtraData = _Class('__NSFontExtraData')
UIFontDescriptor = _Class('UIFontDescriptor')
UICTFontDescriptor = _Class('UICTFontDescriptor')
_UIFontCacheKey = _Class('_UIFontCacheKey')
_UIFontDescriptorCacheKey = _Class('_UIFontDescriptorCacheKey')
_UIFontTextStyleCacheKey = _Class('_UIFontTextStyleCacheKey')
_UIFontNameCacheKey = _Class('_UIFontNameCacheKey')
_UIFontSystemCacheKey = _Class('_UIFontSystemCacheKey')
UIFont = _Class('UIFont')
NSFont = _Class('NSFont')
UICTFont = _Class('UICTFont')
_UICache = _Class('_UICache')
NSParagraphStyle = _Class('NSParagraphStyle')
NSMutableParagraphStyle = _Class('NSMutableParagraphStyle')
UINibEncoder = _Class('UINibEncoder')
UINibDecoder = _Class('UINibDecoder')
NSAttributeDictionaryEnumerator = _Class('NSAttributeDictionaryEnumerator')
_NSCachedAttributedString = _Class('_NSCachedAttributedString')
NSConcreteNotifyingMutableAttributedString = _Class('NSConcreteNotifyingMutableAttributedString')
NSTextStorage = _Class('NSTextStorage')
__NSImmutableTextStorage = _Class('__NSImmutableTextStorage')
NSConcreteTextStorage = _Class('NSConcreteTextStorage')
NSStringDrawingTextStorage = _Class('NSStringDrawingTextStorage')
__NSATSStringSegment = _Class('__NSATSStringSegment')
NSAttributeDictionary = _Class('NSAttributeDictionary')
NSTempAttributeDictionary = _Class('NSTempAttributeDictionary')
