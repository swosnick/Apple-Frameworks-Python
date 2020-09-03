'''
Classes from the 'SwiftUI' framework.
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

    
SceneBridge = _Class('SwiftUI.SceneBridge')
AnyWindowStyleStorageBase = _Class('SwiftUI.AnyWindowStyleStorageBase')
EmptyViewRendererHost = _Class('SwiftUI.EmptyViewRendererHost')
DictionaryDecoder = _Class('SwiftUI.DictionaryDecoder')
DictionaryEncoder = _Class('SwiftUI.DictionaryEncoder')
ScrollViewNode = _Class('SwiftUI.ScrollViewNode')
AnyFallbackDelegateBox = _Class('SwiftUI.AnyFallbackDelegateBox')
SceneStorageTransformBox = _Class('SwiftUI.SceneStorageTransformBox')
SceneStorageValues = _Class('SwiftUI.SceneStorageValues')
AnyWindowToolbarStyleStorageBase = _Class('SwiftUI.AnyWindowToolbarStyleStorageBase')
MainMenuItemHost = _Class('SwiftUI.MainMenuItemHost')
AnyResolvedPaint = _Class('SwiftUI.AnyResolvedPaint')
RBGraphicsContext = _Class('SwiftUI.RBGraphicsContext')
MemoizedGraphicsDrawingCallback = _Class('SwiftUI.MemoizedGraphicsDrawingCallback')
ArchiveReader = _Class('SwiftUI.ArchiveReader')
DataArchiveReader = _Class('SwiftUI.DataArchiveReader')
FileArchiveReader = _Class('SwiftUI.FileArchiveReader')
ArchiveWriter = _Class('SwiftUI.ArchiveWriter')
DataArchiveWriter = _Class('SwiftUI.DataArchiveWriter')
FileArchiveWriter = _Class('SwiftUI.FileArchiveWriter')
ChildIndexProjection = _Class('SwiftUI.ChildIndexProjection')
_PreviewHost = _Class('SwiftUI._PreviewHost')
ScrollTest = _Class('SwiftUI.ScrollTest')
WidgetBundleHost = _Class('SwiftUI.WidgetBundleHost')
UIBarItemTarget = _Class('SwiftUI.UIBarItemTarget')
RootViewDelegate = _Class('SwiftUI.RootViewDelegate')
AnyTextModifier = _Class('SwiftUI.AnyTextModifier')
BoldTextModifier = _Class('SwiftUI.BoldTextModifier')
DisplayLink = _Class('SwiftUI.DisplayLink')
CGGraphicsContext = _Class('SwiftUI.CGGraphicsContext')
AnimationBoxBase = _Class('SwiftUI.AnimationBoxBase')
_ViewList_IndirectMap = _Class('SwiftUI._ViewList_IndirectMap')
AnyImageProviderBox = _Class('SwiftUI.AnyImageProviderBox')
AnyTransitionBox = _Class('SwiftUI.AnyTransitionBox')
ResolvedStyledText = _Class('SwiftUI.ResolvedStyledText')
PreferenceBridge = _Class('SwiftUI.PreferenceBridge')
AnyFontBox = _Class('SwiftUI.AnyFontBox')
AnyTextStorage = _Class('SwiftUI.AnyTextStorage')
_ViewList_Subgraph = _Class('SwiftUI._ViewList_Subgraph')
AccessibilityRelationshipScope = _Class('SwiftUI.AccessibilityRelationshipScope')
AnyColorBox = _Class('SwiftUI.AnyColorBox')
AnyViewStorageBase = _Class('SwiftUI.AnyViewStorageBase')
AnyLocationBase = _Class('SwiftUI.AnyLocationBase')
EventBindingBridge = _Class('SwiftUI.EventBindingBridge')
UIKitEventBindingBridge = _Class('SwiftUI.UIKitEventBindingBridge')
EventBindingManager = _Class('SwiftUI.EventBindingManager')
StyledTextLayoutDelegate = _Class('SwiftUI.StyledTextLayoutDelegate')
ResolvedImageLayoutDelegate = _Class('SwiftUI.ResolvedImageLayoutDelegate')
ViewResponder = _Class('SwiftUI.ViewResponder')
UnaryViewResponder = _Class('SwiftUI.UnaryViewResponder')
UIViewResponder = _Class('SwiftUI.UIViewResponder')
HostingScrollViewResponder = _Class('SwiftUI.HostingScrollViewResponder')
MultiViewResponder = _Class('SwiftUI.MultiViewResponder')
DefaultLayoutViewResponder = _Class('SwiftUI.DefaultLayoutViewResponder')
FocusNamespaceViewResponder = _Class('SwiftUI.FocusNamespaceViewResponder')
DropViewResponder = _Class('SwiftUI.DropViewResponder')
UIViewSnapshotResponder = _Class('SwiftUI.UIViewSnapshotResponder')
ContextMenuResponder = _Class('SwiftUI.ContextMenuResponder')
HoverResponder = _Class('SwiftUI.HoverResponder')
DragViewResponder = _Class('SwiftUI.DragViewResponder')
GraphHost = _Class('SwiftUI.GraphHost')
WidgetGraph = _Class('SwiftUI.WidgetGraph')
_WidgetGraph = _Class('SwiftUI._WidgetGraph')
AppGraph = _Class('SwiftUI.AppGraph')
ViewGraph = _Class('SwiftUI.ViewGraph')
FocusBridge = _Class('SwiftUI.FocusBridge')
UserActivityTrackingInfo = _Class('SwiftUI.UserActivityTrackingInfo')
InteropResponder = _Class('SwiftUI.InteropResponder')
KeyboardShortcutBridge = _Class('SwiftUI.KeyboardShortcutBridge')
ObjcColor = _Class('SwiftUI.ObjcColor')
AccessibilityNode = _Class('SwiftUI.AccessibilityNode')
AccessibilityReadingContentNode = _Class('SwiftUI.AccessibilityReadingContentNode')
BaseDateProvider = _Class('BaseDateProvider')
TimeProvider = _Class('TimeProvider')
RelativeDateProvider = _Class('RelativeDateProvider')
TimeIntervalProvider = _Class('TimeIntervalProvider')
DateProvider = _Class('DateProvider')
SwiftUIEnvironmentWrapper = _Class('SwiftUIEnvironmentWrapper')
PlatformViewCoordinator = _Class('SwiftUI.PlatformViewCoordinator')
UIKitPopUpButtonCoordinator = _Class('SwiftUI.UIKitPopUpButtonCoordinator')
FileImportExportBridge = _Class('SwiftUI.FileImportExportBridge')
UIKitToolbarCoordinator = _Class('SwiftUI.UIKitToolbarCoordinator')
DocumentNavigationItem = _Class('SwiftUI.DocumentNavigationItem')
PlatformDocument = _Class('SwiftUI.PlatformDocument')
SwiftUITabBarItem = _Class('SwiftUI.SwiftUITabBarItem')
UIKitGestureRecognizer = _Class('SwiftUI.UIKitGestureRecognizer')
GradientLayer = _Class('SwiftUI.GradientLayer')
ImageLayer = _Class('SwiftUI.ImageLayer')
MaskLayer = _Class('SwiftUI.MaskLayer')
AppSceneDelegate = _Class('SwiftUI.AppSceneDelegate')
AppDelegate = _Class('SwiftUI.AppDelegate')
TestingSceneDelegate = _Class('SwiftUI.TestingSceneDelegate')
TestingAppDelegate = _Class('SwiftUI.TestingAppDelegate')
UIKitMainMenuController = _Class('SwiftUI.UIKitMainMenuController')
_UIGraphicsView = _Class('SwiftUI._UIGraphicsView')
RenderBoxView = _Class('SwiftUI.RenderBoxView')
ListCoreHeaderHost = _Class('SwiftUI.ListCoreHeaderHost')
ListCoreCellHost = _Class('SwiftUI.ListCoreCellHost')
SwiftUIToolbar = _Class('SwiftUI.SwiftUIToolbar')
HostingScrollView = _Class('SwiftUI.HostingScrollView')
SwiftUITextField = _Class('SwiftUI.SwiftUITextField')
PlatformAlertController = _Class('SwiftUI.PlatformAlertController')
NotificationSendingSplitViewController = _Class('SwiftUI.NotificationSendingSplitViewController')
NotifyingMulticolumnSplitViewController = _Class('SwiftUI.NotifyingMulticolumnSplitViewController')
SplitViewNavigationController = _Class('SwiftUI.SplitViewNavigationController')
DocumentBrowserViewController = _Class('SwiftUI.DocumentBrowserViewController')
